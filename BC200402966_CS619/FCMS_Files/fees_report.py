from datetime import date
from tkcalendar import *
from FCMS_Files.fees_report_save import *
class FeesReports:
    def __init__(self,insertion_fees_panel):
        self.__insertion_fees_panel=insertion_fees_panel

    def __member_upd_selectionID_update(self, member_insertion_select_cb):
        select_id_list =[]
        mem_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        mem_cursor = mem_connection.cursor()
        mem_query = 'SELECT mem_id FROM members'
        try:
            mem_cursor.execute(mem_query)
            for id in mem_cursor:
                select_id_list.append(id)
            mem_cursor.close()
            mem_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
        select_id_list.sort()
        member_insertion_select_cb.config(values=select_id_list)
        member_insertion_select_cb.after(200, lambda : self.__member_upd_selectionID_update(member_insertion_select_cb))
    def __get_values_for_fees_table(self,  e):
        currentValue = self.__member_insertion_select_cb.get()
        # clearing controls
        self.__member_insertion_name_tb.delete(0, 'end')
        self.__member_insertion_email_tb.delete(0, 'end')
        self.__member_insertion_workplan_tb.delete(0, 'end')
        self.__member_insertion_fees_tb.delete(0, 'end')
        # creating connection for fetching member data
        mem_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        mem_cursor = mem_connection.cursor()
        mem_query = 'SELECT * FROM members where mem_id = {currentval}'.format(currentval=currentValue)
        try:
            mem_cursor.execute(mem_query)
            for row in mem_cursor:
                self.__member_insertion_name_tb.insert(0, row[1]+' '+ row[2])
                self.__member_insertion_email_tb.insert(0, row[3])
                self.__member_insertion_workplan_tb.insert(0, row[6])
                self.__member_insertion_fees_tb.insert(0, row[8])
            mem_cursor.close()
            mem_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
    def __set_paid_date_value_according_to_status(self,e):
        status_value = self.__insertion_status_cb.get()
        if status_value == 'Paid':
            self.__member_insertion_paid_date_tb.delete(0, 'end')
            self.__member_insertion_paid_date_tb.insert(0, 'dd/MM/yyyy')
        else:
            self.__member_insertion_paid_date_tb.delete(0, 'end')
            self.__member_insertion_paid_date_tb.insert(0, 'NIL')
    def __send_values_for_save(self, fees_window):
        month = self.__select_insertion_month_cb.get()
        member_id = self.__member_insertion_select_cb.get()
        member_name = self.__member_insertion_name_tb.get()
        member_email = self.__member_insertion_email_tb.get()
        member_workplan = self.__member_insertion_workplan_tb.get()
        member_fees = self.__member_insertion_fees_tb.get()
        status = self.__insertion_status_cb.get()
        fees_year = self.__mem_fees_year_cb.get()
        due_date = self.__member_insertion_due_date_tb.get()
        paid_date = self.__member_insertion_paid_date_tb.get()
        # checking values if empty
        if not (month and member_id and member_name and member_email and member_workplan and
                member_fees and status and fees_year and due_date and paid_date)=='':
            # creating object of class
            confirm_data_available = self.__check_if_data_is_already_present(member_id, month, fees_year, fees_window)
            if confirm_data_available == False:
                save_fees_report = SaveFeesReport(month, member_id, member_name, member_email, member_workplan, member_fees, status,fees_year, due_date, paid_date)
                save_fees_report.create_save_report_fees_table()
                response = save_fees_report.save_fees_report()
                if response:
                    self.__member_insertion_select_cb.index(-1)
                    self.__member_insertion_name_tb.delete(0, 'end')
                    self.__member_insertion_email_tb.delete(0, 'end')
                    self.__member_insertion_workplan_tb.delete(0, 'end')
                    self.__member_insertion_fees_tb.delete(0, 'end')
                    self.__member_insertion_due_date_tb.delete(0, 'end')
                    self.__member_insertion_paid_date_tb.delete(0, 'end')
                    self.__member_insertion_due_date_tb.insert(0, 'dd/MM/yyyy')
                    self.__member_insertion_paid_date_tb.insert(0, 'dd/MM/yyyy')
                    self.__message_lbl.config(text='')
            else:
                self.__message_lbl.config(text='Record is already present')
        else:
            messagebox.showerror('Fitness Club Management System', 'Please fill all the fields', parent=fees_window)

    def __check_if_data_is_already_present(self,id, month, year, fees_window):
        verify_data_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        verify_data_cursor = verify_data_connection.cursor()
        check_query = "SELECT member_id, fees_month, fees_year from save_report_fees where member_id=%s and fees_month =%s and fees_year =%s"
        check_tuple = (id, month, year)
        try:
            verify_data_cursor.execute(check_query, check_tuple)
            result = verify_data_cursor.fetchone()
            verify_data_connection.close()
            if result:
                return True
            else:
                return False

        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e), parent=fees_window)
    def showfeesreport(self, fees_window):
        select_insertion_month_lbl = tk.Label(master=self.__insertion_fees_panel, text='Select Month: ', bg='darkgrey', fg='midnightblue',
                                         font='arial 11 italic')
        select_insertion_month_lbl.place(x=30, y=10)
        months_insertion = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December']
        self.__select_insertion_month_cb = ttk.Combobox(master=self.__insertion_fees_panel, width=15, values=months_insertion)
        self.__select_insertion_month_cb.place(x=160, y=10)
        self.__select_insertion_month_cb.set(months_insertion[0])
        # select member ID
        member_insertion_select_ID_lbl = ttk.Label(master=self.__insertion_fees_panel,
                                              text='Select member ID: ',
                                              background='darkgrey',
                                              font='arial 11 italic',
                                              foreground='midnightblue')
        member_insertion_select_ID_lbl.place(x=30, y=50)
        self.__member_insertion_select_cb = ttk.Combobox(master=self.__insertion_fees_panel, width=15)
        self.__member_insertion_select_cb.place(x=160, y=50)
        self.__member_upd_selectionID_update(self.__member_insertion_select_cb)
        self.__member_insertion_select_cb.current(0)
        if self.__member_insertion_select_cb.current() != -1:
            self.__member_insertion_select_cb.bind('<<ComboboxSelected>>', self.__get_values_for_fees_table)
        else:
            pass
        # creating name
        member_insertion_name_lbl = tk.Label(master=self.__insertion_fees_panel,
                                        text='Member Name: ',
                                        font=('Arial', 11, 'italic'),
                                        fg='midnightblue', bg='darkgrey')
        member_insertion_name_lbl.place(x=30, y=90)
        self.__member_insertion_name_tb = tk.Entry(master=self.__insertion_fees_panel, width=20, font=('Arial', 11, 'italic'))
        self.__member_insertion_name_tb.place(x=160, y=90)
        # creating email
        member_insertion_email_lbl = tk.Label(master=self.__insertion_fees_panel, text='Email: ', font='arial 11 italic ', bg='darkgrey',
                                         fg='midnightblue')
        member_insertion_email_lbl.place(x=30, y=130)
        self.__member_insertion_email_tb = tk.Entry(master=self.__insertion_fees_panel, width=20, font=('Arial', 11, 'italic'))
        self.__member_insertion_email_tb.place(x=160, y=130)
        # creating workout plan
        member_insertion_workplan_lbl = tk.Label(master=self.__insertion_fees_panel, text='Workplan: ', font='arial 11 italic',
                                            bg='darkgrey', fg='midnightblue')
        member_insertion_workplan_lbl.place(x=380, y=10)
        self.__member_insertion_workplan_tb = tk.Entry(master=self.__insertion_fees_panel, width=20, font=('Arial', 11, 'italic'))
        self.__member_insertion_workplan_tb.place(x=480, y=10)
        # creating fees
        member_insertion_fees_lbl = tk.Label(master=self.__insertion_fees_panel, text='Fees: ', font='arial 11 italic',
                                            bg='darkgrey', fg='midnightblue')
        member_insertion_fees_lbl.place(x=380, y=50)
        self.__member_insertion_fees_tb = tk.Entry(master=self.__insertion_fees_panel, width=20, font=('Arial', 11, 'italic'))
        self.__member_insertion_fees_tb.place(x=480, y=50)
        self.__member_insertion_fees_tb.bind('<KeyPress>', self.__checkNumberforfees)
        # Fees pending or paid status
        insertion_status_list=['Pending', 'Paid']
        #creating status combobox
        insertion_status_lbl=tk.Label(master=self.__insertion_fees_panel, text='Status: ', font='arial 11 italic', bg='darkgrey', fg='midnightblue')
        insertion_status_lbl.place(x=380, y=90)
        self.__insertion_status_cb=ttk.Combobox(master=self.__insertion_fees_panel, values=insertion_status_list, width=15)
        self.__insertion_status_cb.place(x=480, y=90)
        self.__insertion_status_cb.set(insertion_status_list[1])
        if self.__insertion_status_cb.current() != -1:
            self.__insertion_status_cb.bind('<<ComboboxSelected>>', self.__set_paid_date_value_according_to_status)
        else:
            pass
        # creating year label
        year_select_lbl = tk.Label(self.__insertion_fees_panel, text='Select Year:', fg='midnightblue', bg='darkgrey', font='arial 11 italic')
        year_select_lbl.place(x=380, y=130)
        year_list=[]
        myear = date.today().year-1
        for i in range(20):
            year_list.append(myear)
            myear += 1
        self.__mem_fees_year_cb = ttk.Combobox(self.__insertion_fees_panel, width=17, value=year_list)
        self.__mem_fees_year_cb.place(x=480, y=130)
        self.__mem_fees_year_cb.current(0)
        # creating due date
        member_insertion_due_date_lbl = tk.Label(master=self.__insertion_fees_panel, text='Due Date: ', font=('arial', 11, 'italic'),
                                            bg='darkgrey', fg='midnightblue')
        member_insertion_due_date_lbl.place(x=720, y=10)
        self.__member_insertion_due_date_tb = tk.Entry(master=self.__insertion_fees_panel, width=20, highlightthickness=0,
                                           font=('yu gothic ui', 10, 'italic', 'bold'), fg='#6b6a69')
        self.__member_insertion_due_date_tb.place(x=815, y=10)
        self.__member_insertion_due_date_tb.insert(0, 'dd/mm/yyyy')
        self.__member_insertion_due_date_tb.bind('<Button-1>', self.__select_due_date)
        # creating paid date
        member_insertion_paid_date_lbl = tk.Label(master=self.__insertion_fees_panel, text='Paid Date: ', font=('arial', 11, 'italic'),
                                             bg='darkgrey', fg='midnightblue')
        member_insertion_paid_date_lbl.place(x=720, y=50)
        self.__member_insertion_paid_date_tb = tk.Entry(master=self.__insertion_fees_panel, width=20, highlightthickness=0,
                                            font=('yu gothic ui', 10, 'italic', 'bold'), fg='#6b6a69')
        self.__member_insertion_paid_date_tb.place(x=815, y=50)
        self.__member_insertion_paid_date_tb.insert(0, 'dd/mm/yyyy')
        self.__member_insertion_paid_date_tb.bind('<Button-1>', self.__select_paid_date)
        # creating save button
        member_insertion_savebtn = tk.Button(master=self.__insertion_fees_panel, text='Save Information', font=('Arial', 11, 'italic'),
                                            bg='maroon', fg='snow')
        member_insertion_savebtn.place(x=835, y=90)
        member_insertion_savebtn.config(command= lambda :self.__send_values_for_save(fees_window))
        # creating message frame
        message_frame = tk.Frame(self.__insertion_fees_panel, width=255,height=30, bd=3, relief=tk.RAISED)
        message_frame.place(x=780, y=135)
        message_lbl_heading = tk.Label(message_frame, text='MESSAGE: ', font='arialblack 10 italic bold', fg='maroon')
        message_lbl_heading.place(x=0, y=0)
        self.__message_lbl = tk.Label(message_frame, text='', fg='red2')
        self.__message_lbl.place(x=80,y=0)
    def __select_due_date(self, e1):
        global cal1, date_window1
        date_window1= tk.Toplevel()
        date_window1.grab_set()
        date_window1.attributes('-topmost', True)
        date_window1.title('Select Due Date')
        date_window1.geometry('250x220+650+400')
        date_window1.resizable(False,False)
        cal1 = Calendar(date_window1, selectmode='day', date_pattern='dd/mm/y')
        cal1.place(x=0, y=0)
        submit_btn1=tk.Button(date_window1, text='Submit' , command=self.__grab_due_date, bg='maroon', fg='grey99',width=20, padx=12, pady=2, font='arial 10 italic bold')
        submit_btn1.place(x=40, y=188)
        date_window1.protocol('WM_DELETE_WINDOW', False)
    def __grab_due_date(self):
        self.__member_insertion_due_date_tb.delete(0, tk.END)
        date1=cal1.get_date()
        self.__member_insertion_due_date_tb.insert(tk.END, date1)
        date_window1.grab_release()
        date_window1.destroy()
    def __select_paid_date(self, e1):
        global cal2, date_window2
        date_window2= tk.Toplevel()
        date_window2.grab_set()
        date_window2.attributes('-topmost', True)
        date_window2.title('Select Paid Date')
        date_window2.geometry('250x220+650+400')
        date_window2.resizable(0, 0)
        cal2 = Calendar(date_window2, selectmode='day', date_pattern='dd/mm/y')
        cal2.place(x=0, y=0)
        submit_btn2=tk.Button(date_window2, text='Submit' , command=self.__grab_paid_date, bg='maroon',
                              fg='grey99',width=20, padx=12, pady=2, font='arial 10 italic bold')
        submit_btn2.place(x=40, y=188)
        date_window2.protocol('WM_DELETE_WINDOW', False)
    def __grab_paid_date(self):
        self.__member_insertion_paid_date_tb.delete(0, tk.END)
        date2=cal2.get_date()
        self.__member_insertion_paid_date_tb.insert(tk.END, date2)
        date_window2.grab_release()
        date_window2.destroy()
    def __checkNumberforfees(self, e):
        try:
            int(self.__member_insertion_fees_tb.get())
            self.__message_lbl.config(text='')
            self.__member_insertion_fees_tb.config(bg='white')
            if len(self.__member_insertion_fees_tb.get()) >= 8:
                self.__member_insertion_fees_tb.delete(7, 'end')

        except ValueError:
            self.__message_lbl.config(text='Invalid fees value')
            self.__member_insertion_fees_tb.config(bg='red2')
            self.__member_insertion_fees_tb.delete(0, 'end')
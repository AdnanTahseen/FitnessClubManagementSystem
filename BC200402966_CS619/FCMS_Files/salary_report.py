from datetime import date
from tkcalendar import *
from FCMS_Files.salary_report_save import *
class SalaryReport:
    def __init__(self, salarypanel,salary_delete_panel, months):
        self.__salary_insertion_panel = salarypanel
        self.__months = months
        self.__salary_delete_panel = salary_delete_panel

    def __auto_update_selection_id_values(self, select_instructor_ID_cb):
        # creating connection
        select_Id_query = 'SELECT inst_id from instructor'
        upd_select_inst_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        upd_select_inst_cursor = upd_select_inst_connection.cursor()
        upd_select_inst_cursor.execute(select_Id_query)
        selection_id_list = []
        for row in upd_select_inst_cursor:
            selection_id_list.append(row[0])
        # close connection
        upd_select_inst_connection.close()
        # sorting values in list
        selection_id_list.sort()
        select_instructor_ID_cb.config(values=selection_id_list)
        # return selection_id_list
        select_instructor_ID_cb.after(200, lambda : self.__auto_update_selection_id_values(select_instructor_ID_cb))
    def __get_values_for_salary_panel(self, e):
        currentValue = self.__select_instructor_ID_cb.get()
        # empyting the boxes
        self.__sal_inst_name_tb.delete(0, tk.END)
        self.__sal_inst_sal_tb.delete(0, tk.END)
        self.__sal_inst_email_tb.delete(0, tk.END)
        self.__sal_inst_paid_date_tb.delete(0, tk.END)
        self.__sal_inst_paid_date_tb.insert(0, 'dd/MM/yyyy')

        #creating the connection
        fetch_query = 'SELECT * FROM instructor WHERE inst_id = {cval}'.format(cval=currentValue)
        fetch_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        fetch_cursor = fetch_connection.cursor()
        try:
            fetch_cursor.execute(fetch_query)
            for row in fetch_cursor:
                self.__sal_inst_name_tb.insert(0, row[1]+' '+row[2])
                self.__sal_inst_sal_tb.insert(0, row[6])
                self.__sal_inst_email_tb.insert(0, row[3])
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
    def __send_salary_data_to_save(self, salary_window):
        inst_id = self.__select_instructor_ID_cb.get()
        inst_name = self.__sal_inst_name_tb.get()
        inst_sal = self.__sal_inst_sal_tb.get()
        inst_email = self.__sal_inst_email_tb.get()
        sal_status = self.__sal_inst_paid_status_cb.get()
        sal_month = self.__sal_inst_month_tb.get()
        inst_paid_date = self.__sal_inst_paid_date_tb.get()
        sal_year = self.__sal_select_year_cb.get()
        # checking the controls if empty
        if not (inst_id and inst_name and inst_sal and inst_email and
                sal_status and sal_month and inst_paid_date and sal_year) == '':
            # creating the object of the class
            verification = self.__check_if_salary_is_already_present(inst_id, sal_month, sal_year, salary_window)
            if verification == False:
                save_sal = SaveSalary(inst_id, inst_name, inst_sal, inst_email,sal_status,sal_month,inst_paid_date,sal_year)
                save_sal.create_salary_table(salary_window)
                response = save_sal.save_salary_instructor(salary_window)
                if response:
                    self.__sal_inst_name_tb.delete(0, 'end')
                    self.__sal_inst_sal_tb.delete(0, 'end')
                    self.__sal_inst_email_tb.delete(0, 'end')
                    self.__sal_inst_paid_date_tb.delete(0, 'end')
                    self.__sal_inst_paid_date_tb.insert(0, 'dd/mm/yyyy')
                    self.__message_lbl.config(text='')
            else:
                # messagebox.showinfo('Fitness Club Management System', "Salary already present")
                self.__message_lbl.config(text='Record is already present')
        else:
            messagebox.showerror('Fitness Club Management System', 'Please fill in the fields', parent=salary_window)

    def __check_if_salary_is_already_present(self,inst_id, month, year, salary_window):
        sal_connection =  pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        sal_cursor = sal_connection.cursor()
        sal_query = 'SELECT * FROM salary WHERE inst_id = %s AND sal_month = %s AND sal_year = %s'
        try:
            sal_cursor.execute(sal_query, (inst_id, month, year))
            sal_data = sal_cursor.fetchone()
            sal_connection.close()
            if sal_data:
                return True
            else:
                return False

        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e), parent=salary_window)
    def showsalaryreport(self, salary_window):
        # creating interface for salary record
        select_instructor_ID_lbl = tk.Label(self.__salary_insertion_panel, text='Select Instructor ID: ', bg='darkgrey',
                                            fg='Snow', font='arial 11 italic')
        select_instructor_ID_lbl.place(x=20, y=10)
        self.__select_instructor_ID_cb = ttk.Combobox(self.__salary_insertion_panel, width=15)
        self.__select_instructor_ID_cb.place(x=160, y=10)
        self.__auto_update_selection_id_values(self.__select_instructor_ID_cb)
        self.__select_instructor_ID_cb.current(0)
        if self.__select_instructor_ID_cb.current() != -1:
            self.__select_instructor_ID_cb.bind('<<ComboboxSelected>>', self.__get_values_for_salary_panel)
        else:
            pass
        # creating name
        sal_inst_name_lbl = tk.Label(self.__salary_insertion_panel, text='Name: ', bg='darkgrey', fg='snow',
                                     font='arial 11 italic')
        sal_inst_name_lbl.place(x=20, y=40)
        self.__sal_inst_name_tb = tk.Entry(self.__salary_insertion_panel, width=20)
        self.__sal_inst_name_tb.place(x=160, y=40)
        # creating salary
        sal_inst_sal_lbl = tk.Label(self.__salary_insertion_panel, text='Salary: ', bg='darkgrey', fg='snow',
                                    font='arial 11 italic')
        sal_inst_sal_lbl.place(x=20, y=75)
        self.__sal_inst_sal_tb = tk.Entry(self.__salary_insertion_panel, width=20)
        self.__sal_inst_sal_tb.place(x=160, y=75)
        self.__sal_inst_sal_tb.bind('<KeyPress>', self.__checkNumberforSalary)
        # creating email
        sal_inst_email_lbl = tk.Label(self.__salary_insertion_panel, text='Email: ', bg='darkgrey', fg='snow',
                                      font='arial 11 italic')
        sal_inst_email_lbl.place(x=20, y=110)
        self.__sal_inst_email_tb = tk.Entry(self.__salary_insertion_panel, width=20)
        self.__sal_inst_email_tb.place(x=160, y=110)
        # creating list for salary paid or pending status
        sal_status_list = ['Pending', 'Paid']
        sal_inst_paid_status_lbl = tk.Label(self.__salary_insertion_panel, text='Status: ', bg='darkgrey', fg='snow',
                                            font='arial 11 italic')
        sal_inst_paid_status_lbl.place(x=20, y=145)
        self.__sal_inst_paid_status_cb = ttk.Combobox(self.__salary_insertion_panel, width=20, values=sal_status_list)
        self.__sal_inst_paid_status_cb.place(x=160, y=145)
        self.__sal_inst_paid_status_cb.set(sal_status_list[0])
        # creating list for months
        sal_inst_month_lbl = tk.Label(self.__salary_insertion_panel, text='Month: ', bg='darkgrey', fg='snow',
                                      font='arial 11 italic')
        sal_inst_month_lbl.place(x=370, y=10)
        self.__sal_inst_month_tb = ttk.Combobox(self.__salary_insertion_panel, width=20, values=self.__months)
        self.__sal_inst_month_tb.place(x=460, y=10)
        self.__sal_inst_month_tb.set(self.__months[0])
        # creating paid date
        sal_inst_paid_date_lbl = tk.Label(self.__salary_insertion_panel, text='Paid Date: ', bg='darkgrey', fg='snow',
                                          font='Arial 11 italic')
        sal_inst_paid_date_lbl.place(x=370, y=40)
        self.__sal_inst_paid_date_tb = tk.Entry(self.__salary_insertion_panel, width=19, highlightthickness=0,
                                         font=('yu gothic ui', 10, 'bold'), fg='#6b6a69')
        self.__sal_inst_paid_date_tb.place(x=460, y=40)
        self.__sal_inst_paid_date_tb.insert(0, 'dd/mm/yyyy')
        self.__sal_inst_paid_date_tb.bind('<Button-1>', self.__select_sal_inst_paid_date)
        # creating year
        sal_select_year = tk.Label(self.__salary_insertion_panel, text='Select year:', bg='darkgrey', fg='snow',
                                   font='arial 11 italic')
        sal_select_year.place(x=370, y=70)
        year_list=[]
        syear = date.today().year - 1
        for i in range(20):
            year_list.append(syear)
            syear +=1
        self.__sal_select_year_cb= ttk.Combobox(self.__salary_insertion_panel, width=20, values=year_list)
        self.__sal_select_year_cb.place(x=460, y=70)
        # creating button for saving data to database
        sal_inst_savebtn = tk.Button(self.__salary_insertion_panel, text='Save', width=10, font=('Arial', 11, 'italic'),
                                     bg='maroon', fg='snow')
        sal_inst_savebtn.place(x=500, y=100)
        sal_inst_savebtn.config(command=lambda :self.__send_salary_data_to_save(salary_window))
        # creating message frame
        message_frame = tk.Frame(self.__salary_insertion_panel, width=255, height=30, bd=3, relief=tk.RAISED)
        message_frame.place(x=370, y=145)
        message_lbl_heading = tk.Label(message_frame, text='MESSAGE: ', font='arialblack 10 italic bold', fg='maroon')
        message_lbl_heading.place(x=0, y=0)
        self.__message_lbl = tk.Label(message_frame, text='', fg='red2')
        self.__message_lbl.place(x=80, y=0)

    def __select_sal_inst_paid_date(self, ev):
        global sal_paid_cal, sal_date_window
        sal_date_window= tk.Toplevel()
        sal_date_window.grab_set()
        sal_date_window.title('Select Date: ')
        sal_date_window.geometry('250x220+650+400')
        sal_date_window.resizable(0, 0)
        sal_paid_cal = Calendar(sal_date_window, selectmode='day', date_pattern='dd/mm/y')
        sal_paid_cal.place(x=0, y=0)
        submit_btn=tk.Button(sal_date_window, text='Submit' , command=self.__grab_sal_inst_paid_date,
                             bg='maroon', fg='grey99',width=20,
                             padx=12, pady=2, font='arial 10 italic bold')
        submit_btn.place(x=40, y=188)
    def __grab_sal_inst_paid_date(self):
        self.__sal_inst_paid_date_tb.delete(0, tk.END)
        sal_date=sal_paid_cal.get_date()
        self.__sal_inst_paid_date_tb.insert(tk.END, sal_date)
        sal_date_window.grab_release()
        sal_date_window.destroy()
    def show_delete_panel(self, salary_window):
        selection_id_panel = tk.Label(self.__salary_delete_panel, text='Select Salary ID: ', bg='darkgrey',
                                            fg='Snow', font='arial 11 italic')
        selection_id_panel.place(x=20, y=20)
        # creating the selection
        self.__selection_del_id_cb = ttk.Combobox(self.__salary_delete_panel, width=15)
        self.__selection_del_id_cb.place(x=160, y=20)
        self.__auto_update_del_selection_id_values(self.__selection_del_id_cb)
        self.__selection_del_id_cb.current(0)
        # creating the delete button
        del_btn = tk.Button(self.__salary_delete_panel,width=10, text='Delete', bg='maroon', fg='snow', font='arial 11 italic',
                             padx=5, pady=5)
        del_btn.place(x=160, y=80)
        if self.__selection_del_id_cb.current()!= -1:
            del_btn.config(command= lambda : self.__delete_salary_data(self.__selection_del_id_cb.get(), salary_window))
        else:
            messagebox.showerror('Fitness Club Management System', 'Select value first!', parent= salary_window)
    def __auto_update_del_selection_id_values(self,selection_del_id_cb):
        del_id_list = []
        # creating connection
        del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        del_cursor = del_connection.cursor()
        # creating query
        del_query = 'SELECT sal_id FROM salary'
        try:
            # executing the query
            del_cursor.execute(del_query)
            # fetching the data
            del_data = del_cursor.fetchall()
            for i in del_data:
                del_id_list.append(i)
            del_connection.close()
            selection_del_id_cb['values'] = del_id_list
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)

        selection_del_id_cb.after(200, lambda : self.__auto_update_del_selection_id_values(selection_del_id_cb))
    def __delete_salary_data(self, cvalue, salary_window):
        # creating connection
        del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        del_cursor = del_connection.cursor()
        # creating query
        del_query = 'DELETE FROM salary WHERE sal_id = %s'
        # creating tuple
        del_tuple = (cvalue,)
        answer = messagebox.askyesno('Fitness Club Management system', 'Are you sure you want to delete?', parent=salary_window)
        if answer:
            try:
                # executing the query
                del_cursor.execute(del_query, del_tuple)
                # commiting the changes
                del_connection.commit()
                # closing the connection
                del_connection.close()
                messagebox.showinfo('Fitness Club Management System', 'Fees deleted successfully', parent=salary_window)
                self.__selection_del_id_cb.delete(0, 'end')
            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e), parent=salary_window)
    def __checkNumberforSalary(self, e):
        try:
            int(self.__sal_inst_sal_tb.get())
            self.__message_lbl.config(text='')
            self.__sal_inst_sal_tb.config(bg='white')
            if len(self.__sal_inst_sal_tb.get()) >= 8:
                self.__sal_inst_sal_tb.delete(7, 'end')

        except ValueError:
            self.__message_lbl.config(text='Invalid salary value')
            self.__sal_inst_sal_tb.config(bg='red2')
            self.__sal_inst_sal_tb.delete(0, 'end')

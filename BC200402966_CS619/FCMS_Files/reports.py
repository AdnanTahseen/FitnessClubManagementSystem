from FCMS_Files.profit_report import *
from FCMS_Files.expense_report import *
from FCMS_Files.salary_report import *
from FCMS_Files.fees_report import *
from FCMS_Files.view_expense_table import *
from FCMS_Files.expense_report_delete import *
class Reports:

    def showFeesPanel(self):
        fees_window = tk.Toplevel()
        fees_window.title("Members Fees Panel")
        fees_window.geometry('1200x650+300+200')
        fees_window.resizable(False,False)
        fees_window.grab_set()
        fees_window.attributes('-topmost', True)
        fees_window.iconphoto(False,tk.PhotoImage(file='Images/fcms_icon.png'))
        fees_frame = tk.Frame(fees_window, width=1200, height=650, bg='lightgrey',
                                                 bd=3)
        fees_frame.place(x=0, y=0)
        fees_heading_lbl = tk.Label(fees_frame, text='FEES STATUS PANEL',
                                               font=('Arial', 18, 'bold', 'italic'),
                                               fg='floralwhite', bg='blue', width=84, height=2)
        fees_heading_lbl.place(x=-5, y=-5)
        fees_upperframe = tk.Frame(fees_frame, width=1170, height=220,
                                   bg='darkgrey')
        fees_upperframe.place(x=10, y=80)
        # label frame
        insertion_fees_panel = tk.LabelFrame(master=fees_upperframe, text='Fees Status Panel',
                                             height=190, width=1080, font='arial 12 italic bold', fg='maroon',
                                             bg='darkgrey',
                                             bd=2)
        insertion_fees_panel.place(x=40, y=10)
        #  Button for refreshing table
        refresh_btn = tk.Button(fees_frame, text='Refresh Table', width=20, background='indianred4', foreground='snow', padx=10, pady=5)
        refresh_btn.place(x=200, y=310)
        # delete panel
        del_frame = tk.Frame(fees_frame, width=490,height=50, bg='darkgrey', relief=tk.RAISED)
        del_frame.place(x=690, y=290)
        del_label = tk.Label(del_frame, text='Select fees ID:', bg='darkgrey', fg='black', font='arial 11 italic')
        del_label.place(x=10, y=10)
        # creating selection comboxbox
        self.__selection_fees_id_cb = ttk.Combobox(del_frame, width=15)
        self.__selection_fees_id_cb.place(x=130, y=10)
        self.__auto_update_selection_fees_values(self.__selection_fees_id_cb)
        # self.__selection_fees_cb.current(0)
        # creating the delete button
        del_btn = tk.Button(del_frame, text='Delete',width=10, background='red2', fg='snow', font='arial 11 italic')
        del_btn.place(x=330, y=8)
        del_btn.config(command=lambda :self.__send_id_for_fees_deletion(fees_window))
        # creating the object of FeesReport class
        feereport=FeesReports(insertion_fees_panel)
        feereport.showfeesreport(fees_window)
        # creating the table for data display
        fees_table_frame = tk.Frame(fees_frame, width=1100, height=250, bg='white', bd=1)
        fees_table_frame.place(x=20, y=350)
        # creating scrollbar for frame
        fees_table_frame_scrollbar = ttk.Scrollbar(fees_table_frame, orient=tk.VERTICAL)
        fees_table_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #creating treeview for data display
        fees_table_treeview = ttk.Treeview(fees_table_frame,show='headings', yscrollcommand=fees_table_frame_scrollbar.set)
        fees_table_treeview.pack(fill=tk.BOTH, expand=1)
        # configuring refresh button
        refresh_btn.config(command=lambda: self.__refresh_fees_table(fees_table_treeview))
        # configuring scrollbar for treeview
        fees_table_frame_scrollbar.config(command=fees_table_treeview.yview)
        #table style
        table_style = ttk.Style(fees_table_treeview)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font='arial 9 italic bold',foreground='snow', background='maroon2')
        # creating columns for treeview
        fees_table_treeview['columns'] =('FeesID','FeesMonth','MemID', 'MemName','MemEmail','MemWorkout','MemFees','MemStatus','FeesYear',
                                         'MemDueDate','MemPaidDate')
        # creating headings for table
        fees_table_treeview.heading('FeesID',text='Fees ID', anchor=tk.CENTER)
        fees_table_treeview.heading('FeesMonth',text='Fees Month', anchor=tk.CENTER)
        fees_table_treeview.heading('MemID',text='Member ID', anchor=tk.CENTER)
        fees_table_treeview.heading('MemName',text='Member Name', anchor=tk.CENTER)
        fees_table_treeview.heading('MemEmail',text='Member Email', anchor=tk.CENTER)
        fees_table_treeview.heading('MemWorkout',text='Workout Plan', anchor=tk.CENTER)
        fees_table_treeview.heading('MemFees',text='Plan Fees', anchor=tk.CENTER)
        fees_table_treeview.heading('MemStatus', text='Status', anchor=tk.CENTER)
        fees_table_treeview.heading('FeesYear', text='Fees Year', anchor=tk.CENTER)
        fees_table_treeview.heading('MemDueDate',text='Due Date', anchor=tk.CENTER)
        fees_table_treeview.heading('MemPaidDate', text='Paid Date', anchor=tk.CENTER)
        # creating column and settig their width
        fees_table_treeview.column('FeesID', width=60, minwidth=60, anchor=tk.CENTER)
        fees_table_treeview.column('FeesMonth', width=100, minwidth=100, anchor=tk.CENTER)
        fees_table_treeview.column('MemID', width=80, minwidth=80, anchor=tk.CENTER)
        fees_table_treeview.column('MemName', width=150, minwidth=150, anchor=tk.CENTER)
        fees_table_treeview.column('MemEmail', width=150, minwidth=150, anchor=tk.CENTER)
        fees_table_treeview.column('MemWorkout',width=150, minwidth=150, anchor=tk.CENTER)
        fees_table_treeview.column('MemFees', width=80, minwidth=80, anchor=tk.CENTER)
        fees_table_treeview.column('MemStatus', width=80, minwidth=80, anchor=tk.CENTER)
        fees_table_treeview.column('FeesYear', width=100, minwidth=100, anchor=tk.CENTER)
        fees_table_treeview.column('MemDueDate', width=100, minwidth=100, anchor=tk.CENTER)
        fees_table_treeview.column('MemPaidDate', width=100, minwidth=100, anchor=tk.CENTER)
        # inserting data into treeview
        table_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = table_connection.cursor()
        table_query = 'SELECT * FROM save_report_fees'
        try:
            table_cursor.execute(table_query)
            table_data = table_cursor.fetchall()
            for row in table_data:
                fees_table_treeview.insert('', tk.END, values=row)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e), parent=fees_window)
    def showSalaryPanel(self):
        salary_window = tk.Toplevel()
        salary_window.title('Salary Management Panel')
        salary_window.geometry('1200x650+300+200')
        salary_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        salary_window.resizable(False,False)
        salary_window.grab_set()
        months=['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
        salary_frame = tk.Frame(salary_window, width=1200, height=650, bg='lightgrey',
                                  bd=3)
        salary_frame.place(x=0, y=0)
        salary_heading_lbl = tk.Label(salary_frame, text='SALARY PANEL',
                                        font=('Arial', 18, 'bold', 'italic'),
                                        fg='floralwhite', bg='blue', width=84, height=2)
        salary_heading_lbl.place(x=-5, y=-5)
        # creating upper frame for insertion panel
        salary_upperframe=tk.Frame(salary_frame, width=1150, height=230, bg='darkgrey')
        salary_upperframe.place(x=20, y=70)
        salary_insertion_panel=tk.LabelFrame(salary_upperframe, text='Salary Insertion Panel',
                                             bg='darkgrey', fg='maroon', font='arial 12 italic bold',
                                             width=700, height=200, bd=3)
        salary_insertion_panel.place(x=60, y=10)
        # delete panel
        salary_delete_panel = tk.LabelFrame(salary_upperframe, text='Salary Delete Panel',
                                             bg='darkgrey', fg='maroon', font='arial 12 italic bold',
                                             width=300, height=200, bd=3)
        salary_delete_panel.place(x=800, y=10)
        # creating lower frame for insertion panel
        salary_lowerframe=tk.Frame(salary_frame, width=1150, height=230, bg='darkgrey')
        salary_lowerframe.place(x=20, y=370)
        #  Button for refreshing table
        refresh_btn = tk.Button(salary_frame, text='Refresh Table',width=20, font='arial 10 bold', fg='snow', bg='purple')
        refresh_btn.place(x=500, y=310)
        refresh_btn.config(padx=5, pady=5)
        # calling salary insertion panel
        salaryreport=SalaryReport(salary_insertion_panel,salary_delete_panel, months)
        salaryreport.showsalaryreport(salary_window)
        salaryreport.show_delete_panel(salary_window)
        # creating scrollbar for frame
        salary_table_frame_scrollbar = ttk.Scrollbar(salary_lowerframe, orient=tk.VERTICAL)
        salary_table_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #creating treeview for data display
        salary_table_treeview = ttk.Treeview(salary_lowerframe,height=9,show='headings', yscrollcommand=salary_table_frame_scrollbar.set)
        salary_table_treeview.pack(fill=tk.BOTH, expand=1)
        refresh_btn.config(command=lambda: self.__refresh_salary_table(salary_table_treeview))
        # configuring scrollbar for treeview
        salary_table_frame_scrollbar.config(command=salary_table_treeview.yview)
        #table style
        table_style = ttk.Style(salary_table_treeview)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font='arial 11 italic bold',foreground='snow', background='maroon2')
        table_style.configure('Treeview', font='arial 9 italic ', background='lightgrey')
        # creating columns for treeview
        salary_table_treeview['columns'] =('SalaryID','Inst_ID','InstName','InstSalary', 'InstEmail',
                                           'InstSalStatus','InstSalMonth','InstSalPaidDate', 'Year')
        # creating headings for table
        salary_table_treeview.heading('SalaryID',text='Salary ID', anchor=tk.CENTER)
        salary_table_treeview.heading('Inst_ID',text='Inst ID', anchor=tk.CENTER)
        salary_table_treeview.heading('InstName',text='Instructor Name', anchor=tk.CENTER)
        salary_table_treeview.heading('InstSalary',text='Salary', anchor=tk.CENTER)
        salary_table_treeview.heading('InstEmail',text='Email', anchor=tk.CENTER)
        salary_table_treeview.heading('InstSalStatus',text='Status', anchor=tk.CENTER)
        salary_table_treeview.heading('InstSalMonth',text='Month', anchor=tk.CENTER)
        salary_table_treeview.heading('InstSalPaidDate',text='Paid Date', anchor=tk.CENTER)
        salary_table_treeview.heading('Year', text='Year', anchor=tk.CENTER)
        # creating column and settig their width
        salary_table_treeview.column('SalaryID', width=100, minwidth=100, anchor=tk.CENTER)
        salary_table_treeview.column('Inst_ID', width=100, minwidth=100, anchor=tk.CENTER)
        salary_table_treeview.column('InstName', width=150, minwidth=150, anchor=tk.CENTER)
        salary_table_treeview.column('InstSalary', width=120, minwidth=120, anchor=tk.CENTER)
        salary_table_treeview.column('InstEmail', width=180, minwidth=180, anchor=tk.CENTER)
        salary_table_treeview.column('InstSalStatus', width=120, minwidth=120, anchor=tk.CENTER)
        salary_table_treeview.column('InstSalMonth', width=100, minwidth=100, anchor=tk.CENTER)
        salary_table_treeview.column('InstSalPaidDate', width=130, minwidth=130, anchor=tk.CENTER)
        salary_table_treeview.column('Year', width=130, minwidth=130, anchor=tk.CENTER)
        # inserting data into treeview
        table_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = table_connection.cursor()
        table_query = 'SELECT * FROM salary'
        try:
            table_cursor.execute(table_query)
            table_data = table_cursor.fetchall()
            for row in table_data:
                salary_table_treeview.insert('', tk.END, values=row)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e), parent=salary_window)
    def __refresh_salary_table(self, table):
        table.delete(*table.get_children())
        table_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = table_connection.cursor()
        table_query = 'SELECT * FROM salary'
        try:
            table_cursor.execute(table_query)
            table_data = table_cursor.fetchall()
            for row in table_data:
                table.insert('', tk.END, values=row)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
    def showExpensePanel(self):
        expense_window = tk.Toplevel()
        expense_window.title('Expense Management Panel')
        expense_window.geometry('1200x650+300+200')
        expense_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        expense_window.resizable(False, False)
        expense_window.grab_set()
        expense_window.attributes('-topmost', True)
        months=['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
        expense_main_frame = tk.Frame(expense_window, width=1200, height=650, bg='lightgrey',
                                  bd=3)
        expense_main_frame.place(x=0, y=0)
        expense_heading_lbl = tk.Label(expense_main_frame, text='EXPENSES PANEL',
                                        font=('Arial', 18, 'bold', 'italic'),
                                        fg='floralwhite', bg='blue', width=84, height=2)
        expense_heading_lbl.place(x=-5, y=-5)
        expense_upperframe=tk.Frame(expense_main_frame, width=1150, height=250, bg='lightgrey')
        expense_upperframe.place(x=20, y=70)
        # insertion panel
        expense_insertion_panel=tk.LabelFrame(expense_upperframe, text='Expense Insertion Panel',
                                             bg='lightgrey', fg='maroon', font='arial 12 italic bold',
                                             width=1110, height=230, bd=3)
        expense_insertion_panel.place(x=20, y=10)
        # calling object of Expense class
        expensereport=ExpenseReport(expense_insertion_panel, months, expense_window)
        expensereport.showExpensePanel()

        # delete panel
        delete_panel = tk.LabelFrame(expense_main_frame, width=300, height=180, text='Delete Expense Panel:',
                                     bg='lightgrey', fg='maroon', font='arial 12 italic bold',bd=3)
        delete_panel.place(x=40, y=350)
        # creating selection ID
        selection_id_lbl = tk.Label(delete_panel, text='Select ID: ', bg='lightgrey', font='arial 11 italic', fg='black')
        selection_id_lbl.place(x=20, y=20)
        # creating entry for selection ID
        self.__selection_id_cb = ttk.Combobox(delete_panel, width=20)
        self.__selection_id_cb.place(x=130, y=20)
        self.__auto_update_selection_id(self.__selection_id_cb)
        self.__selection_id_cb.current(0)
        # creating button for deleting data
        del_btn = tk.Button(delete_panel, text="Delete", width=12, padx=3, pady=2, bg='red2', fg='snow')
        del_btn.place(x=170, y=80)
        if self.__selection_id_cb.current() != -1:
            del_exp = DeleteExpense(self.__selection_id_cb.get())
            del_btn.config(command=lambda :del_exp.delete_expense(expense_window))
        else:
            pass


        # creating object for expense view table
        viewexpensetable = ViewExpenseTable()
        # creating button for expense table view
        expense_table_btn=tk.Button(expense_main_frame, text='View Expense Table', font=('Arial', 12, 'bold', 'italic'),
                                     fg='maroon', bg='white', width=20, height=2, bd=3, command=viewexpensetable.show_expense_table)
        expense_table_btn.place(x=500, y=350)
    def showProfitPanel(self):
        profit_window= tk.Toplevel()
        profit_window.title("Salary Management Panel")
        profit_window.geometry('1200x650+300+200')
        profit_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        profit_window.resizable(False, False)
        profit_window.grab_set()
        profit_window.attributes('-topmost', True)
        profit_frame = tk.Frame(profit_window, width=1200, height=650, bg='lightgrey',bd=3)
        profit_frame.place(x=0, y=0)
        # creating heading label
        profit_heading_lbl = tk.Label(profit_frame, text='PROFIT PANEL',
                                        font=('Arial', 18, 'bold', 'italic'),
                                        fg='floralwhite', bg='blue', width=84, height=2)
        profit_heading_lbl.place(x=-5, y=-5)
        # creating upper frame for insertion panel
        profit_upperframe=tk.Frame(profit_frame, width=1150, height=250, bg='lightgrey', bd=3)
        profit_upperframe.place(x=20, y=70)
        # creating insertion panel
        profit_insertion_panel=tk.LabelFrame(profit_upperframe, text='Profit Insertion Panel: ', font=('Arial', 12, 'bold', 'italic'),
                                             fg='maroon', width=600, height=200, bg='lightgrey', bd=3)
        profit_insertion_panel.place(x=120, y=20)
        # creating message frame
        message_frame = tk.Frame(profit_frame, width=255, height=30, bd=3, relief=tk.RAISED)
        message_frame.place(x=370, y=300)
        message_lbl_heading = tk.Label(message_frame, text='MESSAGE: ', font='arialblack 10 italic bold', fg='maroon')
        message_lbl_heading.place(x=0, y=0)
        self.__message_lbl = tk.Label(message_frame, text='', fg='red2')
        self.__message_lbl.place(x=80, y=0)

        fcms_profit=Profit(profit_insertion_panel, self.__message_lbl, profit_window)
        fcms_profit.showprofitpanel()
        # creating delete panel
        profit_delete_panel = tk.LabelFrame(profit_upperframe, text='Profit Delete Panel: ', font=('arial',12,'italic', 'bold'),
                                            fg='maroon2', width=280, height=200, bg='lightgrey', bd=3)
        profit_delete_panel.place(x=740, y=20)
        select_profilt_id = tk.Label(profit_delete_panel, text='Select Profit ID: ', bg='lightgrey', fg='black',
                                    font='arial 11 italic' )
        select_profilt_id.place(x=20, y= 20)
        self.__profit_id_selection_for_del_cb = ttk.Combobox(profit_delete_panel, width=12)
        self.__profit_id_selection_for_del_cb.place(x=140, y=20)
        # self.__profit_id_selection_for_del_cb.current(0)
        self.__auto_update_profit_del_id(self.__profit_id_selection_for_del_cb)
        del_profit_btn = tk.Button(profit_delete_panel, text="Delete", width=10, fg='snow', bg='red2',
                                   padx=2, pady=2)
        del_profit_btn.place(x=150, y=70)
        del_profit_btn.config(command = lambda :self.__delete_profit_data(profit_window))
        # creating the table for data display
        profit_table_frame = tk.Frame(profit_frame, width=1100, height=250, bg='white')
        profit_table_frame.place(x=80, y=350)
        # creating scrollbar for frame
        profit_table_frame_scrollbar = ttk.Scrollbar(profit_table_frame, orient=tk.VERTICAL)
        profit_table_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #creating treeview for data display
        profit_table_treeview = ttk.Treeview(profit_table_frame,show='headings', yscrollcommand=profit_table_frame_scrollbar.set)
        profit_table_treeview.pack(fill=tk.BOTH, expand=1)
        # configuring scrollbar for treeview
        profit_table_frame_scrollbar.config(command=profit_table_treeview.yview)
        #table style
        table_style = ttk.Style(profit_table_treeview)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font='arial 9 italic bold',foreground='snow', background='maroon2')
        table_style.configure('Treeview', font='arial 9 italic ', background='lightgrey')
        # creating columns for treeview
        profit_table_treeview['columns'] = ('ProfitID','ProfitMonth','ProfitYear','TotalExpense', 'TotalIncome', 'TotalSalaries', 'TotalProfit')
        # creating headings for table
        profit_table_treeview.heading('ProfitID',text='Profit ID', anchor=tk.CENTER)
        profit_table_treeview.heading('ProfitMonth',text='Profit Month', anchor=tk.CENTER)
        profit_table_treeview.heading('ProfitYear',text='Profit Year', anchor=tk.CENTER)
        profit_table_treeview.heading('TotalExpense',text='Total Expense', anchor=tk.CENTER)
        profit_table_treeview.heading('TotalIncome',text='Total Income', anchor=tk.CENTER)
        profit_table_treeview.heading('TotalSalaries',text='Total Salaries', anchor=tk.CENTER)
        profit_table_treeview.heading('TotalProfit',text='Total Profit', anchor=tk.CENTER)
        # creating column and settig their width
        profit_table_treeview.column('ProfitID', width=100, minwidth=100, anchor=tk.CENTER)
        profit_table_treeview.column('ProfitMonth', width=150, minwidth=150, anchor=tk.CENTER)
        profit_table_treeview.column('ProfitYear', width=150, minwidth=150, anchor=tk.CENTER)
        profit_table_treeview.column('TotalExpense', width=150, minwidth=150, anchor=tk.CENTER)
        profit_table_treeview.column('TotalIncome', width=150, minwidth=150, anchor=tk.CENTER)
        profit_table_treeview.column('TotalSalaries', width=150, minwidth=150, anchor=tk.CENTER)
        profit_table_treeview.column('TotalProfit', width=200, minwidth=200, anchor=tk.CENTER)
        # populating table with data from database
        self.__refresh_profit_table(profit_table_treeview)
        # creating button for profit table view
        profit_table_btn=tk.Button(profit_frame, text='Refresh Table', font=('Arial', 10, 'italic'),
                                     fg='snow', bg='maroon2', width=12)
        profit_table_btn.place(x=800, y=300)
        profit_table_btn.config(command = lambda : self.__refresh_profit_table(profit_table_treeview))
    def __refresh_fees_table(self, fees_table_treeview):
        for row in fees_table_treeview.get_children():
            fees_table_treeview.delete(row)
        table_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = table_connection.cursor()
        table_query = 'SELECT * FROM save_report_fees'
        try:
            table_cursor.execute(table_query)
            table_data = table_cursor.fetchall()
            for row in table_data:
                fees_table_treeview.insert('', tk.END, values=row)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
    def __auto_update_selection_id(self,selection_id_cb):
        selection_list=[]
        id_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        id_cursor = id_connection.cursor()
        try:
            id_query = 'SELECT expense_id FROM expense_report'
            id_cursor.execute(id_query)
            id_data = id_cursor.fetchall()
            for row in id_data:
                selection_list.append(row)
                selection_id_cb['values']=selection_list
            id_cursor.close()
            id_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)

        selection_id_cb.after(200, lambda: self.__auto_update_selection_id(selection_id_cb))
    def __refresh_profit_table(self, profit_table_treeview):
        for row in profit_table_treeview.get_children():
            profit_table_treeview.delete(row)
        table_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = table_connection.cursor()
        table_query = 'SELECT * FROM profit'
        try:
            table_cursor.execute(table_query)
            table_data = table_cursor.fetchall()
            for row in table_data:
                profit_table_treeview.insert(parent='',index=tk.END, values=row)

        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
    def __auto_update_profit_del_id(self, profit_id_selection_for_del_cb):
        selection_list = []
        id_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        id_cursor = id_connection.cursor()
        id_query = 'SELECT pro_id FROM profit'
        try:
            id_cursor.execute(id_query)
            id_data = id_cursor.fetchall()
            for row in id_data:
                selection_list.append(row)
                profit_id_selection_for_del_cb['values'] = selection_list
            id_cursor.close()
            id_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))

        profit_id_selection_for_del_cb.after(200, lambda: self.__auto_update_profit_del_id(profit_id_selection_for_del_cb))
    def __delete_profit_data(self, profit_window):
        currentValue = self.__profit_id_selection_for_del_cb.get()
        if currentValue == '':
            messagebox.showerror('Fitness Club Management System', 'Please Select Profit ID', parent=profit_window)
        else:
            del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
            del_cursor = del_connection.cursor()
            del_query = 'DELETE FROM profit WHERE pro_id=%s'
            del_tuple = (currentValue,)
            answer = messagebox.askyesno('Fitness Club Management System', 'Are you sure you want to delete?', parent=profit_window)
            if answer:
                try:
                    del_cursor.execute(del_query, del_tuple)
                    del_connection.commit()
                    del_cursor.close()
                    del_connection.close()
                    messagebox.showinfo('Fitness Club Management System', 'Data Deleted Successfully', parent=profit_window)
                except Exception as e:
                    messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e), parent=profit_window)

            else:
                pass
    def __auto_update_selection_fees_values(self, selection_fees_id_cb):
        del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        del_cursor = del_connection.cursor()
        del_query = 'SELECT fees_id FROM save_report_fees'
        try:
            del_cursor.execute(del_query)
            del_data = del_cursor.fetchall()
            del_list = []
            for row in del_data:
                del_list.append(row)
                selection_fees_id_cb['values'] = del_list
            del_cursor.close()
            del_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))

        selection_fees_id_cb.after(200, lambda : self.__auto_update_selection_fees_values(selection_fees_id_cb))
    def __send_id_for_fees_deletion(self, fees_window):
        currentValue = self.__selection_fees_id_cb.get()
        if currentValue == '':
            messagebox.showerror('Fitness Club Management System', 'Please Select Fees ID', parent=fees_window)
        else:
            del_connection = pms.connect(host='localhost',port=3306, user='root', password='',database='fcms')
            del_cursor = del_connection.cursor()
            del_query = 'DELETE FROM save_report_fees WHERE fees_id=%s'
            del_tuple = (currentValue,)
            answer = messagebox.askyesno('Fitness Club Management System', 'Are you sure you want to delete?', parent=fees_window)
            if answer:
                try:
                    del_cursor.execute(del_query, del_tuple)
                    del_connection.commit()
                    del_cursor.close()
                    del_connection.close()
                    messagebox.showinfo('Fitness Club Management System', 'Data Deleted Successfully', parent=fees_window)
                except Exception as e:
                    messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e),  parent=fees_window)


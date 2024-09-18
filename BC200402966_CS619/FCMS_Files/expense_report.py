import tkinter as tk
from datetime import date
from tkinter import ttk
from tkcalendar import *
from FCMS_Files.expense_report_save import *
class ExpenseReport:
    def __init__(self,expensepanel, months, expense_window):
        self.__expense_insertion_panel = expensepanel
        self.__months = months
        self.__expense_window = expense_window
    def showExpensePanel(self):
        # creating interface for expense record
        expense_year = date.today().year
        year_list = []
        for i in range(20):
            year_list.append(expense_year-1)
            expense_year +=1
        # creating year interface
        expense_year = tk.Label(self.__expense_insertion_panel, text='Select Year', bg='lightgrey', fg='black',
                                font='arial 11 italic')
        expense_year.place(x=20, y=10)
        self.__expense_year_cb = ttk.Combobox(self.__expense_insertion_panel, width=17, values=year_list)
        self.__expense_year_cb.place(x=195, y=10)
        self.__expense_year_cb.set(year_list[0])
        # building rent
        building_rent_lbl=tk.Label(self.__expense_insertion_panel, text='Building Rent Amount: ', bg='lightgrey', fg='black', font='Arial 11 italic')
        building_rent_lbl.place(x=20, y=50)
        self.__building_rent_tb=tk.Entry(self.__expense_insertion_panel, width=20)
        self.__building_rent_tb.place(x=195, y=50)
        self.__building_rent_tb.bind('<KeyPress>', self.__checkNumberforBuildingRent)
        # building rent month
        building_rent_month_lbl = tk.Label(self.__expense_insertion_panel, text='Building Rent Paid Month: ', bg='lightgrey', fg='black',
                                           font='arial 11 italic')
        building_rent_month_lbl.place(x=20, y=90)
        self.__building_rent_month_cb=ttk.Combobox(self.__expense_insertion_panel, width=17, values=self.__months)
        self.__building_rent_month_cb.place(x=195, y=90)
        self.__building_rent_month_cb.set(self.__months[0])
        # building rent paid date
        building_rent_paid_date_lbl= tk.Label(self.__expense_insertion_panel, text='Building Rent Paid Date: ', bg='lightgrey', fg='black', font='arial 11 italic')
        building_rent_paid_date_lbl.place(x=20, y=130)

        self.__building_rent_paid_date_tb= tk.Entry(self.__expense_insertion_panel, width=20, highlightthickness=0, fg='#6b6a69')
        self.__building_rent_paid_date_tb.place(x=195, y=130)
        self.__building_rent_paid_date_tb.insert(0, 'dd/mm/yyyy')
        self.__building_rent_paid_date_tb.bind('<Button-1>', self.__select_building_rent_paid_date)
        # internet bill amount
        internet_bill_amount_lbl = tk.Label(self.__expense_insertion_panel, text='Internet Bill Amount: ', bg='lightgrey',
                                            fg='black', font='arial 11 italic')
        internet_bill_amount_lbl.place(x=20, y=170)
        self.__internet_bill_amount_tb = tk.Entry(self.__expense_insertion_panel, width=20)
        self.__internet_bill_amount_tb.place(x=195, y=170)
        self.__internet_bill_amount_tb.bind('<KeyPress>', self.__checkNumberforInternet)
        # internet bill paid month
        internet_bill_paid_month_lbl = tk.Label(self.__expense_insertion_panel, text='Internet Bill Paid Month: ',
                                                bg='lightgrey', fg='black', font='arial 11 italic')
        internet_bill_paid_month_lbl.place(x=350, y=10)
        self.__internet_bill_paid_month_cb = ttk.Combobox(self.__expense_insertion_panel, width=17, values=self.__months)
        self.__internet_bill_paid_month_cb.place(x=535, y=10)
        self.__internet_bill_paid_month_cb.set(self.__months[0])
        # internet bill paid date
        internet_bill_paid_date_lbl = tk.Label(self.__expense_insertion_panel, text='Internet Bill Paid Date: ',
                                               bg='lightgrey', fg='black', font='arial 11 italic')
        internet_bill_paid_date_lbl.place(x=350, y=50)
        self.__internet_bill_paid_date_tb = tk.Entry(self.__expense_insertion_panel, width=20, highlightthickness=0, fg='#6b6a69')
        self.__internet_bill_paid_date_tb.place(x=535, y=50)
        self.__internet_bill_paid_date_tb.insert(0, 'dd/mm/yyyy')
        self.__internet_bill_paid_date_tb.bind('<Button-1>', self.__select_internet_bill_paid_date)
        # electricity bill
        electricity_bill_amount_lbl = tk.Label(self.__expense_insertion_panel, text='Electricity Bill Amount: ', bg='lightgrey',
                                               fg='black', font='arial 11 italic')
        electricity_bill_amount_lbl.place(x=350, y=90)
        self.__electricity_bill_amount_tb = tk.Entry(self.__expense_insertion_panel, width=20)
        self.__electricity_bill_amount_tb.place(x=535, y=90)
        self.__electricity_bill_amount_tb.bind('<KeyPress>', self.__checkNumberforElectricity)
        # electricity bill paid date
        electricity_bill_paid_date_lbl = tk.Label(self.__expense_insertion_panel, text='Electricity Bill Paid Date: ',
                                                  bg='lightgrey',
                                                  fg='black', font='arial 11 italic')
        electricity_bill_paid_date_lbl.place(x=350, y=130)
        self.__electricity_bill_paid_date_tb = tk.Entry(self.__expense_insertion_panel, width=20, highlightthickness=0, fg='#6b6a69')
        self.__electricity_bill_paid_date_tb.place(x=535, y=130)
        self.__electricity_bill_paid_date_tb.insert(0, 'dd/mm/yyyy')
        self.__electricity_bill_paid_date_tb.bind('<Button-1>', self.__select_electricity_bill_paid_date)
        # electricity bill paid month
        electricity_bill_paid_month_lbl = tk.Label(self.__expense_insertion_panel, text='Electricity Bill Paid Month: ',
                                                   bg='lightgrey', fg='black', font='arial 11 italic')
        electricity_bill_paid_month_lbl.place(x=350, y=170)
        self.__electricity_bill_paid_month_cb = ttk.Combobox(self.__expense_insertion_panel, values=self.__months, width=17)
        self.__electricity_bill_paid_month_cb.place(x=535, y=170)
        self.__electricity_bill_paid_month_cb.set(self.__months[0])
       # watersupply bill amount
        watersupply_bill_amount_lbl = tk.Label(self.__expense_insertion_panel, text='Water Supply Bill Amount: ',
                                               bg='lightgrey',
                                               fg='black', font='arial 11 italic')
        watersupply_bill_amount_lbl.place(x=700, y=10)
        self.__watersupply_bill_amount_tb = tk.Entry(self.__expense_insertion_panel, width=20)
        self.__watersupply_bill_amount_tb.place(x=910, y=10)
        self.__watersupply_bill_amount_tb.bind('<KeyPress>', self.__checkNumberforWaterSupply)
        # Watersupply bill paid date
        watersupply_bill_paid_date_lbl = tk.Label(self.__expense_insertion_panel, text='Water Supply Bill Paid Date: ',
                                                  bg='lightgrey', fg='black', font='arial 11 italic')
        watersupply_bill_paid_date_lbl.place(x=700, y=50)
        self.__watersupply_bill_paid_date_tb = tk.Entry(self.__expense_insertion_panel, width=20, highlightthickness=0, fg='#6b6a69')
        self.__watersupply_bill_paid_date_tb.place(x=910, y=50)
        self.__watersupply_bill_paid_date_tb.insert(0, 'dd/mm/yyyy')
        self.__watersupply_bill_paid_date_tb.bind('<Button-1>', self.__select_watersupply_bill_paid_date)
        # water supply bill paid month
        watersupply_bill_paid_month_lbl = tk.Label(self.__expense_insertion_panel, text='Water Supply Bill Paid Month: ',
                                                   bg='lightgrey',
                                                   fg='black', font='arial 11 italic')
        watersupply_bill_paid_month_lbl.place(x=700, y=90)
        self.__watersupply_bill_paid_month_cb = ttk.Combobox(self.__expense_insertion_panel, values=self.__months, width=17)
        self.__watersupply_bill_paid_month_cb.place(x=910, y=90)
        self.__watersupply_bill_paid_month_cb.set(self.__months[0])
       # button for saving data to database
        expenseSaveBtn = tk.Button(self.__expense_insertion_panel, text='Save Information', bg='maroon', fg='snow', width=20,
                                   padx=6, pady=8)
        expenseSaveBtn.place(x=873, y=125)
        expenseSaveBtn.config(command=self.__send_expense_data_to_save)
        # creating message frame
        message_frame = tk.Frame(self.__expense_insertion_panel, width=300, height=30, bd=3, relief=tk.GROOVE)
        message_frame.place(x=785, y=172)
        message_lbl_heading = tk.Label(message_frame, text='MESSAGE: ', font='arialblack 10 italic bold', fg='maroon')
        message_lbl_heading.place(x=0, y=0)
        self.__message_lbl = tk.Label(message_frame, text='', fg='red2')
        self.__message_lbl.place(x=80, y=0)

    def __select_internet_bill_paid_date(self, ev):
        global internetWindow, internetCalendar
        internetWindow = tk.Toplevel()
        internetWindow.grab_set()
        internetWindow.title('Electricity Bill Paid Date')
        internetWindow.geometry('253x220+600+400')
        internetWindow.resizable(False, False)
        internetWindow.attributes('-topmost', True)
        internetCalendar = Calendar(internetWindow, selectmode='day', date_pattern='dd/mm/y')
        internetCalendar.place(x=0, y=0)
        billSaveBtn = tk.Button(internetWindow, text='Submit', bg='maroon', fg='grey50', width=20)
        billSaveBtn.place(x=50, y=190)
        billSaveBtn.config(command=self.__grab_internet_bill_paid_date)
        internetWindow.protocol('WM_DELETE_WINDOW', False)
    def __grab_internet_bill_paid_date(self):
        self.__internet_bill_paid_date_tb.delete(0, tk.END)
        self.__internet_bill_paid_date_tb.insert(0, internetCalendar.get_date())
        internetWindow.grab_release()
        internetWindow.destroy()
    def __select_watersupply_bill_paid_date(self, ev):
        global watersupplyWindow, watersupplyCalendar
        watersupplyWindow=tk.Toplevel()
        watersupplyWindow.grab_set()
        watersupplyWindow.title('Electricity Bill Paid Date')
        watersupplyWindow.geometry('253x220+600+400')
        watersupplyWindow.resizable(False,False)
        watersupplyWindow.attributes('-topmost', True)
        watersupplyCalendar=Calendar(watersupplyWindow, selectmode='day', date_pattern='dd/mm/y')
        watersupplyCalendar.place(x=0, y=0)
        billSaveBtn=tk.Button(watersupplyWindow, text='Submit', bg='maroon', fg='grey50', width=20)
        billSaveBtn.place(x=50, y=190)
        billSaveBtn.config(command=self.__grab_watersupply_bill_paid_date)
        watersupplyWindow.protocol('WM_DELETE_WINDOW', False)
    def __grab_watersupply_bill_paid_date(self):
        self.__watersupply_bill_paid_date_tb.delete(0,tk.END)
        self.__watersupply_bill_paid_date_tb.insert(0, watersupplyCalendar.get_date())
        watersupplyWindow.grab_release()
        watersupplyWindow.destroy()
    def __select_electricity_bill_paid_date(self, ev):
        global electricityWindow, electricityCalendar
        electricityWindow=tk.Toplevel()
        electricityWindow.grab_set()
        electricityWindow.title('Electricity Bill Paid Date')
        electricityWindow.geometry('253x220+600+400')
        electricityWindow.resizable(0,0)
        electricityWindow.attributes('-topmost', True)
        electricityCalendar=Calendar(electricityWindow, selectmode='day', date_pattern='dd/mm/y')
        electricityCalendar.place(x=0, y=0)
        billSaveBtn=tk.Button(electricityWindow, text='Submit', bg='maroon', fg='grey50', width=20)
        billSaveBtn.place(x=50, y=190)
        billSaveBtn.config(command=self.__grab_electricity_bill_paid_date)
        electricityWindow.protocol('WM_DELETE_WINDOW', False)
    def __grab_electricity_bill_paid_date(self):
        self.__electricity_bill_paid_date_tb.delete(0,tk.END)
        self.__electricity_bill_paid_date_tb.insert(0, electricityCalendar.get_date())
        electricityWindow.grab_release()
        electricityWindow.destroy()
    def __select_building_rent_paid_date(self, ev):
        global buildingRentWindow, buildingRentCalendar
        buildingRentWindow=tk.Toplevel()
        buildingRentWindow.grab_set()
        buildingRentWindow.attributes('-topmost', True)
        buildingRentWindow.title('Building Rent Paid Date')
        buildingRentWindow.geometry('253x220+600+400')
        buildingRentWindow.resizable(0,0)
        buildingRentCalendar=Calendar(buildingRentWindow, selectmode='day', date_pattern='dd/mm/y')
        buildingRentCalendar.place(x=0, y=0)
        rentSaveBtn=tk.Button(buildingRentWindow, text='Submit', bg='maroon', fg='grey50', width=20)
        rentSaveBtn.place(x=50, y=190)
        rentSaveBtn.config(command=self.__grab_building_rent_paid_date)
        buildingRentWindow.protocol('WM_DELETE_WINDOW', False)
    def __grab_building_rent_paid_date(self):
        self.__building_rent_paid_date_tb.delete(0,tk.END)
        self.__building_rent_paid_date_tb.insert(0, buildingRentCalendar.get_date())
        buildingRentWindow.grab_release()
        buildingRentWindow.destroy()

    def __send_expense_data_to_save(self):
        # get data from text boxes
        expense_year = self.__expense_year_cb.get()
        building_rent_amount = self.__building_rent_tb.get()
        building_rent_paid_date = self.__building_rent_paid_date_tb.get()
        building_rent_paid_month = self.__building_rent_month_cb.get()
        electricity_bill_amount = self.__electricity_bill_amount_tb.get()
        electricity_bill_paid_date = self.__electricity_bill_paid_date_tb.get()
        electricity_bill_paid_month = self.__electricity_bill_paid_month_cb.get()
        watersupply_bill_amount = self.__watersupply_bill_amount_tb.get()
        watersupply_bill_paid_date = self.__watersupply_bill_paid_date_tb.get()
        watersupply_bill_paid_month = self.__watersupply_bill_paid_month_cb.get()
        internet_bill_amount = self.__internet_bill_amount_tb.get()
        internet_bill_paid_month = self.__internet_bill_paid_month_cb.get()
        internet_bill_paid_date = self.__internet_bill_paid_date_tb.get()
        # creating the object of the class
        expense_report = SaveExpenseReport(
            expense_year,
            building_rent_amount,
            building_rent_paid_date,
            building_rent_paid_month,
            electricity_bill_amount,
            electricity_bill_paid_date,
            electricity_bill_paid_month,
            watersupply_bill_amount,
            watersupply_bill_paid_date,
            watersupply_bill_paid_month,
            internet_bill_amount,
            internet_bill_paid_month,
            internet_bill_paid_date,
            self.__expense_window
        )
        if not (expense_year and building_rent_amount and building_rent_paid_date and building_rent_paid_month and electricity_bill_amount and
            electricity_bill_paid_date and electricity_bill_paid_month and watersupply_bill_amount and watersupply_bill_paid_date and
            watersupply_bill_paid_month and internet_bill_amount and internet_bill_paid_month and internet_bill_paid_date) == '':
            verification = self.__check_if_data_is_already_present(expense_year,building_rent_paid_month, electricity_bill_paid_month,
                                                                   watersupply_bill_paid_month, internet_bill_paid_month)
            if verification == False:
                response = expense_report.save_expense_report()
                if response:
                    # clearing the contr
                    self.__building_rent_tb.delete(0,'end')
                    self.__building_rent_paid_date_tb.delete(0,'end')
                    self.__building_rent_paid_date_tb.insert(0,'dd/mm/yyyy')
                    self.__electricity_bill_amount_tb.delete(0,'end')
                    self.__electricity_bill_paid_date_tb.delete(0,'end')
                    self.__electricity_bill_paid_date_tb.insert(0,'dd/mm/yyyy')
                    self.__watersupply_bill_amount_tb.delete(0,'end')
                    self.__watersupply_bill_paid_date_tb.delete(0,'end')
                    self.__watersupply_bill_paid_date_tb.insert(0,'dd/mm/yyyy')
                    self.__internet_bill_amount_tb.delete(0,'end')
                    self.__internet_bill_paid_date_tb.delete(0,'end')
                    self.__internet_bill_paid_date_tb.insert(0,'dd/mm/yyyy')
                    self.__message_lbl.config(text='')
            else:
                self.__message_lbl.config(text='Record is already present')
        else:
            messagebox.showerror('Fitness Club Management System', 'Please fill all the fields', parent=self.__expense_window)

    def __check_if_data_is_already_present(self,expense_year,br_month, eb_month, wb_month, ib_month):
        exp_connection =  pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        exp_cursor = exp_connection.cursor()
        exp_query = '''SELECT expense_year, building_rent_month, e_bill_paid_month,ws_bill_paid_month, i_bill_paid_month
                        FROM expense_report WHERE 
                        expense_year = %s AND building_rent_month = %s AND e_bill_paid_month = %s and ws_bill_paid_month = %s and i_bill_paid_month = %s'''
        try:
            exp_cursor.execute(exp_query, (expense_year,br_month, eb_month, wb_month, ib_month))
            exp_data = exp_cursor.fetchone()
            exp_connection.close()
            if exp_data:
                return True
            else:
                return False

        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e), parent= self.__expense_window)
    def __checkNumberforBuildingRent(self, e):
        try:
            int(self.__building_rent_tb.get())
            self.__message_lbl.config(text='')
            self.__building_rent_tb.config(bg='white')
            if len(self.__building_rent_tb.get()) >= 8:
                self.__building_rent_tb.delete(7, 'end')

        except ValueError:
            self.__message_lbl.config(text='Invalid rent amount value')
            self.__building_rent_tb.config(bg='red2')
            self.__building_rent_tb.delete(0, 'end')
    def __checkNumberforElectricity(self, e):
        try:
            int(self.__electricity_bill_amount_tb.get())
            self.__message_lbl.config(text='')
            self.__electricity_bill_amount_tb.config(bg='white')
            if len(self.__electricity_bill_amount_tb.get()) >= 8:
                self.__building_rent_tb.delete(7, 'end')

        except ValueError:
            self.__message_lbl.config(text='Invalid electricity amount value')
            self.__electricity_bill_amount_tb.config(bg='red2')
            self.__electricity_bill_amount_tb.delete(0, 'end')

    def __checkNumberforWaterSupply(self, e):
        try:
            int(self.__watersupply_bill_amount_tb.get())
            self.__message_lbl.config(text='')
            self.__watersupply_bill_amount_tb.config(bg='white')
            if len(self.__watersupply_bill_amount_tb.get()) >= 8:
                self.__watersupply_bill_amount_tb.delete(7, 'end')

        except ValueError:
            self.__message_lbl.config(text='Invalid watersupply amount value')
            self.__watersupply_bill_amount_tb.config(bg='red2')
            self.__watersupply_bill_amount_tb.delete(0, 'end')
    def __checkNumberforInternet(self, e):
        try:
            int(self.__internet_bill_amount_tb.get())
            self.__message_lbl.config(text='')
            self.__internet_bill_amount_tb.config(bg='white')
            if len(self.__internet_bill_amount_tb.get()) >= 8:
                self.__internet_bill_amount_tb.delete(7, 'end')

        except ValueError:
            self.__message_lbl.config(text='Invalid internet amount value')
            self.__internet_bill_amount_tb.config(bg='red2')
            self.__internet_bill_amount_tb.delete(0, 'end')
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import pymysql as pms
from FCMS_Files.profit_report_save import *
class Profit:
    def __init__(self, profitpanel, msg_lbl, profit_window):
        self.__profitInsertionPanel=profitpanel
        self.__msg_lbl=msg_lbl
        self.__profit_window = profit_window
    def showprofitpanel(self):
        select_year_lbl = tk.Label(self.__profitInsertionPanel, text='Select Year: ', bg='lightgrey', fg='black',
                                   font='arial 11 italic')
        select_year_lbl.place(x=30, y=10)
        year_list= []
        # for i in range(2020, 2030):
        #     year_list.append(str(i))
        pyear = date.today().year
        for i in range(20):
            year_list.append(pyear-1)
            pyear +=1
        self.__select_year_cb = ttk.Combobox(master=self.__profitInsertionPanel, width=17, values=year_list)
        self.__select_year_cb.place(x=140, y=10)
        self.__select_year_cb.set(year_list[0])
        # month
        months=['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
        select_month_lbl = tk.Label(master=self.__profitInsertionPanel, text='Select Month: ',
                                           bg='lightgrey', fg='black', font='arial 11 italic')
        select_month_lbl.place(x=30, y=50)
        self.__select_month_cb = ttk.Combobox(master=self.__profitInsertionPanel, width=17, values=months)
        self.__select_month_cb.place(x=140, y=50)
        # self.__select_month_cb.set(months[0])
        self.__select_month_cb.bind('<<ComboboxSelected>>', self.__gather_complete_information)
        # if self.__select_month_cb.current() != -1:
        #     self.__select_month_cb.bind('<<ComboboxSelected>>', self.__gather_complete_information)
        # else:
        #     messagebox.showerror('Fitness Club Management System', 'Select month!')
        # expense
        total_expense_lbl=tk.Label(self.__profitInsertionPanel, text='Total Expense: ', bg='lightgrey', fg='black', font='arial 11 italic')
        total_expense_lbl.place(x=30, y=90)
        self.__total_expense_tb=tk.Entry(self.__profitInsertionPanel, width=20)
        self.__total_expense_tb.place(x=140, y=90)
        # income
        total_income_lbl=tk.Label(self.__profitInsertionPanel, text='Total Income: ', bg='lightgrey', fg='black', font='arial 11 italic')
        total_income_lbl.place(x=30, y=130)
        self.__total_income_tb=tk.Entry(self.__profitInsertionPanel, width=20)
        self.__total_income_tb.place(x=140, y=130)

        # salary paid date
        total_salaries_paid_lbl=tk.Label(self.__profitInsertionPanel, text='Total Salaries Paid: ',
                                         bg='lightgrey', fg='black', font='arial 11 italic')
        total_salaries_paid_lbl.place(x=300, y=10)
        self.__total_salaries_paid_tb=tk.Entry(self.__profitInsertionPanel, width=20)
        self.__total_salaries_paid_tb.place(x=440, y=10)
        # profit
        total_profit_lbl=tk.Label(self.__profitInsertionPanel, text='Total Profit: ', bg='lightgrey', fg='black', font='arial 11 italic')
        total_profit_lbl.place(x=300, y=50)
        self.__total_profit_tb =tk.Entry(self.__profitInsertionPanel, width=20)
        self.__total_profit_tb.place(x=440, y=50)
        # total member
        total_member = tk.Label(self.__profitInsertionPanel, text='Total Member: ', bg='lightgrey', fg='black',
                                font='arial 11 italic')
        total_member.place(x=300, y=90)
        self.__total_member_tb = tk.Entry(self.__profitInsertionPanel, width=20)
        self.__total_member_tb.place(x=440, y=90)
        # save info
        saveInfoBtn=tk.Button(self.__profitInsertionPanel, width=15, text='Save Info', bg='maroon', fg='snow', font='arial 10 italic')
        saveInfoBtn.place(x=440, y=130)
        saveInfoBtn.config(command = self.__save_profit_information)

    def __gather_complete_information(self, e):
        month = self.__select_month_cb.get()
        year = self.__select_year_cb.get()
        self.__total_expense_tb.delete(0, 'end')
        self.__total_income_tb.delete(0, 'end')
        self.__total_salaries_paid_tb.delete(0, 'end')
        self.__total_profit_tb.delete(0, 'end')
        self.__total_member_tb.delete(0, 'end')
        if not (month and year ) == '':
            income = self.__gather_income_information(self.__total_income_tb, month, year)
            expense = self.__gather_expense_information(self.__total_expense_tb, month, year)
            total_salaries_paid = self.__gather_salaries_information(self.__total_salaries_paid_tb, month, year)
            total_profit= (int(income)-((int(expense))+(int(total_salaries_paid))))
            self.__total_profit_tb.insert(0, str(total_profit))
        else:
            messagebox.showerror("Fitness Club Management System", 'Select year and month.', parent= self.__profit_window)
    def __gather_income_information(self, total_income_tb, month, year):
        month= month
        year = year
        total_income_tb.delete(0, tk.END)
        income_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        income_cursor = income_connection.cursor()
        mem_fees=[]
        income_query = '''
                          SELECT * FROM save_report_fees WHERE 
                          fees_month = %s and fees_year = %s and status='Paid' 
                          '''
        try:
            income_cursor.execute(income_query, (month, year))
            income_result = income_cursor.fetchall()
            for row in income_result:
                mem_fees.append(int(row[6]))
            total_income = str(sum(mem_fees))
            total_income_tb.insert(0, total_income)
            self.__total_member_tb.insert(0, len(mem_fees))
            return total_income
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: ' + str(e), parent = self.__profit_window)
    def __gather_expense_information(self, total_expense_tb, month, year):
        month= month
        year = year
        total_expense_tb.delete(0, tk.END)
        expense_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        expense_cursor = expense_connection.cursor()
        building_rent_amount=[]
        e_bill_amount=[]
        ws_bill_amount=[]
        i_bill_amount=[]
        expense_query = '''
                          SELECT * FROM expense_report WHERE 
                          building_rent_month = %s and e_bill_paid_month = %s and ws_bill_paid_month = %s and i_bill_paid_month =%s and expense_year = %s 
                          '''
        try:
            expense_cursor.execute(expense_query, (month,month,month,month,year))
            expense_result = expense_cursor.fetchall()
            for row in expense_result:
                building_rent_amount.append(int(row[2]))
                e_bill_amount.append(int(row[5]))
                ws_bill_amount.append(int(row[8]))
                i_bill_amount.append(int(row[11]))
            total_expense = str(sum(building_rent_amount) + sum(e_bill_amount)+ sum (ws_bill_amount) + sum (i_bill_amount))
            total_expense_tb.insert(0, total_expense)
            expense_connection.close()
            return total_expense
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: ' + str(e), parent = self.__profit_window)
    def __gather_salaries_information(self, total_salaries_paid_tb, month, year):
        month= month
        year = year
        total_salaries_paid_tb.delete(0, tk.END)
        salary_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        salary_cursor = salary_connection.cursor()
        inst_sal=[]
        salary_query = '''
                          SELECT * FROM salary WHERE 
                          sal_month = %s and sal_year = %s and sal_status='Paid' 
                          '''
        try:
            salary_cursor.execute(salary_query, (month, year))
            salary_result = salary_cursor.fetchall()
            for row in salary_result:
                inst_sal.append(int(row[3]))
            total_salaries = str(sum(inst_sal))
            total_salaries_paid_tb.insert(0, total_salaries)
            salary_connection.close()
            return total_salaries
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: ' + str(e), parent = self.__profit_window)
    def __save_profit_information(self):
        year = self.__select_year_cb.get()
        month = self.__select_month_cb.get()
        total_expense = self.__total_expense_tb.get()
        total_income = self.__total_income_tb.get()
        total_salaries = self.__total_salaries_paid_tb.get()
        total_profit = self.__total_profit_tb.get()

        if not (year and month and total_expense and total_income and total_salaries and total_profit) == '':
            save_profit  = SaveProfitReport(year, month, total_expense, total_income, total_salaries, total_profit)
            verification = self.__check_if_data_is_already_present(month , year)
            if verification is not True:
                response = save_profit.save_profit_information()
                if response:
                    self.__select_year_cb.delete(0, 'end')
                    self.__select_month_cb.delete(0, 'end')
                    self.__total_expense_tb.delete(0, 'end')
                    self.__total_income_tb.delete(0, 'end')
                    self.__total_salaries_paid_tb.delete(0, 'end')
                    self.__total_profit_tb.delete(0, 'end')
                    self.__total_member_tb.delete(0, 'end')
                    self.__msg_lbl.config(text='')
            else:
                self.__msg_lbl.config(text='Record is already present')
        else:
            messagebox.showerror('Fitness Club Management System', 'Fetch data by selecting year and month', parent = self.__profit_window)
    def __check_if_data_is_already_present(self,month, year):
        sal_connection =  pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        sal_cursor = sal_connection.cursor()
        sal_query = 'SELECT pro_month, pro_year FROM profit WHERE pro_month = %s AND pro_year = %s'
        try:
            sal_cursor.execute(sal_query, (month, year))
            sal_data = sal_cursor.fetchone()
            sal_connection.close()
            if sal_data:
                return True
            else:
                return False

        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e), parent= self.__profit_window)
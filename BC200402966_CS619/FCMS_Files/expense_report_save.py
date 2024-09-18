import pymysql as pms
from tkinter import messagebox

class SaveExpenseReport:
    def __init__(self,expense_year, building_rent_amount, building_rent_paid_date,building_rent_month,e_bill_amount,
                 e_bill_paid_date,e_bill_paid_month,ws_bill_amount,ws_bill_paid_date,
                 ws_bill_paid_month,i_bill_amount,i_bill_paid_month,i_bill_paid_date,expense_window):
        # creating class level variables
        self.__expense_year = expense_year
        self.__building_rent_amount = building_rent_amount
        self.__building_rent_paid_date = building_rent_paid_date
        self.__building_rent_month = building_rent_month
        self.__e_bill_amount = e_bill_amount
        self.__e_bill_paid_date = e_bill_paid_date
        self.__e_bill_paid_month = e_bill_paid_month
        self.__ws_bill_amount = ws_bill_amount
        self.__ws_bill_paid_date = ws_bill_paid_date
        self.__ws_bill_paid_month = ws_bill_paid_month
        self.__i_bill_amount = i_bill_amount
        self.__i_bill_paid_month = i_bill_paid_month
        self.__i_bill_paid_date = i_bill_paid_date
        self.__expense_window= expense_window
        #creating table in database
        expense_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        expense_cursor = expense_connection.cursor()
        expense_query = '''
                        CREATE TABLE IF NOT EXISTS expense_report(
                        expense_id INT AUTO_INCREMENT PRIMARY KEY,
                        expense_year INT NOT NULL,
                        building_rent_amount VARCHAR(255) NOT NULL,
                        building_rent_paid_date VARCHAR(255) NOT NULL,
                        building_rent_month VARCHAR(255) NOT NULL,
                        e_bill_amount VARCHAR(255) NOT NULL,
                        e_bill_paid_date VARCHAR(255) NOT NULL,
                        e_bill_paid_month VARCHAR(255) NOT NULL,
                        ws_bill_amount VARCHAR(255) NOT NULL,
                        ws_bill_paid_date VARCHAR(255) NOT NULL,
                        ws_bill_paid_month VARCHAR(255) NOT NULL,
                        i_bill_amount VARCHAR(255) NOT NULL,
                        i_bill_paid_month VARCHAR(255) NOT NULL,
                        i_bill_paid_date VARCHAR(255) NOT NULL
                        )'''
        try:
            expense_cursor.execute(expense_query)
            expense_cursor.close()
            expense_connection.close()

        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e), parent=self.__expense_window)

    def save_expense_report(self):
        expense_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        expense_cursor = expense_connection.cursor()
        expense_query = '''
                        INSERT INTO expense_report(
                        expense_year,
                        building_rent_amount,
                        building_rent_paid_date,
                        building_rent_month,
                        e_bill_amount,
                        e_bill_paid_date,
                        e_bill_paid_month,
                        ws_bill_amount,
                        ws_bill_paid_date,
                        ws_bill_paid_month,
                        i_bill_amount,
                        i_bill_paid_month,
                        i_bill_paid_date)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        '''
        expense_tuple = (
            self.__expense_year,
            self.__building_rent_amount,
            self.__building_rent_paid_date,
            self.__building_rent_month,
            self.__e_bill_amount,
            self.__e_bill_paid_date,
            self.__e_bill_paid_month,
            self.__ws_bill_amount,
            self.__ws_bill_paid_date,
            self.__ws_bill_paid_month,
            self.__i_bill_amount,
            self.__i_bill_paid_month,
            self.__i_bill_paid_date
        )
        try:
            expense_cursor.execute(expense_query, expense_tuple)
            expense_connection.commit()
            expense_cursor.close()
            expense_connection.close()
            messagebox.showinfo('Fitness Club Management System', 'Expense report saved successfully', parent=self.__expense_window)
            return True
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e), parent=self.__expense_window)

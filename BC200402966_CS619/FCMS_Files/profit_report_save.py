import tkinter as tk
from tkinter import ttk, messagebox
import pymysql as pms

class SaveProfitReport:
    def __init__(self, pro_year, pro_month, pro_total_expense, pro_total_income, pro_total_salaries, pro_total_profit):
        self.__pro_year = pro_year
        self.__pro_month = pro_month
        self.__pro_total_expense = pro_total_expense
        self.__pro_total_income = pro_total_income
        self.__pro_total_salaries = pro_total_salaries
        self.__pro_total_profit = pro_total_profit

        # creating table in database
        pro_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        pro_cursor = pro_connection.cursor()
        pro_query = '''
                    CREATE TABLE IF NOT EXISTS profit (
                    pro_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    pro_month VARCHAR(50) NOT NULL,
                    pro_year INT NOT NULL,
                    pro_total_expense INTEGER NOT NULL,
                    pro_total_income INTEGER NOT NULL,
                    pro_total_salaries INTEGER NOT NULL,
                    pro_total_profit INTEGER NOT NULL
                    )
                    '''
        try:
            pro_cursor.execute(pro_query)
            pro_cursor.close()
            pro_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))

    def save_profit_information(self):
        pro_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        pro_cursor = pro_connection.cursor()
        profit_query = '''
                        INSERT INTO profit(
                        pro_month, pro_year,pro_total_expense,pro_total_income,
                        pro_total_salaries, pro_total_profit
                        )
                        values(%s, %s, %s, %s, %s, %s)
                        '''
        pro_tuple= (
            self.__pro_month,self.__pro_year, self.__pro_total_expense, self.__pro_total_income,
            self.__pro_total_salaries, self.__pro_total_profit
        )
        try:
            pro_cursor.execute(profit_query, pro_tuple)
            pro_connection.commit()
            pro_cursor.close()
            pro_connection.close()
            messagebox.showinfo('Fitness Club Management System', 'Profit report saved successfully')
            return True
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))
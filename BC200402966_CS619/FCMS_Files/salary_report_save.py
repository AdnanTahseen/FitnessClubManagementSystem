import tkinter as tk
from tkinter import ttk, messagebox
import pymysql as pms


class SaveSalary:
    def __init__(self, inst_id, inst_name,inst_salary, inst_email, sal_status,
                 sal_month,paid_date, sal_year):
        self.__inst_id = inst_id
        self.__inst_name = inst_name
        self.__inst_salary = inst_salary
        self.__inst_email = inst_email
        self.__sal_status = sal_status
        self.__sal_month = sal_month
        self.__paid_date = paid_date
        self.__sal_year = sal_year

    def create_salary_table(self, salary_window):
        sal_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        sal_cursor = sal_connection.cursor()
        sal_query = '''
                    CREATE TABLE IF NOT EXISTS salary
                    (
                    sal_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    inst_id INT NOT NULL,
                    inst_name VARCHAR(50) NOT NULL,
                    inst_salary VARCHAR(50) NOT NULL,
                    inst_email VARCHAR(50) NOT NULL,
                    sal_status VARCHAR(50) NOT NULL,
                    sal_month VARCHAR(50) NOT NULL,
                    paid_date VARCHAR(50) NOT NULL,
                    sal_year INT NOT NULL
                    )'''
        try:
            sal_cursor.execute(sal_query)
            sal_connection.close()
        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e), parent=salary_window)

    def save_salary_instructor(self, salary_window):
        sal_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        sal_cursor = sal_connection.cursor()
        sal_tuple = (self.__inst_id,self.__inst_name, self.__inst_salary, self.__inst_email, self.__sal_status, self.__sal_month,self.__paid_date, self.__sal_year)
        sal_query = '''
                    INSERT INTO salary
                    (inst_id,
                    inst_name, 
                    inst_salary, 
                    inst_email,
                    sal_status, 
                    sal_month,
                    paid_date,
                    sal_year) 
                     VALUES(%s,%s, %s, %s, %s, %s, %s, %s)'''
        try:
            sal_cursor.execute(sal_query, sal_tuple)
            sal_connection.commit()
            sal_connection.close()
            messagebox.showinfo('Fitness Club Management System', "Salary saved successfully", parent=salary_window)
            return True
        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e), parent=salary_window)



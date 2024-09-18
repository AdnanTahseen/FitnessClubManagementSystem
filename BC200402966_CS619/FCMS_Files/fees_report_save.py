import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as pms

class SaveFeesReport:
    def __init__(self, month, member_id, member_name,member_email, member_workplan, member_fees,status, fees_year,
                 due_date, paid_date):
        self.__month= month
        self.__member_id = member_id
        self.__member_name = member_name
        self.__member_email = member_email
        self.__member_workplan = member_workplan
        self.__member_fees = member_fees
        self.__status = status
        self.__fees_year = fees_year
        self.__due_date = due_date
        self.__paid_date = paid_date

    def create_save_report_fees_table(self):
        fees_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        fees_cursor = fees_connection.cursor()
        fees_query='''
                        CREATE TABLE IF NOT EXISTS save_report_fees(
                        fees_id INT AUTO_INCREMENT PRIMARY KEY, 
                        fees_month VARCHAR(20) NOT NULL, 
                        member_id INT NOT NULL, 
                        member_name VARCHAR(50) NOT NULL, 
                        member_email VARCHAR(50) NOT NULL, 
                        member_workplan VARCHAR(100) NOT NULL, 
                        member_fees VARCHAR(20) NOT NULL, 
                        status VARCHAR(20) NOT NULL,
                        fees_year INT NOT NULL, 
                        due_date VARCHAR(40) NOT NULL,   
                        paid_date VARCHAR(40) NOT NULL  )
                        '''
        if not (self.__month and self.__member_id and self.__member_name and self.__member_email,
               self.__member_workplan, self.__member_fees, self.__status, self.__due_date, self.__paid_date) == '':
            try:
                fees_cursor.execute(fees_query)
                fees_connection.close()
            except Exception as e:
                messagebox.showerror('Fitness Club Management System', e)

        else:
            messagebox.showwarning('Fitness Club Management System', 'One or more fields  is/are empty')
    def save_fees_report(self):
        fees_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        fees_cursor = fees_connection.cursor()
        fees_tuple = (self.__month, self.__member_id, self.__member_name, self.__member_email,
                      self.__member_workplan, self.__member_fees, self.__status, self.__fees_year, self.__due_date,
                      self.__paid_date)
        fees_query = '''
                    INSERT INTO save_report_fees(fees_month, member_id, member_name,
                     member_email, member_workplan, member_fees, status,fees_year, due_date, paid_date)
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'''
        try:
            fees_cursor.execute(fees_query, fees_tuple)
            fees_connection.commit()
            fees_connection.close()
            messagebox.showinfo('Fitness Club Management System', 'Fees report saved successfully')
            return True
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as pms

class SaveBMI:
    def __init__(self, mem_id, mem_bmi):
        self.__mem_id = mem_id
        self.__mem_bmi= mem_bmi

    def create_BMI_table(self):
        bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        bmi_cursor = bmi_connection.cursor()
        bmi_query = '''
                    CREATE TABLE IF NOT EXISTS member_BMI (
                    bmi_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    mem_id INT NOT NULL UNIQUE,
                    mem_bmi FLOAT NOT NULL
                    )
                    '''
        try:
            bmi_cursor.execute(bmi_query)
            bmi_cursor.close()
            bmi_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

    def save_bmi(self, members_window):
        bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        bmi_cursor = bmi_connection.cursor()
        bmi_query = '''
                    INSERT INTO member_BMI (mem_id, mem_bmi)
                    VALUES (%s, %s)
                    '''
        try:
            bmi_cursor.execute(bmi_query, (self.__mem_id, self.__mem_bmi))
            bmi_connection.commit()
            bmi_cursor.close()
            bmi_connection.close()
            messagebox.showinfo('Fitness Club Management System', 'BMI saved successfully!', parent=members_window)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e), parent=members_window)
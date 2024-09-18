import tkinter as tk
from tkinter import ttk
import pymysql as pms
from tkinter import messagebox

class MemberMeasurement:
    def __init__(self, id, name,height, weight,age):
        self.__mem_id = id
        self.__mem_name = name
        self.__mem_height = height
        self.__mem_weight = weight
        self.__mem_age = age


    def create_meaurement_table(self):
        measurement_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        measurement_cursor = measurement_connection.cursor()
        measurement_query = '''CREATE TABLE IF NOT EXISTS members_measurement(
                                measurement_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                mem_id INT NOT NULL ,
                                mem_name VARCHAR(50) NOT NULL,
                                mem_height FLOAT NOT NULL,
                                mem_weight FLOAT NOT NULL,
                                mem_age INT NOT NULL)
                                '''
        measurement_cursor.execute(measurement_query)
        measurement_connection.close()
    def save_member_measurement(self, members_window):
        save_measurement_connection = pms.connect(host='localhost', port=3306,user='root', password='',database='fcms')
        save_measurement_cursor = save_measurement_connection.cursor()
        save_measurement_query = '''INSERT INTO members_measurement(mem_id,mem_name,mem_height,mem_weight,mem_age)
                                    VALUES(%s,%s,%s,%s,%s)'''
        try:
            save_measurement_cursor.execute(save_measurement_query,(self.__mem_id,self.__mem_name,self.__mem_height,self.__mem_weight,self.__mem_age))
            save_measurement_connection.commit()
            save_measurement_connection.close()
            messagebox.showinfo('Fitness Club Management System', 'Member measurement saved successfully', parent=members_window)
            return True
        except :
            messagebox.showerror('Fitness Club Management System', 'Member measurement insertion failed', parent=members_window)

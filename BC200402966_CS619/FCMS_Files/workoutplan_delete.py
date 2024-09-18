import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as pms

class DeleteWorkoutplan:
    def __init__(self, wp_id):
        self.__wp_id = wp_id

    def delete_workoutplan(self):
        wp_del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        wp_del_cursor = wp_del_connection.cursor()
        wp_del_tuple = (self.__wp_id,)
        wp_del_query = '''
                        DELETE FROM workoutplan where wp_id = %s
                        '''

        answer = messagebox.askyesno('Fitness Club Management System','Are you sure you want to delete?')
        if answer:
            try:
                wp_del_cursor.execute(wp_del_query, wp_del_tuple)
                wp_del_connection.commit()
                wp_del_cursor.close()
                wp_del_connection.close()
                messagebox.showinfo('Fitness Club Management System', 'Workoutplan deleted successfully')
            except Exception as e:
                messagebox.showinfo('Fitness Club Management System',e)
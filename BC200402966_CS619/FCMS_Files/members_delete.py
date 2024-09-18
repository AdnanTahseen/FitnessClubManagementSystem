import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql as pms

class DeleteMember:
    def __init__(self,mem_id):
        self.__mem_id=mem_id


    def delete_member(self, members_window):
        mem_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        mem_cursor = mem_connection.cursor()
        mem_query = 'DELETE FROM members WHERE mem_id = %s'
        query_tuple=(self.__mem_id,)
        answer = messagebox.askyesno('Fitness Club Management System', 'Do you really want to delete member?', parent=members_window)
        if answer:
            try:
                mem_cursor.execute(mem_query,query_tuple)
                mem_connection.commit()
                mem_connection.close()
                messagebox.showinfo("Success", "Member Deleted Successfully", parent=members_window)
            except Exception as e:
                messagebox.showerror("Failure", str(e), parent=members_window)
        else:
            pass
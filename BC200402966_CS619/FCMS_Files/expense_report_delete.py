import tkinter as tk
from tkinter import ttk, messagebox
import pymysql as pms

class DeleteExpense:
    def __init__(self, expense_id):
        self.__expense_id = expense_id

    def delete_expense(self, expense_window):
        expense_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        expense_cursor = expense_connection.cursor()
        answer = messagebox.askyesno('Fitness Club Management System', 'Are you sure you want to delete?', parent=expense_window)
        if answer:
            try:
                expense_cursor.execute("DELETE FROM expense_report WHERE expense_id = %s", self.__expense_id)
                expense_connection.commit()
                expense_cursor.close()
                expense_connection.close()
                messagebox.showinfo("Success", "Expense deleted successfully", parent=expense_window)

            except Exception as e:
                messagebox.showerror("Fitness Club Management System", 'Error: '+str(e), parent=expense_window)
        else:
            pass
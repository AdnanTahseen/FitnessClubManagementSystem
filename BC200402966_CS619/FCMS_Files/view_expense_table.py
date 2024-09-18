import tkinter as tk
from tkinter import ttk, messagebox
import pymysql as pms

class ViewExpenseTable:
    def show_expense_table(self):
        expense_window = tk.Toplevel()
        expense_window.title("Expense Table")
        expense_window.geometry('1480x480+70+200')
        expense_window.grab_set()
        expense_window.resizable(False, False)
        expense_window.attributes('-topmost', True)
        expense_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        # creating the table for data display
        expense_table_frame = tk.Frame(expense_window, width=1480, height=450, bg='white', bd=1)
        expense_table_frame.place(x=0, y=0)
        # creating scrollbar for frame
        expense_table_frame_scrollbar = ttk.Scrollbar(expense_table_frame, orient=tk.VERTICAL)
        expense_table_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #creating treeview for data display
        expense_table_treeview = ttk.Treeview(expense_table_frame,show='headings',
                                              yscrollcommand=expense_table_frame_scrollbar.set, height=18)
        expense_table_treeview.pack(fill=tk.BOTH, expand=1)
        # configuring scrollbar for treeview
        expense_table_frame_scrollbar.config(command=expense_table_treeview.yview)
        #table style
        table_style = ttk.Style(expense_table_treeview)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font='arial 11 italic bold',foreground='snow', background='maroon2')
        table_style.configure('Treeview', font='arial 9 italic ', background='lightgrey')
        # creating columns for treeview
        expense_table_treeview['columns'] =('ExpenseID','ExpenseYear','BuildingRentAmount','BuildingRentPaidDate', 'BuildingRentMonth',
                                            'ElectricityBillAmount','ElectricityBillPaidDate', 'ElectricityBillMonth',
                                            'WaterBillAmount','WaterBillPaidDate', 'WaterBillMonth',
                                            'InternetBillAmount', 'InternetBillMonth','InternetBillPaidDate')
        # creating headings for table
        expense_table_treeview.heading('ExpenseID',text='Expense ID', anchor=tk.CENTER)
        expense_table_treeview.heading('ExpenseYear',text='Expense Year', anchor=tk.CENTER)
        expense_table_treeview.heading('BuildingRentAmount',text='Building Rent', anchor=tk.CENTER)
        expense_table_treeview.heading('BuildingRentPaidDate',text='B-R Paid Date', anchor=tk.CENTER)
        expense_table_treeview.heading('BuildingRentMonth',text='B-R Month', anchor=tk.CENTER)
        expense_table_treeview.heading('ElectricityBillAmount',text='Electricity Bill', anchor=tk.CENTER)
        expense_table_treeview.heading('ElectricityBillPaidDate',text='E-B Paid Date', anchor=tk.CENTER)
        expense_table_treeview.heading('ElectricityBillMonth',text='E-B Month', anchor=tk.CENTER)
        expense_table_treeview.heading('WaterBillAmount',text='Water Bill', anchor=tk.CENTER)
        expense_table_treeview.heading('WaterBillPaidDate',text='W-B Paid Date', anchor=tk.CENTER)
        expense_table_treeview.heading('WaterBillMonth',text='W-B Month', anchor=tk.CENTER)
        expense_table_treeview.heading('InternetBillAmount',text='Internet Bill', anchor=tk.CENTER)
        expense_table_treeview.heading('InternetBillMonth',text='I-B Month', anchor=tk.CENTER)
        expense_table_treeview.heading('InternetBillPaidDate',text='I-B Paid Date', anchor=tk.CENTER)
        # creating column and settig their width
        expense_table_treeview.column('ExpenseID', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('ExpenseYear', width=110, minwidth=110, anchor=tk.CENTER)
        expense_table_treeview.column('BuildingRentAmount', width=110, minwidth=110, anchor=tk.CENTER)
        expense_table_treeview.column('BuildingRentPaidDate', width=110, minwidth=110, anchor=tk.CENTER)
        expense_table_treeview.column('BuildingRentMonth', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('ElectricityBillAmount', width=110, minwidth=110, anchor=tk.CENTER)
        expense_table_treeview.column('ElectricityBillPaidDate', width=110, minwidth=110, anchor=tk.CENTER)
        expense_table_treeview.column('ElectricityBillMonth', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('WaterBillAmount', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('WaterBillPaidDate', width=110, minwidth=110, anchor=tk.CENTER)
        expense_table_treeview.column('WaterBillMonth', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('InternetBillAmount', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('InternetBillMonth', width=100, minwidth=100, anchor=tk.CENTER)
        expense_table_treeview.column('InternetBillPaidDate', width=100, minwidth=100, anchor=tk.CENTER)
        # populating the table with data
        table_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        table_cursor = table_connection.cursor()
        table_query = 'SELECT * FROM expense_report'
        try:
            table_cursor.execute(table_query)
            for row in table_cursor:
                expense_table_treeview.insert(parent='', index='end', text='', values=row)

            table_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e), parent=expense_window)

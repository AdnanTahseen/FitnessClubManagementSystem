import tkinter as tk
from tkinter import ttk
import pymysql as pms


class ViewInstructorTable:

    def __init__(self):
        pass

    def show_instructor_table(self):
        inst_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        inst_cursor = inst_connection.cursor()
        inst_query = 'SELECT * FROM instructor'
        inst_cursor.execute(inst_query)
        # creating frame for data table

        inst_root = tk.Toplevel()
        inst_root.title('Instructor Table')
        inst_root.geometry('1240x500+100+100')
        inst_root.grab_set()
        inst_root.resizable(False, False)
        inst_root.wm_attributes('-topmost', True)
        inst_root.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))

        # creating vertical scrollbar
        inst_vt_table_scrollbar = ttk.Scrollbar(inst_root, orient=tk.VERTICAL)
        inst_vt_table_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating table
        inst_table = ttk.Treeview(inst_root, show='headings', yscrollcommand=inst_vt_table_scrollbar.set, height=500)
        inst_table.place(x=0, y=0)
        # configuring the scrollbar
        inst_vt_table_scrollbar.config(command=inst_table.yview)
        # creating columns for table
        inst_table['columns'] = ('InstID', 'FirstName','LastName','Email','JoiningDate', 'Address',
                               'Salary', 'Qualification', 'Age', 'Specialization', 'AssignedClass', 'Contact')
        table_style=ttk.Style(inst_table)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font=('helvetica', 11, 'bold'), foreground='snow', background='maroon2')
        table_style.configure('Treeview', font=('helvetica', 9, 'italic'), foreground='black',
                              background='silver')
        table_style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'purple4')])

        inst_table.heading('InstID', text='ID', anchor=tk.CENTER)
        inst_table.heading('FirstName', text='First Name', anchor=tk.CENTER)
        inst_table.heading('LastName', text='Last Name', anchor=tk.CENTER)
        inst_table.heading('Email', text='Email', anchor=tk.CENTER)
        inst_table.heading('JoiningDate', text='Joining Date', anchor=tk.CENTER)
        inst_table.heading('Address', text='Address', anchor=tk.CENTER)
        inst_table.heading('Salary', text='Salary', anchor=tk.CENTER)
        inst_table.heading('Qualification', text='Qualification', anchor=tk.CENTER)
        inst_table.heading('Age', text='Age', anchor=tk.CENTER)
        inst_table.heading('Specialization', text='Specialization', anchor=tk.CENTER)
        inst_table.heading('AssignedClass', text='Assigned Class', anchor=tk.CENTER)
        inst_table.heading('Contact', text='Contact', anchor=tk.CENTER)
        inst_table.column('InstID',width=40,minwidth=40, anchor=tk.CENTER)
        inst_table.column('FirstName',width=110,minwidth=110, anchor=tk.CENTER)
        inst_table.column('LastName', width=110,minwidth=110,anchor=tk.CENTER)
        inst_table.column('Email',width=150,minwidth=150, anchor=tk.CENTER)
        inst_table.column('JoiningDate', width=100,minwidth=100,anchor=tk.CENTER)
        inst_table.column('Address', width=170,minwidth=170,anchor=tk.CENTER)
        inst_table.column('Salary', width=80,minwidth=80,anchor=tk.CENTER)
        inst_table.column('Qualification',width=100,minwidth=100, anchor=tk.CENTER)
        inst_table.column('Age', width=50,minwidth=50,anchor=tk.CENTER)
        inst_table.column('Specialization', width=100,minwidth=100,anchor=tk.CENTER)
        inst_table.column('AssignedClass', width=120,minwidth=120,anchor=tk.CENTER)
        inst_table.column('Contact', width=90,minwidth=90,anchor=tk.CENTER)

        inst_table.tag_configure('evenrow', background='lightblue')
        inst_table.tag_configure('oddrow', background='lightyellow')

        global count
        count = 0
        # inserting data in table
        for row in inst_cursor:
            if count % 2 == 0:
                 inst_table.insert('', 'end', text='',
                              values=(row[0], row[1], row[2],row[3],row[4],row[5],row[6],
                                      row[7], row[8], row[9], row[10], row[11]), tags=('evenrow',))
            else:
                inst_table.insert(parent='', index='end', text='',
                                  values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                          row[7], row[8], row[9], row[10], row[11]), tags=('oddrow',)
                                  )
            count = count + 1


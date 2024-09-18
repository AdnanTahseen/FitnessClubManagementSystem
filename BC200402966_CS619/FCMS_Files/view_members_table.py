import tkinter as tk
from tkinter import ttk
import pymysql as pms


class ViewMemberTable:

    def __init__(self):
        pass

    def show_member_table(self):
        mem_root = tk.Toplevel()
        mem_root.title('Members Information Table')
        mem_root.geometry('1050x500+250+150')
        mem_root.grab_set()
        mem_root.resizable(0, 0)
        mem_root.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))

        # creating vertical scrollbar
        mem_vt_table_scrollbar = ttk.Scrollbar(mem_root, orient=tk.VERTICAL)
        mem_vt_table_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating table
        mem_table = ttk.Treeview(mem_root, show='headings',height=500, yscrollcommand=mem_vt_table_scrollbar.set)
        mem_table.place(x=0, y=0)
        # configuring the scrollbar
        mem_vt_table_scrollbar.config(command=mem_table.yview)
        # creating columns for table
        mem_table['columns'] = ('memID', 'FirstName','LastName','Email','Contact','Address','Workoutplan','JoiningDate','Assignedfees')
        table_style=ttk.Style(mem_table)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font=('helvetica', 11, 'bold'), foreground='snow', background='maroon2')
        table_style.configure('Treeview', font=('helvetica', 9, 'italic'), foreground='black',
                              background='silver')
        table_style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'purple4')])

        mem_table.heading('memID', text='ID', anchor=tk.CENTER)
        mem_table.heading('FirstName', text='First Name', anchor=tk.CENTER)
        mem_table.heading('LastName', text='Last Name', anchor=tk.CENTER)
        mem_table.heading('Email', text='Email', anchor=tk.CENTER)
        mem_table.heading('Contact', text='Contact', anchor=tk.CENTER)
        mem_table.heading('Address', text='Address', anchor=tk.CENTER)
        mem_table.heading('Workoutplan', text='Workoutplan', anchor=tk.CENTER)
        mem_table.heading('JoiningDate', text='Joining Date', anchor=tk.CENTER)
        mem_table.heading('Assignedfees', text='Assigned Fees', anchor=tk.CENTER)

        mem_table.column('memID',width=40,minwidth=40, anchor=tk.CENTER)
        mem_table.column('FirstName',width=110,minwidth=110, anchor=tk.CENTER)
        mem_table.column('LastName', width=110,minwidth=110,anchor=tk.CENTER)
        mem_table.column('Email',width=150,minwidth=150, anchor=tk.CENTER)
        mem_table.column('Contact', width=90,minwidth=90,anchor=tk.CENTER)
        mem_table.column('Address', width=170,minwidth=170,anchor=tk.CENTER)
        mem_table.column('Workoutplan', width=140,minwidth=140,anchor=tk.CENTER)
        mem_table.column('JoiningDate', width=100,minwidth=100,anchor=tk.CENTER)
        mem_table.column('Assignedfees', width=120,minwidth=120,anchor=tk.CENTER)

        mem_table.tag_configure('evenrow', background='lightblue')
        mem_table.tag_configure('oddrow', background='lightyellow')

        mem_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        mem_cursor = mem_connection.cursor()
        mem_query = 'SELECT * FROM members'
        mem_cursor.execute(mem_query)
        global count
        count = 0
        # inserting data in table
        for row in mem_cursor:
            if count % 2 == 0:
                 mem_table.insert(parent='', index='end', text='',
                              values=(row[0], row[1], row[2],row[3],row[4],row[5],row[6],
                                      row[7], row[8]), tags=('evenrow',))
            else:
                mem_table.insert(parent='', index='end', text='',
                                  values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                          row[7], row[8]), tags=('oddrow',)
                                  )
            count = count + 1


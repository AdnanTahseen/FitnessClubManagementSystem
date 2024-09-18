import tkinter as tk
from tkinter import ttk
import pymysql as pms

class ViewBMI:
    def __init__(self):
        pass

    def show_bmi_table(self):
        bmi_root = tk.Toplevel()
        bmi_root.title('BMI Table')
        bmi_root.geometry('320x300+500+350')
        bmi_root.grab_set()
        bmi_root.resizable(0, 0)
        bmi_root.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))

        # creating vertical scrollbar
        bmi_vt_table_scrollbar = ttk.Scrollbar(bmi_root, orient=tk.VERTICAL)
        bmi_vt_table_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating table
        bmi_table = ttk.Treeview(bmi_root, show='headings', yscrollcommand=bmi_vt_table_scrollbar.set, height=300)
        bmi_table.place(x=0, y=0)
        # configuring the scrollbar
        bmi_vt_table_scrollbar.config(command=bmi_table.yview)
        # creating columns for table
        bmi_table['columns'] = ('bmi_id','mem_id','mem_bmi')
        table_style=ttk.Style(bmi_table)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font=('helvetica', 11, 'bold'), foreground='snow', background='maroon2')
        table_style.configure('Treeview', font=('helvetica', 9, 'italic'), foreground='black',
                              background='silver')
        table_style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'purple4')])

        bmi_table.heading('bmi_id', text='ID', anchor=tk.CENTER)
        bmi_table.heading('mem_id', text='Member ID', anchor=tk.CENTER)
        bmi_table.heading('mem_bmi', text='BMI', anchor=tk.CENTER)

        bmi_table.column('bmi_id', width=100, minwidth=100, anchor=tk.CENTER)
        bmi_table.column('mem_id', width=100, minwidth=100, anchor=tk.CENTER)
        bmi_table.column('mem_bmi', width=100, minwidth=100, anchor=tk.CENTER)
        # creating tags
        bmi_table.tag_configure('oddrow', background='white')
        bmi_table.tag_configure('eventrow', background='lightgray')
        #  populating the bmi table
        bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        bmi_cursor = bmi_connection.cursor()
        bmi_query = 'SELECT * FROM member_bmi'
        bmi_cursor.execute(bmi_query)
        global count
        count = 0
        # inserting data in table
        for row in bmi_cursor:
            if count % 2 == 0:
                bmi_table.insert(parent='', index='end', text='',tags='eventrow',
                                 values=(row[0], row[1], row[2]))
            else:
                bmi_table.insert(parent='', index='end', text='',tags='oddrow',
                                 values=(row[0], row[1], row[2]))
            count += 1

        bmi_cursor.close()
        bmi_connection.close()



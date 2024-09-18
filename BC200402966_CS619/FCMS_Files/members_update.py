from tkcalendar import *
import pymysql as pms
from tkinter import messagebox

class UpdateMembers:
    def __init__(self,mem_id,fname, lname,email,contact,address,workoutplan,joiningdate,assignedfees):
        self.__mem_id = mem_id
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__contact = contact
        self.__address = address
        self.__workoutplan = workoutplan
        self.__joiningdate = joiningdate
        self.__assignedfees = assignedfees

    def update_member(self, members_window):
        # creating conneciton
        mem_up_connection = pms.connect(host='localhost', user='root', password='', database='fcms')
        mem_up_cursor = mem_up_connection.cursor()
        # creating query
        upd_mem_query = (
                    ''' UPDATE members SET mem_fname=%s, mem_lname=%s, mem_email=%s,mem_contact=%s,
                    mem_address=%s, mem_workoutplan=%s,mem_joiningdate=%s, 
                    mem_assignedfees=%s WHERE mem_id=%s
                    ''')
        query_tuple=(self.__fname, self.__lname, self.__email, self.__contact, self.__address,
                     self.__workoutplan, self.__joiningdate, self.__assignedfees, self.__mem_id)
        if not (self.__mem_id and self.__fname and self.__lname and self.__email and
                self.__contact and self.__address and self.__workoutplan and self.__joiningdate and self.__assignedfees) =='':
            try:
                mem_up_cursor.execute(upd_mem_query, query_tuple)
                mem_up_connection.commit()
                mem_up_connection.close()
                messagebox.showinfo('Fitness Club Management System', "Data updated successfully", parent = members_window)
            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e), parent= members_window)
        else:
            messagebox.showerror('Fitness Club Management System', "Please fill in the all the fields", parent=members_window)
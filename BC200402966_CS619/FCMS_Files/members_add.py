from tkinter import messagebox
import pymysql as pms

class AddMembers:
    def __init__(self, fname, lname, email, contact, address, workoutplan,
                 joiningdate, assignedfees):
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__contact = contact
        self.__address = address
        self.__workoutplan = workoutplan
        self.__joiningdate = joiningdate
        self.__assignedfees = assignedfees
    def create_add_member_table(self):
        member_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        member_cursor = member_connection.cursor()
        member_create_query = '''
                            CREATE TABLE IF NOT EXISTS members(
                            mem_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                            mem_fname VARCHAR(100) NOT NULL,
                            mem_lname VARCHAR(100) NOT NULL,
                            mem_email VARCHAR(100) NOT NULL UNIQUE,
                            mem_contact VARCHAR(100) NOT NULL UNIQUE,
                            mem_address VARCHAR(200) NOT NULL,
                            mem_workoutplan VARCHAR(100) NOT NULL,
                            mem_joiningdate VARCHAR(100) NOT NULL,
                            mem_assignedfees VARCHAR(100) NOT NULL
                            )
                            '''
        try:
            member_cursor.execute(member_create_query)
            member_connection.close()
        except Exception as e:
            messagebox.showinfo('Fitness Club Management System', str(e))

    def add_members_information(self, members_window):
        # self.__create_add_member_table()
        member_add_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        member_add_cursor = member_add_connection.cursor()
        member_add_tuple = (self.__fname, self.__lname, self.__email, self.__contact, self.__address,
                            self.__workoutplan, self.__joiningdate, self.__assignedfees)
        member_add_query='''
                        INSERT INTO members(mem_fname, mem_lname, mem_email, mem_contact, mem_address, mem_workoutplan,
                         mem_joiningdate, mem_assignedfees) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
                        '''
        if not (self.__fname and self.__lname and self.__email and self.__contact and self.__address and
                self.__workoutplan and self.__joiningdate and self.__assignedfees) == '':
            try:
                member_add_cursor.execute(member_add_query, member_add_tuple)
                member_add_connection.commit()
                member_add_connection.close()
                messagebox.showinfo('Fitness Club Management System',"New member added successfully", parent=members_window)
                return True
            except :
                messagebox.showinfo('Fitness Club Management System', "Data insertion failed", parent=members_window)
        else:
            messagebox.showinfo('Fitness Club Management System', 'Please fill all fields with information', parent=members_window)

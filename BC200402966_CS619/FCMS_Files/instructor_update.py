import pymysql as pms
from tkinter import messagebox
class UpdateInstructor:
    def __init__(self,id,fname, lname,email,joiningdate,address,contact,salary,qualification,age,specialization,assignclass):
        self.__upd_id = int(id)
        self.__fname=fname
        self.__lname=lname
        self.__email=email
        self.__joiningdate=joiningdate
        self.__address=address
        self.__salary=salary
        self.__qualification=qualification
        self.__age=age
        self.__specialization=specialization
        self.__assignclass=assignclass
        self.__contact=contact

    def update_instructor_information(self, inst_window):
        inst_upd_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        inst_upd_cursor = inst_upd_connection.cursor()
        inst_upd_tuple=(
            self.__fname, self.__lname, self.__email, self.__joiningdate, self.__address,
            self.__salary,self.__qualification, self.__age,
            self.__specialization, self.__assignclass, self.__contact, self.__upd_id
        )
        inst_upd_query = '''UPDATE instructor SET inst_fname = %s, inst_lname = %s, inst_email = %s, 
                        inst_joiningdate = %s, inst_address = %s,
                         inst_salary = %s, inst_qualification = %s,inst_age = %s, 
                        inst_specialization = %s, inst_assignedclass = %s, inst_contact = %s WHERE inst_id = %s'''

        if not (self.__fname and self.__lname and self.__email and self.__joiningdate and self.__address and
            self.__salary and self.__qualification and self.__age and
            self.__specialization and self.__assignclass and self.__contact and self.__upd_id) == '':
            answer = messagebox.askyesno('Fitness Club Management System', 'Are you sure you want to update the information?', parent=inst_window)
            if answer:
                try:
                    inst_upd_cursor.execute(inst_upd_query, inst_upd_tuple)
                    inst_upd_connection.commit()
                    inst_upd_connection.close()
                    messagebox.showinfo("Success", "Instructor information updated successfully", parent=inst_window)
                except Exception as e:
                    messagebox.showerror("Failure", str(e), parent=inst_window)
            else:
                pass
        else:
            messagebox.showwarning("Fitness Club Management System", 'Input text fields are empty', parent=inst_window)
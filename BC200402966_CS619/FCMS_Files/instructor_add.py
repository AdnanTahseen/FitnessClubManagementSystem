import pymysql as pms
from tkinter import messagebox
class AddInstructor:
    def __init__(self,fname, lname,email,joiningdate,address,contact,salary,qualification,age,specialization,assignclass):
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

    def createinstructortable(self):
        instructor_add_connection1 = pms.connect(host='localhost', user='root', password='', database='fcms')
        instructor_add_cursor1 = instructor_add_connection1.cursor()
        instructor_add_cursor1.execute(
            '''
            CREATE TABLE IF NOT EXISTS instructor(
            inst_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY ,
            inst_fname VARCHAR(100) NOT NULL,
            inst_lname VARCHAR(100) NOT NULL,
            inst_email VARCHAR(100) NOT NULL UNIQUE,
            inst_joiningdate VARCHAR(100) NOT NULL,
            inst_address VARCHAR(100) NOT NULL,
            inst_salary VARCHAR(100) NOT NULL,
            inst_qualification VARCHAR(100) NOT NULL,
            inst_age INT NOT NULL,
            inst_specialization VARCHAR(100) NOT NULL,
            inst_assignedclass VARCHAR(100) NOT NULL,
            inst_contact VARCHAR(100) NOT NULL UNIQUE
            )
            ''')
        instructor_add_connection1.close()

    def addinstructorinformation(self, inst_window):
        instructor_add_connection2=pms.connect(host='localhost', user='root', password='', database='fcms')
        instructor_add_cursor2=instructor_add_connection2.cursor()
        # creating tuple for saving information
        info_tuple=(self.__fname, self.__lname, self.__email, self.__joiningdate, self.__address, self.__salary,
                    self.__qualification, self.__age, self.__specialization, self.__assignclass, self.__contact)
        # creating query for inserting information
        insert_query = '''
        INSERT INTO instructor(
        inst_fname, inst_lname,inst_email,inst_joiningdate,inst_address, inst_salary, inst_qualification,
        inst_age,inst_specialization,inst_assignedclass, inst_contact
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        try:
            instructor_add_cursor2.execute(insert_query,info_tuple)
            instructor_add_connection2.commit()
            messagebox.showinfo("Success", "Instructor added successfully", parent =inst_window)
            instructor_add_connection2.close()
            return True
        except Exception as e:
            messagebox.showerror("Failure", str(e), parent =inst_window)
            return False
from tkinter import messagebox
import pymysql as pms

class InstructorDelete:
    def __init__(self, id_val):
        self.__id_value = id_val

    def delete_instructor_information(self, inst_window):
        inst_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        inst_cursor = inst_connection.cursor()
        inst_del_tuple = (self.__id_value,)
        inst_query ="DELETE FROM instructor WHERE inst_id = %s"
        answer = messagebox.askyesno('Fitness Club Management Sytem', "Do you really want to delete the instructor?", parent=inst_window)
        if answer:
            try:
                    inst_cursor.execute(inst_query, inst_del_tuple)
                    inst_connection.commit()
                    inst_connection.close()
                    messagebox.showinfo("Success", "Instructor Deleted Successfully", parent=inst_window)
                    return True
            except :
                    messagebox.showinfo("Fitness Club Management System", "Member deletion failed", parent=inst_window)
                    return False
        else:
            pass
        # messagebox.showinfo("FCMS", self.__id_value)

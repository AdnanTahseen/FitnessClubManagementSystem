from tkinter import messagebox
import pymysql as pms

class EditWorkoutplan:
    def __init__(self, wp_id, wp_name, wp_category, wp_description):
        self.__wp_id = wp_id
        self.__wp_name = wp_name
        self.__wp_category = wp_category
        self.__wp_description = wp_description

    def update_workoutplan(self,addWPframe):
        wp_upd_connection = pms.connect(host='localhost',port=3306, user='root', password='', database='fcms')
        wp_upd_cursor = wp_upd_connection.cursor()
        if not(self.__wp_name and self.__wp_category and self.__wp_description and self.__wp_id)=="":
            wp_upd_tuple = (
                self.__wp_name, self.__wp_category, self.__wp_description, self.__wp_id
            )
            wp_upd_query = '''UPDATE workoutplan SET wp_name = %s, wp_category = %s, 
                            wp_description= %s WHERE wp_id = %s'''
            try:
                wp_upd_cursor.execute(wp_upd_query, wp_upd_tuple)
                wp_upd_connection.commit()
                wp_upd_cursor.close()
                wp_upd_connection.close()
                messagebox.showinfo(title='Fitness Club Management System', message='Workoutplan updated successfully',parent=addWPframe)
                return True
            except Exception as e:
                messagebox.showinfo(title='Fitness Club Management System', message=str(e),parent=addWPframe)
        else:
            messagebox.showerror(title="Fitness Club Management System",message='Please fill in all the fields', parent=addWPframe)
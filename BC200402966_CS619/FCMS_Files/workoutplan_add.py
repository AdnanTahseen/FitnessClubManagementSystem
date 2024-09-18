from tkinter import messagebox
import pymysql as pms

class AddWorkoutplan:
    def __init__(self, wp_name, wp_category, wp_description):
        self.__wp_name = wp_name
        self.__wp_category = wp_category
        self.__wp_description = wp_description

    def create_workoutplan(self):
        workoutplan_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        workoutplan_cursor = workoutplan_connection.cursor()
        workoutplan_query='''
                          CREATE TABLE IF NOT EXISTS workoutplan(
                          wp_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                          wp_name VARCHAR(100) NOT NULL,
                          wp_category VARCHAR(100) NOT NULL,
                          wp_description VARCHAR(150) NOT NULL
                          )  
                          '''
        try:
            workoutplan_cursor.execute(workoutplan_query)
            workoutplan_cursor.close()
            workoutplan_connection.close()

        except Exception as e:
            messagebox.showerror('Fitness Club Management  System', e)

    def save_workoutplan(self,addWPframe):
        workoutplan_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        workoutplan_cursor = workoutplan_connection.cursor()
        if not (self.__wp_name and self.__wp_category and self.__wp_description)=="":
            workoutplan_tuple =(self.__wp_name, self.__wp_category, self.__wp_description)
            workoutplan_query = '''
                              INSERT INTO workoutplan(wp_name, wp_category, wp_description)
                              VALUES (%s, %s,%s)
                              '''
            try:
                workoutplan_cursor.execute(workoutplan_query, workoutplan_tuple)
                workoutplan_connection.commit()
                workoutplan_cursor.close()
                workoutplan_connection.close()
                messagebox.showinfo(title='Fitness Club Management System', message='Workout plan saved successfully', parent=addWPframe)
                return True
            except Exception as e:
                messagebox.showerror(title='Fitness Club Management  System', message=str(e), parent=addWPframe)
        else:
            messagebox.showerror(title="Fitness Club Management System", message='Fields are empty. Please input some data',parent=addWPframe)
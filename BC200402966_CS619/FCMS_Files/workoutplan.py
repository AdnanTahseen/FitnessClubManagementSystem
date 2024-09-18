import tkinter as tk
from tkinter import ttk
from FCMS_Files.workoutplan_add import *
from FCMS_Files.workoutplan_edit import *
from FCMS_Files.workoutplan_delete import *
import pymysql as pms

class Workplan:

    def showWorkoutPlanManagement(self):
        workout_window = tk.Toplevel()
        workout_window.title('Workout Plan Management')
        workout_window.geometry('1200x650+320+160')
        workout_window.resizable(False , False)
        workout_window.grab_set()
        workout_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        addWPframe = tk.Frame(workout_window, width=1200, height=650, bg='lightgrey',
                                     bd=3)
        addWPframe.place(x=0, y=0)
        addWPlbl = tk.Label(addWPframe, text='WORKOUT PLAN PANEL',
                                   font=('Arial', 18, 'bold', 'italic'),
                                   fg='floralwhite', bg='blue', width=84, height=2)
        addWPlbl.place(x=-5, y=-5)
        # calling add function
        self.__showAddWorkplanPanel(addWPframe)
        # calling update function
        self.__showUpdateWorkplanPanel(addWPframe)
        # calling delete function
        self.__showDeleteWorkplanPanel(addWPframe)
        # creating table for workplan data
        wp_tableframe = tk.Frame(addWPframe, width=1050, height=300,
                                       bg='white', bd=1,
                                       relief=tk.SOLID)
        wp_tableframe.place(x=30, y=390)
        # creating scrollbar for workout table
        wp_vt_scrollbar= ttk.Scrollbar(wp_tableframe)
        wp_vt_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating treeview for workout plan
        wp_table = ttk.Treeview(wp_tableframe, show='headings', yscrollcommand=wp_vt_scrollbar.set, height=8)
        wp_table.place(x=0, y=0)
        # configuring the scrollbar
        wp_vt_scrollbar.config(command=wp_table.yview)
        # setting style for table
        table_style = ttk.Style(wp_table)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font=('helvetica', 11, 'bold'), foreground='snow', background='maroon2')
        table_style.configure('Treeview', font=('helvetica', 9, 'italic'), foreground='black', background='lightgrey')

        # creating columns for workout plan table
        wp_table['columns'] = ('WorkoutID', 'WorkoutName', 'WorkoutCategory', 'WorkoutDescription')
        wp_table.heading('WorkoutID', text='WP ID', anchor=tk.CENTER)
        wp_table.heading('WorkoutName', text='Workout Name', anchor=tk.CENTER)
        wp_table.heading('WorkoutCategory', text='Workplan Sub Category', anchor=tk.CENTER)
        wp_table.heading('WorkoutDescription', text='Description', anchor=tk.CENTER)
        # adding data to workout plan table
        wp_table.column('WorkoutID', width=100, minwidth=100, anchor=tk.CENTER)
        wp_table.column('WorkoutName',width=200, minwidth=200, anchor=tk.CENTER)
        wp_table.column('WorkoutCategory',width=300, minwidth=300, anchor=tk.CENTER)
        wp_table.column('WorkoutDescription',width=500,minwidth=500, anchor=tk.CENTER)
        wp_table.pack(fill=tk.BOTH, expand=1)
        # adding data to workout plan table
        connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = connection.cursor()
        table_query = 'SELECT * FROM workoutplan'
        table_cursor.execute(table_query)
        for row in table_cursor:
            wp_table.insert(parent='', index='end', text='', values=row)
        table_cursor.close()
        connection.close()
        # refresh table button
        refresh_table_btn = tk.Button(addWPframe, text='Refresh Table', fg='snow', bg='maroon2', padx=15, pady=6,
                                      activebackground='mediumvioletred', width=30)
        refresh_table_btn.place(x=450, y=330)
        refresh_table_btn.config(command=lambda: self.__auto_refresh_table(wp_table))

    def __auto_refresh_table(self, wp_table):
        for item in wp_table.get_children():
            wp_table.delete(item)
        #populating the table
        connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = connection.cursor()
        table_query = 'SELECT * FROM workoutplan'
        table_cursor.execute(table_query)
        for row in table_cursor:
            wp_table.insert(parent='', index='end', text='', values=row)
        table_cursor.close()
        connection.close()

    def __send_wp_for_save(self,addWPframe):
        add_wp = AddWorkoutplan(self.__wp_add_workout_name_tb.get(), self.__wp_add_workout_category_tb.get(),
                                self.__wp_add_workout_description_tb.get(1.0 , tk.END))
        add_wp.create_workoutplan()  # creating table in database
        response=add_wp.save_workoutplan(addWPframe)
        if response == 1:
            self.__wp_add_workout_name_tb.delete(0, 'end')
            self.__wp_add_workout_category_tb.delete(0, 'end')
            self.__wp_add_workout_description_tb.delete(1.0, 'end')
        else:
            pass
    def __showAddWorkplanPanel(self, addWPframe):

        WP_add_upperframe = tk.LabelFrame(addWPframe, width=360, height=240, text='Add Workoutplan: ', font='arial 11 italic ',
                                                       bg='lightgrey', fg='maroon2')
        WP_add_upperframe.place(x=20, y=80)
        # workout name
        wp_add_workout_name_lbl=tk.Label(WP_add_upperframe, text='Workoutplan name: ', font=('arial',9, 'italic'),bg='lightgrey')
        wp_add_workout_name_lbl.place(x=20, y=20)
        self.__wp_add_workout_name_tb=tk.Entry(WP_add_upperframe, width=25,font=('arial',9, 'italic'))
        self.__wp_add_workout_name_tb.place(x=160, y=20)
        # workout date
        wp_add_workout_category_lbl=tk.Label(WP_add_upperframe, text='Workoutplan Category: ', font=('arial',9, 'italic'),bg='lightgrey')
        wp_add_workout_category_lbl.place(x=20, y=60)
        self.__wp_add_workout_category_tb=tk.Entry(WP_add_upperframe, width=25,font=('arial',9, 'italic'))
        self.__wp_add_workout_category_tb.place(x=160, y=60)
        # workout description
        wp_add_workout_description_lbl=tk.Label(WP_add_upperframe, text='Workoutplan description: ', font=('arial',9, 'italic'),bg='lightgrey')
        wp_add_workout_description_lbl.place(x=20, y=100)
        self.__wp_add_workout_description_tb=tk.Text(WP_add_upperframe,height=4, width=25,font=('arial',9, 'italic'))
        self.__wp_add_workout_description_tb.place(x=160, y=100)
        # button for saving workoutplan in database
        WP_add_saveBtn = tk.Button(WP_add_upperframe, text='Save Plan',
                                                       width=18, fg='blue',
                                                       bg='lightblue', font=('arial',10, 'italic'))
        WP_add_saveBtn.place(x=187, y=180)
        WP_add_saveBtn.config(command=lambda :self.__send_wp_for_save(addWPframe))

    def __auto_refresh_values(self,wp_delete_selection_cb):
        delete_wp_list = []
        connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = connection.cursor()
        table_query = 'SELECT wp_id FROM workoutplan'
        table_cursor.execute(table_query)
        for row in table_cursor:
            delete_wp_list.append(row[0])
        table_cursor.close()
        connection.close()
        delete_wp_list.sort()
        wp_delete_selection_cb['values'] = delete_wp_list
        wp_delete_selection_cb.after(200, lambda: self.__auto_refresh_values(wp_delete_selection_cb))
    def __showDeleteWorkplanPanel(self,addWPframe):
        wp_del_upperframe = tk.LabelFrame(addWPframe, width=350, height=150,text="Delete Workoutplan", font='arial 11 italic',
                                            bg='lightgrey', fg='maroon2')
        wp_del_upperframe.place(x=400, y=80)
        # selection id
        wp_del_selection_lbl = tk.Label(wp_del_upperframe, text='Select Workout plan ID: ', bg='lightgrey',font=('arial',9,'italic'))
        wp_del_selection_lbl.place(x=20, y=20)
        self.__wp_delete_selection_cb = ttk.Combobox(wp_del_upperframe,width=15)
        self.__wp_delete_selection_cb.place(x=175, y=20)
        self.__auto_refresh_values(self.__wp_delete_selection_cb)
        self.__wp_delete_selection_cb.current(0)
        # Button for deletion
        wp_del_Btn = tk.Button(wp_del_upperframe, text='Delete Plan',
                                          width=18, fg='blue',
                                          bg='lightblue', font=('arial', 10, 'italic'))
        wp_del_Btn.place(x=133, y=60)
        # creating the object of class
        if self.__wp_delete_selection_cb.current() != -1:
            del_wp = DeleteWorkoutplan(self.__wp_delete_selection_cb.get())
            wp_del_Btn.config(command = del_wp.delete_workoutplan)

    def __wp_upd_selectionID_Auto_update(self, wp_upd_selection_cb):
        wp_upd_selection_list = []
        connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        table_cursor = connection.cursor()
        table_query = 'SELECT wp_id FROM workoutplan'
        table_cursor.execute(table_query)
        for row in table_cursor:
            wp_upd_selection_list.append(row[0])

        wp_upd_selection_list.sort()
        wp_upd_selection_cb['values'] = wp_upd_selection_list
        table_cursor.close()
        connection.close()
        wp_upd_selection_cb.after(200, lambda :self.__wp_upd_selectionID_Auto_update(wp_upd_selection_cb))

    def __get_values_for_edit(self,e):
        currentValue = self.__wp_upd_selection_cb.get()
        self.__wp_upd_workout_name_tb.delete(0, 'end')
        self.__wp_upd_workout_category_tb.delete(0, 'end')
        self.__wp_upd_workout_description_tb.delete(1.0, 'end')
        edit_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        edit_cursor = edit_connection.cursor()
        edit_query = 'SELECT * FROM workoutplan WHERE wp_id = {edit_id}'.format(edit_id=currentValue)
        try:
            edit_cursor.execute(edit_query)
            for row in edit_cursor:
                self.__wp_upd_workout_name_tb.insert(0, row[1])
                self.__wp_upd_workout_category_tb.insert(0, row[2])
                self.__wp_upd_workout_description_tb.insert(1.0, row[3])
            edit_cursor.close()
            edit_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)

    def __send_values_for_edit(self,addWPframe):
        id = self.__wp_upd_selection_cb.get()
        wp_upd_workout_name = self.__wp_upd_workout_name_tb.get()
        wp_upd_workout_category = self.__wp_upd_workout_category_tb.get()
        wp_upd_workout_description = self.__wp_upd_workout_description_tb.get(1.0, 'end')
        # creating the object of the class
        wp_upd_obj = EditWorkoutplan(id, wp_upd_workout_name, wp_upd_workout_category, wp_upd_workout_description)
        response= wp_upd_obj.update_workoutplan(addWPframe)
        if response == 1:
            self.__wp_upd_workout_name_tb.delete(0, 'end')
            self.__wp_upd_workout_category_tb.delete(0, 'end')
            self.__wp_upd_workout_description_tb.delete(1.0, 'end')
        else:
            pass
    def __showUpdateWorkplanPanel(self,addWPframe):
        wp_upd_upperframe = tk.LabelFrame(addWPframe, width=380, height=260, text='Update Workoutplan: ', font='arial 11 italic',
                                            bg='lightgrey', fg='maroon2')
        wp_upd_upperframe.place(x=780, y=80)
        # selection label
        wp_upd_selection_lbl = tk.Label(wp_upd_upperframe, text='Workout plan ID: ',bg='lightgrey',font=('arial',9, 'italic'))
        wp_upd_selection_lbl.place(x=20, y=10)
        self.__wp_upd_selection_cb = ttk.Combobox(wp_upd_upperframe, width=10)
        self.__wp_upd_selection_cb.place(x=175, y=10)
        self.__wp_upd_selectionID_Auto_update(self.__wp_upd_selection_cb)
        self.__wp_upd_selection_cb.current(0)
        if self.__wp_upd_selection_cb.current() != -1:
            self.__wp_upd_selection_cb.bind('<<ComboboxSelected>>',self.__get_values_for_edit)
        else:
            pass
        # workout name label
        wp_upd_workout_name_lbl=tk.Label(wp_upd_upperframe, text='Workout plan Name: ', bg='lightgrey',font=('arial',9,'italic'))
        wp_upd_workout_name_lbl.place(x=20, y=50)
        self.__wp_upd_workout_name_tb=tk.Entry(wp_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__wp_upd_workout_name_tb.place(x=175, y=50)
        # workout date label
        wp_upd_workout_category_lbl=tk.Label(wp_upd_upperframe, text='Workoutplan category: ', bg='lightgrey',font=('arial',9,'italic'))
        wp_upd_workout_category_lbl.place(x=20, y=90)
        self.__wp_upd_workout_category_tb=tk.Entry(wp_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__wp_upd_workout_category_tb.place(x=175, y=90)
        # workout description label
        wp_upd_workout_description_lbl=tk.Label(wp_upd_upperframe, text='Workout plan Description: ', bg='lightgrey',font=('arial',9,'italic'))
        wp_upd_workout_description_lbl.place(x=20, y=130)
        self.__wp_upd_workout_description_tb=tk.Text(wp_upd_upperframe,height=4, width=25,font=('arial',9, 'italic'))
        self.__wp_upd_workout_description_tb.place(x=175, y=130)

        wp_upd_saveBtn = tk.Button(wp_upd_upperframe, text='Update Plan',
                                          width=18, fg='blue',
                                          bg='lightblue', font=('arial', 10, 'italic'))
        wp_upd_saveBtn.place(x=202, y=205)
        wp_upd_saveBtn.config(command= lambda :self.__send_values_for_edit(addWPframe))




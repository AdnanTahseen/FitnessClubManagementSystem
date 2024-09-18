import tkinter as tk
from FCMS_Files.instructor_add import *
from tkcalendar import *
from FCMS_Files.view_inst_table import *
from FCMS_Files.instructor_update import *
from FCMS_Files.instructor_delete import *

class Instructor:

    def __addinstructorinfo(self, inst_window):
        firstname=self.__instructor_add_first_name_tb.get()
        lastname=self.__instructor_add_last_name_tb.get()
        email=self.__instructor_add_email_tb.get()
        joiningdate = self.__instructor_add_joiningDate_tb.get()
        address=self.__instructor_add_address_tb.get(1.0, tk.END)
        contact = self.__instructor_add_contact_tb.get()
        salary=self.__instructor_add_salary_tb.get()
        qualification=self.__instructor_add_qualification_tb.get()
        age=self.__instructor_add_age_tb.get()
        specialization=self.__instructor_add_specialization_cb.get()
        assignedclass=self.__instructor_add_assignclass_selectOption_cb.get()

        if not (firstname and lastname and email and joiningdate and address and contact and salary
                and qualification and age and specialization and assignedclass) == '':
            addinst= AddInstructor(firstname,lastname,email,joiningdate,address,contact,
                                salary,qualification,age,specialization,assignedclass)
            addinst.createinstructortable()
            response=addinst.addinstructorinformation(inst_window)
            if response == True:
                self.__instructor_add_first_name_tb.delete(0,tk.END)
                self.__instructor_add_last_name_tb.delete(0,tk.END)
                self.__instructor_add_email_tb.delete(0,tk.END)
                self.__instructor_add_joiningDate_tb.delete(0,tk.END)
                self.__instructor_add_address_tb.delete(1.0,tk.END)
                self.__instructor_add_contact_tb.delete(0,tk.END)
                self.__instructor_add_salary_tb.delete(0,tk.END)
                self.__instructor_add_qualification_tb.delete(0,tk.END)
                self.__instructor_add_age_tb.delete(0,tk.END)
                self.__instructor_add_specialization_cb.delete(0,tk.END)
                self.__instructor_add_assignclass_selectOption_cb.delete(0,tk.END)
            else:
                pass
        else:
            messagebox.showerror('Fitness Club Managment System', 'Please fill-in all the fields',parent =inst_window)
    def __setjoiningdate(self, ev):
        global joiningdatecal,joiningdatecalendar
        joiningdatecalendar= tk.Toplevel()
        joiningdatecalendar.grab_set()
        joiningdatecalendar.wm_attributes('-topmost', True)
        joiningdatecalendar.title('Select Joining Date')
        joiningdatecalendar.geometry('250x220+650+400')
        joiningdatecalendar.resizable(False, False)
        joiningdatecal = Calendar(joiningdatecalendar, selectmode='day', date_pattern='dd/mm/y')
        joiningdatecal.place(x=0, y=0)
        submit_btn=tk.Button(joiningdatecalendar, text='Submit' , command=self.__grab_joiningdate,
                                 bg='maroon', fg='grey99',width=20,
                                 padx=12, pady=2, font='arial 10 italic bold')
        submit_btn.place(x=40, y=188)
        joiningdatecalendar.protocol('WM_DELETE_WINDOW', False)
    def __grab_joiningdate(self):
        self.__instructor_add_joiningDate_tb.delete(0,tk.END)
        joiningdate=joiningdatecal.get_date()
        self.__instructor_add_joiningDate_tb.insert(tk.END, joiningdate)
        joiningdatecalendar.grab_release()
        joiningdatecalendar.destroy()
    def showInstructorManagementPanel(self):
        inst_window = tk.Toplevel()
        inst_window.title = ('Instructor Management Panel')
        inst_window.geometry('1200x650+350+150')
        inst_window.resizable(False, False)
        inst_window.grab_set()
        inst_window.wm_attributes('-topmost', True)
        inst_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        workspace_frame = tk.Frame(inst_window, width=1200, height=650, bd=2, bg='lightgrey')
        workspace_frame.place(x=0, y=0)
        #creating frame
        addInstructorframe=tk.Frame(workspace_frame, width=1200, height=650, bg='lightgrey', bd=3)
        addInstructorframe.place(x=0, y=0)
        addInstructorlbl=tk.Label(addInstructorframe, text='INSTRUCTOR PANEL', font=('Arial', 18, 'bold', 'italic'),
                                         fg='floralwhite', bg='blue', width=84, height=2)
        addInstructorlbl.place(x=-5, y=-5)
        # calling add function
        self.__showAddInstructorPanel(addInstructorframe, inst_window)
        # calling update function
        self.__showUpdateInstructorPanel(addInstructorframe, inst_window)
        # calling delete function
        self.__showDeleteInstructorPanel(addInstructorframe, inst_window)

        # creating button to show instructor information
        inst_view_btn= tk.Button(addInstructorframe, text='Show Instructor Information',bg='maroon2', fg='white',padx=10,pady=10)
        inst_view_btn.place(x=930, y=300)
        # creating the object of ViewInstructorTable class and calling its table function
        inst_table_obj = ViewInstructorTable()
        inst_view_btn.config(command=inst_table_obj.show_instructor_table)
    def __showAddInstructorPanel(self,addInstructorframe, inst_window):
        # creating controls
        instructor_add_upperframe = tk.LabelFrame(addInstructorframe, text='Add Intructor: ', width=360, height=550,
                                                  bg='lightgrey', font='arial 11 italic bold', fg='maroon2')
        instructor_add_upperframe.place(x=20, y=80)

        # first name
        instructor_add_first_name_lbl = tk.Label(instructor_add_upperframe, text='First Name: ',
                                                 bg='lightgrey', font=('arial', 9, 'italic'))
        instructor_add_first_name_lbl.place(x=20, y=10)

        self.__instructor_add_first_name_tb = tk.Entry(instructor_add_upperframe, width=25,
                                                       font=('arial', 9, 'italic'))
        self.__instructor_add_first_name_tb.place(x=130, y=10)

        instructor_add_last_name_lbl = tk.Label(instructor_add_upperframe, text="Last Name: ",
                                                bg='lightgrey', font=('arial', 9, 'italic'))
        instructor_add_last_name_lbl.place(x=20, y=50)
        self.__instructor_add_last_name_tb = tk.Entry(instructor_add_upperframe, width=25,
                                                      font=('arial', 9, 'italic'))
        self.__instructor_add_last_name_tb.place(x=130, y=50)

        instructor_add_email_lbl = tk.Label(instructor_add_upperframe, text='Email: ', bg='lightgrey',
                                            font=('arial', 9, 'italic'))
        instructor_add_email_lbl.place(x=20, y=90)
        self.__instructor_add_email_tb = tk.Entry(instructor_add_upperframe, width=25, font=('arial', 9, 'italic'))
        self.__instructor_add_email_tb.place(x=130, y=90)

        instructor_add_joiningDate_lbl = tk.Label(instructor_add_upperframe, text='Joining Date:', bg='lightgrey',
                                                  font=('arial', 9, 'italic'))
        instructor_add_joiningDate_lbl.place(x=20, y=130)
        self.__instructor_add_joiningDate_tb = tk.Entry(instructor_add_upperframe, width=25, fg='#6b6a69',
                                                        highlightthickness=0,
                                                        font=('arial', 9, 'italic'))
        self.__instructor_add_joiningDate_tb.place(x=130, y=130)
        self.__instructor_add_joiningDate_tb.insert(0, 'DD-MM-YYYY')
        self.__instructor_add_joiningDate_tb.bind('<Button-1>', self.__setjoiningdate)

        # address
        instructor_add_address_lbl = tk.Label(instructor_add_upperframe, text="Address: ", bg='lightgrey',
                                              font=('arial', 9, 'italic'))
        instructor_add_address_lbl.place(x=20, y=170)
        self.__instructor_add_address_tb = tk.Text(instructor_add_upperframe, width=25, height=4,
                                                   font=('arial', 9, 'italic'))
        self.__instructor_add_address_tb.place(x=130, y=170)

        instructor_add_contact_lbl = tk.Label(instructor_add_upperframe, text='Contact: ', bg='lightgrey',
                                              font=('arial', 9, 'italic'))
        instructor_add_contact_lbl.place(x=20, y=250)
        self.__instructor_add_contact_tb = tk.Entry(instructor_add_upperframe, width=25, fg='grey2',
                                                    font=('arial', 9, 'italic'))
        self.__instructor_add_contact_tb.place(x=130, y=250)
        self.__instructor_add_contact_tb.bind('<KeyPress>', self.__checkNumberforcontact)
        instructor_add_salary_lbl = tk.Label(instructor_add_upperframe, text='Salary:', bg='lightgrey',
                                             font=('arial', 9, 'italic'))
        instructor_add_salary_lbl.place(x=20, y=290)
        self.__instructor_add_salary_tb = tk.Entry(instructor_add_upperframe, width=25, font=('arial', 9, 'italic'))
        self.__instructor_add_salary_tb.place(x=130, y=290)
        self.__instructor_add_salary_tb.bind('<KeyPress>', self.__checkNumberforsalary)
        instructor_add_qualification_lbl = tk.Label(instructor_add_upperframe, text='Qualification: ', bg='lightgrey',
                                                    font=('arial', 9, 'italic'))
        instructor_add_qualification_lbl.place(x=20, y=330)
        self.__instructor_add_qualification_tb = tk.Entry(instructor_add_upperframe, width=25,
                                                          font=('arial', 9, 'italic'))
        self.__instructor_add_qualification_tb.place(x=130, y=330)

        instructor_add_age_lbl = tk.Label(instructor_add_upperframe, text='Age: ', bg='lightgrey',
                                          font=('arial', 9, 'italic'))
        instructor_add_age_lbl.place(x=20, y=370)
        self.__instructor_add_age_tb = tk.Entry(instructor_add_upperframe, width=25, font=('arial', 9, 'italic'))
        self.__instructor_add_age_tb.place(x=130, y=370)
        self.__instructor_add_age_tb.bind('<KeyPress>', self.__checkNumberforage)
        instructor_add_specialization_lbl = tk.Label(instructor_add_upperframe, text='Specialization: ', bg='lightgrey',
                                                     font=('arial', 9, 'italic'))
        instructor_add_specialization_lbl.place(x=20, y=410)
        instructor_add_specialization = ['Strength and conditioning coach', 'Bodybuilding Specialist',
                                         'Group exercise instructor', 'Fitness manager', 'Senior fitness specialist',
                                         'Youth fitness specialist', 'Weight loss transformation specialist',
                                         'Corrective exercise specialist', 'Health coaching', 'Glute Specialist',
                                         'Kickboxing instructor', 'Power lifting instructor',
                                         'Performance enhancement coach',
                                         'Tactical conditioning coach', 'Exercise recovery specialist',
                                         'Exercise therapy specialist',
                                         'Running coach', 'Transformation Specialist', 'Yoga fundamentals',
                                         'Indoor cycling']
        self.__instructor_add_specialization_cb = ttk.Combobox(instructor_add_upperframe,
                                                               values=instructor_add_specialization,
                                                               width=23, font=('arial', 9, 'italic'))
        self.__instructor_add_specialization_cb.place(x=130, y=410)
        self.__instructor_add_specialization_cb.set(instructor_add_specialization[0])

        instructor_add_assingclass_lbl = tk.Label(instructor_add_upperframe, text='Assign Class: ', bg='lightgrey',
                                                  font=('arial', 9, 'italic'))
        instructor_add_assingclass_lbl.place(x=20, y=450)
        # add_fitnessClassList = ['Cardio', 'Swimming', 'Weight Lifting', 'Body Building',
        #                         'Mobility', 'Core', 'Cycle','Dance', 'HIIT', 'Intervals',
        #                         'Cardio Equipment', 'Circuit Equipment', 'Body Combat',
        #                         'Body Pump', 'RPM','Sprint','MIXXEDFIT','Pilates',
        #                         'Piloga','Piyo', 'Silver Sneakers','Spinning','Step',
        #                         'Step Strength', 'Strength','Strong Nation', 'Synergy',
        #                         'Tabata','Toning', 'Turbo Kick', 'Vinyasa', 'Yoga', 'Zumba']
        self.__instructor_add_assignclass_selectOption_cb = ttk.Combobox(instructor_add_upperframe,
                                                                         width=23, font=('arial', 9, 'italic'))
        self.__instructor_add_assignclass_selectOption_cb.place(x=130, y=450)
        self.__auto_update_class_list(self.__instructor_add_assignclass_selectOption_cb)

        instructor_add_saveInfoBtn = tk.Button(instructor_add_upperframe, text='Save Information', width=18, fg='blue',
                                               bg='lightblue', font=('arial', 10, 'italic'))
        instructor_add_saveInfoBtn.place(x=160, y=490)
        instructor_add_saveInfoBtn.config(command=lambda: self.__addinstructorinfo(inst_window))
    def __inst_send_id_for_deletion(self, inst_window):
        id_value = self.__instructor_delete_selection_cb.get()
        inst_del = InstructorDelete(id_value)
        inst_del.delete_instructor_information(inst_window)
        self.__instructor_delete_selection_cb.delete(0, tk.END)
    def __showDeleteInstructorPanel(self, addInstructorframe, inst_window):
          instructor_delete_upperframe = tk.LabelFrame(addInstructorframe, width=320, height=150, bg='lightgrey',
                                                       text='Delete Instructor: ', font='arial 11 italic bold', fg='maroon2')
          instructor_delete_upperframe.place(x=830, y=80)
          # creating database connection
          # creating selection id label
          instructor_delete_selection_lbl = tk.Label(instructor_delete_upperframe, text='Select ID: ',bg='lightgrey',font=('arial',9,'italic'))
          instructor_delete_selection_lbl.place(x=20, y=30)
          self.__instructor_delete_selection_cb = ttk.Combobox(instructor_delete_upperframe, width=10)
          self.__instructor_delete_selection_cb.place(x=130, y=30)
          self.__del_selection_id(self.__instructor_delete_selection_cb)
          self.__instructor_delete_selection_cb.current(0)
          instructor_delete_deleteBtn = tk.Button(instructor_delete_upperframe, text='Delete Instructor',
                                                    width=18, fg='blue', bg='lightblue', font=('arial',10, 'italic'))
          instructor_delete_deleteBtn.place(x=100, y=80)
          if self.__instructor_delete_selection_cb.current() != -1:
            instructor_delete_deleteBtn.config(command = lambda :self.__inst_send_id_for_deletion(inst_window))
          else:
            messagebox.showerror('Fitness Club Management System', 'Select ID first!', parent=inst_window)
    def __set_form_values(self, e):
        currentValue= self.__instructor_upd_selection_cb.get()
        fetch_query = 'SELECT * FROM instructor WHERE inst_id = {cval}'.format(cval=currentValue)
        fetch_conn = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        fetch_cursor = fetch_conn.cursor()
        fetch_cursor.execute(fetch_query)
        # empyting the boxes
        self.__instructor_update_first_name_tb.delete(0, tk.END)
        self.__instructor_update_last_name_tb.delete(0, tk.END)
        self.__instructor_update_email_tb.delete(0, tk.END)
        self.__instructor_update_joiningDate_tb.delete(0, tk.END)
        self.__instructor_update_address_tb.delete(1.0, tk.END)
        self.__instructor_update_contact_tb.delete(0, tk.END)
        self.__instructor_update_salary_tb.delete(0, tk.END)
        self.__instructor_update_qualification_tb.delete(0, tk.END)
        self.__instructor_update_age_tb.delete(0, tk.END)
        self.__instructor_update_specialization_tb.delete(0, tk.END)
        self.__instructor_update_assignclass_selectOption.delete(0, tk.END)
        # iterating through cursor to get values
        for row in fetch_cursor:
            self.__instructor_update_first_name_tb.insert(0, row[1])
            self.__instructor_update_last_name_tb.insert(0, row[2])
            self.__instructor_update_email_tb.insert(0, row[3])
            self.__instructor_update_joiningDate_tb.insert(0, row[4])
            self.__instructor_update_address_tb.insert(1.0, row[5])
            self.__instructor_update_contact_tb.insert(0, row[11])
            self.__instructor_update_salary_tb.insert(0, row[6])
            self.__instructor_update_qualification_tb.insert(0, row[7])
            self.__instructor_update_age_tb.insert(0, row[8])
            self.__instructor_update_specialization_tb.insert(0, row[9])
            self.__instructor_update_assignclass_selectOption.insert(0, row[10])
        fetch_conn.close()
    def __collect_inst_update_info(self, inst_window):
        update_id = self.__instructor_upd_selection_cb.get()
        update_first_name = self.__instructor_update_first_name_tb.get()
        update_last_name = self.__instructor_update_last_name_tb.get()
        update_email = self.__instructor_update_email_tb.get()
        update_joiningDate = self.__instructor_update_joiningDate_tb.get()
        update_address = self.__instructor_update_address_tb.get(1.0, tk.END)
        update_contact = self.__instructor_update_contact_tb.get()
        update_salary = self.__instructor_update_salary_tb.get()
        update_qualification = self.__instructor_update_qualification_tb.get()
        update_age = self.__instructor_update_age_tb.get()
        update_specialization = self.__instructor_update_specialization_tb.get()
        update_assignclass = self.__instructor_update_assignclass_selectOption.get()
        # creating the object of UpdateInstructor class
        update_instructor = UpdateInstructor(update_id, update_first_name, update_last_name, update_email,
                                             update_joiningDate, update_address, update_contact, update_salary,
                                             update_qualification, update_age, update_specialization, update_assignclass)
        update_instructor.update_instructor_information(inst_window)
    def __showUpdateInstructorPanel(self,addInstructorframe, inst_window):
        # creating controls
        instructor_update_upperframe = tk.LabelFrame(addInstructorframe, width=360, height=550, text='Update Instructor: ',
                                                     bg='lightgrey', font='arial 11 italic bold', fg='maroon2')
        instructor_update_upperframe.place(x=430, y=80)

        # creating selection label
        instructor_selection_lbl = tk.Label(instructor_update_upperframe, text='Select ID: ', bg='lightgrey', font=('arial',9, 'italic'))
        instructor_selection_lbl.place(x=20, y=10)
        # selection_id_list=[]
        # selection_id_list=self.__update_selection_id()
        self.__instructor_upd_selection_cb = ttk.Combobox(instructor_update_upperframe, width=13)
        self.__instructor_upd_selection_cb.place(x=130, y=10)
        self.__update_selection_id(self.__instructor_upd_selection_cb)
        self.__instructor_upd_selection_cb.current(0)
        if not (self.__instructor_upd_selection_cb.current() == -1):
            self.__instructor_upd_selection_cb.bind("<<ComboboxSelected>>",self.__set_form_values)
        else:
            pass

        # first name
        instructor_update_first_name_lbl = tk.Label(instructor_update_upperframe, text='First Name: ',bg='lightgrey',font=('arial', 9, 'italic'))
        instructor_update_first_name_lbl.place(x=20, y=40)
        self.__instructor_update_first_name_tb = tk.Entry(instructor_update_upperframe, width=25, font=('arial',9, 'italic'))
        self.__instructor_update_first_name_tb.place(x=130, y=40)
        # last name
        instructor_update_last_name_lbl = tk.Label(instructor_update_upperframe, text="Last Name: ", bg='lightgrey',font=('arial', 9, 'italic'))
        instructor_update_last_name_lbl.place(x=20, y=70)
        self.__instructor_update_last_name_tb = tk.Entry(instructor_update_upperframe, width=25,font=('arial', 9, 'italic'))
        self.__instructor_update_last_name_tb.place(x=130, y=70)
        # email
        instructor_update_email_lbl = tk.Label(instructor_update_upperframe, text='Email: ',bg='lightgrey',font=('arial',9, 'italic'))
        instructor_update_email_lbl.place(x=20, y=100)
        self.__instructor_update_email_tb = tk.Entry(instructor_update_upperframe, width=25,font=('arial',9, 'italic'))
        self.__instructor_update_email_tb.place(x=130, y=100)
        # joining date
        instructor_update_joiningDate_lbl = tk.Label(instructor_update_upperframe, text='Joining Date:',bg='lightgrey',font=('arial',9, 'italic'))
        instructor_update_joiningDate_lbl.place(x=20, y=130)
        self.__instructor_update_joiningDate_tb = tk.Entry(instructor_update_upperframe, width=25,font=('arial',9,'italic'))
        self.__instructor_update_joiningDate_tb.place(x=130, y=130)
        self.__instructor_update_joiningDate_tb.insert(0, 'DD-MM-YYYY')
        # address
        instructor_update_address_lbl = tk.Label(instructor_update_upperframe, text="Address: ",bg='lightgrey',font=('arial',9, 'italic'))
        instructor_update_address_lbl.place(x=20, y=170)
        self.__instructor_update_address_tb = tk.Text(instructor_update_upperframe, width=25, height=4,font=('arial',9,'italic'))
        self.__instructor_update_address_tb.place(x=130, y=170)
        # contact
        instructor_update_contact_lbl = tk.Label(instructor_update_upperframe, text='Contact: ',bg='lightgrey',font=('arial',9,'italic'))
        instructor_update_contact_lbl.place(x=20, y=250)
        self.__instructor_update_contact_tb = tk.Entry(instructor_update_upperframe, width=25,font=('arial',9,'italic'))
        self.__instructor_update_contact_tb.place(x=130, y=250)
        # salary
        instructor_update_salary_lbl = tk.Label(instructor_update_upperframe,text='Salary:',bg='lightgrey',font=('arial',9,'italic'))
        instructor_update_salary_lbl.place(x=20, y=290)
        self.__instructor_update_salary_tb = tk.Entry(instructor_update_upperframe, width=25,font=('arial',9, 'italic'))
        self.__instructor_update_salary_tb.place(x=130, y=290)
        # qualification
        instructor_update_qualification_lbl = tk.Label(instructor_update_upperframe,text='Qualification: ',bg='lightgrey',font=('arial',9,'italic'))
        instructor_update_qualification_lbl.place(x=20, y=330)
        self.__instructor_update_qualification_tb = tk.Entry(instructor_update_upperframe, width=25, font=('arial',9, 'italic'))
        self.__instructor_update_qualification_tb.place(x=130, y=330)
        # age
        instructor_update_age_lbl = tk.Label(instructor_update_upperframe, text='Age: ', bg='lightgrey',font=('arial',9,'italic'))
        instructor_update_age_lbl.place(x=20, y=370)
        self.__instructor_update_age_tb = tk.Entry(instructor_update_upperframe, width=25,font=('arial',9, 'italic'))
        self.__instructor_update_age_tb.place(x=130, y=370)
        # specialization
        instructor_update_specialization_lbl=tk.Label(instructor_update_upperframe, text='Specialization: ', bg='lightgrey',font=('arial',9, 'italic'))
        instructor_update_specialization_lbl.place(x=20, y=410)
        update_instructor_specialization=['Strength and conditioning coach', 'Bodybuilding Specialist',
                                         'Group exercise instructor', 'Fitness manager', 'Senior fitness specialist',
                                         'Youth fitness specialist', 'Weight loss transformation specialist',
                                         'Corrective exercise specialist', 'Health coaching', 'Glute Specialist',
                                         'Kickboxing instructor', 'Power lifting instructor',
                                         'Performance enhancement coach',
                                         'Tactical conditioning coach', 'Exercise recovery specialist',
                                         'Exercise therapy specialist',
                                         'Running coach', 'Transformation Specialist', 'Yoga fundamentals',
                                         'Indoor cycling']
        self.__instructor_update_specialization_tb=ttk.Combobox(instructor_update_upperframe, values=update_instructor_specialization,width=23, font=('arial',9, 'italic'))
        self.__instructor_update_specialization_tb.place(x=130, y=410)
        # assign class
        instructor_update_assingclass_lbl=tk.Label(instructor_update_upperframe, text='Assign Class: ',bg='lightgrey',font=('arial',9,'italic'))
        instructor_update_assingclass_lbl.place(x=20, y=450)
        update_fitnessClassList=['Cardio', 'Swimming', 'Weight Lifting', 'Body Building',
                                'Mobility', 'Core', 'Cycle','Dance', 'HIIT', 'Intervals',
                                'Cardio Equipment', 'Circuit Equipment', 'Body Combat',
                                'Body Pump', 'RPM','Sprint','MIXXEDFIT','Pilates',
                                'Piloga','Piyo', 'Silver Sneakers','Spinning','Step',
                                'Step Strength', 'Strength','Strong Nation', 'Synergy',
                                'Tabata','Toning', 'Turbo Kick', 'Vinyasa', 'Yoga', 'Zumba']
        self.__instructor_update_assignclass_selectOption = ttk.Combobox(instructor_update_upperframe,values=update_fitnessClassList, width=23, font=('arial',9, 'italic'))
        self.__instructor_update_assignclass_selectOption.place(x=130, y=450)

        # Button for updating data
        instructor_update_saveInfoBtn = tk.Button(instructor_update_upperframe, text='Update Information',width=18, fg='blue',
                                                       bg='lightblue', font=('arial', 10, 'italic'))
        instructor_update_saveInfoBtn.place(x=160, y=490)
        instructor_update_saveInfoBtn.config(command =lambda: self.__collect_inst_update_info(inst_window))
    def __update_selection_id(self,instructor_upd_selection_cb):
        selection_id_list = []
        # creating conneciton and select query
        select_Id_query = 'SELECT inst_id from instructor'
        upd_select_inst_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        upd_select_inst_cursor = upd_select_inst_connection.cursor()
        upd_select_inst_cursor.execute(select_Id_query)

        for number in upd_select_inst_cursor:
            selection_id_list.append(number)
        # close connection
        upd_select_inst_connection.close()
        # sorting values in list
        selection_id_list.sort()
        instructor_upd_selection_cb.config(values=selection_id_list)
        # return selection_id_list
        instructor_upd_selection_cb.after(200, lambda : self.__update_selection_id(instructor_upd_selection_cb))
    def __del_selection_id(self,instructor_delete_selection_cb):
        selection_id_list = []
        # creating conneciton and select query
        select_Id_query = 'SELECT inst_id from instructor'
        upd_select_inst_connection = pms.connect(host='localhost', port=3306, user='root', password='',database='fcms')
        upd_select_inst_cursor = upd_select_inst_connection.cursor()
        try:
            upd_select_inst_cursor.execute(select_Id_query)

            for number in upd_select_inst_cursor:
                selection_id_list.append(number)
            # close connection
            upd_select_inst_connection.close()
        # sorting values in list
            selection_id_list.sort()
            instructor_delete_selection_cb.config(values=selection_id_list)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error'+ str(e))
        # return selection_id_list
        instructor_delete_selection_cb.after(200, lambda : self.__update_selection_id(instructor_delete_selection_cb))
    def __auto_update_class_list(self,instructor_add_assignclass_selectOption_cb):
        auto_update_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        auto_update_cursor = auto_update_connection.cursor()
        # auto_update_query = 'SELECT wp_name, COUNT(*) from workoutplan GROUP BY wp_name HAVING COUNT(*) >1'
        auto_update_query = 'SELECT distinct wp_name from workoutplan'
        try:
            auto_update_cursor.execute(auto_update_query)
            auto_update_class_list = []
            for name in auto_update_cursor:
                auto_update_class_list.append(name)
            auto_update_class_list.sort()
            instructor_add_assignclass_selectOption_cb.config(values=auto_update_class_list)
            auto_update_connection.close()
            instructor_add_assignclass_selectOption_cb.after(200, lambda : self.__auto_update_class_list(instructor_add_assignclass_selectOption_cb))
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))
    def __checkNumberforcontact(self, e):
        try:
            int(self.__instructor_add_contact_tb.get())
            self.__instructor_add_contact_tb.config(bg='white')
            if len(self.__instructor_add_contact_tb.get()) >=11:
                self.__instructor_add_contact_tb.delete(10, 'end')

        except ValueError:
            self.__instructor_add_contact_tb.config(bg='red2')
            self.__instructor_add_contact_tb.delete(0, 'end')
    def __checkNumberforsalary(self, e):
        try:
            int(self.__instructor_add_salary_tb.get())
            self.__instructor_add_salary_tb.config(bg='white')
            if len(self.__instructor_add_salary_tb.get()) >=8:
                self.__instructor_add_salary_tb.delete(7, 'end')

        except ValueError:
            self.__instructor_add_salary_tb.config(bg='red2')
            self.__instructor_add_salary_tb.delete(0, 'end')
    def __checkNumberforage(self, e):
        try:
            int(self.__instructor_add_age_tb.get())
            self.__instructor_add_age_tb.config(bg='white')
            if len(self.__instructor_add_age_tb.get()) >= 3:
                self.__instructor_add_age_tb.delete(2, 'end')

        except ValueError:
            self.__instructor_add_age_tb.config(bg='red2')
            self.__instructor_add_age_tb.delete(0, 'end')
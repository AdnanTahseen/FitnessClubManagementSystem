import tkinter as tk
from FCMS_Files.view_members_table import *
from FCMS_Files.members_add import *
from FCMS_Files.members_update import *
from FCMS_Files.members_delete import *
from FCMS_Files.members_measurement import *
from FCMS_Files.members_BMI import *
from FCMS_Files.view_member_bmi import *
from FCMS_Files.member_bmi_delete import *
from FCMS_Files.member_bmi_edit import *
from tkinter import messagebox
class MembersRegistration:
    def showMemberManagementPanel(self):
        members_window = tk.Toplevel()
        members_window.geometry('1200x650+350+150')
        members_window.resizable(False, False)
        members_window.grab_set()
        # members_window.wm_attributes('-topmost', True)
        members_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        self.member_add_workspace = tk.Frame(members_window, width=1200, height=650, bg='lightgrey',
                                        bd=3)
        self.member_add_workspace.place(x=0, y=0)
        member_add_heading_lbl = tk.Label(self.member_add_workspace, text='MEMBER PANEL',
                                          font=('Arial', 18, 'bold', 'italic'),
                                          fg='floralwhite', bg='blue', width=84, height=2)
        member_add_heading_lbl.place(x=-5, y=-5)
        # calling add member function
        self.__showAddMemberPanel(self.member_add_workspace, members_window)
        #calling delete member function
        self.__showDeleteMemberPanel(self.member_add_workspace, members_window)
        # calling update member function
        self.__showUpdateMemberPanel(self.member_add_workspace, members_window)
        # calling member measurement function
        self.__showMemberMeasurementPanel(self.member_add_workspace, members_window)
        # calling member BMI measurement function
        self.__showMemberBMIPanel(self.member_add_workspace, members_window)
        ################################
        member_table_btn= tk.Button(self.member_add_workspace, text='Show Members Information', bg='coral4',fg='white', padx=10, pady=10)
        member_table_btn.place(x=470, y=570)
        mem_table= ViewMemberTable()
        member_table_btn.config(command=mem_table.show_member_table)
    def __send_member_add_data(self, members_window):
        fname = self.__member_add_fname_tb.get()
        lname = self.__member_add_lname_tb.get()
        email = self.__member_add_email_tb.get()
        contact = self.__member_add_contact_tb.get()
        address = self.__member_add_Address_tb.get(1.0,tk.END)
        workoutplan = self.__member_add_workoutplan_cb.get()
        joiningdate = self.__member_add_joinDate_tb.get()
        assignedfees  = self.__member_add_assign_fees_tb.get()

        if workoutplan == '':
            messagebox.showinfo('Fitness Club Management System','Please add a workout plan first.', parent=members_window)
        else:
            addMem = AddMembers(fname,lname, email, contact, address, workoutplan,joiningdate,assignedfees)
            addMem.create_add_member_table()
            response = addMem.add_members_information(members_window)
            if response:
                self.__member_add_fname_tb.delete(0,'end')
                self.__member_add_lname_tb.delete(0,'end')
                self.__member_add_email_tb.delete(0,'end')
                self.__member_add_contact_tb.delete(0,'end')
                self.__member_add_Address_tb.delete(1.0, tk.END)
                self.__member_add_workoutplan_cb.delete(0,'end')
                self.__member_add_joinDate_tb.delete(0,'end')
                self.__member_add_assign_fees_tb.delete(0,'end')
    def __member_add_selectdate(self,e):
        global member_add_calendar, calendar_window
        calendar_window = tk.Toplevel()
        calendar_window.geometry('260x240+350+420')
        calendar_icon= tk.PhotoImage(file='Images/fcms_icon.png')
        calendar_window.iconphoto(False, calendar_icon)
        calendar_window.resizable(0, 0)
        calendar_window.grab_set()
        member_add_calendar = Calendar(calendar_window, selectmode='day', date_pattern='dd/mm/y')
        member_add_calendar.place(x=0, y=0)
        submit_btn=tk.Button(calendar_window, text='Submit' , command=self.__grab_member_add_date,
                             bg='maroon', fg='grey99',width=20,
                             padx=12, pady=2, font='arial 10 italic bold')
        submit_btn.place(x=40, y=200)
        calendar_window.protocol('WM_DELETE_WINDOW', False)
    def __grab_member_add_date(self):
        self.__member_add_joinDate_tb.delete(0, tk.END)
        date=member_add_calendar.get_date()
        self.__member_add_joinDate_tb.insert(tk.END, date)
        calendar_window.grab_release()
        calendar_window.destroy()
    def __showAddMemberPanel(self, member_add_workspace, members_window ):
        # frame for creating controls
        member_add_upperframe = tk.LabelFrame(member_add_workspace,text='Add Member: ',font='arial 11 italic bold', fg='maroon2',
                                              width=340, height=440,bg='lightgrey')
        member_add_upperframe.place(x=20, y=70)
        # first name
        member_add_fname_lbl = tk.Label(member_add_upperframe, text='First Name: ', font=('arial',9, 'italic'), bg='lightgrey')
        member_add_fname_lbl.place(x=20, y=10)
        self.__member_add_fname_tb = tk.Entry(member_add_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_add_fname_tb.place(x=130, y=10)
        # last name
        member_add_lname_lbl = tk.Label(member_add_upperframe, text='Last Name: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_add_lname_lbl.place(x=20, y=50)
        self.__member_add_lname_tb = tk.Entry(member_add_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_add_lname_tb.place(x=130, y=50)
        # email
        member_add_email_lbl = tk.Label(member_add_upperframe, text='Email: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_add_email_lbl.place(x=20, y=90)
        self.__member_add_email_tb = tk.Entry(member_add_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_add_email_tb.place(x=130, y=90)
        # contact
        member_add_contact_lbl = tk.Label(member_add_upperframe, text='Contact Number: ',font=('arial',9,'italic'), bg='lightgrey')
        member_add_contact_lbl.place(x=20, y=130)
        self.__member_add_contact_tb = tk.Entry(member_add_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_add_contact_tb.place(x=130, y=130)
        self.__member_add_contact_tb.bind('<KeyPress>', self.__checkNumberforcontact)
        # address
        member_add_Address_lbl = tk.Label(member_add_upperframe, text='Address: ', font=('arial',9, 'italic'),bg='lightgrey')
        member_add_Address_lbl.place(x=20, y=170)
        self.__member_add_Address_tb = tk.Text(member_add_upperframe, width=25,height=4, font=('arial',9, 'italic'))
        self.__member_add_Address_tb.place(x=130, y=170)
        # workout
        # member_select_workoutplan=['Arial','Barre','Bootcamp','Boxing','Circuit Training',
        #                            'Cycling','Gymnastics','Martial Arts','Outdoor','Pilates',
        #                            'Pole Fitness','Rock Climbing','Sports','Tai Chi','Weight Training','Yoga']
        member_add_workoutplan_lbl = tk.Label(member_add_upperframe, text='Workout plan: ', font=('arial',9, 'italic'),bg='lightgrey')
        member_add_workoutplan_lbl.place(x=20, y=250)
        self.__member_add_workoutplan_cb = ttk.Combobox(member_add_upperframe, width=26)
        self.__member_add_workoutplan_cb.place(x=130, y=250)
        self.__auto_update_class_list(self.__member_add_workoutplan_cb)

        # joinning date
        member_add_joinDate_lbl=tk.Label(member_add_upperframe, text='Joining Date: ', font=('arial',9, 'italic'),bg='lightgrey')
        member_add_joinDate_lbl.place(x=20,y=290)
        self.__member_add_joinDate_tb=tk.Entry(member_add_upperframe, width=25, font=('arial',9, 'italic'))
        self.__member_add_joinDate_tb.place(x=130,y=290)
        self.__member_add_joinDate_tb.insert(0, 'dd/mm/yyyy')
        self.__member_add_joinDate_tb.bind('<Button-1>', self.__member_add_selectdate)
        # asign fees
        member_add_assign_fees_lbl=tk.Label(member_add_upperframe,text='Assign Fees: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_add_assign_fees_lbl.place(x=20,y=330)
        self.__member_add_assign_fees_tb=tk.Entry(member_add_upperframe, width=25, font=('arial',9, 'italic'))
        self.__member_add_assign_fees_tb.place(x=130,y=330)
        self.__member_add_assign_fees_tb.bind('<KeyPress>', self.__checkNumberforfees)
        # Button for saving members information in the database
        member_add_save_btn=tk.Button(member_add_upperframe, text='Save Member', font=('arial',9, 'italic'), fg='snow', bg='navyblue')
        member_add_save_btn.place(x=220,y=370)
        member_add_save_btn.config(command =lambda :self.__send_member_add_data(members_window))
    def __mem_send_data_to_delete(self, members_window):
        currentValue = self.__member_del_selection_cb.get()
        delMem = DeleteMember(currentValue)
        delMem.delete_member(members_window)
    def __showDeleteMemberPanel(self, member_add_workspace, members_window):
        member_del_upperframe = tk.LabelFrame(member_add_workspace, width=340, height=100, text='Delete Member: ',font='arial 11 italic bold',
                                         bg='lightgrey', fg='maroon2')
        member_del_upperframe.place(x=20, y=520)
        # member id selection
        member_del_selection_lbl = tk.Label(member_del_upperframe, text='Select Mem ID: ', font=('arial',9, 'italic'),bg='lightgrey')
        member_del_selection_lbl.place(x=20, y=10)
        self.__member_del_selection_cb = ttk.Combobox(member_del_upperframe, width=25)
        self.__member_del_selection_cb.place(x=130, y=10)
        self.__member_upd_selectionID_update(self.__member_del_selection_cb)
        self.__member_del_selection_cb.current(0)

        # Button for saving data
        member_del_save_btn = tk.Button(member_del_upperframe, text='Delete Member', font=('arial',9, 'italic'),
                                        fg='snow', bg='navyblue', padx=8)
        member_del_save_btn.place(x=190, y=45)
        if self.__member_del_selection_cb.current() != -1:
            member_del_save_btn.config(command=lambda: self.__mem_send_data_to_delete(members_window))
        else:
            messagebox.showerror('Fitness Club Management System', 'Value is not selected', parent = members_window)
    def __send_member_upd_values(self, members_window):
        updMem = UpdateMembers(
            self.__member_upd_selection_cb.get(),
            self.__member_upd_fname_tb.get(),
            self.__member_upd_lname_tb.get(),
            self.__member_upd_email_tb.get(),
            self.__member_upd_contact_tb.get(),
            self.__member_upd_Address_tb.get(1.0, tk.END),
            self.__member_upd_workoutplan_cb.get(),
            self.__member_upd_joinDate_tb.get(),
            self.__member_upd_assign_fees_tb.get()
        )
        updMem.update_member(members_window)
    def __member_upd_selection_getvalues(self, e):
        currentValue = self.__member_upd_selection_cb.get()
        # clearing controls values
        self.__member_upd_fname_tb.delete(0, tk.END)
        self.__member_upd_lname_tb.delete(0, tk.END)
        self.__member_upd_email_tb.delete(0, tk.END)
        self.__member_upd_contact_tb.delete(0, tk.END)
        self.__member_upd_Address_tb.delete(1.0, tk.END)
        self.__member_upd_workoutplan_cb.delete(0, tk.END)
        self.__member_upd_joinDate_tb.delete(0, tk.END)
        self.__member_upd_assign_fees_tb.delete(0, tk.END)
        # connection
        select_id_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        select_id_cursor = select_id_connection.cursor()
        select_upd_query = 'SELECT * FROM members where mem_id = {currentval}'.format(currentval=currentValue)
        select_id_cursor.execute(select_upd_query)
        for row in select_id_cursor:
            self.__member_upd_fname_tb.insert(0, row[1])
            self.__member_upd_lname_tb.insert(0, row[2])
            self.__member_upd_email_tb.insert(0, row[3])
            self.__member_upd_contact_tb.insert(0, row[4])
            self.__member_upd_Address_tb.insert(1.0, row[5])
            self.__member_upd_workoutplan_cb.insert(0, row[6])
            self.__member_upd_joinDate_tb.insert(0, row[7])
            self.__member_upd_assign_fees_tb.insert(0, row[8])

        select_id_cursor.close()
        select_id_connection.close()
    def __member_upd_selectionID_update(self, member_upd_selection_cb):
        # member selection id
        member_upd_selection_list = []
        # creating database connection
        update_db_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        update_db_cursor = update_db_connection.cursor()
        update_db_cursor.execute('SELECT mem_id FROM members')
        for id in update_db_cursor:
            member_upd_selection_list.append(id)

        update_db_cursor.close()
        update_db_connection.close()
        # sorting list
        member_upd_selection_list.sort()
        # configuring list
        member_upd_selection_cb.config(values=member_upd_selection_list)

        member_upd_selection_cb.after(200, lambda : self.__member_upd_selectionID_update(member_upd_selection_cb))
    def __measurement_del_selectionID_update(self, measurement_id_selection_update_cb):
        # member selection id
        measurement_upd_selection_list = []
        # creating database connection
        update_db_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        update_db_cursor = update_db_connection.cursor()
        update_db_cursor.execute('SELECT measurement_id FROM members_measurement')
        for id in update_db_cursor:
            measurement_upd_selection_list.append(id)

        update_db_cursor.close()
        update_db_connection.close()
        # sorting list
        measurement_upd_selection_list.sort()
        # configuring list
        measurement_id_selection_update_cb.config(values=measurement_upd_selection_list)

        measurement_id_selection_update_cb.after(200, lambda : self.__measurement_del_selectionID_update(measurement_id_selection_update_cb))
    def __member_measurement_selectionID_update(self, measurement_edit_id_cb):
        # member selection id
        mem_measurement_edit_selection_list = []
        # creating database connection
        update_db_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        update_db_cursor = update_db_connection.cursor()
        update_db_cursor.execute('SELECT measurement_id FROM members_measurement')
        for id in update_db_cursor:
            mem_measurement_edit_selection_list.append(id)

        update_db_cursor.close()
        update_db_connection.close()
        # sorting list
        mem_measurement_edit_selection_list.sort()
        # configuring list
        measurement_edit_id_cb.config(values=mem_measurement_edit_selection_list)

        measurement_edit_id_cb.after(200, lambda : self.__member_measurement_selectionID_update(measurement_edit_id_cb))
    def __showUpdateMemberPanel(self,member_add_workspace, members_window):
        member_upd_upperframe = tk.LabelFrame(member_add_workspace, width=340, height=490,text='Update Member: ', font='arial 11 italic bold',
                                         bg='lightgrey', fg='maroon2')
        member_upd_upperframe.place(x=390, y=70)
        # selection id
        member_upd_selection_lbl = tk.Label(member_upd_upperframe, text='Select Mem ID: ', font=('arial',9, 'italic'), bg='lightgrey')
        member_upd_selection_lbl.place(x=20, y=10)
        self.__member_upd_selection_cb = ttk.Combobox(member_upd_upperframe, width=23)
        self.__member_upd_selection_cb.place(x=130, y=10)
        # calling function for auto update values
        self.__member_upd_selectionID_update(self.__member_upd_selection_cb)
        self.__member_upd_selection_cb.current(0)
        # calling function when value is changed
        if self.__member_upd_selection_cb.current() != -1:
            self.__member_upd_selection_cb.bind('<<ComboboxSelected>>', self.__member_upd_selection_getvalues)
        else:
            pass
        # first name
        member_upd_fname_lbl = tk.Label(member_upd_upperframe, text='First Name: ',font=('arial',9, 'italic'), bg='lightgrey')
        member_upd_fname_lbl.place(x=20, y=50)
        self.__member_upd_fname_tb = tk.Entry(member_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_upd_fname_tb.place(x=130, y=50)
        # last name
        member_upd_lname_lbl = tk.Label(member_upd_upperframe, text='Last Name: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_lname_lbl.place(x=20, y=90)
        self.__member_upd_lname_tb = tk.Entry(member_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_upd_lname_tb.place(x=130, y=90)
        # email
        member_upd_email_lbl = tk.Label(member_upd_upperframe, text='Email: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_email_lbl.place(x=20, y=130)
        self.__member_upd_email_tb = tk.Entry(member_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_upd_email_tb.place(x=130, y=130)
        # contact
        member_upd_contact_lbl = tk.Label(member_upd_upperframe, text='Contact Number: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_contact_lbl.place(x=20, y=170)
        self.__member_upd_contact_tb = tk.Entry(member_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_upd_contact_tb.place(x=130, y=170)
        # address
        member_upd_Address_lbl = tk.Label(member_upd_upperframe, text='Address: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_Address_lbl.place(x=20, y=210)
        self.__member_upd_Address_tb = tk.Text(member_upd_upperframe, width=25,height=4, font=('arial',9, 'italic'))
        self.__member_upd_Address_tb.place(x=130, y=210)
        # workout plan
        member_select_workoutplan = ['Arial', 'Barre', 'Bootcamp', 'Boxing', 'Circuit Training',
                                     'Cycling', 'Gymnastics', 'Martial Arts', 'Outdoor', 'Pilates',
                                     'Pole Fitness', 'Rock Climbing', 'Sports', 'Tai Chi', 'Weight Training', 'Yoga']
        member_upd_workoutplan_lbl = tk.Label(member_upd_upperframe, text='Workout plan: ',font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_workoutplan_lbl.place(x=20, y=300)
        self.__member_upd_workoutplan_cb = ttk.Combobox(member_upd_upperframe, values=member_select_workoutplan, width=26)
        self.__member_upd_workoutplan_cb.place(x=130, y=300)
        # joining date
        member_upd_joinDate_lbl = tk.Label(member_upd_upperframe, text='Joining Date: ', font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_joinDate_lbl.place(x=20, y=340)
        self.__member_upd_joinDate_tb = tk.Entry(member_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_upd_joinDate_tb.place(x=130, y=340)
        # assign fees to members
        member_upd_assign_fees_lbl = tk.Label(member_upd_upperframe, text='Assign Fees: ', font=('arial',9, 'italic'),bg='lightgrey')
        member_upd_assign_fees_lbl.place(x=20, y=380)
        self.__member_upd_assign_fees_tb = tk.Entry(member_upd_upperframe, width=25,font=('arial',9, 'italic'))
        self.__member_upd_assign_fees_tb.place(x=130, y=380)
        # Button for saving data of members
        member_upd_save_btn = tk.Button(member_upd_upperframe, text='Update Member', font=('arial',9, 'italic'),
                                        fg='snow', bg='navyblue')
        member_upd_save_btn.place(x=210, y=420)
        member_upd_save_btn.config(command= lambda :self.__send_member_upd_values(members_window))
    def __member_name_for_measurement(self,e):
        self.__member_meas_name_tb.delete(0, 'end')
        currentValue = self.__member_select_id_cb.get()
        meaurement_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        member_measurement_cursor = meaurement_connection.cursor()
        measurement_query='SELECT * FROM members WHERE mem_id=%s'
        measurement_tuple = (currentValue,)
        try:
            member_measurement_cursor.execute(measurement_query, measurement_tuple)

            for row in member_measurement_cursor:
                self.__member_meas_name_tb.insert(0, row[1])
                # self.__member_name_tb.config(state='readonly')
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

        member_measurement_cursor.close()
        meaurement_connection.close()
    def __member_edit_name_for_measurement(self, e):
        currentValue = self.__measurement_edit_id_cb.get()
        self.__member_edit_id_tb.delete(0, 'end')
        self.__member_edit_name_tb.delete(0, 'end')
        self.__member_edit_height_tb.delete(0, 'end')
        self.__member_edit_weight_tb.delete(0, 'end')
        self.__member_edit_age_tb.delete(0, 'end')

        meaurement_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        member_measurement_cursor = meaurement_connection.cursor()
        measurement_query='SELECT * FROM members_measurement WHERE measurement_id=%s'
        measurement_tuple = (currentValue,)
        try:
            member_measurement_cursor.execute(measurement_query, measurement_tuple)

            for row in member_measurement_cursor:
                self.__member_edit_id_tb.insert(0, row[1])
                self.__member_edit_name_tb.insert(0, row[2])
                self.__member_edit_height_tb.insert(0, row[3])
                self.__member_edit_weight_tb.insert(0, row[4])
                self.__member_edit_age_tb.insert(0, row[5])
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

        member_measurement_cursor.close()
        meaurement_connection.close()
    def __send_member_measurement_values(self, members_window):
        mem_id = self.__member_select_id_cb.get()
        mem_name = self.__member_meas_name_tb.get()
        mem_height = self.__member_meas_height_tb.get()
        mem_weight = self.__member_meas_weight_tb.get()
        mem_age = self.__member_age_tb.get()

        if mem_name and mem_height and mem_weight and mem_age != '':
            memMeasurement = MemberMeasurement(mem_id,mem_name, mem_height, mem_weight, mem_age)
            memMeasurement.create_meaurement_table()
            response= memMeasurement.save_member_measurement(members_window)
            if response:
                self.__member_select_id_cb.set('')
                self.__member_name_tb.delete(0, 'end')
                self.__member_height_tb.delete(0, 'end')
                self.__member_weight_tb.delete(0, 'end')
                self.__member_age_tb.delete(0, 'end')
        else:
            messagebox.showerror('Fitness Club Management System',
                                 'All fields are required. Please change index and enter height and width of the member.',
                                 parent=members_window)
    def __view_member_measurement_table(self):
        measurement_window = tk.Toplevel()
        measurement_window.title('Member Measurement')
        measurement_window.geometry('620x290+500+250')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        measurement_window.iconphoto(False, window_icon)
        measurement_window.resizable(False, False)
        measurement_window.grab_set()
        measurement_window.wm_attributes('-topmost', True)
        # creating scrollbar
        mem_measurement_scrollbar = tk.Scrollbar(measurement_window)
        mem_measurement_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating measurement treeview table
        mem_measurement_table = ttk.Treeview(measurement_window,show='headings',height=290,columns=('meas_id','mem_id','mem_name','mem_height','mem_weight','mem_age'))
        mem_measurement_table.place(x=0, y=0)
        mem_measurement_table.config(yscrollcommand=mem_measurement_scrollbar.set)
        mem_measurement_table.heading('meas_id', text='Measurement ID')
        mem_measurement_table.heading('mem_id', text='Member ID')
        mem_measurement_table.heading('mem_name', text='Member Name')
        mem_measurement_table.heading('mem_height', text='Member Height')
        mem_measurement_table.heading('mem_weight', text='Member Weight')
        mem_measurement_table.heading('mem_age', text='Member Age')
        mem_measurement_table.column('meas_id', width=100, minwidth=100, anchor=tk.CENTER)
        mem_measurement_table.column('mem_id', width=100, minwidth=100, anchor=tk.CENTER)
        mem_measurement_table.column('mem_name', width=100,minwidth=100, anchor=tk.CENTER)
        mem_measurement_table.column('mem_height', width=100,minwidth=100, anchor=tk.CENTER)
        mem_measurement_table.column('mem_weight', width=100,minwidth=100, anchor=tk.CENTER)
        mem_measurement_table.column('mem_age', width=100,minwidth=100, anchor=tk.CENTER)
        # styling table
        table_style = ttk.Style(mem_measurement_table)
        table_style.theme_use('clam')
        table_style.configure('Treeview.Heading', font=('arial', 10, 'italic'), background='orange4', foreground='white')
        table_style.configure('Treeview', font=('arial', 10, 'italic'), background='lightgrey', foreground='black')
        # fetching data from database
        mem_measurement_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        mem_measurement_cursor = mem_measurement_connection.cursor()
        mem_measurement_query = 'SELECT * FROM members_measurement'
        try:
            mem_measurement_cursor.execute(mem_measurement_query)
            for row in mem_measurement_cursor:
                mem_measurement_table.insert('', 'end', values=row)
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

        mem_measurement_cursor.close()
        mem_measurement_connection.close()
    def __send_measurement_values_for_edit(self, edit_window):
        currentValue = self.__measurement_edit_id_cb.get()
        mem_name = self.__member_edit_name_tb.get()
        mem_height = self.__member_edit_height_tb.get()
        mem_weight = self.__member_edit_weight_tb.get()
        mem_age = self.__member_edit_age_tb.get()
        if mem_name == '' or mem_height == '' or mem_weight == '' or mem_age == '' or currentValue == -1:
            messagebox.showerror('Fitness Club Management System', 'All fields are required!', parent= edit_window)
        else:
            edit_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
            edit_cursor = edit_connection.cursor()
            edit_query = 'UPDATE members_measurement SET mem_name=%s, mem_height=%s, mem_weight=%s, mem_age=%s WHERE measurement_id=%s'
            edit_tuple = (mem_name, mem_height, mem_weight, mem_age, currentValue)
            try:
                edit_cursor.execute(edit_query, edit_tuple)
                edit_connection.commit()
                messagebox.showinfo('Fitness Club Management System', 'Member measurement updated successfully!', parent= edit_window)
                edit_connection.close()
            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e), parent= edit_window)

        # self.__measurement_edit_id_cb.current(-1)
        self.__member_edit_name_tb.delete(0, 'end')
        self.__member_edit_height_tb.delete(0, 'end')
        self.__member_edit_weight_tb.delete(0, 'end')
        self.__member_edit_age_tb.delete(0, 'end')
    def __edit_member_measurement_table(self):
        edit_window = tk.Toplevel(bg='lightgrey')
        edit_window.title('Edit Member Measurement')
        edit_window.geometry('450x300+250+250')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        edit_window.iconphoto(False, window_icon)
        edit_window.resizable(False, False)
        edit_window.grab_set()
        edit_window.wm_attributes('-topmost', True)
        # measurement selection id
        measurement_id_lbl = ttk.Label(master=edit_window, text='Select measurement ID: ', background='lightgrey',
                                  font='arial 9 italic')
        measurement_id_lbl.place(x=20, y=10)
        self.__measurement_edit_id_cb = ttk.Combobox(master=edit_window, width=15)
        self.__measurement_edit_id_cb.place(x=160, y=10)
        self.__member_measurement_selectionID_update(self.__measurement_edit_id_cb)
        # calling function
        self.__measurement_edit_id_cb.current(0)
        # if self.__measurement_edit_id_cb.current() != -1:
        self.__measurement_edit_id_cb.bind('<<ComboboxSelected>>', self.__member_edit_name_for_measurement)
        # else:
        #     messagebox.showerror('Fitness Club Management System', 'Please select Id!', parent= edit_window)
        # member selection id
        member_id_lbl = ttk.Label(master=edit_window, text='Select member ID: ', background='lightgrey',
                                  font='arial 9 italic')
        member_id_lbl.place(x=20, y=50)
        self.__member_edit_id_tb = tk.Entry(master=edit_window, width=25,font='arial 9 italic')
        self.__member_edit_id_tb.place(x=160, y=50)
        # member name
        member_name_lbl = ttk.Label(edit_window, text='Member Name: ', background='lightgrey',
                                     font='arial 9 italic')
        member_name_lbl.place(x=20, y=90)
        self.__member_edit_name_tb = ttk.Entry(edit_window, width=25, font='arial 9 italic')
        self.__member_edit_name_tb.place(x=160, y=90)
        # member height
        member_height_lbl = ttk.Label(edit_window,text='Member Height(cm): ',background='lightgrey',font='arial 9 italic')
        member_height_lbl.place(x=20, y=130)
        self.__member_edit_height_tb=ttk.Entry(edit_window, width=25, font='arial 9 italic')
        self.__member_edit_height_tb.place(x=160, y=130)
        # member weight
        member_weight_lbl = ttk.Label(master=edit_window,text='Member Weight(Kg): ',background='lightgrey',font='arial 9 italic')
        member_weight_lbl.place(x=20, y=180)
        self.__member_edit_weight_tb = ttk.Entry(edit_window, width=25, font='arial 9 italic', background='lightgrey')
        self.__member_edit_weight_tb.place(x=160, y=170)
        # member age
        member_age_lbl = ttk.Label(edit_window,text='Member Age: ',background='lightgrey',font='arial 9 italic')
        member_age_lbl.place(x=20, y=200)
        self.__member_edit_age_tb = ttk.Spinbox(edit_window, width=10, font='arial 9 italic',from_=1, to=150)
        self.__member_edit_age_tb.place(x=160, y=200)
        # button for table
        member_edit_btn = tk.Button(edit_window, text='Edit', width=10, background='maroon2',
                                    foreground='snow', padx=2, pady=5)
        member_edit_btn.place(x=250, y=250)
        member_edit_btn.config(command=lambda :self.__send_measurement_values_for_edit(edit_window))
    def __del_member_measurement_table(self):
        del_window = tk.Toplevel(bg='lightgrey')
        del_window.title('Delete Member Measurement')
        del_window.geometry('300x150+800+450')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        del_window.iconphoto(False, window_icon)
        del_window.resizable(False, False)
        del_window.grab_set()
        del_window.wm_attributes('-topmost', True)
        # creating selection id
        member_id_lbl = ttk.Label(master=del_window, text='Select measurement ID: ', background='lightgrey',
                                  font='arial 9 italic')
        member_id_lbl.place(x=20, y=10)
        self.__member_del_id_cb = ttk.Combobox(master=del_window, width=15)
        self.__member_del_id_cb.place(x=160, y=10)
        self.__measurement_del_selectionID_update(self.__member_del_id_cb)  # calling function
        # defining inner function
        def del_measurement():
            if self.__member_del_id_cb.current() != -1:
                answer = messagebox.askyesno('Fitness Club Management System', 'Do you really want to delete?', parent=del_window)
                if answer:
                    del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
                    del_cursor = del_connection.cursor()
                    del_query = 'DELETE FROM members_measurement WHERE measurement_id=%s'
                    del_tuple = (self.__member_del_id_cb.get(),)
                    try:
                        del_cursor.execute(del_query, del_tuple)
                        del_connection.commit()
                        del_connection.close()
                        messagebox.showinfo('Fitness Club Management System', 'Member measurement deleted successfully!', parent= del_window)
                    except :
                        messagebox.showerror('Fitness Club Management System', 'Member measurement deletion failed', parent = del_window)
            else:
                messagebox.showerror('Fitness Club Management System', 'Please select id first!', parent=del_window)
        # Button for saving member data
        del_btn = tk.Button(del_window, text="Del", width=20, background='red2',
                                       foreground='snow', padx=5, pady=5)
        del_btn.place(x=70, y=80)

        del_btn.config(command=del_measurement)
    def __showMemberMeasurementPanel(self, member_add_workspace, members_window):
        member_meas_upperframe = tk.LabelFrame(member_add_workspace, width=410, height=290,text='Member Measurement: ', font='arial 11 italic bold',
                                         bg='lightgrey', fg='maroon2')
        member_meas_upperframe.place(x=760, y=70)
        # member selection id
        member_id_lbl = ttk.Label(master=member_meas_upperframe,text='Select member ID: ',background='lightgrey',font='arial 9 italic')
        member_id_lbl.place(x=20, y=10)
        self.__member_select_id_cb=ttk.Combobox(master=member_meas_upperframe, width=15)
        self.__member_select_id_cb.place(x=160, y=10)
        self.__member_upd_selectionID_update(self.__member_select_id_cb) # calling function
        self.__member_select_id_cb.current(0)
        if self.__member_select_id_cb.current() != -1:
            self.__member_select_id_cb.bind('<<ComboboxSelected>>', self.__member_name_for_measurement)
        else:
            messagebox.showerror('Fitness Club Management System', 'Please select Id!', parent=members_window)
        # member name
        member_name_lbl=tk.Label(member_meas_upperframe, text='Member Name: ', background='lightgrey', font='arial 9 italic')
        member_name_lbl.place(x=20, y=50)
        self.__member_meas_name_tb=tk.Entry(member_meas_upperframe, width=25, font='arial 9 italic')
        self.__member_meas_name_tb.place(x=160, y=50)
        # member height
        member_height_lbl = tk.Label(member_meas_upperframe,text='Member Height (m): ',background='lightgrey',font='arial 9 italic')
        member_height_lbl.place(x=20, y=90)
        self.__member_meas_height_tb=tk.Entry(member_meas_upperframe, width=25, font='arial 9 italic')
        self.__member_meas_height_tb.place(x=160, y=90)
        # member weight
        member_weight_lbl = tk.Label(master=member_meas_upperframe,text='Member Weight (Kg): ',background='lightgrey',font='arial 9 italic')
        member_weight_lbl.place(x=20, y=130)
        self.__member_meas_weight_tb = tk.Entry(member_meas_upperframe, width=25, font='arial 9 italic')
        self.__member_meas_weight_tb.place(x=160, y=130)
        # member age
        member_age_lbl = tk.Label(member_meas_upperframe,text='Member Age: ',background='lightgrey',font='arial 9 italic')
        member_age_lbl.place(x=20, y=170)
        self.__member_age_tb = ttk.Spinbox(member_meas_upperframe, width=10, font='arial 9 italic',from_=1, to_=150)
        self.__member_age_tb.place(x=160, y=170)
        # button for table
        member_view_btn = tk.Button(member_meas_upperframe, text='View Table', width=10, background='maroon2',foreground='snow', padx=5, pady=5)
        member_view_btn.place(x=20, y=225)
        member_view_btn.config(command=self.__view_member_measurement_table)
        # button for table
        member_edit_btn = tk.Button(member_meas_upperframe, text='Edit', width=10, background='maroon2',
                                    foreground='snow', padx=2, pady=5)
        member_edit_btn.place(x=120, y=225)
        member_edit_btn.config(command=self.__edit_member_measurement_table)
        # Button for saving member data
        member_meas_saveBtn=tk.Button(member_meas_upperframe,text="Save", width=10, background='lightblue2', foreground='magenta4', padx=5, pady=5)
        member_meas_saveBtn.place(x=210, y=225)
        member_meas_saveBtn.config(command= lambda: self.__send_member_measurement_values(members_window))
        # Button for saving member data
        member_meas_delBtn = tk.Button(member_meas_upperframe, text="Delete", width=10, background='red2',
                                        foreground='snow', padx=5, pady=5)
        member_meas_delBtn.place(x=310, y=225)
        member_meas_delBtn.config(command=self.__del_member_measurement_table)
    def __update_member_id_from_measurement_table(self, select_member_ID_cb):
        bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        bmi_cursor = bmi_connection.cursor()
        bmi_id_list = []
        bmi_query = 'SELECT mem_id from members_measurement'
        try:
            bmi_cursor.execute(bmi_query)
            bmi_result = bmi_cursor.fetchall()
            for i in bmi_result:
                bmi_id_list.append(i)
            bmi_cursor.close()
            bmi_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)

        bmi_id_list.sort()
        select_member_ID_cb.config(values=bmi_id_list)
        select_member_ID_cb.after(200, lambda: self.__update_member_id_from_measurement_table(select_member_ID_cb))
    def __get_measurement_values_for_BMI(self, e):
        currentValue = self.__select_member_ID_cb.get()
        # clearing the controls
        self.__member_name_tb.delete(0, 'end')
        self.__member_height_tb.delete(0, 'end')
        self.__member_weight_tb.delete(0, 'end')
        self.__bmi_tb.delete(0, 'end')
        # creating connection
        bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        bmi_cursor = bmi_connection.cursor()
        bmi_query = 'SELECT * FROM members_measurement WHERE mem_id=%s'
        try:
            bmi_cursor.execute(bmi_query, (currentValue,))
            for row in bmi_cursor:
                self.__member_name_tb.insert(0, row[2])
                self.__member_height_tb.insert(0, row[3])
                self.__member_weight_tb.insert(0, row[4])
            bmi_cursor.close()
            bmi_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)
    def __send_member_BMI_values(self, members_window):
        currentID = self.__select_member_ID_cb.get()
        mem_bmi = self.__bmi_tb.get()
        if mem_bmi == '':
            messagebox.showerror('Fitness Club Management System', 'Please calculate BMI first!', parent=members_window)
        else:
            memSaveBmi = SaveBMI(currentID, mem_bmi)
            memSaveBmi.create_BMI_table()
            memSaveBmi.save_bmi(members_window)
    def __showMemberBMIPanel(self,member_add_workspace, members_window):
        member_BMI_insertion_panel=tk.LabelFrame(member_add_workspace, text='Member BMI: ',width=410, height=250,
                                                 background='lightgrey', font='arial 11 italic bold', foreground='maroon2')
        member_BMI_insertion_panel.place(x=760, y=370)
        # member selection id
        select_member_ID_lbl= ttk.Label(member_BMI_insertion_panel, text='Select Member ID',background='lightgrey',font='arial 9 italic')
        select_member_ID_lbl.place(x=20, y=10)
        self.__select_member_ID_cb=ttk.Combobox(member_BMI_insertion_panel, width=17)
        self.__select_member_ID_cb.place(x=160, y=10)
        self.__update_member_id_from_measurement_table(self.__select_member_ID_cb)
        self.__select_member_ID_cb.current(0)
        # if self.__select_member_ID_cb.current()!= -1:
        self.__select_member_ID_cb.bind('<<ComboboxSelected>>', self.__get_measurement_values_for_BMI)
        # else:
        #     messagebox.showerror('Fitness Club Management System', 'Please select Id!', parent=members_window)
        # member name
        member_name_lbl=ttk.Label(master=member_BMI_insertion_panel,text='Member Name:', background='lightgrey', font='arial 9 italic')
        member_name_lbl.place(x=20, y=40)
        self.__member_name_tb=tk.Entry(master=member_BMI_insertion_panel, width=25)
        self.__member_name_tb.place(x=160, y=40)
        # member height
        member_height_lbl=ttk.Label(master=member_BMI_insertion_panel, text='Member Height:', background='lightgrey', font='arial 9 italic')
        member_height_lbl.place(x=20, y=80)
        self.__member_height_tb=tk.Entry(master=member_BMI_insertion_panel, width=25)
        self.__member_height_tb.place(x=160, y=80)
        # member weight
        member_weight_lbl = ttk.Label(master=member_BMI_insertion_panel, text='Member Weight:', background='lightgrey',font='arial 9 italic')
        member_weight_lbl.place(x=20, y=120)
        self.__member_weight_tb = ttk.Entry(master=member_BMI_insertion_panel, width=25)
        self.__member_weight_tb.place(x=160, y=120)
        # collection values

        # Button for BMI calculation
        member_bmi_lbl = ttk.Label(master=member_BMI_insertion_panel, text='Member BMI:', background='lightgrey',
                                      font='arial 9 italic')
        member_bmi_lbl.place(x=20, y=150)
        self.__bmi_tb=ttk.Entry(member_BMI_insertion_panel, width=25)
        self.__bmi_tb.place(x=160, y=150)
        # function for calculating BMI
        def calculate_bmi():
            if self.__member_height_tb.get() != '' and self.__member_weight_tb.get() != '':
                try:
                    height = float(self.__member_height_tb.get())
                    weight = float(self.__member_weight_tb.get())
                    bmi = weight / (height * height)
                    self.__bmi_tb.delete(0, 'end')
                    self.__bmi_tb.insert(0, bmi)
                except Exception as e:
                    messagebox.showerror('Fitness Club Management System', str(e), parent =members_window )
            else:
                messagebox.showerror('Fitness Club Management System', 'Please change index to get info and enter height and weight of the member.', parent=members_window)

        # Button for viewing BMI
        bmi_viewBtn = tk.Button(master=member_BMI_insertion_panel, text='view BMI',
                                background='rosybrown1',
                                foreground='black', width=12, font='arial 9 italic bold', pady=4)
        bmi_viewBtn.place(x=10, y=190)
        view_table = ViewBMI()
        bmi_viewBtn.config(command=view_table.show_bmi_table)
        # Button for calculating BMI
        bmi_calcBtn = tk.Button(master=member_BMI_insertion_panel, text='Calc BMI', background='darkorchid4',
                                foreground='snow', width=8, font='arial 9 italic bold', pady=1)
        bmi_calcBtn.place(x=325, y=144)
        bmi_calcBtn.config(command=calculate_bmi)

        # Button for saving BMI
        bmi_saveBtn=tk.Button(master=member_BMI_insertion_panel, text='Save BMI', background='purple',
                              foreground='snow', width=10, font='arial 9 italic bold', pady=4)
        bmi_saveBtn.place(x=210, y=190)
        bmi_saveBtn.config(command=lambda :self.__send_member_BMI_values(members_window))
        # Button for edit BMI
        bmi_editBtn = tk.Button(master=member_BMI_insertion_panel, text='Edit', background='purple',
                                foreground='snow',width=10, font='arial 9 italic bold', pady=4)
        bmi_editBtn.place(x=120, y=190)
        edit_bmi = EditBMI()
        bmi_editBtn.config(command=edit_bmi.show_edit_bmi_window)
        # Button for del BMI
        bmi_delBtn = tk.Button(master=member_BMI_insertion_panel, text='Del', background='red2',
                                foreground='snow', width=10, font='arial 9 italic bold', pady=4)
        bmi_delBtn.place(x=300, y=190)
        del_bmi = DeleteBMI()
        bmi_delBtn.config(command=del_bmi.show_del_window)
    def __auto_update_class_list(self,member_add_workoutplan_cb):
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
            member_add_workoutplan_cb.config(values=auto_update_class_list)
            auto_update_connection.close()
            member_add_workoutplan_cb.after(200, lambda : self.__auto_update_class_list(member_add_workoutplan_cb))
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))
    def __checkNumberforcontact(self, e):
        try:
            int(self.__member_add_contact_tb.get())
            self.__member_add_contact_tb.config(bg='white')
            if len(self.__member_add_contact_tb.get()) >=11:
                self.__member_add_contact_tb.delete(10, 'end')

        except ValueError:
            self.__member_add_contact_tb.config(bg='red2')
            self.__member_add_contact_tb.delete(0, 'end')
    def __checkNumberforfees(self, e):
        try:
            int(self.__member_add_assign_fees_tb.get())
            self.__member_add_assign_fees_tb.config(bg='white')
            if len(self.__member_add_assign_fees_tb.get()) >= 8:
                self.__member_add_assign_fees_tb.delete(7, 'end')

        except ValueError:
            self.__member_add_assign_fees_tb.config(bg='red2')
            self.__member_add_assign_fees_tb.delete(0, 'end')

from tkinter import messagebox
from FCMS_Files.instructor import *
from FCMS_Files.workoutplan import *
from FCMS_Files.members import *
from FCMS_Files.reports import *
from FCMS_Files.pdfreport import *
from FCMS_Files.backup_database import *
import datetime

class fcms_dashboard:

    def __init__(self, username, email, contact, mng_id):
        self.__d_username = username
        self.__d_email = email
        self.__d_contact = contact
        self.__d_mng_id = mng_id
    def __confirmwindowclose(self):
        answer = tk.messagebox.askyesno('Fitness Club Management System', "Do you want to close the application?")
        if answer:
            self.__dashboardwindow.destroy()
    def __showTime(self):
        dateVar = datetime.datetime.now()
        currentTime = dateVar.strftime("%I:%M:%S %p")
        todayDate = dateVar.strftime("%d/%m/%Y")
        self.__clock.config(text="Current Time: " + currentTime)
        self.__fcms_dashboard_datelbl.config(text="Today's Date: " + todayDate)
        self.__clock.after(200, self.__showTime)
    def showdashboard(self):
        self.__dashboardwindow = tk.Tk()
        self.__dashboardwindow.title("Fitness Club Management System")
        self.__dashboardwindow.geometry("1366x968")
        self.__dashboardwindow.resizable(False, False)
        self.__dashboardwindow.state("zoomed")
        self.__dashboardwindowicon = tk.PhotoImage(file="Images/fcms_icon.png")
        self.__dashboardwindow.iconphoto(False, self.__dashboardwindowicon)

        # creating background image
        bg_image = tk.PhotoImage(file='Images/fcms_bg_2.png')
        self.__dashboard_bg_label = tk.Label(self.__dashboardwindow, image=bg_image)
        self.__dashboard_bg_label.pack(fill='both', expand=1)

        # creating management panel
        self.__managementpanel = tk.Frame(self.__dashboard_bg_label, width=300, bg='mediumvioletred', bd=1, height=900)
        self.__managementpanel.place(x=-2, y=-1)
        self.__managementpanel_heading_frame = tk.Frame(self.__managementpanel, bg='maroon2', height=83, width=302,
                                                        bd=1, relief=tk.RAISED)
        self.__managementpanel_heading_frame.place(x=-2, y=-3)
        self.__managementpanel_heading_label = tk.Label(self.__managementpanel_heading_frame, text='Management Panel',
                                                        fg='floralwhite', font=('Arial', 20, 'bold'), bg='maroon2')
        self.__managementpanel_heading_label.place(x=20, y=20)
        # creating manager info panel
        self.__main_header_panel=tk.Frame(self.__dashboard_bg_label, width=1300, height=100,bd=2, bg='maroon4')
        self.__main_header_panel.place(x=298,y=0)
        self.__manager_info_panel = tk.Frame(self.__main_header_panel, width=800, height=80, bd=2, bg='maroon3', relief=tk.SUNKEN)
        self.__manager_info_panel.place(x=200, y=10)
        # name label
        manager_name = tk.Label(self.__manager_info_panel, text='Name: ', fg='floralwhite',
                                       font=('Arial', 10, 'bold'), bg='maroon3')
        manager_name.place(x=100, y=10)
        self.__manager_name_value = tk.Label(self.__manager_info_panel, text=str(self.__d_username), fg='white',
                                             font=('Arial', 10, 'italic'), bg='maroon3')
        self.__manager_name_value.place(x=190, y=10)
        # email label
        manager_email = tk.Label(self.__manager_info_panel, text='Email: ', fg='floralwhite',
                                        font=('Arial', 10, 'bold'), bg='maroon3')
        manager_email.place(x=100, y=30)
        self.__manager_email_value = tk.Label(self.__manager_info_panel, text=str(self.__d_email), fg='white',
                                              font=('Arial', 10, 'italic'), bg='maroon3')
        self.__manager_email_value.place(x=190, y=30)
        # contact label
        manager_contact = tk.Label(self.__manager_info_panel, text='Contact: ', fg='floralwhite',
                                          font=('Arial', 10, 'bold'), bg='maroon3')
        manager_contact.place(x=100, y=50)
        self.__manager_contact_value = tk.Label(self.__manager_info_panel, text=str(self.__d_contact), fg='white',
                                                font=('Arial', 10, 'italic'), bg='maroon3')
        self.__manager_contact_value.place(x=190, y=50)
        # manager id label
        manager_id_lbl = tk.Label(self.__manager_info_panel, text='Manager ID: ', fg='floralwhite',
                                         bg='maroon3', font=('Arial', 18, 'bold'), bd=2)
        manager_id_lbl.place(x=550, y=20)
        self.__manager_id_value = tk.Label(self.__manager_info_panel, text=str(self.__d_mng_id), fg='floralwhite',
                                           bg='maroon3', font=('Arial', 18, 'bold'), bd=2)
        self.__manager_id_value.place(x=690, y=20)

        # instructor panel
        inst_panel = tk.LabelFrame(self.__managementpanel, text='Instructor: ',
                                          bg='mediumvioletred', bd=3, width=280, height=90,
                                          font=('Arial', 12,'bold', 'italic'), fg='purple4')
        inst_panel.place(x=10, y=100)
        # creating button on instructor panel
        inst_btn=tk.Button(inst_panel,text='INSTRUCTOR', fg='black',bg='hotpink', width=30,
                             padx=15, pady=8, activebackground='mediumvioletred')
        inst_btn.place(x=10,y=13)
        inst = Instructor()  # creating object variable of Instructor class
        inst_btn.config(command=inst.showInstructorManagementPanel)

        # members registration panel
        members_registration_panel = tk.LabelFrame(self.__managementpanel, text='Members Registration: ',
                                                          bg='mediumvioletred', bd=3, width=280, height=100,
                                                          font=('Arial', 12,'bold', 'italic'), fg='purple4')
        members_registration_panel.place(x=10, y=200)
        # member add button
        mem_Btn = tk.Button(members_registration_panel, text='MEMBER REGISTRATION', width=30, fg='black', bg='hotpink',
                                padx=19, pady=12,
                                activebackground='mediumvioletred')
        mem_Btn.place(x=10, y=15)
        members_registration = MembersRegistration()
        mem_Btn.config(command=members_registration.showMemberManagementPanel)

        # workplan panel
        workoutplan_panel = tk.LabelFrame(self.__managementpanel, text='Workout plan: ', bg='mediumvioletred', bd=3,
                                              width=280, height=70,
                                              font=('Arial', 12,'bold', 'italic'), fg='purple4')
        workoutplan_panel.place(x=10, y=310)
        WP_Btn = tk.Button(workoutplan_panel, text='WORKOUT PLAN', fg='black', bg='hotpink', padx=15,
                                      pady=6,
                                      activebackground='mediumvioletred', width=30)
        WP_Btn.place(x=10, y=6)
        workoutplan = Workplan()
        WP_Btn.config(command=workoutplan.showWorkoutPlanManagement)



        # reports panel
        reports = Reports()
        reports_panel = tk.LabelFrame(self.__managementpanel, text='Reports: ', bg='mediumvioletred', bd=3,
                                             width=280, height=130,
                                             font=('Arial', 12,'bold', 'italic'), fg='purple4')
        reports_panel.place(x=10, y=390)
        # fees window
        fees_Btn = tk.Button(reports_panel, text='FEES REPORT', fg='black', bg='hotpink', padx=17, pady=6,
                             activebackground='mediumvioletred')
        fees_Btn.place(x=10, y=10)
        fees_Btn.config(command=reports.showFeesPanel)
        # Create expense window
        expense_Btn = tk.Button(reports_panel, text='EXPENSE REPORT', fg='black', bg='hotpink', padx=7,
                                       pady=6, activebackground='mediumvioletred')
        expense_Btn.place(x=10, y=60)
        expense_Btn.config(command=reports.showExpensePanel)
        # creating salary panel
        salary_btn = tk.Button(reports_panel, text='SALARY REPORT', fg='black', bg='hotpink', padx=13,
                                      pady=6, activebackground='mediumvioletred')
        salary_btn.place(x=140, y=10)
        salary_btn.config(command=reports.showSalaryPanel)
        # creating profit panel
        profit_btn = tk.Button(reports_panel, text='PROFIT REPORT', fg='black', bg='hotpink', padx=15,
                                      pady=6, activebackground='mediumvioletred')
        profit_btn.place(x=140, y=60)
        profit_btn.config(command=reports.showProfitPanel)
        # generating pdf reports
        generate_report_pdf = tk.LabelFrame(self.__managementpanel, text='Generate Report in PDF: ', bg='mediumvioletred', bd=3,
                                            width=280, height=150,
                                            font=('Arial', 12,'bold', 'italic'), fg='purple4')
        generate_report_pdf.place(x=10, y=530)
        pdf_repo = PDF_Report(generate_report_pdf)
        pdf_repo.show_pdf_panel()
        # creating database backup
        backup_database_mysql = tk.LabelFrame(self.__managementpanel, text="Database backup: ", bg='mediumvioletred', bd=3,
                                              width=280, height=80,
                                              font=('Arial', 12,'bold', 'italic'), fg='purple4')
        backup_database_mysql.place(x=10, y=690)
        monthly_report_btn = tk.Button(backup_database_mysql, text="BACKUP FCMS DATABASE", width=30,
                                       padx=15, pady=8, bg='hotpink', activebackground='mediumvioletred',
                                       fg='black')
        monthly_report_btn.place(x=10, y=10)
        bd = BackupDB()  # creating the object of class
        monthly_report_btn.config(command = bd.create_backup_db)
        # creating FCMS record button
        fcms_record_frame = tk.LabelFrame(self.__managementpanel, text='FCMS Record: ',bg='mediumvioletred', bd=3,
                                          width=280, height=80,
                                          font=('Arial', 12,'bold', 'italic'), fg='purple4')
        fcms_record_frame.place(x=10, y=780)
        show_record_button = tk.Button(fcms_record_frame, text='Show', width=30, padx=15, pady=8, bg='hotpink',activebackground='mediumvioletred',
                                       fg='black')
        show_record_button.place(x=10, y=10)
        show_record_button.config(command=self.__show_instructor_and_members_tables)
        # creating clock
        self.__fcms_dashboard_datelbl = tk.Label(self.__dashboard_bg_label, fg='lightyellow', font=('Arial', 10, 'bold'),
                                                 bg='maroon4')
        self.__fcms_dashboard_datelbl.place(x=1390, y=10)
        self.__clock = tk.Label(self.__dashboard_bg_label, fg='floralwhite', font=('Arial', 10, 'bold'), bg='maroon4')
        self.__clock.place(x=1390, y=30)
        self.__showTime()
        self.__dashboardwindow.protocol('WM_DELETE_WINDOW', self.__confirmwindowclose)
        # self.__dashboardwindow.protocol('WM_DELETE_WINDOW', False)
        self.__dashboardwindow.mainloop()
    def __show_instructor_and_members_tables(self):
        workspace_window = tk.Toplevel()
        workspace_window.geometry('1200x650+350+200')
        workspace_window.title('Fitness Club and Management System(FCMS)')
        workspace_window.config(bg='indianred4')
        workspace_window.grab_set()
        workspace_window.attributes('-topmost', True)
        workspace_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        instructor_lbl = tk.Label(workspace_window, text="FITNESS CLUB STAFF AND MEMBER INFORMATION", bg='indianred4',
                                  foreground='snow', font=('arial',16, 'italic bold'), bd=2, padx=12, pady=2)
        instructor_lbl.place(x=300, y=10)
        # workspace_frame.config(bg='indianred4')
        instructor_frame = tk.Frame(workspace_window, width=1100, height=150, bd=1)
        instructor_frame.place(x=30, y=50)
        # creating scrollbar for frame
        inst_scrollbar = ttk.Scrollbar(instructor_frame)
        inst_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating instructor table
        instructor_table = ttk.Treeview(instructor_frame, show='headings' ,yscrollcommand=inst_scrollbar.set, height=7)
        # instructor_table.pack(fill=tk.BOTH, expand=True)
        instructor_table.place(x=0, y=0)
        inst_scrollbar.config(command=instructor_table.yview)
        # table styling
        table_style = ttk.Style(instructor_table)
        table_style.theme_use('clam')
        table_style.configure('Treeview', rowheight=25, font=('Arial', 10, 'bold'))
        table_style.configure('Treeview.Heading', font=('Arial', 12, 'bold'), background='maroon2', foreground='snow')
        #creating instructor table headings
        instructor_table['columns'] = ('Inst_ID', 'FullName', 'Email','JoiningDate', 'Address', 'Contact', 'Specialization', 'Age',"Qualification" )
        instructor_table.heading('Inst_ID', text='Inst ID', anchor=tk.CENTER)
        instructor_table.heading('FullName', text='Full Name', anchor=tk.CENTER)
        instructor_table.heading('Email', text='Email', anchor=tk.CENTER)
        instructor_table.heading('JoiningDate', text='Joining Date', anchor=tk.CENTER)
        instructor_table.heading('Address', text='Address', anchor=tk.CENTER)
        instructor_table.heading('Contact', text='Contact', anchor=tk.CENTER)
        instructor_table.heading('Specialization', text='Specialization', anchor=tk.CENTER)
        instructor_table.heading('Age', text='Age', anchor=tk.CENTER)
        instructor_table.heading('Qualification', text='Qualification', anchor=tk.CENTER)
        #creating instructor table column
        instructor_table.column('Inst_ID', width=80, minwidth=80, anchor=tk.CENTER)
        instructor_table.column('FullName', width=150, minwidth=150, anchor=tk.CENTER)
        instructor_table.column('Email', width=150, minwidth=150, anchor=tk.CENTER)
        instructor_table.column('JoiningDate', width=120, minwidth=120, anchor=tk.CENTER)
        instructor_table.column('Address', width=150, minwidth=150, anchor=tk.CENTER)
        instructor_table.column('Contact', width=100, minwidth=100, anchor=tk.CENTER)
        instructor_table.column('Specialization', width=150, minwidth=150, anchor=tk.CENTER)
        instructor_table.column('Age', width=80, minwidth=80, anchor=tk.CENTER)
        instructor_table.column('Qualification', width=150, minwidth=150, anchor=tk.CENTER)
        instructor_table.pack(fill=tk.BOTH, expand=True)
        # populating the table
        inst_query = 'SELECT * FROM instructor'
        try:
            inst_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
            inst_cursor = inst_connection.cursor()
            inst_cursor.execute(inst_query)
            inst_result = inst_cursor.fetchall()
            for row in inst_result:
                instructor_table.insert('', tk.END, values=(row[0], row[1]+' '+row[2], row[3], row[4], row[5], row[11], row[9], row[8], row[7]))
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)


        #creating for members table

        mem_frame = tk.Frame(workspace_window, width=1100, height=250, bd=1)
        mem_frame.place(x=30, y=290)
        # creating scrollbar for frame
        mem_scrollbar = ttk.Scrollbar(mem_frame)
        mem_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # creating instructor table
        mem_table = ttk.Treeview(mem_frame, show='headings', yscrollcommand=mem_scrollbar.set, height=12)
        # instructor_table.pack(fill=tk.BOTH, expand=True)
        mem_table.place(x=0, y=0)
        mem_scrollbar.config(command=mem_table.yview)
        # table styling
        mem_style = ttk.Style(mem_table)
        mem_style.theme_use('clam')
        mem_style.configure('Treeview', rowheight=25, font=('Arial', 10, 'bold'))
        mem_style.configure('Treeview.Heading', font=('Arial', 12, 'bold'), background='maroon2', foreground='snow')
        # creating instructor table headings
        mem_table['columns'] = (
        'Member_ID', 'FullName', 'Email', 'JoiningDate', 'Address', 'Contact', 'WorkoutPlan','AssignedFees')
        mem_table.heading('Member_ID', text='Member ID', anchor=tk.CENTER)
        mem_table.heading('FullName', text='Full Name', anchor=tk.CENTER)
        mem_table.heading('Email', text='Email', anchor=tk.CENTER)
        mem_table.heading('JoiningDate', text='Joining Date', anchor=tk.CENTER)
        mem_table.heading('Address', text='Address', anchor=tk.CENTER)
        mem_table.heading('Contact', text='Contact', anchor=tk.CENTER)
        mem_table.heading('WorkoutPlan', text='Workout Plan', anchor=tk.CENTER)
        mem_table.heading('AssignedFees', text='Assigned Fees', anchor=tk.CENTER)
        # creating instructor table column
        mem_table.column('Member_ID', width=100, minwidth=100, anchor=tk.CENTER)
        mem_table.column('FullName', width=160, minwidth=160, anchor=tk.CENTER)
        mem_table.column('Email', width=150, minwidth=150, anchor=tk.CENTER)
        mem_table.column('JoiningDate', width=120, minwidth=120, anchor=tk.CENTER)
        mem_table.column('Address', width=150, minwidth=150, anchor=tk.CENTER)
        mem_table.column('Contact', width=120, minwidth=120, anchor=tk.CENTER)
        mem_table.column('WorkoutPlan', width=180, minwidth=180, anchor=tk.CENTER)
        mem_table.column('AssignedFees', width=150, minwidth=150, anchor=tk.CENTER)
        mem_table.pack(fill=tk.BOTH, expand=True)
        # populating the table
        mem_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        mem_cursor = mem_connection.cursor()
        mem_query = 'SELECT * FROM members'
        try:
            mem_cursor.execute(mem_query)
            mem_result = mem_cursor.fetchall()
            for row in mem_result:
                mem_table.insert('', tk.END, values=(
                row[0], row[1] + ' ' + row[2], row[3], row[7], row[5], row[4], row[6], row[8]))
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)


from FCMS_Files.Registeration import *
from fcms_dashboard import *
import tkinter as tk
from tkinter import messagebox
import pymysql as pms
class Login:
    def __init__(self, root):
        self.__root = root

    def __show(self):
        self.__hideIcon.config(file='Images/witness.png')
        self.__passwordTB.config(show='')
        self.__hideShowBtn.config(command=self.__hide)

    def __hide(self):
        self.__hideIcon.config(file='Images/hide.png')
        self.__passwordTB.config(show='*')
        self.__hideShowBtn.config(command=self.__show)

    def showRegWindow(self, event):
        reg = Registration()
        reg.showRegistrationPage()
    def __connectDB(self,fcms_root):
        try:
            self.__fcmsDB_connection = pms.connect(host="localhost", user="root", password="", database="fcms")
            self.__fcmsDB_cursor = self.__fcmsDB_connection.cursor()
            self.__connect_DB_Btn.config(text='Connected to Database')
            self.__connect_DB_Btn.config(bg="darkgreen")
            self.__loginBtn.config(state='normal')
            self.__loginBtn.config(cursor='hand2')
            self.__registerBtn.config(state='normal')
            self.__registerBtn.config(cursor='hand2')
            self.__connect_DB_Btn.config(state="disabled")
            self.__forgetBtn.config(state='normal')
            self.__registerBtn.bind("<Button-1>", self.showRegWindow)
            self.__fcmsDB_cursor.execute('''
                create table IF NOT EXISTS manager(
                mng_id INT AUTO_INCREMENT PRIMARY KEY,
                mng_firstName varchar(100) NOT NULL,
                mng_lastName varchar(100) NOT NULL,
                mng_userName varchar(100) NOT NULL,
                mng_email varchar(100) NOT NULL,
                mng_password varchar(100) NOT NULL,
                mng_password_confirmation varchar(100) NOT NULL,
                mng_contact varchar(100) NOT NULL,
                mng_address varchar(100) NOT NULL
                )
            ''')
            self.__fcmsDB_connection.close()
        except Exception as e:
             messagebox.showerror("Fitness Club Management System", "Coudn't connect database server on localhost",
                             parent=fcms_root)
    def __checkPasswordStrength(self, pwd):
        self.__alpha = None
        self.__num = None
        self.__special = None

        if not pwd == '':
            for char in pwd:
                if char.isalpha():
                    self.__alpha = True
                if char.isdigit():
                    self.__num = True
                if not char.isalnum():
                    self.__special = True

        if self.__alpha and self.__num and self.__special == True:
            return True
        else:
            return False
    def __checkCredentials(self,fcms_root):
        uname = self.__usernameTB.get()
        pwd = self.__passwordTB.get()

        if uname == '' and pwd == '':
            tk.messagebox.showinfo("Fitness Club Management System", "Please fill in all the fields",parent=fcms_root)
        else:
            if self.__checkPasswordStrength(pwd):
                fcmsDB_connection = pms.connect(host='localhost', user='root', password='', database='fcms')
                fcmsDB_cursor = fcmsDB_connection.cursor()
                login_query =" SELECT * FROM manager WHERE mng_userName = %s AND mng_password = %s "
                try:
                    fcmsDB_cursor.execute(login_query, (uname,pwd))
                    result = fcmsDB_cursor.fetchone()
                    # creating the object of dashboard class
                    dashboard = fcms_dashboard(result[3], result[4], result[7], result[0])
                    self.__root.destroy()
                    dashboard.showdashboard()

                except:
                    tk.messagebox.showinfo("Fitness Club Management System", "Login failed. Please check your credentials.", parent=fcms_root)
                fcmsDB_cursor.close()
                fcmsDB_connection.close()
            else:
                tk.messagebox.showinfo("Fitness Club Management System",
                                                    "Password must contain alphanumeric with special character", parent=fcms_root)

    def showLoginPage(self,fcms_root):
        self.__bg_image = tk.PhotoImage(file="Images/fcms_bg_2.png")
        bg_label = tk.Label(self.__root, image=self.__bg_image)
        bg_label.pack(fill='both', expand=1)
        # creating button to connect database
        self.__connect_DB_Btn = tk.Button(bg_label, text="Connect to database",
                                                       font=('Calibre', 16, 'italic'), bg='red2', fg='floralwhite',
                                                       activebackground='coral',cursor='hand2',
                                                       activeforeground='tomato', border=2, padx=5, pady=5,
                                                       command=lambda: self.__connectDB(fcms_root))
        self.__connect_DB_Btn.place(x=10, y=10)
        # self.__connect_DB_Btn.place_forget()
        titleHeading = tk.Label(self.__root, text='Fitness Club Management System', fg='lavender',
                                                    font=('Arial', 30, 'bold'), bg='slateblue3', padx=10, pady=10)
        titleHeading.place(x=530, y=30)
        login_frame = tk.Frame(self.__root, width=400, height=460, bd=2, bg='white')
        login_frame.place(x=650, y=200)
        self.__login_title_frame = tk.Frame(login_frame, width=410, height=60, bd=1, bg='deeppink4')
        self.__login_title_frame.place(x=-5, y=-2)
        formTitle = tk.Label(self.__login_title_frame, text="ADMIN LOGIN",
                                                 font=('Arial', 25, 'bold'),
                                                 bg="deeppink4", fg='floralwhite')
        formTitle.place(x=80, y=10)

        # creating username text box
        usernamelbl = tk.Label(login_frame, text="Username:", font=('Arial', 16, 'normal'),
                                                   fg='salmon4', bg='white')
        usernamelbl.place(x=35, y=120)
        self.__usernameTB = tk.Entry(login_frame, width=17, bd=0, font=('calibri', 14, 'normal'),
                                                  fg='black', bg='white')
        self.__usernameTB.place(x=145, y=120)
        bottomlineUsername = tk.Frame(login_frame, width=208, height=2, bg='firebrick')
        bottomlineUsername.place(x=145, y=146)

        # creating password text box
        passwordlbl = tk.Label(login_frame, text="Password:", font=('Arial', 16, 'normal'),
                                                   fg='salmon4', bg='white')
        passwordlbl.place(x=35, y=200)
        self.__passwordTB = tk.Entry(login_frame, width=17, bd=0, font=('calibri', 14, 'normal'),
                                                  fg='black', bg='white', show='*')
        self.__passwordTB.place(x=145, y=200)
        bottomlinePassword = tk.Frame(login_frame, width=208, height=2, bg='firebrick')
        bottomlinePassword.place(x=145, y=226)

        # creating hide and show button
        self.__hideIcon = tk.PhotoImage(file='Images/hide.png')
        self.__hideShowBtn = tk.Button(login_frame, image=self.__hideIcon, bd=0, bg='white',
                                                    activebackground='white', cursor='hand2', command=self.__show)
        self.__hideShowBtn.place(x=328, y=200)
        # creating forget button
        self.__forgetBtn = tk.Button(login_frame, text='Forget password?', fg='darkorchid1', bd=0,
                                                  font=('Arial', 12, 'italic', 'underline'), activebackground='white',
                                                  cursor='hand2', bg='white', state='disabled')
        self.__forgetBtn.place(x=225, y=255)
        self.__forgetBtn.config(command=self.__show_forget_window)
        # creating login button
        self.__loginBtn = tk.Button(login_frame, text='Login', width=20, padx=10, pady=10,
                                                 bg='deeppink2',
                                                 fg='grey99', font=('Arial', 14, 'normal'),
                                                 state='disabled', bd=1)
        self.__loginBtn.place(x=80, y=320)
        self.__loginBtn.config(command=lambda :self.__checkCredentials(fcms_root))
        # creating registration label with button to call registration window
        registrationLabel = tk.Label(login_frame, text="Didn't create account yet?",
                                                         bg='white',
                                                         font=('Arial', 10, 'normal'))
        registrationLabel.place(x=80, y=410)
        self.__registerBtn = tk.Button(login_frame, text="Register Here!", bd=0, fg='blue',
                                                    bg='white',
                                                    activebackground='white', font=('Helvetica', 10, 'italic'), state='disabled')
        self.__registerBtn.place(x=240, y=410)

    def __show_forget_window(self):
        forget_window = tk.Toplevel()
        forget_window.title("Forget Password(FCMS)")
        forget_window.geometry("400x200+650+250")
        forget_window.resizable(False, False)
        forget_window.attributes('-topmost', True)
        forget_window.iconphoto(False, tk.PhotoImage(file='Images/fcms_icon.png'))
        # enter email
        email_lbl = tk.Label(forget_window, text='Enter your email: ', font=('calibri', 14, 'normal'))
        email_lbl.place(x=10, y=10)
        self.__emailTB = tk.Entry(forget_window, width=20, bd=0, font=('calibri', 14, 'normal'), fg='black', bg='white')
        self.__emailTB.place(x=165, y=10)
        # enter contact
        contact_lbl = tk.Label(forget_window, text='Enter your contact: ', font=('calibri',14, 'normal'))
        contact_lbl.place(x=10, y=50)
        self.__contactTB = tk.Entry(forget_window, width=20, bd=0, font=('calibri', 14, 'normal'), fg='black', bg='white')
        self.__contactTB.place(x=165, y=50)
        self.__contactTB.bind('<KeyPress>', self.__checkNumber)
        # show button
        show_btn = tk.Button(forget_window, text='Show', width=20, font=('calibri', 14, 'normal'), fg='snow', bg='maroon2', cursor='hand2')
        show_btn.place(x=120, y=100)
        show_btn.config(command=self.__fetch_password)
        # message label
        self.__message_lbl = tk.Label(forget_window, font=('calibri', 14, 'normal'))
        self.__message_lbl.place(x=10, y=160)
    def __fetch_password(self):
        email = self.__emailTB.get()
        contact = self.__contactTB.get()
        fetch_query = 'SELECT mng_password FROM manager WHERE mng_email=%s ANd mng_contact = %s'
        if not (email and contact) == '':
            try:
                fetch_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
                fetch_cursor = fetch_connection.cursor()
                fetch_cursor.execute(fetch_query,(email, contact))
                fetch_result = fetch_cursor.fetchone()
                if fetch_result:
                    self.__message_lbl.config(text='Your password is: '+str(fetch_result[0]), fg='green')

                else:
                    self.__message_lbl.config(text='Please enter valid email or contact number', fg='blue')

                fetch_cursor.close()
                fetch_connection.close()

            except Exception as e:
                self.__message_lbl.config(text="Error: " + str(e), fg='red2')
        else:
            self.__message_lbl.config(text='Fill in the empty fields', fg='red')

    def __checkNumber(self, e):
        try:
            int(self.__contactTB.get())
            self.__message_lbl.config(text='')
            if len(self.__contactTB.get()) >=11:
                self.__contactTB.delete(10, 'end')
            elif len(self.__contactTB.get()) <10:
                self.__message_lbl.config(text='Enter complete mobile number.', fg='red')

        except ValueError:
            self.__message_lbl.config(text='Invalid contact number', fg='red')
            self.__contactTB.delete(0, 'end')
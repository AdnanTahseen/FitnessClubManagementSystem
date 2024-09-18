import pymysql as pms
import tkinter as tk


class Registration:

    def __checkreg_passwordFormat(self, reg_password):
        num = None
        alpha = None
        special = None

        for char in reg_password:
            if char.isdigit():
                num = True
            if char.isalpha():
                alpha = True
            if not char.isalnum():
                special = True
        if num and alpha and special == True:
            return True
        else:
            return False

    # creating function for matching reg_password
    def __confirmreg_passwordMatch(self, event):
        getreg_passwordVal = self.__reg_reg_password_tb.get()
        getConfirmreg_passwordVal = self.__reg_confirm_reg_password_tb.get()
        reg_passwordStatus = self.__checkreg_passwordFormat(getreg_passwordVal)
        confirmreg_passwordStatus = self.__checkreg_passwordFormat(getConfirmreg_passwordVal)

        if reg_passwordStatus and confirmreg_passwordStatus:
            if getreg_passwordVal == getConfirmreg_passwordVal:
                self.__messagelbl.config(text='Passwords matched.', fg='green')
            else:
                self.__messagelbl.config(text='Passwords do not match.', fg='red')
        else:
            self.__messagelbl.config(text='Password must be alphanumeric with special characters.', fg='orangered')

    # creating function for saving credentials for managers
    def __saveCredentials(self, event):
        fname = self.__reg_firstname_tb.get()
        lname = self.__reg_lastname_tb.get()
        uname = self.__reg_username_tb.get()
        reg_pass = self.__reg_reg_password_tb.get()
        creg_pass = self.__reg_confirm_reg_password_tb.get()
        contact = self.__reg_contact_tb.get()
        email = self.__reg_email_tb.get()
        address = self.__reg_address_tb.get(1.0, tk.END)

        data_insert_tuple = (fname, lname, uname, email, reg_pass, creg_pass, contact, address)

        if not (fname and lname and uname and reg_pass and creg_pass and contact and email and address) == '':
            fcmsDB_connection = pms.connect(host='localhost', user='root', password='', database='fcms')
            insertQuery = '''
                INSERT INTO manager (mng_firstName, mng_lastName, mng_userName,
                                     mng_email, mng_password, mng_password_confirmation, 
                                     mng_contact, mng_address) 
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''

            fcmsDB_cursor = fcmsDB_connection.cursor()
            if fcmsDB_cursor:
                fcmsDB_cursor.execute(insertQuery, data_insert_tuple)
                fcmsDB_connection.commit()
                self.__messagelbl.config(text="Data saved successfully", fg='green')
                fcmsDB_connection.close()
            else:
                self.__messagelbl.config(text='Data insertion failed.', fg='red2')



        else:
            self.__messagelbl.config(text="All fields are required *", fg='red2')

    # creating function for showing registration panel
    def showRegistrationPage(self):
        reg_window = tk.Toplevel()
        reg_window.geometry('1000x700+300+100')
        reg_window.resizable(0, 0)
        regIcon = tk.PhotoImage(file='Images/fcms_icon.png')
        reg_window.iconphoto(False, regIcon)
        reg_window.title('Fitness Club Management System')

        reg_bg_image = tk.PhotoImage(file="Images/fcms_bg_1.png")
        reg_bg_label = tk.Label(reg_window, image=reg_bg_image)
        reg_bg_label.pack(fill='both', expand='yes')

        reg_frame = tk.Frame(reg_window, width=400, height=560, bd=2, bg='hotpink3')
        reg_frame.place(x=300, y=70)
        reg_title_frame = tk.Frame(reg_frame, width=410, height=60, bd=1, bg='hotpink4')
        reg_title_frame.place(x=-5, y=-2)
        reg_title_text = "Manager Registration"
        reg_title_label = tk.Label(reg_title_frame, text=reg_title_text.upper(),
                                   font=('Arial', 16, 'bold'), bg='hotpink4', fg='white')
        reg_title_label.place(x=70, y=10)

        # creating message label
        messageFrame = tk.Frame(reg_frame, bd=2, width=380, height=30, bg='lavenderblush3',
                                relief=tk.GROOVE)
        messageFrame.place(x=6, y=520)
        messageHeading = tk.Label(messageFrame, text="MESSAGE: ", pady=4, padx=2,
                                  bg='hotpink1', fg='blue2', font=('Arial', 8, 'bold'))
        messageHeading.place(x=0, y=0)
        self.__messagelbl = tk.Label(messageFrame, bg='lavenderblush3')
        self.__messagelbl.place(x=67, y=4)

        # creating first text box for first name
        reg_firstname_lbl = tk.Label(reg_frame, text="First Name:",
                                     font=('Arial', 10, 'normal'), fg='cadetblue1', bg='hotpink3')
        reg_firstname_lbl.place(x=30, y=80)
        self.__reg_firstname_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', bd=1,
                                           font=('Arial', 10, 'normal'), fg='grey1')
        self.__reg_firstname_tb.place(x=145, y=80)

        # creating second text box for last name
        reg_lastname_lbl = tk.Label(reg_frame, text="Last Name:", font=('Arial', 10, 'normal'),
                                    fg='cadetblue1', bg='hotpink3')
        reg_lastname_lbl.place(x=30, y=130)
        self.__reg_lastname_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                          font=('Arial', 10, 'normal'), bd=1)
        self.__reg_lastname_tb.place(x=145, y=130)

        # creating third text box for username
        reg_username_lbl = tk.Label(reg_frame, text="Username:", font=('Arial', 10, 'normal'),
                                    fg='cadetblue1', bg='hotpink3')
        reg_username_lbl.place(x=30, y=170)
        self.__reg_username_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                          font=('Arial', 10, 'normal'), bd=1)
        self.__reg_username_tb.place(x=145, y=170)

        # creating fourth text box for email
        reg_email_lbl = tk.Label(reg_frame, text="Email:", font=('Arial', 10, 'normal'),
                                 fg='cadetblue1', bg='hotpink3')
        reg_email_lbl.place(x=30, y=210)
        self.__reg_email_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                       font=('Arial', 10, 'normal'), bd=1)
        self.__reg_email_tb.place(x=145, y=210)

        # creating fifth text box for reg_password
        reg_reg_password_lbl = tk.Label(reg_frame, text="Password:", font=('Arial', 10, 'normal'),
                                        fg='cadetblue1', bg='hotpink3')
        reg_reg_password_lbl.place(x=30, y=250)
        self.__reg_reg_password_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                              font=('Arial', 10, 'normal'), bd=1, show='*')
        self.__reg_reg_password_tb.place(x=145, y=250)

        # creating sixth text box for confirm reg_password
        reg_confirm_reg_password_lbl = tk.Label(reg_frame, text="Confirm Password:",
                                                font=('Arial', 10, 'normal'),
                                                fg='cadetblue1', bg='hotpink3')
        reg_confirm_reg_password_lbl.place(x=30, y=290)
        self.__reg_confirm_reg_password_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                                      font=('Arial', 10, 'normal'), bd=1, show='*')
        self.__reg_confirm_reg_password_tb.place(x=145, y=290)
        self.__reg_confirm_reg_password_tb.bind("<FocusOut>", self.__confirmreg_passwordMatch)

        # creating seventh text box for contact
        reg_contact_lbl = tk.Label(reg_frame, text='Contact No:', font=('Arial', 10, 'normal'),
                                   fg='cadetblue1', bg='hotpink3')
        reg_contact_lbl.place(x=30, y=330)
        self.__reg_contact_tb = tk.Entry(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                         font=('Arial', 10, 'normal'), bd=1)
        self.__reg_contact_tb.place(x=145, y=330)
        self.__reg_contact_tb.bind("<KeyPress>", self.__validateContact)
        # creating eight text box for address
        reg_address_lbl = tk.Label(reg_frame, text='Address:', font=('Arial', 10, 'normal'),
                                   fg='cadetblue1', bg='hotpink3')
        reg_address_lbl.place(x=30, y=370)
        self.__reg_address_tb = tk.Text(reg_frame, width=30, bg='floralwhite', fg='grey1',
                                        font=('Arial', 10, 'normal'), bd=1, height=4)
        self.__reg_address_tb.place(x=145, y=370)

        # creating submit button for registration
        reg_submitBtn = tk.Button(reg_frame, text="Save Info", bd=1, fg='floralwhite',
                                  bg='darkorchid4', width=20, padx=5, pady=5,
                                  activebackground='purple', font=('Helvetica', 10, 'italic'),
                                  cursor='hand2')
        reg_submitBtn.place(x=160, y=465)
        reg_submitBtn.bind("<Button-1>", self.__saveCredentials)

        reg_window.grab_set()  # to set the priority of form

    def __validateContact(self,e):
        try:
            int(self.__reg_contact_tb.get())
            self.__messagelbl.configure(text='')
            if len(self.__reg_contact_tb.get()) >= 11:
                self.__reg_contact_tb.delete(10, 'end')
        except ValueError:
            self.__messagelbl.configure(text='Invalid Contact Number')
            self.__reg_contact_tb.delete(0, 'end')
from FCMS_Files.yearly_report_pdf import *
from FCMS_Files.monthly_report_pdf import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql as pms

class PDF_Report:
    def __init__(self,report_label_panel):
        self.__report_label_panel = report_label_panel

    def show_pdf_panel(self):
        # monthly button
        monthly_report_btn =tk.Button(self.__report_label_panel, text="Monthly Report", width=30,
                                      padx=15, pady=8, bg='hotpink', activebackground='mediumvioletred',
                                      fg='black')
        monthly_report_btn.place(x=10, y=13)
        monthly_report_btn.config(command=self.__showMonthlyReportWindow)

        # yearly button
        yearly_report_btn = tk.Button(self.__report_label_panel, text="Yearly Report", width=30,
                                       padx=15, pady=8, bg='hotpink', activebackground='mediumvioletred',
                                       fg='black')
        yearly_report_btn.place(x=10, y=70)
        yearly_report_btn.config(command=self.__showYearlyReportWindow)

    def __showMonthlyReportWindow(self):
        monthly_window = tk.Toplevel()
        monthly_window.title('Fitness Club Management System')
        monthly_window.geometry('500x250+600+250')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        monthly_window.iconphoto(False, window_icon)
        monthly_window.resizable(False, False)
        monthly_window.grab_set()
        monthly_window.attributes('-topmost', True)
        # creating controls
        # months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
        monthly_label_frame = tk.LabelFrame(monthly_window, text="Monthly Report: ", font=('arial',12,'italic bold'), fg='maroon2')
        monthly_label_frame.place(x=10, y=10, width=480, height=210)
        # creating months label and combobox
        monthly_report_month_lbl = tk.Label(monthly_label_frame, text='Select Month: ')
        monthly_report_month_lbl.place(x=100, y=10)
        monthly_report_month_cb = ttk.Combobox(monthly_label_frame, width=20)
        monthly_report_month_cb.place(x=200, y=10)
        self.__updatemonthlist(monthly_report_month_cb)
        # creating monthly report year label and combobox
        monthly_report_year_lbl = tk.Label(monthly_label_frame, text='Select Year: ')
        monthly_report_year_lbl.place(x=100, y=50)
        monthly_report_year_cb = ttk.Combobox(monthly_label_frame, width=20)
        monthly_report_year_cb.place(x=200, y=50)
        self.__updateyearlist(monthly_report_year_cb)
        # creating report button
        monthly_report_btn = tk.Button(monthly_label_frame, text='Generate Report', width=20, padx=15, pady=8,
                                       bg='hotpink', activebackground='mediumvioletred', fg='black')
        monthly_report_btn.place(x=170, y=100)
        # message label
        message_label = tk.Label(monthly_label_frame)
        message_label.place(x=80, y=150)
        # calling monthly report class
        monthly_report_btn.config(command=lambda: self.__send_values_for_monthly_report(monthly_report_month_cb.get(), monthly_report_year_cb.get(),
                                                                                        message_label))
    def __showYearlyReportWindow(self):
        monthly_window = tk.Toplevel()
        monthly_window.title('Fitness Club Management System')
        monthly_window.geometry('500x250+600+250')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        monthly_window.iconphoto(False, window_icon)
        monthly_window.resizable(False, False)
        monthly_window.grab_set()
        monthly_window.attributes('-topmost', True)
        # creating controls
        monthly_label_frame = tk.LabelFrame(monthly_window, text="Yearly Report: ", font=('arial',12,'italic bold'), fg='maroon2')
        monthly_label_frame.place(x=10, y=10, width=480, height=210)
        # creating monthly report year label and combobox
        yearly_report_year_lbl = tk.Label(monthly_label_frame, text='Select Year: ')
        yearly_report_year_lbl.place(x=100, y=10)
        yearly_report_year_cb = ttk.Combobox(monthly_label_frame, width=20)
        yearly_report_year_cb.place(x=200, y=10)
        self.__updateyearlist(yearly_report_year_cb)
        # creating report button
        yearly_report_btn = tk.Button(monthly_label_frame, text='Generate Report', width=20, padx=15, pady=8,
                                       bg='hotpink', activebackground='mediumvioletred', fg='black')
        yearly_report_btn.place(x=170, y=50)
        # message label
        message_label = tk.Label(monthly_label_frame)
        message_label.place(x=80, y=140)
        # calling monthly report class
        yearly_report_btn.config(command=lambda: self.__send_values_for_yearly_report(yearly_report_year_cb.get(),
                                                                                        message_label))
    def __updateyearlist(self, monthly_report_year_cb):
        year_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        year_cursor = year_connection.cursor()
        year_query = 'SELECT DISTINCT pro_year FROM profit'

        try:
            year_cursor.execute(year_query)
            year_data = year_cursor.fetchall()
            year_list = []
            for row in year_data:
                year_list.append(row)
            monthly_report_year_cb['values'] = year_list
            year_cursor.close()
            year_connection.close()

        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

        monthly_report_year_cb.after(200, lambda: self.__updateyearlist(monthly_report_year_cb))

    def __updatemonthlist(self, monthly_report_month_cb):
        month_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        month_cursor = month_connection.cursor()
        month_query = 'SELECT DISTINCT pro_month FROM profit'

        try:
            month_cursor.execute(month_query)
            month_data = month_cursor.fetchall()
            month_list = []
            for row in month_data:
                month_list.append(row)
            monthly_report_month_cb['values'] = month_list
            month_cursor.close()
            month_connection.close()

        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

        monthly_report_month_cb.after(200, lambda: self.__updatemonthlist(monthly_report_month_cb))
    def __send_values_for_monthly_report(self, month, year, message_label):
        if month and year != '':
            message_label.config(text='')
            mreport = MonthlyPDF(month, year)
            response = mreport.create_monthly_pdf()
            if response == 1:
                message_label.config(text='Monthly report generated successfully.Report saved in Reports folder.', fg='green')
            else:
                message_label.config(text='Monthly report not generated.', fg='red2')
        else:
            message_label.config(text='Fields are empty. Please select values.', fg='red2')
    def __send_values_for_yearly_report(self,year, message_label):
        if year != '':
            message_label.config(text='')
            yreport = YearlyPDF(year)
            response = yreport.create_yearly_pdf()
            if response == 1:
                message_label.config(text='Yearly report generated successfully.Report saved in Reports folder.', fg='green')
            else:
                message_label.config(text='Yearly report not generated.', fg='red2')
        else:
            message_label.config(text='Field is empty. Please select value.', fg='red2')
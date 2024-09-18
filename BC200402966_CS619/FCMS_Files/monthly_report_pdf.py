from fpdf import FPDF, FontFace
from tkinter import messagebox
import pymysql as pms
from datetime import date
import tkinter as tk
class PDF(FPDF):
    def header(self):
        pass
        # self.set_font('Arial', 'B', 15)
        # self.set_text_color(180, 180, 180)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(180, 180, 180)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')
class MonthlyPDF:
    def __init__(self, month, year):
        self.__month_report = month
        self.__year_report = year
        self.__day = date.today().day
        self.__month = date.today().month
        self.__year = date.today().year
    def create_monthly_pdf(self):
        title = "Fitness Club Management System"
        report_title='{m} {y}, Profit Report'.format(m=self.__month_report, y=self.__year_report)
        table_title ='{m} {y} Profit Report Table'.format(m=self.__month_report, y=self.__year_report)
        try:
            pdf = PDF('L', 'mm', 'Letter')
            pdf.alias_nb_pages()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=16)
            # creating main page tile
            pdf.set_font('Arial','', 18)
            pdf.set_text_color(204,0, 204)
            pdf.cell(200, 10, txt=title, ln=1, align='C')
            pdf.image('Images/fcms_icon.png', 10, 7, 20)
            pdf.image('Images/fcms_icon.png', 185, 7, 20)
            #creating report title
            pdf.set_font('Arial','I', 16)
            pdf.set_text_color(128,0, 0)
            pdf.cell(200, 10, txt=report_title, ln=1, align='C')
            # creating Summary
            pdf.set_font('Arial', 'B', 18)
            pdf.set_text_color(152,0, 76)
            pdf.cell(20, 60, txt='Summary:', ln=1, align='C')
            #creating total instructor
            pdf.set_font('arial','',12)
            pdf.set_text_color(25,0,51)
            pdf.cell(40,-40, txt='Total Instructor: ', ln=0, align='C')
            # getting total number from database  for instructor
            total_instructor = self.__get_total_number_of_instructor()
            pdf.set_font('arial','', 12)
            pdf.set_text_color(25,0,51)
            pdf.cell(5, -40, txt=str(total_instructor), ln=1, align='C')
            #creating total members
            pdf.set_font('arial','',12)
            pdf.set_text_color(25,0,51)
            pdf.cell(40,52, txt='Total Members: ', ln=0, align='C')
            # getting total number from database  for members
            total_members = self.__get_total_number_of_members()
            pdf.set_font('arial','', 12)
            pdf.set_text_color(25,0,51)
            pdf.cell(5, 52, txt=str(total_members), ln=1, align='C')
            # creating total income
            pdf.set_font('arial', '', 14)
            pdf.set_text_color(0, 0, 128)
            pdf.cell(200, 20, txt=table_title, ln=0, align='C')
            # creating list for holding table information
            monthly_profit_list=[('Profit ID','Profit Month','Profit Year','Total Expense', 'Total Income','Total Salaries','Total Profit')]
            # fetching monthly profit
            connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
            cursor = connection.cursor()
            query = '''
                            SELECT * FROM profit where pro_month = %s and pro_year = %s
                            '''
            temp_list = []
            try:
                cursor.execute(query, (self.__month_report, self.__year_report))
                for profit in cursor:
                    for item in profit:
                        temp_list.append(str(item))
                monthly_profit_list.append(temp_list)
                connection.close()

            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e))
            blue=(255,255,255)
            grey=(128,0,0)
            headings_style = FontFace(emphasis='ITALICS', color=blue, fill_color=grey)
            pdf.cell(0,20,'',ln=1,align='C')
            pdf.set_font('arial','',10)
            pdf.set_text_color(0, 0, 0)
            with pdf.table(text_align='CENTER', headings_style=headings_style) as table:
                for data_row in monthly_profit_list:
                    table_row = table.row()
                    for data_col in data_row:
                        table_row.cell(str(data_col))
            ################################################################
            pdf.cell(0, 40,'', ln=1, align='C')
            # creating members table information
            members_info_list = [
                ('Name', 'Email', 'Contact', 'Workout Plan', 'Joined Date', 'Plan Fees')
            ]
            # creating members information
            pdf.set_font('arial', '', 14)
            pdf.set_text_color(0, 0, 128)
            pdf.cell(200,-30, txt='Members Information', ln=1, align='C')
            # fetching members information from database
            mem_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
            member_cursor = mem_connection.cursor()
            member_query = 'SELECT mem_fname, mem_email, mem_contact, mem_workoutplan, mem_joiningdate,mem_assignedfees FROM members'

            try:
                member_cursor.execute(member_query)
                for member in member_cursor:
                    members_info_list.append(member)
                mem_connection.close()

            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e))
            # print(members_info_list)

            blue1 = (255, 255, 255)
            grey1 = (128, 0, 0)
            headings_style1 = FontFace(emphasis='ITALICS', color=blue1, fill_color=grey1)
            pdf.cell(0, 20, '', ln=1, align='C')
            pdf.set_font('arial', '', 10)
            pdf.set_text_color(0, 0, 0)
            with pdf.table(text_align='CENTER', headings_style=headings_style1) as table:
                for data_row in members_info_list:
                    table_row = table.row()
                    for data_col in data_row:
                        table_row.cell(str(data_col))
            ################################################################
            pdf.cell(0, 40, '', ln=1, align='C')
            # creating instructor table information
            instructor_info_list = [
                ('Name', 'Email', 'Contact', 'Specialization', 'Joined Date', 'Salary')
            ]
            # creating members information
            pdf.set_font('arial', '', 14)
            pdf.set_text_color(0, 0, 128)
            pdf.cell(200, -30, txt='Instructor Information', ln=1, align='C')
            # fetching members information from database
            inst_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
            inst_cursor = inst_connection.cursor()
            inst_query = 'SELECT inst_fname, inst_email, inst_contact, inst_specialization, inst_joiningdate,inst_salary FROM instructor'

            try:
                inst_cursor.execute(inst_query)
                for member in inst_cursor:
                    instructor_info_list.append(member)
                inst_connection.close()

            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e))
            # print(instructor_info_list)

            blue2 = (255, 255, 255)
            grey2 = (128, 0, 0)
            headings_style2 = FontFace(emphasis='ITALICS', color=blue2, fill_color=grey2)
            pdf.cell(0, 20, '', ln=1, align='C')
            pdf.set_font('arial', '', 10)
            pdf.set_text_color(0, 0, 0)
            with pdf.table(text_align='CENTER', headings_style=headings_style2) as table:
                for data_row in instructor_info_list:
                    table_row = table.row()
                    for data_col in data_row:
                        table_row.cell(str(data_col))




            pdf_name='Reports/{mon}_fcms_{day}_{month}_{year}_report(Monthly).pdf'.format(mon=self.__month_report,day=self.__day, month=self.__month, year=self.__year)
            pdf.output(pdf_name)
            return True
        except Exception as e:
            return False



    def __get_total_number_of_instructor(self):
        inst_list=[]
        inst_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        inst_cursor = inst_connection.cursor()
        inst_query = 'SELECT inst_id FROM instructor'
        try:
            inst_cursor.execute(inst_query)
            for inst in inst_cursor:
                inst_list.append(inst)
            total_number = len(inst_list)
            inst_connection.close()
            return total_number
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))
    def __get_total_number_of_members(self):
        mem_list=[]
        mem_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        mem_cursor = mem_connection.cursor()
        mem_query = 'SELECT mem_id FROM members'
        try:
            mem_cursor.execute(mem_query)
            for inst in mem_cursor:
                mem_list.append(inst)
            total_number = len(mem_list)
            mem_connection.close()
            return total_number
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Error: '+ str(e))

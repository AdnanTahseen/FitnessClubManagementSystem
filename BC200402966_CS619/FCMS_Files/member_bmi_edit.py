import tkinter as tk
from tkinter import ttk
import pymysql as pms
from tkinter import messagebox

class EditBMI:
    def __init__(self):
        pass

    def __update_member_id_from_bmi_table(self,select_member_ID_cb):
        selection_id_list = []
        # creating connection to database
        select_id_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        select_id_cursor = select_id_connection.cursor()
        bmi_query ='SELECT mem_id FROM member_bmi'
        try:
            select_id_cursor.execute(bmi_query)
            bmi_result = select_id_cursor.fetchall()
            for id in bmi_result:
                selection_id_list.append(id)

            select_member_ID_cb.config(values=selection_id_list)
            select_id_cursor.close()
            select_id_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', e)

        select_member_ID_cb.after(200, lambda : self.__update_member_id_from_bmi_table(select_member_ID_cb))

    def __get_measurement_values_for_BMI(self, event):
        currentValue=self.__select_member_ID_cb.get()
        self.__bmi_edit_tb.delete(0, 'end')
        mem_bmi_query = 'SELECT * FROM member_bmi WHERE mem_id = {cval}'.format(cval=currentValue)
        mem_bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        mem_bmi_cursor = mem_bmi_connection.cursor()
        try:
            mem_bmi_cursor.execute(mem_bmi_query)
            mem_bmi_result = mem_bmi_cursor.fetchall()
            for row in mem_bmi_result:
                self.__bmi_edit_tb.insert(0, row[2])
            mem_bmi_cursor.close()
            mem_bmi_connection.close()
        except Exception as e:
            messagebox.showerror('Fitness Club Management System', str(e))

    def show_edit_bmi_window(self):
        edit_bmi_window = tk.Toplevel()
        edit_bmi_window.title("Edit BMI")
        edit_bmi_window.geometry('450x250+250+250')
        edit_bmi_window.resizable(False, False)
        edit_bmi_window.configure(background='lightgrey')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        edit_bmi_window.iconphoto(False, window_icon)
        edit_bmi_window.grab_set()

        select_member_ID_lbl = ttk.Label(edit_bmi_window, text='Select Member ID', background='lightgrey',
                                         font='arial 9 italic')
        select_member_ID_lbl.place(x=20, y=10)
        self.__select_member_ID_cb = ttk.Combobox(edit_bmi_window, width=17)
        self.__select_member_ID_cb.place(x=160, y=10)
        self.__update_member_id_from_bmi_table(self.__select_member_ID_cb)
        self.__select_member_ID_cb.current(0) # setting the index of combo box to 0 from -1
        # if self.__select_member_ID_cb.current() != -1:
        self.__select_member_ID_cb.bind('<<ComboboxSelected>>', self.__get_measurement_values_for_BMI)
        # else:
        #     messagebox.showerror('Fitness Club Management System', 'Please select Id!')

        # Button for BMI calculation
        member_bmi_lbl = ttk.Label(master=edit_bmi_window, text='Member BMI:', background='lightgrey',
                                   font='arial 9 italic')
        member_bmi_lbl.place(x=20, y=50)
        self.__bmi_edit_tb = ttk.Entry(edit_bmi_window, width=25)
        self.__bmi_edit_tb.place(x=160, y=50)
        # creating button for editing
        bmi_editBtn = tk.Button(master=edit_bmi_window, text='Edit', background='purple',
                                foreground='snow', width=10, font='arial 9 italic bold', pady=4)
        bmi_editBtn.place(x=120, y=90)
        bmi_editBtn.config(command= lambda :self.__send_values_for_editing(edit_bmi_window))

    def __send_values_for_editing(self, edit_bmi_window):
        #creating connection
        connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        cursor = connection.cursor()
        # getting values from text boxes
        member_id = self.__select_member_ID_cb.get()
        member_bmi = self.__bmi_edit_tb.get()
        if member_bmi != '':
            try:
                cursor.execute('UPDATE member_bmi SET mem_bmi = {mbmi} WHERE mem_id = {mid}'.format(mbmi=member_bmi, mid=member_id))
                connection.commit()
                messagebox.showinfo('Fitness Club Management System', 'Member BMI updated successfully!', parent=edit_bmi_window)
            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e), parent=edit_bmi_window)
        else:
            messagebox.showerror('Fitness Club Management System', 'Please change index to get BMI value.',parent=edit_bmi_window)
        cursor.close()
        connection.close()
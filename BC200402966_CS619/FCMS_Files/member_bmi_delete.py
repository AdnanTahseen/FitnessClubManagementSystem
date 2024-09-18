import tkinter as tk
from tkinter import ttk
import pymysql as pms
from tkinter import messagebox

class DeleteBMI:
    def __init__(self):
        pass

    def __update_member_id_from_bmi_table(self, select_member_ID_cb):
        bmi_id_list = []
        bmi_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        bmi_cursor = bmi_connection.cursor()
        bmi_query = "SELECT bmi_id FROM member_bmi"
        try:
            bmi_cursor.execute(bmi_query)
            bmi_result = bmi_cursor.fetchall()
            for bmi_id in bmi_result:
                bmi_id_list.append(bmi_id)

            select_member_ID_cb.config(values=bmi_id_list)
            bmi_cursor.close()
            bmi_connection.close()
        except Exception as e:
            messagebox.showerror("Fitness Club Management System", str(e))

        select_member_ID_cb.after(200, lambda: self.__update_member_id_from_bmi_table(select_member_ID_cb))


    def show_del_window(self):
        del_root = tk.Toplevel()
        del_root.title('Delete Member')
        del_root.geometry('400x200+500+200')
        del_root.resizable(False, False)
        del_root.config(bg='lightgrey')
        window_icon = tk.PhotoImage(file='Images/fcms_icon.png')
        del_root.iconphoto(False, window_icon)
        del_root.grab_set()
        # creating controls
        select_member_ID_lbl = ttk.Label(del_root, text='Select Member ID', background='lightgrey',
                                         font='arial 9 italic')
        select_member_ID_lbl.place(x=20, y=10)
        self.__select_member_ID_cb = ttk.Combobox(del_root, width=17)
        self.__select_member_ID_cb.place(x=160, y=10)
        self.__update_member_id_from_bmi_table(self.__select_member_ID_cb)
        self.__select_member_ID_cb.current(0)
        # Button for del BMI
        bmi_delBtn = tk.Button(master=del_root, text='Delete BMI', background='red2',
                               foreground='snow', width=10, font='arial 9 italic bold', pady=4)
        bmi_delBtn.place(x=210, y=50)
        bmi_delBtn.config(command= lambda : self.__delete_bmi(self.__select_member_ID_cb.get(), del_root))

    def __delete_bmi(self, mem_id, del_root):
        del_connection = pms.connect(host='localhost', port=3306, user='root', password='', database='fcms')
        del_cursor = del_connection.cursor()
        del_query = 'DELETE FROM member_bmi WHERE mem_id = {del_var}'.format(del_var=mem_id)
        answer = messagebox.askyesno('Fitness Club Management System', 'Do you really want to delete member?', parent=del_root)
        if answer:
            try:
                del_cursor.execute(del_query)
                del_connection.commit()
                del_connection.close()
                messagebox.showinfo("Success", "Member Deleted Successfully", parent=del_root)
                return True
            except Exception as e:
                messagebox.showerror('Fitness Club Management System', str(e), parent=del_root)
        else:
            pass
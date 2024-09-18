import subprocess
from tkinter import messagebox
from datetime import date

class BackupDB:
    def __init__(self):
        self.__host = 'localhost',
        self.__user= 'root',
        self.__password = '',
        self.__database = 'fcms',
        self.__day = date.today().day
        self.__month = date.today().month
        self.__year = date.today().year
        self.__backup_file = 'Database_backup/fcms_backup_{d}_{m}_{y}.sql'.format(d=self.__day,m=self.__month,y=self.__year)

    def create_backup_db(self):
        try:
            command = f"mysqldump -h{self.__host} -u{self.__user} -p{self.__password} {self.__database} > {self.__backup_file}"
            subprocess.run(command, shell=True)
            messagebox.showinfo('Fitness Club Management System', 'Database Backup Successful. \nBackup file saved in Database_backup folder')

        except Exception as e:
            messagebox.showerror('Fitness Club Management System', 'Database Backup Failed {e}')
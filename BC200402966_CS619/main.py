from tkinter import messagebox
from Login import *

fcms_root= tk.Tk()
fcms_root.geometry('1366x968')
fcms_root.title('Fitness Club Management System')
fcms_root.state('zoomed')
fcms_root.resizable(False, False)
windowIcon=tk.PhotoImage(file='Images/fcms_icon.png')
fcms_root.iconphoto(False, windowIcon)

def showLoginWindow():
    # Calling Login Class
    loginWindow=Login(fcms_root)
    loginWindow.showLoginPage(fcms_root)

if __name__ == "__main__":
    showLoginWindow()
def confirmationWindowClosing():
    answer=tk.messagebox.askyesno("Fitness Club Management System", "Do you really want to close the application?")
    if answer:
        fcms_root.destroy()

fcms_root.protocol('WM_DELETE_WINDOW',confirmationWindowClosing)
fcms_root.mainloop()
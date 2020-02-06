#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : password.py
# Description : perform password management
#------------------------------------------------



#Import Libraries

from tkinter import *
from tkinter import  messagebox
import sqlite3


# Main class
class pass_login():
    def __init__(self,master):

        # Code to retrieve current user
        try:
            with open('login_details.txt', 'r') as f:
                lines = f.read().splitlines()
                   # last_line = lines[-1]
                self.username = lines[-2]
        except:
            messagebox.showerror("Failed","Unable to unlock root directory")

        frame = Frame(master)

        # Variables
        self.passw1 = StringVar()
        self.passw2 = StringVar()
        self.passw3 = StringVar()
        pass_font = ('Courier', 20)

        # password box code
        pass_label = Label(master, text="Please enter old password", font=("Courier", 20))
        pass_label.grid(row=2, column=0)
        pass_entry = Entry(master, textvariable=self.passw1, show="*", bd=10, font=pass_font)
        pass_entry.grid(row=2, column=1)
        pass_label = Label(master, text="Please enter new password", font=("Courier", 20))
        pass_label.grid(row=3, column=0)
        pass_entry = Entry(master, textvariable=self.passw2, show="*", bd=10, font=pass_font)
        pass_entry.grid(row=3, column=1)
        pass_label = Label(master, text="Please re-enter new password", font=("Courier", 20))
        pass_label.grid(row=4, column=0)
        pass_entry = Entry(master, textvariable=self.passw3, bd=10, show="*", font=pass_font)
        pass_entry.grid(row=4, column=1)

        # Submit button
        message_submit = Button(master, text='Submit', command=self.change_pass)
        message_submit.grid(row=4, column=5)
        close_button = Button(master, text='Close', command=master.quit)
        close_button.grid(row=7, column=1)


    # Function to change password
    def change_pass(self):
        # get values
        self.pass1 = self.passw1.get()
        self.pass2 = self.passw2.get()
        self.pass3 = self.passw3.get()

        # Connect to register file
        try:
            conn = sqlite3.connect('EMS.db')
            pass_db = conn.cursor()
            pass_db.execute('SELECT * FROM register WHERE username = "%s"' %(self.username))
            pass_data = pass_db.fetchall()
            for row in pass_data:
                self.pass0 = row[1]
            print(pass_data)
            print(self.pass0)
            print(self.pass1)
            print(self.pass2)
            print(self.pass3)

            # update register with latest password
            if self.pass0 == self.pass1:
                if self.pass3 == self.pass2 and self.pass2.lower().isalpha() == False and self.pass2.islower() == False and self.pass2.isupper() == False and len(self.pass2) >6:

                    # Update register
                    pass_db.execute('UPDATE register SET password = "%s" WHERE username = "%s"' % (self.pass2 , self.username))

                    # Update login_details
                    pass_db.execute('UPDATE login_details SET password = "%s" WHERE username = "%s"' % (self.pass2 , self.username))
                    print("Password changed successfully")
                    messagebox.showinfo("Success", "Password changed successfully")

                    # Save changes
                    conn.commit()

                    # Close connection
                    conn.close()

                else:
                    print("New password doesn't match with re-entered new password")
                    messagebox.showerror("Failed", "New password doesn't match with re-entered new password")
            else:
                print("Entered doesn't match old password")
                messagebox.showerror("Failed", "Entered doesn't match old password")
        except:
            print("Can't open file")
            messagebox.showerror("Failed", "File can't be open")


# Main Tkinter GUI
root = Tk()
login_home_success = pass_login(root)
root.wm_geometry("800x600")
root.title("Password Management")
root.mainloop()
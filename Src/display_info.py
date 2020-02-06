#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : display_info.py
# Description : Displays employee information
#------------------------------------------------


#Import Libraries
from tkinter import *
from tkinter import  messagebox
import sqlite3


# Main class
class display_info():
    def __init__(self,master):

        # Code to retrieve current user
        try:
            with open('login_details.txt', 'r') as f:
                lines = f.read().splitlines()
                self.username = lines[-2]
        except:
            messagebox.showerror("Failed","Unable to unlock root directory")

        # Variable
        self.nrow = 2


        # Fetch data of user
        try:
            conn = sqlite3.connect('EMS.db')
            info = conn.cursor()
            info.execute('SELECT * FROM register WHERE username = "%s"' %(self.username))
            info_db =info.fetchall()
            print("Data is fetched")

            # Display details of employee
            for row in info_db:

                info_label = Label(text="Name : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow, column=0,sticky=W)
                info_label = Label(text=row[5], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow, column=1,sticky=W)

                info_label = Label(text="Email id : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+1, column=0,sticky=W)
                info_label = Label(text=row[4], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 1, column=1,sticky=W)

                info_label = Label(text="Phone No : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+2, column=0,sticky=W)
                info_label = Label(text=row[7], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 2, column=1,sticky=W)

                info_label = Label(text="SIN : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+3, column=0,sticky=W)
                info_label = Label(text=row[3], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 3, column=1,sticky=W)

                info_label = Label(text="Address : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+4, column=0,sticky=W)
                info_label = Label(text=row[8], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 4, column=1,sticky=W)

                info_label = Label(text="Designation: ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+5, column=0,sticky=W)
                info_label = Label(text=row[6], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 5, column=1,sticky=W)

                info_label = Label(text="Basic Pay : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+6, column=0,sticky=W)
                info_label = Label(text=row[2], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 6, column=1,sticky=W)

                info_label = Label(text="Total leaves taken : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+7, column=0,sticky=W)
                info_label = Label(text=row[10], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 7, column=1,sticky=W)

                info_label = Label(text="Total leaves left : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+8, column=0,sticky=W)
                info_label = Label(text=row[9], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 8, column=1,sticky=W)

                info_label = Label(text="Total leaves pending for approval : ", font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow+9, column=0,sticky=W)
                info_label = Label(text=row[11], font=("Courier", 20),justify=LEFT, anchor="w")
                info_label.grid(row=self.nrow + 9, column=1,sticky=W)

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

        except:
            print("Error in executing display_info")
            messagebox.showerror("Failed", "Error occured while displaying info")

        # Close button
        close_button = Button(master, text='Close', command=master.quit)
        close_button.grid(row=self.nrow + 11, column=0)


# Main Tkinter GUI
root = Tk()
login_home_success = display_info(root)
root.wm_geometry("1000x600")
root.title("Display Information")
root.mainloop()
#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : admin_login_success.py
# Description : Provides admin to perform employee management functions
#------------------------------------------------

# Import Libraries
from tkinter import *
from tkinter import  messagebox
import os
from subprocess import  call
import sqlite3
import datetime


# Main calling class - Home
class Home():
    def __init__(self,master):

        # Variable
        self.date = datetime.date.today()
        self.large_font = ('Courier', 40)
        self.medium_font = ('Courier', 30)
        self.small_font = ('Courier', 20)
        self.message_variable = StringVar()
        self.display_variable = StringVar()

        # Welcome note to admin
        login_label = Label(text="Welcome Professor", font=self.large_font, justify=LEFT, anchor="w")
        login_label.grid(row=0, column=0, sticky=W)
        login_label = Label(text="Mohamed Abdelazez", font=self.large_font, justify=LEFT, anchor="w")
        login_label.grid(row=0, column=1, sticky=W)

        # Clear space for clarity
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=1, column=0, sticky=W)
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=2, column=0, sticky=W)
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=3, column=0, sticky=W)
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=4, column=0, sticky=W)

        # Attendance button
        update_attendance=Button(master,text='Upload Attendance',command=self.update_attendance)
        update_attendance.grid(row=4,column=0)

        # Check leave
        leave_button = Button(master, text='Check Leave Requests', command=self.check_leave)
        leave_button.grid(row=3, column=6)

        # Delete employee button
        delete_submit = Button(master, text='Delete Employee', command=self.delete)
        delete_submit.grid(row=2, column=6)

        # Display employee button
        display_submit = Button(master, text='Display Info', command=self.display)
        display_submit.grid(row=2, column=2)
        display_entry = Entry(master, textvariable=self.display_variable, bd=10, font=self.small_font)
        display_entry.grid(row=2, column=1)

        #Logout Button
        logout_button = Button(master, text='Logout',justify=RIGHT,anchor="w", command=master.quit)
        logout_button.grid(row=0, column=7,sticky=W)


        # Message box code
        message_label=Label(master,text="   Message to Employees",font=("Courier", 30))
        message_label.grid(row=5,column=1)
        message_entry = Entry(master, textvariable=self.message_variable, bd=10, font=self.large_font)
        message_entry.grid(row=5,column=1)
        message_submit=Button(master,text='Send to all the Employees',command=self.send_message)
        message_submit.grid(row=6,column=1)


    # Check leave requests
    def check_leave(self):
        call('python3 leaves.py', shell=True)


    # Function to update attendance
    def update_attendance(self):

        # Attendance
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=6, column=0, sticky=W)
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=7, column=0, sticky=W)
        Label(text="", font=self.small_font, justify=LEFT, anchor="w").grid(row=8, column=0, sticky=W)

        attendance = Label(text='Attendance', font=self.medium_font)
        attendance.grid(row=9, column=0)

        # Variable
        i=0

        # Connect to database
        conn = sqlite3.connect('EMS.db')
        attendance = conn.cursor()
        attendance.execute('SELECT * from register')
        store = attendance.fetchall()
        for row in store:
            conn = sqlite3.connect('EMS.db')
            attend = conn.cursor()
            attend.execute('SELECT * FROM attendance WHERE username = "%s" and date = "%s"' %(row[5],self.date))
            if attend.fetchone():
                status = 'Present'
            else:
                status = 'Absent'

            Label(text=row[5], font=self.small_font, justify=LEFT, anchor="w").grid(row=10+i, column=0,sticky=W)
            Label(text=status, font=self.small_font, justify=LEFT, anchor="w").grid(row=10 + i, column=1, sticky=W)
            i +=1

        # save changes
        conn.commit()

        # close the connection
        conn.close()


    # Function to send messages to all employee
    def send_message(self):
        messagebox.showinfo("Message Sent","Your Message has been Sent")
        message_value=self.message_variable.get()
        date=self.date
        try:
            conn = sqlite3.connect('EMS.db')
            message_insert=conn.cursor()
            message_insert.execute("INSERT into message_alerts(message,date) values(?,?) ",(message_value,date))
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Alert","Error occured in sending message")
        os.system('clear')


    # Function to delete record of a employee
    def delete(self):
        # call delete.py to perform delete function
        call('python3 delete.py', shell=True)


    # Function to displau employee information
    def display(self):
        username = self.display_variable.get()
        password = ' '
        file = open("login_details.txt", "w+")
        file.writelines(username + '\n')
        file.writelines(password)
        file.close()
        call('python3 display_info.py', shell=True)


# Main Tkinter GUI
root=Tk()
admin_login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Admin Login")
root.mainloop()
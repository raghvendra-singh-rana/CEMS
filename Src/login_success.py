#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : login_success.py
# Description : perform employee related functions
#------------------------------------------------


#Import Libraries

from tkinter import *
from tkinter import messagebox
from subprocess import *
import sqlite3
import datetime


# Main class
class home_login():
    def __init__(self,master):

        # Retrieve current user
        try:
            with open('login_details.txt', 'r') as f:
                lines = f.read().splitlines()
                   # last_line = lines[-1]
                self.username = lines[-2]
        except:
            messagebox.showerror("Failed","Unable to unlock root directory")

        # Logout Button
        logout_button=Button(master,text='Logout',command=master.quit)
        logout_button.grid(row=0,column=7)

        # Welcome text for user
        username_label=Label(master,text="Welcome "+self.username + " !!!",font=("Courier", 40))
        username_label.grid(row=0,column=0)

        # Button to display user information
        info_button = Button(master, text='Display Information', command=self.display_info)
        info_button.grid(row=0, column=6)

        # Mark Attendance
        info_button = Button(master, text='Mark Attendance', command=self.mark_attend)
        info_button.grid(row=2, column=5)

        # Change Password
        info_button = Button(master, text='Change Password', command=self.change_password)
        info_button.grid(row=2, column=6)

        # Admin messages
        messages_label=Label(master,text="Admin Messages",font=("Courier", 30))
        messages_label.grid(row=40,column=1)

        # connect to message file
        try:
            conn = sqlite3.connect('EMS.db')
            message_db = conn.cursor()
            message_db.execute('SELECT * from message_alerts')
            message_db_store = message_db.fetchall()
            print("Connection to message_alert successful")
        except:
            print("Connection to message_alert failed")
            messagebox.showerror("Failed","Failed to Load  Messages")


        # Apply leaves
        date_label_messages=Label(master,text="Date",font=("Courier", 25))
        date_label_messages.grid(row=41,column=0)
        message_content=Label(master,text='Message',font=("Courier", 25))
        message_content.grid(row=41,column=1)

        # Fetch admin messages
        for self.i in range(0,len(message_db_store)):
            details_messages=Label(master,text=message_db_store[self.i][0],font=("Courier", 25))
            details_messages.grid(row=42+self.i,column=1)
            date_message=Label(master,text=message_db_store[self.i][1],font=("Courier", 25))
            date_message.grid(row=42+self.i,column=0)

        # Leave details
        leave_request_label=Label(master,text='Leave Request',font=("Courier", 25))
        leave_request_label.grid(row=32,column=1)
        from_date_label=Label(master,text='From Date',font=("Courier", 25))
        from_date_label.grid(row=33,column=0)
        to_date_label=Label(master,text='To Date',font=("Courier", 25))
        to_date_label.grid(row=33,column=1)
        reason_label=Label(master,text='Reason',font=("Courier", 25))
        reason_label.grid(row=33,column=2)

        # variables
        self.from_date=StringVar()
        self.to_date=StringVar()
        self.reasons=StringVar()

        # pull leave frame values
        from_date_entry=Entry(master,bd=5,textvariable=self.from_date)
        from_date_entry.grid(row=34,column=0)
        to_date_entry=Entry(master,bd=5,textvariable=self.to_date)
        to_date_entry.grid(row=34,column=1)
        reason_entry=Entry(master,bd=5,textvariable=self.reasons)
        reason_entry.grid(row=34,column=2)

        # leave submit button
        submit_button=Button(master,text='Submit',command=self.submit_leave)
        submit_button.grid(row=34,column=3)


    # Change password
    def change_password(self):
        call('python3 password.py', shell=True)


    # Submit leave
    def submit_leave(self):
       try:
            # get screen values
            from_date=self.from_date.get()
            to_date=self.to_date.get()
            reason=self.reasons.get()

            # Variable
            leave_status = 'Pending Approval'
            print(from_date,to_date,reason)

            # Connect to database
            conn = sqlite3.connect('EMS.db')
            leave_db = conn.cursor()

            # Check for pending approval leave
            leave_db.execute('SELECT * FROM leave_requests WHERE username = "%s" AND status = "%s"' %(self.username,leave_status))
            if leave_db.fetchone():
                messagebox.showerror("Failed", "One leave request still in pending approval")
            else:
                leave_db.execute("INSERT into leave_requests(username,from_date,to_date,reason,status) values(?,?,?,?,?) ",(self.username,from_date,to_date,reason,leave_status))
                messagebox.showinfo("Success","Leave request sent to admin")

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

       except:
            print("Error in executing submit_leave")
            messagebox.showerror("Failed","Internal Server error occured")


    #Function to display employee information
    def display_info(self):
        call('python3 display_info.py', shell=True)


    # Function to mark attendance for an employee
    def mark_attend(self):

        # Variable
        self.date = datetime.date.today()
        self.attend_status = 'Present'
        print(self.username,self.attend_status,self.date)

        # Connect to attendance file
        try:
            conn = sqlite3.connect('EMS.db')
            attend = conn.cursor()
            attend.execute('SELECT * FROM attendance WHERE username = "%s" AND date = "%s"' %(self.username,self.date))
            if attend.fetchone():
                print("Already marked present")
                messagebox.showinfo("Info", "Your attendance has already been marked")

            # Update attendance file - mark employee's presence
            else:
                attend.execute('INSERT INTO attendance (username,status,date) values(?,?,?) ',(self.username,self.attend_status,self.date))
                messagebox.showinfo("Info", "Your attendance has been marked")

             # Save changes
            conn.commit()

            # Close connection
            conn.close()

        except:
            print("Error occured in writing to attendance file")
            messagebox.showerror("Failed", "Error occured in writting attendance file")


    # Function to logout of the menu
    def logout(self):
        import login
        print('logout called')


# Main Tkinter GUI
root=Tk()
login_home_success=home_login(root)
root.wm_geometry("1360x1200")
root.title("Login")
root.mainloop()

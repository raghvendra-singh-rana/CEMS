#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : leave.py
# Description : perform leave approval and rejection function to admin
#------------------------------------------------


#Import Libraries

from tkinter import *
from tkinter import  messagebox
import sqlite3
import datetime


# Main class
class leaves():
    def __init__(self,master):

        # Master frame
        frame = Frame(master)

        # Variables
        self.user1 = StringVar()
        self.date = datetime.date.today()
        self.large_font = ('Courier', 40)
        self.medium_font = ('Courier', 30)
        self.small_font = ('Courier', 20)
        self.nrow = 3
        self.leave_status = 'Pending Approval'

        # Close button
        close_button = Button(master, text='Close', command=master.quit)
        close_button.grid(row=0, column=4)

        # Details of user applied leaves
        Label(text="Name ", font=self.medium_font, justify=LEFT, anchor="w").grid(row=0, column=0, sticky=W)
        Label(text="From ", font=self.medium_font, justify=LEFT, anchor="w").grid(row=0, column=1, sticky=W)
        Label(text="To ", font=self.medium_font, justify=LEFT, anchor="w").grid(row=0, column=2, sticky=W)
        Label(text="Reason ", font=self.medium_font, justify=LEFT, anchor="w").grid(row=0, column=3, sticky=W)

        # Connect to database
        conn = sqlite3.connect('EMS.db')

        leave = conn.cursor()
        leave.execute('SELECT * FROM leave_requests where from_date>="%s" AND status ="%s"' % (self.date,
                                                                                               self.leave_status))
        leave_db = leave.fetchall()

        i = 0

        # fetch records of all users who applied leaves
        for row in leave_db:
            Label(text=row[0], font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + i, column=0, sticky=W)
            Label(text=row[1], font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + i, column=1,
                                                                                    sticky=W)
            Label(text=row[2], font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + i, column=2,
                                                                                    sticky=W)
            Label(text=row[3], font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + i, column=3,
                                                                                    sticky=W)
            i +=1


        # For pending leaves
        if i>0:
            self.nrow += i
            Label(text=" ", font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + 1, column=0,
                                                                                    sticky=W)
            Label(text=" ", font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + 2, column=0,
                                                                                 sticky=W)

            Label(text="Enter user name to approve/reject", font=self.small_font, justify=LEFT, anchor="w").grid(row=self.nrow + 3, column=0,
                                                                                 sticky=W)


            Entry(master, textvariable=self.user1, bd=10, font=self.medium_font).grid(row=self.nrow + 4, column=0)

            # Approval button
            Button(master, text='Approve', command=self.approve_leaves).grid(row=self.nrow + 4, column=1)

            # Rejection button
            Button(master, text='Reject', command=self.reject_leaves).grid(row=self.nrow + 4, column=2)

        # Save changes
        conn.commit()

        # close the connection
        conn.close()


    # Function to approve leaves of employees
    def approve_leaves(self):

        # Variables
        left_leave = 0
        left_leaves = ' '
        leave_status = 'Approved'
        leave_value = self.user1.get()

        try:
            # connect to database
            conn = sqlite3.connect('EMS.db')
            leave_d1 = conn.cursor()

            # check leave requests
            leave_d1.execute('SELECT * FROM leave_requests WHERE username = "%s" and status = "%s"' %(leave_value,self.leave_status ))
            leave_data = leave_d1.fetchall()

            for row in leave_data:
                s_value = row[1]
                s_value = s_value[8:10]
                e_value = row[2]
                e_value = e_value[8:10]
                left_leave = int(e_value) - int(s_value) + 1
                left_leaves= str(left_leave)
                approve_leaves = left_leaves

            # Save changes
            conn.commit()

            # Close connections
            conn.close()

            # Connect to register
            conn = sqlite3.connect('EMS.db')
            register1 = conn.cursor()

            register1.execute(
                'SELECT * FROM register WHERE username = "%s"' % (leave_value))
            register_data = register1.fetchall()

            # Fetch data from register table
            for row in register_data:
                left_leave = int(row[9]) - left_leave
                left_leaves = str(left_leave)

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

            # Update register with updated leaves
            conn = sqlite3.connect('EMS.db')
            print(approve_leaves)
            print(left_leaves)
            register = conn.cursor()

            # update register
            register.execute(
                'UPDATE register SET lleave = "%s" WHERE username = "%s"' % (left_leaves, leave_value))
            register.execute('UPDATE register SET aleave = "%s" WHERE username = "%s"' % (approve_leaves, leave_value))

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

            # connect to leave file
            conn = sqlite3.connect('EMS.db')
            leave = conn.cursor()

            # Update leave request file
            leave.execute(
                'UPDATE leave_requests SET status = "%s" where username = "%s"' % (leave_status, leave_value))

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

            # Approval message
            messagebox.showinfo("Info", "Leave requests has been approved")

        except:
            print("Leave requests can't be displayed for approval")
            messagebox.showinfo("Error", "Leave requests can't be displayed for approval")

    # Function to reject leaves of employee
    def reject_leaves(self):

        # Variable
        leave_status = 'Rejected'

        try:
            # Connect to leave request file
            conn = sqlite3.connect('EMS.db')
            leave = conn.cursor()
            leave_value = self.user1.get()

            # Update leave request file
            leave.execute(
                'UPDATE leave_requests SET status = "%s" where username = "%s"' % (leave_status, leave_value))

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

            # Connection to employee register
            conn = sqlite3.connect('EMS.db')
            register = conn.cursor()
            a_leaves = '0'

            # Update employee register
            register.execute('UPDATE register SET aleave = "%s" where username = "%s"' % (a_leaves, leave_value))

            # Save changes
            conn.commit()

            # Close connections
            conn.close()

            # Rejection mesaage
            messagebox.showinfo("Info", "Leave requests has been denied")

        except:
            print("Leave requests can't be displayed for rejection")
            messagebox.showinfo("Error", "Leave requests can't be displayed for rejection")


# Main Tkinter GUI
root = Tk()
login_home_success = leaves(root)
root.wm_geometry("1000x600")
root.title("Leave Management")
root.mainloop()
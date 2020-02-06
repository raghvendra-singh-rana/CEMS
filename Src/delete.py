#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : delete.py
# Description : Class to perform deletion of an employee
#------------------------------------------------


#Import Libraries
from tkinter import *
from tkinter import  messagebox
import sqlite3


# Main class
class delete():
    def __init__(self,master):

        # Master frame
        frame = Frame(master)

        # Variables
        self.user1 = StringVar()
        self.username = ' '
        self.del_font = ('Courier', 20)

        # password box code
        pass_label = Label(master, text="Please enter employee user name to be deleted", font=self.del_font)
        pass_label.grid(row=2, column=0)
        pass_entry = Entry(master, textvariable=self.user1,  bd=10, font=self.del_font)
        pass_entry.grid(row=3, column=0)

        # Submit button
        message_submit = Button(master, text='Submit', command=self.delete_employee)
        message_submit.grid(row=3, column=1)

        # Close button
        close_button = Button(master, text='Close', command=master.quit)
        close_button.grid(row=0, column=3)


    # Function to delete selected employee
    def delete_employee(self):

        # get values
        self.username = self.user1.get()
        print(self.username)

        try:
            conn = sqlite3.connect('EMS.db')
            del_db = conn.cursor()

            # Check record for deletion
            del_db.execute('SELECT * FROM register WHERE username = "%s"' %(self.username))

            if del_db.fetchone():
                conn = sqlite3.connect('EMS.db')
                delete_db = conn.cursor()

                # Create a temporary table
                delete_db.execute('''CREATE TABLE IF NOT EXISTS register_temp 
                 (username varchar PRIMARY KEY , password varchar,salary varchar, SIN varchar,email varchar,name varchar,post varchar,phone varchar,address varchar,lleave varchar,tleave varchar,aleave varchar)''')

                # Insert data to temporary table
                delete_db.execute('SELECT * FROM register WHERE username != "%s"' %(self.username))
                del_data = delete_db.fetchall()
                for row in del_data:
                    delete_db.execute("INSERT INTO register_temp (username,password,salary,SIN,email,name,post,phone,address,lleave,tleave,aleave) values (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (row[0], row[1], row[2], row[3], row[4],
                         row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

                # Delete orignal table
                delete_db.execute('DROP TABLE register')

                # Rename temporary table
                delete_db.execute('ALTER TABLE register_temp RENAME TO register')

            else:
                print("User doesn't exists in register")
                messagebox.showerror("Failed", "User doesn't exists in register")

            # Save changes
            conn.commit()

            # Close connection
            conn.close()
        except:
            print("Can't open file")
            messagebox.showerror("Failed", "File can't be open - register")

        # Delete from login_details
        try:
            conn = sqlite3.connect('EMS.db')
            log_db = conn.cursor()

            # Check record for deletion
            log_db.execute('SELECT * FROM login_details WHERE username = "%s"' % (self.username))

            if log_db.fetchone():
                conn = sqlite3.connect('EMS.db')
                login_db = conn.cursor()

                # Create a temporary table
                login_db.execute('''CREATE TABLE IF NOT EXISTS login_details_temp (username varchar PRIMARY KEY , password varchar)''')

                # Insert data to temporary table
                login_db.execute('SELECT * FROM login_details WHERE username != "%s"' % (self.username))
                log_data = login_db.fetchall()
                for row in log_data:
                    login_db.execute("INSERT INTO login_details_temp (username,password)  values (?,?)", (row[0], row[1]))

                # Delete orignal table
                login_db.execute('DROP TABLE login_details')

                # Rename temporary table
                login_db.execute('ALTER TABLE login_details_temp RENAME TO login_details')
                messagebox.showerror("Failed", "User deleted")

            else:
                print("User doesn't exists in login details")
                messagebox.showerror("Failed", "User doesn't exists in login_details")

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

        except:
            print("Can't open file")
            messagebox.showerror("Failed", "File can't be open - login_details")


# Main Tkinter GUI
root = Tk()
login_home_success = delete(root)
root.wm_geometry("800x400")
root.title("Delete Employee")
root.mainloop()
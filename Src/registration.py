#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : registration.py
# Description : perform registration
#------------------------------------------------


# Import libraries

from tkinter import *
from tkinter import messagebox
import os
import signal
from subprocess import *
import sqlite3
import re
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# Get user login details
def login_details(username, password):
    file = open("login_details.txt", "w+")
    file.writelines(username + '\n')
    file.writelines(password)
    file.close()


# main class begins
class Home():
    def __init__(self, master):

        # Master menu
        menu = Menu(master)
        master.config(menu=menu)

        # Home menu
        home = Menu(menu)
        menu.add_cascade(label='Home', menu=home)
        home.add_command(label='Take a Tour!!', command=self.take_a_tour)
        home.add_command(label='Terms of Use', command=self.terms_of_use)
        home.add_separator()

        # Login option
        login_option = Menu(menu)
        menu.add_cascade(label='Register and Login', menu=login_option)
        login_option.add_command(label='Login', command=self.login)
        login_option.add_command(label='Register', command=self.register)
        login_option.add_separator()

        # Submenu - Help, Contact us, FAQs etc
        submenu = Menu(menu)
        menu.add_cascade(label='Help!!!', menu=submenu)
        submenu.add_command(label='Contact Us!', command=self.contact_us)
        submenu.add_command(label='FAQs', command=self.faq)
        submenu.add_command(label='Report Infringement', command=self.report_infringement)
        submenu.add_separator()

        # About us
        about_us = Menu(menu)
        menu.add_cascade(label='About Us', menu=about_us)
        about_us.add_command(label='About us', command=self.about_us)
        about_us.add_separator()

        # Exit button
        exit_button = Menu(menu)
        menu.add_cascade(label='Exit', menu=exit_button)
        exit_button.add_command(label='Exit', command=menu.quit)


        # Registration starts here

        frame = Frame(master)

        # Frame variable
        self.username = StringVar(master)
        self.password = StringVar()
        self.name = StringVar()
        self.dob = StringVar()
        self.email = StringVar()
        self.mobile_number = StringVar()
        self.SIN = StringVar()
        self.variable = StringVar(master)
        self.address_var = StringVar()
        self.variable.set("Select Post:")  # default value

        post_employee = Label(master, text="Post:")
        # for options menu of post of employee
        w = OptionMenu(master, self.variable, "J. Developer", "Developer", "Manager")
        w.pack(padx=15, pady=3)

        # Name
        employee_name = Label(master, text="Name:")
        employee_name.pack(padx=15, pady=4)
        employee_name_entry = Entry(master, bd=5, textvariable=self.name)
        employee_name_entry.pack(padx=24, pady=4)

        # User name
        Label1 = Label(master, text='Username:')
        Label1.pack(padx=15, pady=5)
        entry1 = Entry(master, bd=5, textvariable=self.username)
        entry1.pack(padx=15, pady=5)

        # Email address
        email_label = Label(master, text='Email:')
        email_label.pack(padx=15, pady=6)
        email_entry = Entry(master, bd=5, textvariable=self.email)
        email_entry.pack(padx=15, pady=6)

        # phone number
        mobile_label = Label(master, text="Mobile:")
        mobile_label.pack(padx=15, pady=7)
        mobile_entry = Entry(master, bd=5, textvariable=self.mobile_number)
        mobile_entry.pack(padx=15, pady=7)

        # SIN number
        SIN_label = Label(master, text="SIN:")
        SIN_label.pack(padx=15, pady=8)
        SIN_entry = Entry(master, bd=5, textvariable=self.SIN)
        SIN_entry.pack(padx=15, pady=8)

        # Password
        Label2 = Label(master, text='Password: ')
        Label2.pack(padx=15, pady=9)
        entry2 = Entry(master, show="*", bd=5, textvariable=self.password)
        entry2.pack(padx=15, pady=9)

        # Address
        address_label = Label(master, text='Address:')
        address_label.pack(padx=15, pady=10)

        # font
        medium_font = ('Courier', 30)
        address_entry = Entry(master, textvariable=self.address_var, bd=10, font=medium_font)
        address_entry.pack(padx=15, pady=10)

        # Register button
        btn = Button(frame, text='Register', command=self.register_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)


    # Function to perform registration
    def register_submit(self):

        # Variables
        self.select_employee_type = self.variable.get()
        self.username_v = self.username.get()
        self.name_v = self.name.get()
        self.email_v = self.email.get()
        self.SIN_v = self.SIN.get()
        self.mobile_number_v = self.mobile_number.get()
        self.password_v = self.password.get()
        self.address_v = self.address_var.get()
        self.error =0

        # Validation for user name
        if (self.username_v == ' '):
            messagebox.showinfo("Username cant be blank")
            print("Error","Blank user name")
            self.error =1

        # check uniqueness of username
        try:
            conn = sqlite3.connect('EMS.db')
            user_db = conn.cursor()
            print(self.username_v)
            user_db.execute('SELECT * FROM register WHERE username = "%s" ' % (self.username_v))
            if user_db.fetchone():
                messagebox.showerror("Failed",
                                     "Username is already been registered, Please provide a different username")

                # set error code 1
                self.error = 1

            # Save changes
            conn.commit()

            # Close connection
            conn.close()

        except:
            messagebox.showerror("Error", "Error occured in checking the uniqueness of username")
            self.error = 1

        # validation for name
        if (self.name_v == ' '):
            messagebox.showinfo("Error", "Name cant be blank")
            print("Error","Blank Name")
            self.error =1

        # validation for email address
        # pass the regular expression
        # and the string in search() method
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, self.email_v)):
            print(self.email_v)
            try:
                conn = sqlite3.connect('EMS.db')
                mail = conn.cursor()
                mail.execute('SELECT * FROM register WHERE email = "%s" ' % (self.email_v))
                if mail.fetchone():
                    messagebox.showerror("Failed",
                                         "Email is already been registered, Please provide a different email")

                    # set error code 1
                    self.error = 1

                # Save changes
                conn.commit()

                # Close connection
                conn.close()

            except:
                messagebox.showerror("Error", "Error occured in checking the uniqueness of email address")
                self.error = 1
        else:
            print("Invalid Email")
            messagebox.showinfo("Error", "Invalid Email")


        # validation for mobile number
        nnum = ''
        for letter in self.mobile_number_v:
            if (letter.isdigit() == True):
                nnum += letter
        if len(nnum) != 10:
            print("\nInvalid phone number")
            messagebox.showinfo("Error","Invalid phone number")
            self.error =1
        elif len(nnum) == 10:
            self.mobile_number_v = nnum

        #validate SIN number
        nnum = ''
        for letter in self.SIN_v:
            if (letter.isdigit() == True):
                nnum += letter
        if len(nnum) != 10:
            print(nnum)
            print("\nInvalid SIN number")
            messagebox.showinfo("Error", "Invalid SIN number")
            self.error = 1
        elif len(nnum) == 10:
            self.SIN_v = nnum

        #Validation for password
        if self.password_v.lower().isalpha() == True or self.password_v.islower() == True or self.password_v.isupper() == True or len(self.password_v) <6:
            print("Password must be more than 6 character long, with atleast 1 capital.")
            messagebox.showinfo("Error", "Password must be more than 6 character long, with atleast 1 capital.")
            self.error =1
        try:
            conn = sqlite3.connect('EMS.db')
            register_db_object = conn.cursor()
            login_db_object = conn.cursor()
        except:
            messagebox.showinfo("Failed", "Can't connect to the server")
            print("cant connect")

        # Salary assignment
        if (self.select_employee_type == 'J. Deveoper'):
            print('JDev')
            self.salary = '30000'

        elif (self.select_employee_type == 'Developer'):
            print('Dev')
            self.salary = '130000'

        else:
            self.salary = '70000'

        # Perform registration
        if self.error == 0:

            # assign default leaves
            self.tleave = '25'
            self.aleave = '0'
            self.lleave = '25'
            print(self.username_v, self.password_v, self.salary, self.SIN_v, self.email_v,
                     self.name_v, self.select_employee_type, self.mobile_number_v, self.address_v, self.lleave, self.tleave, self.aleave)

            # connect to employee's file
            try:
                register_db_object.execute(
                    "INSERT INTO register (username,password,salary,SIN,email,name,post,phone,address,lleave,tleave,aleave) values (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (self.username_v, self.password_v, self.salary, self.SIN_v, self.email_v,
                     self.name_v, self.select_employee_type, self.mobile_number_v, self.address_v, self.lleave, self.tleave, self.aleave))
                conn.commit()
                login_db_object.execute("INSERT INTO main.login_details (username,password)  values (?,?)",
                                        (self.username_v, self.password_v))

                # save changes
                conn.commit()

                # Close connection
                conn.close()
                print("Record written in register")

                # If no error send email to registered employee
                # Send email to newly registered employee
                self.send_email(self.email_v, self.username_v)

                # Display success message
                messagebox.showinfo("Success", "User registered")


            except:
                print("Unable to register")
                messagebox.showinfo("Failed", "Can't Register")

        else:
            messagebox.showerror("Failed", "Can't Register")


    # Send Email to registered employee
    def send_email(self,email_v, username_v):
        print("trying sending email")
        try:
            subject = "Welcome to Carleton Employee Management System"
            body = "Hello " + self.username_v + ",\n\nYou have been registered to Carleton Employee Management System.\n\nThanks for choosing Carleton.\n\n\n\nRegards,\nCarleton EMS"
            sender_email = "your email id"
            receiver_email = self.email_v
            password = "password for email address"

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = "Carleton EMS"
            message["To"] = self.username_v
            message["Subject"] = subject

            # Add body to email
            message.attach(MIMEText(body, "plain"))
            text = message.as_string()
            # Log in to server using secure context and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)

        except:
            messagebox.showinfo("Error while sending Mail", "Mail can't be sent")
            print("Mail can't be send")
            self.error =1


    # Contact details
    def contact_us(self):
        print("contact")


    # Message box indicating faqs
    def faq(self):
         print('FAQs')


    # Goto login screen
    def login(self):
        print('login ')
        call('python3 login.py', shell=True)


    # Call registration
    def register(self):
        print('register')


    # Define report of infringement
    def report_infringement(self):
        ##essage box
        print('Report')


    # Define take a tour
    def take_a_tour(self):
        ##take a tour of the app
        print('take a tour')


    # Define terms of use
    def terms_of_use(self):
        print('message box having   terms of use')


    # define about us
    def about_us(self):
        print('Display your info')


# Main Tkinter GUI
root = Tk()
login_home = Home(root)
root.wm_geometry("1360x1200")
root.title("Register Here")
root.mainloop()

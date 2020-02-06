#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : admin_login.py
# Description : gives login screen to admin
#------------------------------------------------



# Import libraries

from tkinter import *
from tkinter import  messagebox
import os
import signal
from subprocess import  *
import sqlite3




# Main class
class Home():
    def __init__(self,master):

        # Master menu
        menu = Menu(master)
        master.config(menu=menu)

        # Home option
        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Take a Tour!!',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()

        # Login option
        login_option=Menu(menu)
        menu.add_cascade(label='Register and Login',menu=login_option)
        login_option.add_command(label='Login',command=self.login)
        login_option.add_command(label='Register',command=self.register)
        login_option.add_separator()

        # Sub-menu(Help, Contact us, FAQs and Report)
        submenu = Menu(menu)
        menu.add_cascade(label='Help!!!', menu=submenu)
        submenu.add_command(label='Contact Us!',command=self.contact_us)
        submenu.add_command(label='FAQs', command=self.faq)
        submenu.add_command(label='Report Infringement', command=self.report_infringement)
        submenu.add_separator()

        # About us
        about_us=Menu(menu)
        menu.add_cascade(label='About Us',menu=about_us)
        about_us.add_command(label='About us',command=self.about_us)
        about_us.add_separator()


        # Exit
        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=menu.quit)


        # Login frame starts here

        frame = Frame(master)
        self.var1 = StringVar()
        self.var2 = StringVar()

        # Get username
        Label1 = Label(master, text='Username:')
        Label1.pack(padx=15, pady=5)

        entry1 = Entry(master, bd=5,textvariable=self.var1)
        entry1.pack(padx=15, pady=5)

        # Get password
        Label2 = Label(master, text='Password: ')
        Label2.pack(padx=15, pady=6)

        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.var2)
        entry2.pack(padx=15, pady=7)

        # Button to login
        btn = Button(frame, text='Check Login', command=self.login_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)


    # Function to submit login
    def login_submit(self):
        print("Attemted to login")
        try:
            conn = sqlite3.connect('EMS.db')
            login_db_object = conn.cursor()
            print("Attempt successful")
        except:
            messagebox.showinfo("Failed", "Can't connect to the server")
            print("cant connect")

        # Retrieve username and password from GUI
        self.username=self.var1.get()
        self.password=self.var2.get()
        print(self.username,self.password)

        # Checks for admin login
        if self.username== 'admin' and self.password== 'admin' :
            print("Welcome Professor")
            call('python3 admin_login_success.py', shell=True)
        else:
            print("Login failed")
            messagebox.showinfo("Login Failed", "Invalid Username or Password")


    # Function to define contact us sub-menu
    def contact_us(self):
        messagebox.showerror("Contact us","Please contact us at www.CarletonEMS.com or call us at **********")


    # Function to define FAQ sub-menu
    def faq(self):
        print('FAQ')
        messagebox.showerror("Information","No FAQ has been uploaded yet")


    # Funtion to login
    def login(self):
        print('login ')
        call('python3 login.py', shell=True)


    # Funtion to call registration
    def register(self):
        print('register')
        call('python3 registration.py', shell=True)


    # Function to give information in case of infringement
    def report_infringement(self):
        print('Report')
        messagebox.showerror("Report Infringement","If found any infringement please mail us at www.CarletonEMS.com or call us at +1 **********")


    # Take a tour sub-menu
    def take_a_tour(self):
        print('take a tour')


    # Define terms of use
    def terms_of_use(self):
        print('message box having terms of use')


    # Define about us
    def about_us(self):
        print('Display your info')


# Main GUI window
root=Tk()
login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Admin Login")
root.mainloop()

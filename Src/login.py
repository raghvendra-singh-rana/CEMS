#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : login.py
# Description : perform login for employee
#------------------------------------------------


# Import libraries

from tkinter import *
from tkinter import  messagebox
import os
import signal
from subprocess import  *
import sqlite3



# Read login details from file
def login_details(username,password):
    file=open("login_details.txt","w+")
    file.writelines(username+'\n')
    file.writelines(password)
    file.close()


# Main class
class Home():
    def __init__(self,master):

        # Master menu
        menu = Menu(master)
        master.config(menu=menu)

        # Home menu
        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Take a Tour!!',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()

        # Menu Options - login, register
        login_option=Menu(menu)
        menu.add_cascade(label='Register and Login',menu=login_option)
        login_option.add_command(label='Login',command=self.login)
        login_option.add_command(label='Register',command=self.register)
        login_option.add_separator()

        # Menu for Help, Contact us, FAQs etc
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

        # Exit button
        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=menu.quit)

        # Login frame starts here
        frame = Frame(master)

        # frame variables
        self.var1 = StringVar()
        self.var2 = StringVar()

        # Get user name
        Label1 = Label(master, text='Username:')
        Label1.pack(padx=15, pady=5)

        entry1 = Entry(master, bd=5,textvariable=self.var1)
        entry1.pack(padx=15, pady=5)

        # Get Password
        Label2 = Label(master, text='Password: ')
        Label2.pack(padx=15, pady=6)

        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.var2)
        entry2.pack(padx=15, pady=7)

        # login button
        btn = Button(frame, text='Check Login', command=self.login_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)


    # Main login logic
    def login_submit(self):

        print("Attemted to login")
        try:
            conn = sqlite3.connect('EMS.db')
            login_db_object = conn.cursor()
        except:
            messagebox.showinfo("Failed", "Can't connect to the server")
            print("cant connect")

        # get frame values for username and password
        self.username=self.var1.get()
        self.password=self.var2.get()
        print(self.username,self.password)

        # connect to login details
        login_db_object.execute('SELECT * from login_details WHERE username="%s" AND password="%s"' % (self.username,self.password))
        if login_db_object.fetchone() is not None:
            login_details(self.username,self.password)

            # call login_success
            call('python3 login_success.py', shell=True)

        # handle failure
        else:
            print("Login failed")
            messagebox.showinfo("Login Failed", "Invalid Username or Password")

        # Save changes
        conn.commit()

        # Close connection
        conn.close()


    # Define contact us
    def contact_us(self):
        print("contact")


    # Define FAQs
    def faq(self):
        print('FAQs')


    # Define login
    def login(self):
        print('login ')
        call('python3 login.py', shell=True)


    # Call registration screen
    def register(self):
        ##create a register Frame
        print('register')
        call('python3 registration.py', shell=True)


    # Define infringement
    def report_infringement(self):
        print('report')


    # Define take a tour
    def take_a_tour(self):
        print('take a tour')


    # Define terms of use
    def terms_of_use(self):
        print('message box having   terms of use')


    # Define about us
    def about_us(self):
        print('Display your info')


# Main Tkinter Gui
root=Tk()
login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Login")
root.mainloop()

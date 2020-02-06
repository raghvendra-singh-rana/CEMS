#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : home.py
# Description : home page
#------------------------------------------------


# Import libraries

from tkinter import *
import os
import signal
from subprocess import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk



# Main class
class Home():
    def __init__(self,master):

        # Master Menu
        menu = Menu(master)
        master.config(menu=menu)

        # Home menu
        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Take a Tour!!',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()

        # Option for login, registration
        login_option=Menu(menu)
        menu.add_cascade(label='Register and Login',menu=login_option)
        login_option.add_command(label='Login',command=self.login)
        login_option.add_command(label='Register',command=self.register)
        login_option.add_command(label='Admin Login',command=self.admin_login)
        login_option.add_separator()

        # Sub-menu
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

        # exit
        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=menu.quit)


    # Function to perform admin login
    def admin_login(self):
        #import  admin_login
        call('python3 admin_login.py', shell=True)


    # Function to display about us
    def about_us(self):
        top = Toplevel()
        top.geometry("200x200")
        top.title("About Us")

        # Declare a message box
        msg = Message(top, text='Carleton employee management system is part of ITEC course project')
        msg.grid(row=0, column=15)
        button = Button(top, text="Dismiss", command=top.destroy)
        button.grid(row=4, column=15)


    # Populate FAQs
    def faq(self):

        # Message box indicating faqs
        print('No FAQs have been uploaded')


    # Define login
    def login(self):
        print('login ')
        call('python3 login.py', shell=True)


    # Function to call registration function
    def register(self):

        # Create a register Frame
        print('register')

        # Import registration
        call('python3 registration.py', shell=True)


    # Function to report in case of any infringement
    def report_infringement(self):

        # Message box
        messagebox.showerror("Report Infringement","If found any infringement please mail us at www.CarletonEMS.com or call us at +1 **********")


    # Take a tour
    def take_a_tour(self):
        ##take a tour of the app
        tour_take=Toplevel()
        tour_take.geometry("180x180")
        tour_take.title("Take a Tour")
        message=Message(tour_take,text="Press Register to Register an employee and fill the required details.Then Press Login to Login The Employee.")
        message.grid(row=0,column=1)
        button = Button(tour_take, text="Close", command=tour_take.destroy)
        button.grid(row=4, column=1)
        print('take a tour')


    # Define "terms of use"
    def terms_of_use(self):
        string_terms="Privacy Statement Welcome to carleton employee management system(www.carleton.com). By accessing or using this Software, you agree to comply with the terms and conditions governing your use of any areas of the Carleton.com web Software (the Software) as set forth below. USE OF Software Please read the Terms of Use (Terms) carefully before you start using the Software. By using the Software you accept and agree to be bound and abide by these Terms of Use and our Privacy Policy, found at incorporated herein by reference. If you do not agree to these Terms of Use or the Privacy Policy, you must not access or use the Software. This Software or any portion of this Software may not be reproduced, duplicated, copied, sold, resold, or otherwise exploited for any commercial purpose except as expressly permitted by Carleton.com, Inc. Carleton.com, Inc. and its affiliates reserve the right to refuse service, terminate accounts, and/or cancel orders in its discretion, including, without limitation, if Carleton.com, Inc. believes that User conduct violates applicable law or is harmful to the interests of carleton.com, Inc. or its affiliates."
        dialog=Toplevel()
        dialog.geometry("400x400")
        dialog.title("Terms of Use")
        message=Message(dialog,text=string_terms)
        message.grid(row=0,column=0)
        button = Button(dialog, text="Close", command=dialog.destroy)
        button.grid(row=4, column=0)


    # Define "contact us"
    def contact_us(self):
        messagebox.showerror("Contact us ","In case of any dicrepancy or misbehaving of software Please contact us immediately.You can mail us at proudofec@gmail.com or call us at XXXXXXXXXX ")


# Main Tkinter GUI
root=Tk()
image = ImageTk.PhotoImage(Image.open("car.png"))
Lower_frame=Frame(root)
label = Label(Lower_frame, image=image)
label.pack()
Lower_frame.pack()
login_home=Home(root)
root.wm_geometry("1362x1200")
root.title("Home")
root.mainloop()

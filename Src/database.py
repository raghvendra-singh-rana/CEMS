#-------------------------------------------------
# Project Name : Carleton Employee Management System
# Author : Raghvendra Singh Rana
# Carleon id : 101123931
# Email id : raghvendrarana@cmail.carleton.ca
# Date Written : 17 Dec 2019
# File Name : database.py
# Description : File to hold all database files used in rest part of program
#------------------------------------------------


# Import libraries
import sqlite3
conn = sqlite3.connect('EMS.db')
c = conn.cursor()

# Create table for login details
c.execute('''CREATE TABLE IF NOT EXISTS login_details
             (username varchar PRIMARY KEY , password varchar)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

c_register = conn.cursor()

# Create table for employee details

c_register.execute('''CREATE TABLE IF NOT EXISTS register
             (username varchar PRIMARY KEY , password varchar,salary varchar, SIN varchar,email varchar,name varchar,post varchar,phone varchar,address varchar,lleave varchar,tleave varchar,aleave varchar)''')

# Save (commit) the changes
conn.commit()


# Create table for attendance
attendance=conn.cursor()

attendance.execute('''CREATE TABLE IF NOT EXISTS attendance(username varchar PRIMARY KEY ,status varchar,date varchar)''')

# Save (commit) the changes
conn.commit()


# Create table for messages
message=conn.cursor()

message.execute('''CREATE table if not exists message_alerts(message varchar,date varchar)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

# Create leave table for leaves

leave=conn.cursor()

leave.execute('''CREATE TABLE IF NOT EXISTS leave_requests(username varchar,from_date varchar,to_date varchar,reason varchar, status varchar)''')

# Save (commit) the changes
conn.commit()


# Finally close the connection
conn.close()




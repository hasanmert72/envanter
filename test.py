__author__ = 'hasan'

from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4.QtCore import *
import sys


users = {}
status = ""

while status != "q":
    status = raw_input("Are you a registered user? y/n? Press q to quit: ")

    if status == "n": #create new login
         createLogin = raw_input("Create login name: ")

         if createLogin in users: # check if login name exist in the dictionary
             print "Login name already exist!\n"
         else:
             createPassw = raw_input("Create password: ")
             users[createLogin] = createPassw # add login and password
             print("\nUser created!\n")

    elif status == "y": #login the user
        login = raw_input("Enter login name: ")

        if login in users:
           passw = raw_input("Enter password: ")
           print

           if login in users and passw in users: # login matches password
               print "Login successful!\n"

        else:
            print
            print("User doesn't exist!\n")
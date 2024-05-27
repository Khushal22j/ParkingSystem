#program to access the reports and other observatory options.
#requires the administrative access using an ID and a password.
import mysql.connector
db=mysql.connector.connect(user="root",password="admin",host="localhost",database="parking_system")
mycursordb=db.cursor()
initial_count = 1
chances = 5
input_id = str(input("Enter the login id here: "))
mycursordb.execute("select count(*) from adminlogin where userid = %s",(input_id))
idcheck = mycursordb.fetchone()
print(idcheck)
passcheck=mycursordb.execute("Select userid,password from adminlogin")
idpass = mycursordb.execute("select count(*) userid,password from adminlogin where userid=(%s) and password = (%s)" , (idcheck,passcheck) )

if input_id in idcheck :
    input_pass = input("Enter the password here: ")
while initial_count != chances:
    if idpass == 0:
        print("ID and Password do not match try again")
        initial_count += 1

options = ["1: Tabular Report","2: Revenue collected","3: No. of cars","4: Get Log Files of Specified Date","5: Current status of Pillars","6: Cars Present Inside Currently"]
while initial_count != chances:
    try:
        print("Welcome to the Rajiv Chowk car parking administrative system...")
        print("Options available are:")
        for i in options:
            print(i)
            print("Enter the respective serial number against the option you wish to avail-")
            admin_preference = int(input("Enter the serial number here: "))
                
            break
    except ValueError:
        print("Incorrect input, no such option available...!")

       

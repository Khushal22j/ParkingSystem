#user operational program for data entry, availability of space.
import datetime
import pickle
import random
import mysql.connector as mysql
def Connector(query):
    db = mysql.connect(user='admin',password='admin',host='localhost',database='parking_data')
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
space = 5
Data = {}
original_file = open(r"C:\Users\DELL\Desktop\Python\Project\parking_data_file.dat","wb+")
while space >0:
    print("Available space is",space)
    Data["Name"] = input("Enter your name here: ")
    Data["Reg_number"] = int(input("Enter your registered car number here: "))
    current_time = datetime.datetime.now()
    minute_base = current_time.hour + (current_time.minute/60)
    Data["Time"] = minute_base
    Data["code"]= Code = random.randint(1,1000)
    print(f"Your indentification code is: {Code}. You will need it at the time of exit.")
    pickle.dump(Data,original_file)
    space -= 1
    space_file = open(r"C:\Users\DELL\Desktop\Python\Project\space_file.dat", "wb")             #here to manage space algorithm between Exit.py and Surface_information.py
    pickle.dump(space,space_file)
original_file.close()
space_file.close()


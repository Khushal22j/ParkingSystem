import mysql.connector
import datetime
db=mysql.connector.connect(user="root",password="admin",host="localhost",database="parking_system")
mycursordb=db.cursor()
now = datetime.datetime.now()
x = int(input("Enter 1:For Entrying Parking zone 2:Leaving Parking zone 3:Misplaced Parking Slip   "))
if x == 1:
    print("Welcome to Rajiv Chowk")
    FName=input("Enter First Name  ")
    while FName.isalpha() != True:
        FName=input("Enter Again should be aplhabets only" )
    LName = input("Enter Last Name (Enter If not any) ")
    while LName.isalpha() != True:
        LName=input("Enter Again should be aplhabets only")
    VehicleNum=input("Enter The Number Plate  ")
    while len(VehicleNum)<10:
        VehicleNum=input("Should be 10 Characters Enter again")
    mycursordb.execute("select count(*) from floor_1 where Reserved='NOT RES'")
    r1=mycursordb.fetchone()
    mycursordb.execute("select count(*) from floor_2 where Reserved='NOT RES'")
    r2=mycursordb.fetchone()
    mycursordb.execute("select count(*) from floor_3 where Reserved='NOT RES'")
    r3=mycursordb.fetchone()
    if r1[0] != 0:
        mycursordb.execute("select Pillars from floor_1 where Reserved ='NOT RES' limit 3")
        print("\nOn floor 1 pillar nearest to you are\n")
        for i in mycursordb:
            stripi=str(i)
            print(stripi.strip("(',)")+'\t')
    elif r2[0] !=0:
        print("\nSorry Floor 1 is fully Booked. Nearest Floor empty is 2\n")
        mycursordb.execute("select Pillars from floor_2 where Reserved ='NOT RES' limit 3")
        print("\nOn floor 2 pillar nearest to you are\n")
        for i in mycursordb:
            stripi=str(i)
            print(stripi.strip("(',)")+'\n')
    elif r3[0] != 0:
        print("\nSorry Floor 1 and 2 are fully Booked. Nearest Floor empty is 3\n")
        mycursordb.execute("select Pillars from floor_3 where Reserved ='NOT RES' limit 3")
        print("\nOn floor 3 pillar nearest to you are\n")
        for i in mycursordb:
            stripi=str(i)
            print(stripi.strip("(',)")+'\n')
    else:
        print("Sorry we are fully booked no parking space is available.")
    
    pillarin=input("\nPlease choose a pillar: ").upper()
    floor=pillarin[0]
    EntryTime=now.strftime("%Y-%m-%d %H:%M:%S")
    mycursordb.execute("insert into logfiles(Name,VehicleNum,Floor,Pillar,EntryTime) values (%s,%s,%s,%s,%s)" , (FName+' '+LName,VehicleNum,floor,pillarin[1],EntryTime))
    db.commit()
mycursordb.close()
mycursordb.close()
db.close()
db.close()
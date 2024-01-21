import os 
import platform
import mysql.connector

mydb=mysql.connector.connect(

    host="localhost",
    user="<your_username>",
    password="<your_password>",
    database="<your_database>"

)
mycursor=mydb.cursor()


#MODULE FOR NEW ADMISSION
def newStudent():
    createTable	="""CREATE TABLE IF	NOT	EXISTS STUDENT(SROLL_NO	VARCHAR(5),SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30),PHONE VARCHAR(12),ADDRESS VARCHAR(100),SCLASS VARCHAR(5),SSECTION VARCHAR(5),
SADMISSION_NO VARCHAR(10) PRIMARY KEY)"""
    mycursor.execute(createTable) 
    sroll_no=input(" ENTER ROLL_NO : ") 
    sname=input("\n ENTER STUDENT'S NAME : ") 
    fname=input(" ENTER FATHER'S NAME : ") 
    mname=input(" ENTER MOTHER'S NAME : ")
    phone=input(" ENTER CONTACT NO. : ") 
    address=input(" ENTER ADDRESS : ")
    sclass =input(" ENTER CLASS : ") 
    ssection=input(" ENTER SECTION : ")
    sadmission_no=input(" ENTER ADMISSION_NO  :  ")
    sql="insert into student (sroll_no,sname,fname,mname,phone,address,sclass,ssection,sadmission_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(sroll_no,sname,fname,mname,phone,address,sclass,ssection,sadmission_no) 
    mycursor.execute(sql,values) 
    mycursor.execute("COMMIT") 
    mydb.commit()



#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent(): 
    mycursor.execute("SELECT * FROM student") 
    data=mycursor.fetchall()
    for i in range(len(data)+1):
        if i<=(len(data)-1):
            print("--------------------------------------------------------------")
            print("Admission_Number = ",data[i][8]) 
            print("Roll Number = ",data[i][0]) 
            print("Name = ",data[i][1])
            print("Class = ",data[i][6])
            print("Section = ",data[i][7])
            print("--------------------------------------------------------------")
        elif i==len(data):
            continue
    mydb.commit()


#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent(): 
    admission_no=input("ENTER ADMISSION NO :")
    mycursor.execute("SELECT * FROM student WHERE sadmission_no=%s",(admission_no,)) 
    data=mycursor.fetchall() 
    if data:
        print("PRESS 1 TO EDIT NAME") 
        print("PRESS 2 TO EDIT CLASS") 
        print("PRESS 3 TO EDIT ROLL NO")
        choice=int(input("Enter Your Choice:")) 
        if choice==1:
            name=input("ENTER NAME OF THE STUDENT :")
            sql="UPDATE student SET sname= %s WHERE sadmission_no =%s" 
            mycursor.execute(sql,(name,admission_no)) 
            mycursor.execute("COMMIT")
            print("NAME UPDATED")
        elif choice == 2:
            std=input("ENTER CLASS OF THE STUDENT  :")
            sql="UPDATE student SET sclass= %s WHERE sadmission_no=%s" 
            mycursor.execute(sql,(std,admission_no)) 
            mycursor.execute("COMMIT")
            print("CLASS UPDATED")
 
        elif choice==3:
            roll_no=int(input("ENTER ROLL NO OF THE STUDENT :")) 
            sql="UPDATE	student	SET	sroll_no=%s	WHERE sadmission_no = %s"
            mycursor.execute(sql,(roll_no,admission_no)) 
            mycursor.execute("COMMIT")
            print("ROLL NO UPDATED")
        else:
            print("Record Not Found Try Again !") 
    else:
        print("\nSomething Went Wrong ,Please Try Again !") 
        mydb.commit()

#MODULE TO ENTER MARKS OF THE STUDENT
def marksStudent () :
    createTable ="""CREATE TABLE IF NOT EXISTS MARKS(SADMISSION_NO VARCHAR(10) PRIMARY KEY,HINDI INT,ENGLISH INT,MATH INT,SCIENCE INT,SOCIAL INT,COMPUTER INT,TOTAL IN,AVERAGE DECIMAL)"""
    mycursor.execute(createTable)
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :") 
    hindi=int(input("\n ENTER MARKS OF HINDI : ")) 
    english=int(input("\n ENTER MARKS OF ENGLISH : ")) 
    math=int(input("\n ENTER MARKS OF MATH : ")) 
    science=int(input("\n ENTER MARKS OF SCIENCE : ")) 
    social=int(input("\n ENTER MARKS OF SOCIAL : "))
    computer =int(input("\n ENTER MARKS OF COMPUTER : ")) 
    total = hindi + english + math + science + social + computer 
    average = total/6
    sql="INSERT INTO MARKS(SADMISSION_NO,HINDI,ENGLISH,MATH,SCIENCE,SOCIAL,COMPUTER, TOTAL,AVERAGE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(admission_no,hindi,english,math,science,social,computer , total , average)
    mycursor.execute(sql,values) 
    mycursor.execute("COMMIT")
    print("\nMarks of the Student Entered Successfully !") 
    mydb.commit()

#MODULE TO PRINT REPORT CARDS OF ALL STUDENTS
def reportCardAllStudent () : 
    sql="SELECT * FROM MARKS"
    mycursor.execute(sql) 
    data=mycursor.fetchall() 
    for i in range(len(data)+1):
        if i<=(len(data)-1):
            print("--------------------------------------------------------------")
            print("Admission_Number = ",data[i][0]) 
            print("Hindi = ",data[i][1])
            print("English = ",data[i][2])
            print("Math = ",data[i][3])
            print("Science = ",data[i][4])
            print("Social Science = ",data[i][5]) 
            print("Computer Science = ",data[i][6]) 
            print("Average = ",(data[i][7])/6)
            print("--------------------------------------------------------------")
        elif i==len(data): 
            continue
    mydb.commit()



#MODULE TO GENERATE REPORT CARD OF ONE STUDENTS
def reportCardOneStudent():
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT:")
    sql="SELECT * FROM MARKS WHERE SADMISSION_NO= %s"
    mycursor.execute(sql,(admission_no,)) 
    data=mycursor.fetchall()
    for i in range(len(data)):
        if data[i][0]==admission_no:
            print("--------------------------------------------------------------")
            print("Admission_Number = ",data[i][0]) 
            print("Hindi = ",data[i][1])
            print("English = ",data[i][2])
            print("Math = ",data[i][3])
            print("Science = ",data[i][4])
            print("Social Science = ",data[i][5]) 
            print("Computer Science = ",data[i][6]) 
            print("Average = ",(data[i][7])/6)
            print("--------------------------------------------------------------")
        else:
            print("Admission Not found") 
            mydb.commit()
            continue

#MODULE TO GENERATE THE PROJECTED SCORES OF THE STUDENT
def Proj_scores():
    admission_no=input("ENTER ADMISSION NO:") 
    mycursor.execute("SELECT * FROM MARKS WHERE sadmission_no=%s",(admission_no,)) 
    data=mycursor.fetchall() 
    for i in range(len(data)):
        if data[i][0]==admission_no: 
            a=data[i][7]
            avg=a/6
            print("Projected Score is ",avg) 
        else:
            print("Admission not found") 
            mydb.commit()


#HELP!!!!
def helpMe():
    print("Please Visit The Offcial Website Of Indian School Muscat To Download The Manual !!!")
    mydb.commit()


print("#####################################################################")

#DRIVER LOOP
while(1):
    print("|	Enter 1 - Add Student.    |")	
    print("|	Enter 2 - Display Student's Data.		|")
    print("|	Enter 3 - Update Students's Data.		|")
    print("|	Enter 4 - Add Student's Marks Detail.		|")
    print("|	Enter 5 - Generate All Student's Report Card.	    |")
    print("|	Enter 6 - Generate Student Wise Report Card.		|") 
    print("|	Enter 7 - Projected Scores of the Student.		|") 
    print("|	Enter 8 - Exit Application.     |")
    print("|	Enter 0 (ZERO) - Help.		|") 
    choice=int(input("PLEASE ENTER YOUR CHOICE :	"))
    if choice==1: 
        newStudent()
    elif choice==2: 
        displayStudent()
    elif choice==3: 
        updateStudent()
    elif choice==4: 
        marksStudent()
    elif choice==5: 
        reportCardAllStudent()
    elif choice==6: 
        reportCardOneStudent()
    elif choice==7: 
        Proj_scores()
    elif choice==8: 
        quit()
    elif choice==0: 
        helpMe()
    else:
        print("Please enter the right choice from the given options !!! ")

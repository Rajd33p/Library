######################################IMPORTS#########################################
import mysql.connector
from datetime import datetime
import random
import string
import time
#######################################################################################

#######################################MYSQL###########################################
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="library"
)
mycursor = mydb.cursor()
#######################################################################################

#######################################Helper Functions################################
date = datetime.today().strftime("%Y-%m-%d")


def ran(len=5):
    char = ""
    while(len > 0):
        char = char + str((random.choice(string.digits)))
        len -= 1
    return int(char)


def fine(day):
    if(day <= 7):
        return int(0)
    else:
        return int((day - 7)*5)

########################################################################################


#############################################CORE#######################################

def B_issued():
    sql = 'select name , ID , Book_ID ,Add_no from issued where status="false"'
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mydb.commit()
    return data


def issue():
    name = input("Enter Student Name: ")
    add_no = int(input("Enter Addmission Number: "))
    book_ID = int(input("Enter Book ID : "))
    ID = ran()
    sql = "INSERT INTO ISSUED(Name,ID,Add_no,Book_ID,Iss_D,Status) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (name, ID, add_no, book_ID, date, "false")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.", "ID - ", ID)


def collect():
    I_ID = int(input("Enter Issue ID"))

    sql = "SELECT Iss_D FROM Issued WHERE ID = %s"
    val = (I_ID,)
    mycursor.execute(sql, val)
    Idate = mycursor.fetchall()
    Idate = Idate[0][0]
    diff = abs(datetime.strptime(str(Idate), "%Y-%m-%d") -
               datetime.strptime(str(date), "%Y-%m-%d"))
    if(diff.days <= 7):
        sql = 'UPDATE ISSUED SET STATUS = "true" , Rcv_D = %s WHERE ID = %s'
        val = (date, I_ID)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Records Updated Take the book Back")
    else:
        print("Late Submission \n Please Collect fine of ", fine(diff.days))


########################################################################################

######################################IMPORTS#########################################
import mysql.connector
from datetime import datetime
import random
import string
import time
#######################################################################################

#######################################MYSQL###########################################
mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
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


def DateDiffernce(IDate):
    return abs(datetime.strptime(str(IDate), "%Y-%m-%d") -
               datetime.strptime(str(date), "%Y-%m-%d")).days


########################################################################################


#############################################CORE#######################################

def BookS():
    sql = 'select * from books'
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mydb.commit()
    return data


def B_issued():
    response = list()
    sql = 'select name , ID , Book_ID ,Add_no,Iss_D from issued where status="false"'
    mycursor.execute(sql)
    data = mycursor.fetchall()
    mydb.commit()

    for x in data:
        x = list(x)
        diff = DateDiffernce(x[4])
        if (diff >= 7):
            x[4] = (diff-7)
            response.append(x)

    return response


def issue(name, add_no, book_ID):
    ID = ran()
    sql = "INSERT INTO issued(Name,ID,Add_no,Book_ID,Iss_D,Status) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (name, ID, add_no, book_ID, date, "false")
    mycursor.execute(sql, val)
    update = "UPDATE books SET Issused = Issused + 1 WHERE ID = %s"
    mycursor.execute(update, (book_ID,))
    mydb.commit()
    return ID


def collect(I_ID):
    sql = "SELECT Iss_D , Book_ID FROM issued WHERE ID = %s"
    val = (I_ID,)
    mycursor.execute(sql, val)
    Idate = mycursor.fetchall()
    if len(Idate) != 0:
        diff = DateDiffernce(Idate[0][0])
        if(diff <= 7):
            sql = 'UPDATE issued SET STATUS = "true" , Rcv_D = %s WHERE ID = %s'
            val = (date, I_ID)
            mycursor.execute(sql, val)
            update = "UPDATE books SET Issused = Issused - 1 WHERE ID = %s"
            mycursor.execute(update, (Idate[0][1],))
            mydb.commit()
            print("Records Updated Take the book Back")
            return "Good"
        else:
            sql = 'UPDATE issued SET STATUS = "true" , Rcv_D = %s WHERE ID = %s'
            val = (date, I_ID)
            mycursor.execute(sql, val)
            update = "UPDATE books SET Issused = Issused - 1 WHERE ID = %s"
            mycursor.execute(update, (Idate[0][1],))
            mydb.commit()
            return fine(diff)
    else:
        return "ID_NOT_FOUND"

########################################################################################


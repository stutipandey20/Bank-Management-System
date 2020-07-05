import pymysql as sql
con = sql.connect("localhost","root","password","bankinfo")
c = con.cursor()

import pygame
import tkinter as tkr
import os

f=open("bank_proj",'w+')
banker = tkr.Tk()
banker.title("BANK MANAGEMENT SYSTEM")
banker.configure(width=1200,height=600,bg='POWDER BLUE')
banker.mainloop()
var=-1

b1 = tkr.Button(banker,text="CREATE ACCOUNT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b2 = tkr.Button(banker,text="WITHDRAW AMOUNT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b3 = tkr.Button(banker,text="DEPOSIT AMOUNT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b4 = tkr.Button(banker,text="CHECK BALANCE", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b5 = tkr.Button(banker,text="CHANGE PASSWORD", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b6 = tkr.Button(banker,text="EXIT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))

def show():
    i = (input("Enter id: "))
    qry = "select amount from bank where id = '%s'" % (i)
    r = c.execute(qry)
    print("Balance is : ")
    for data in c.fetchone():
        print(data[3])
    con.commit()


def withdraw():
    i = input("Enter id: ")
    amt = int(input("Enter amount to withdraw: "))
    qry = "update bank set amount = amount-'%d' where id = '%s'" % (int(amt),i)
    r = c.execute(qry)
    if (r > 0):
        print("Transaction Successful!")
    else:
        print("Transaction fail!")
    con.commit()


def deposit():
    i = input("Enter id: ")
    amt = int(input("Enter amount to deposit: "))
    qry = "update bank set amount = amount+'%d' where id = '%s'" % (int(amt),i)
    r = c.execute(qry)
    if (r > 0):
        print("Transaction Successful!")
    else:
        print("Transaction Fail!")
    con.commit()

def passwrd():
    i = input("Enter id: ")
    old = input("Enter old password: ")
    new = input("Enter new password: ")
    neww = input("Confirm new password: ")
    if(new==neww):
        qry = "update user set password = '%s' where id = '%s'" % (new,i)
        r = c.execute(qry)
        if(r>0):
            print("Password Changed!")
        else:
            print("Password Change Fail!")
    else:
        print("Please re-confirm your new password!")

    con.commit()

def add():
    i = input("Enter id: ")
    n = input("Enter name: ")
    p = input("Enter password: ")
    a = input("Enter address: ")
    m = int(input("Enter mobile_no: "))
    amt = int(input("Enter amount: "))
    qry = "insert into user(id,name,password,address,mobile_no) values('%s','%s','%s','%s','%d')" %(i,n,p,a,int(m))
    q2 = "insert into bank(id,name,acc_no,amount) values('%s','%s','%d','%d')" %(i,n,int(m),int(amt))
    s= c.execute(q2)
    r = c.execute(qry)
    if(r>0):
        print("Record Inserted")
    else:
        print("Record not Inserted")
    con.commit()



def main():
    while True:
        print("-----CHOOSE FROM BELOW OPTIONS-----\n")
        choice = int(input("1.CHECK BALANCE\n2.WITHDRAW\n3.DEPOSIT\n4.CHANGE PASSWORD\n5.NEW ACCOUNT\n6.EXIT\nEnter your choice:\t"))

        if choice == 1:
            show()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            deposit()
        elif choice == 4:
            passwrd()
        elif choice == 5:
            add()
        else:
            print("Invalid Choice")
        main()

main()

con.close()


import mysql.connector
import pandas as pd
from datetime import date 
from tabulate import tabulate

import datetime #to get 2020-03-05
con=mysql.connector.connect(host="localhost",user="root",password="",database="movie")
res=con.cursor()

def check_db():  
    a=True  
    qry="SELECT count(SCHEMA_NAME) FROM information_schema.SCHEMATA  where SCHEMA_NAME='movie';";
    res.execute(qry)
    result=res.fetchone()
    return result[0]

def create_db():
    if(check_db()==0):
        res.execute('CREATE database IF NOT EXISTS movie;')
    return True

def user(login):
    qry="select UID from user where uname='{a}' and upass='{b}';".format(a=uname,b=upass)
    res.execute(qry)
    result=res.fetchone()
    if result is None:
        return 0
    else:
        return(result[0])
        
def add(sql):
    res.execute(sql)
    con.commit()
    
def update(sql):
    res.execute(sql)
    con.commit()
    
def delete(sql):
    res.execute(sql)
    con.commit()

def view(sql):    
    res=con.cursor()
    res.execute(sql)
    result=res.fetchall()
    return result

def fetchone(sql):
    res=con.cursor()
    res.execute(sql)
    result=res.fetchone()
    return result
    
def fetchall(sql):
    res=con.cursor()
    res.execute(sql)
    result=res.fetchall()  
    return result
#---------------------------------------------------------------------------------------------------------

check_db()
create_db()
c='Y'
print("\t\t*************************************************")
print("\n\t\t\t WELCOME TO MOVIE TICKET BOOKING")
print("\n\t\t\t\tTICKETSHOP THEATRE")
print("\n\t\t*************************************************")
while(c=='y' or c=='Y'):
    print("1.Enter as admin")
    print("2.Enter as worker")
    n=int(input("Enter your choice : "))
    if(n==1):
    
        uname=input("Enter Your Uname : ")
        upass=input("Enter Your Upass : ")
        login=(uname,upass)
        u=user(login)   #for login check
        if(u==1):
            print("\n\n************************")
            print("   Welcome admin")
            print("************************\n")
            cc='y'
            while(cc=='y' or cc=='Y'):      
                mes="""
                print("1.Add movie")
                print("2.Update movie records")
                print("3.Delete movie records")                               
                print("4.Status")
                print("5.Customer list")
                print("6.View Bookings")
                """
                print(mes)
                no=int(input("Enter your choice : "))
                if(no==1):
                    print("Add movie")
                    name=input("Enter movie name : ")
                    mformat=input("Enter hall format : ")
                    showdate=input("Enter show date : ")
                    showtime=input("Enter show time : ")
                    price=input("Enter price per person : ")
                    seat=input("Enter no of seat available : ")
                    #MID, NAME, FORMAT, SHOWDATE, SHOWTIME, PRICE, SEAT
                    sql="insert into movie (NAME, FORMAT, SHOWDATE, SHOWTIME, PRICE, SEAT) values ('"+name+"','"+mformat+"','"+showdate+"','"+showtime+"','"+price+"','"+seat+"');"
                    add(sql)
                    print("Movie added successfully")
                elif(no==2):
                    print("Update movie records")
                    mid=input("Enter movie id : ")
                    name=input("Enter movie name : ")
                    mformat=input("Enter hall format : ")
                    showdate=input("Enter show date : ")
                    showtime=input("Enter show time : ")
                    price=input("Enter price per person : ")
                    seat=input("Enter no of seat available : ")
                    sql="update movie set NAME='"+name+"',FORMAT='"+mformat+"',SHOWDATE='"+showdate+"',SHOWTIME='"+showtime+"',PRICE='"+price+"',SEAT='"+seat+"' where MID="+mid
                    update(sql)
                    print("Movie updated successfully")
                elif(no==3):
                    print("Delete movie records")
                    mid=input("Enter movie id : ")
                    sql="delete from movie where mid="+mid
                    delete(sql)
                    print("Movie deleted successfully")
                elif(no==4):
                    print("status")
                    sql="select * from movie"
                    #col=('MID', 'NAME', 'FORMAT', 'SHOWDATE', 'SHOWTIME', 'PRICE', 'SEAT')
                    
                    table = (view(sql))
                    headers = ('MID', 'NAME', 'FORMAT', 'SHOWDATE', 'SHOWTIME', 'PRICE', 'SEAT')
                    print(tabulate(table, headers, tablefmt="psql"))

                elif(no==5):
                    print("Customer list")  
                    sql="select * from customer;"                    
                    table = (fetchall(sql))
                    headers = ('CID','NAME','PHONE','ADDRESS','EMAIL')
                    print(tabulate(table, headers, tablefmt="psql"))

                elif(no==6):   
                    print("View Bookings")
                    sql="select * from booking;"
                    a=fetchall(sql)
                    s=[]
                    for i in range(len(a)):
                        s.append(int(a[i][4]))
                    s=sum(s)
                    table = (fetchall(sql))
                    headers = ('BID', 'CID', 'MID', 'SEAT', 'TOTAL')
                    print(tabulate(table, headers, tablefmt="psql")) 
                    print("\t\t\t TOTAL :  ", s,"\n")
                   
                else:
                    print("Invalid choice")
                cc=input("Do you want to choose correct choice (Y/N) : ")

        else:
            print("Invalid uname or pass")

    elif(n==2):
        cc='y'
        print("\n\n************************")
        print("   Welcome worker")
        print("************************\n")

        while(cc=='y' or cc=='Y'):    
            mes="""
            print("1.Add details")
            print("2.Edit details")
            print("3.View Movie list")
            print("4.Book Tickets")           
            print("5.View ticket")
            print("6.Cancel tickets")
            """
            print(mes)
            no=int(input("Enter your choice : "))
            if(no==1):
                print("Add details")
                cname=input("Enter customer name : ")
                phno=input("Enter phno : ")
                addr=input("Enter addr : ")
                email=input("Enter email : ")
                #CID, CNAME, PHNO, ADDR, EMAIL
                sql="insert into customer (CNAME, PHNO, ADDR, EMAIL) values ('"+cname+"','"+phno+"','"+addr+"','"+email+"');"
                add(sql)
                print("customer details added successfully")
            elif(no==2):
                print("Edit details")
                cid=input("Enter cid : ")
                cname=input("Enter customer name : ")
                phno=input("Enter phno : ")
                addr=input("Enter addr : ")
                email=input("Enter email : ")
                #CID, CNAME, PHNO, ADDR, EMAIL
                sql="update customer set CNAME='"+cname+"',PHNO='"+phno+"',ADDR='"+addr+"',EMAIL='"+email+"' where cid="+cid
                update(sql)
            elif(no==3):
                print("View Movie list")
                sql="select * from movie"
                #col=('MID', 'NAME', 'FORMAT', 'SHOWDATE', 'SHOWTIME', 'PRICE', 'SEAT')
                table = (view(sql))
                headers = ('MID', 'NAME', 'FORMAT', 'SHOWDATE', 'SHOWTIME', 'PRICE', 'SEAT')
                print(tabulate(table, headers, tablefmt="psql"))
               
            elif(no==4):
                print("Book Tickets")
                cid=input("Enter customer id : ")
                mid=input("Enter movie id : ")
                seat=input("Enter no of seats : ")
                sql="select seat,price from movie where mid="+mid
                s=fetchone(sql)               
                #BID, CID, MID, SEAT, TOTAL  
                if(int(s[0])==0 or int(s[0])<0):
                    print("Invalid seats")                  
                elif(int(s[0])<int(seat)):
                    print(int(s[0]))
                    g=input("is available - do you want to book {y|n}")
                    if(g=='y' or g=='Y'):
                        ss=0
                        seat=int(s[0])
                        ss=str(int(s[0])-seat)
                        total=str(int(seat)*int(s[1]))
                        print(total)
                        sql="insert into booking (CID, MID, SEAT, TOTAL) values ('"+cid+"','"+mid+"','"+str(seat)+"','"+total+"');"
                        add(sql)
                        sql="update movie set seat='"+ss+"' where mid='"+mid+"'";
                        update(sql)
                    else:
                        pass
                else:
                    ss=str(int(s[0])-int(seat))
                    total=str(int(seat)*int(s[1]))
                    print(total)
                    sql="insert into booking (CID, MID, SEAT, TOTAL) values ('"+cid+"','"+mid+"','"+seat+"','"+total+"');"
                    add(sql)
                    sql="update movie set seat='"+ss+"' where mid='"+mid+"'";
                    update(sql)
            elif(no==5):
                print("View ticket")
                #BID, CID, MID, SEAT, TOTAL   - booking
                #CID, CNAME, PHNO, ADDR, EMAIL - customer
                #MID, NAME, FORMAT, SHOWDATE, SHOWTIME, PRICE, SEAT
                cid=input("Enter customer cid : ")
                sql="select customer.cid,customer.cname, customer.phno, customer.addr, customer.email, movie.name, movie.format, DATE_FORMAT(movie.showdate,'%d-%m-%Y'), movie.showtime, booking.seat, booking.total from booking inner join  customer on booking.cid=customer.cid inner join movie on booking.mid=movie.mid where booking.cid="+cid
                table = (fetchall(sql))
                headers = ('CID','NAME','PHONE','ADDRESS','EMAIL', 'MOVIE NAME', 'FORMAT', 'SHOWDATE', 'SHOWTIME', 'SEAT','TOTAL')
                print(tabulate(table, headers, tablefmt="psql"))
                
                
            elif(no==6):
                print("Cancel tickets")  
                cid=input("Enter customer cid : ")
                sql="delete from booking where cid="+cid
                delete(sql)              
            else:
                print("Invalid choice")
            cc=input("Do you want to choose correct choice (Y/N) : ")
    else:
        print("Invalid choice")
    c=input("Do u want to continue (Y/N) : ")

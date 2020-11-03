import mysql.connector
import pandas as pd
con=mysql.connector.connect(host="localhost",user="root",password="root",database="lib")
sql=con.cursor()

def checkDb():
	a=True
	qry="SELECT count(SCHEMA_NAME) FROM information_schema.SCHEMATA  where SCHEMA_NAME='lib';";
	sql.execute(qry)
	result=sql.fetchone()
	return result[0]

def createDb():
	if(checkDb()==0):
		sql.execute('CREATE database IF NOT EXISTS lib;')
	return True

def createUser(user):
	qry="insert into users (UNAME,UPASS,ROLE) values (%s,%s,%s)"
	sql.execute(qry,user)
	con.commit()
	print('User Registration Success')
#
def login(user):
	a=0
	qry="SELECT UID from users where UNAME=%s and UPASS=%s"
	sql.execute(qry,user)
	result=sql.fetchone()
	if result is None:
		return 0
	else:
		return(result[0])

def searchBooks(key):
	qry="select BNAME,AUTHOR,ISBN,STOCK from books where BNAME like '%{k1}%' or ISBN like '%{k2}%' or AUTHOR like '%{k3}%';".format(k1=key,k2=key,k3=key)
	sql.execute(qry)
	result=sql.fetchall()
	data = pd.DataFrame(result)
	print(data)

def checkRoll(roll):
    qry="SELECT count(Roll),ID  FROM students where roll='{r}'and status='Yes';".format(r=roll)
    sql.execute(qry)
    result=sql.fetchone()
    return result
def checkIsbn(isbn):
    qry="SELECT * FROM books where isbn='{i}';".format(i=isbn)
    sql.execute(qry)
    result=sql.fetchone()
    if result is None:
        return 0
    else:
        return(result)
def issueBook(id,bid):
    #print(id,bid)
    qry="update students set status='iss' where id={i};".format(i=id)
    sql.execute(qry)
    con.commit()
    qry="update books set stock=stock-1 where bid={b};".format(b=bid)
    sql.execute(qry)
    con.commit()
    qry="insert into trans(ID,BID) values ({i},{b});".format(i=id,b=bid)
    sql.execute(qry)
    con.commit()
    print("Book Issued")
def printBookDetails(mes,qry):
    print(mes)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)
def checkStudent(roll):
    qry=" select count(students.ID),students.ID,trans.BID  from students inner join trans on students.ID=trans.ID where students.ROLL='{r}' and trans.STATUS='No'".format(r=roll)
    sql.execute(qry)
    result=sql.fetchone()
    return result
def returnBooks(id,bid):
    qry="update students set status='Yes' where id={i};".format(i=id)
    sql.execute(qry)
    con.commit()
    qry="insert into trans(ID,BID,REMARKS,STATUS) values ({i},{b},'Book Returned','Yes')".format(i=id,b=bid)
    sql.execute(qry)
    con.commit()   
    qry="update trans set status='Yes' where bid={b} and id={i};".format(b=bid,i=id)
    sql.execute(qry)
    con.commit()  
    qry="update books set STOCK=STOCK+1 where bid={b}".format(b=bid)
    sql.execute(qry)
    print("Return Book Success")
    con.commit()  
#------------------------------------------------------
createDb()
#user=('Sam','1234','Student')
#createUser(user)
c='Y'
while c=='Y' or c=='y':
	name=input("Enter User Name : ")
	upass=input("Enter Password  : ")
	user=(name,upass)
	u=login(user)
	if(u==1):
		print('Welcome Admin')
		print("1.Issue Book")
		print("2.Return Book")
		print("3.Users Details")
		print("4.Issue Book Details")
		print("5.Transaction")
		x='Y'
		while(x=='Y' or x=='y'):
			ch=int(input("Select Your Choice : "))
			if(ch==1):
				roll=input("Enter Roll No : ")
				rollno=checkRoll(roll)
				if(rollno[0]==1):
					isbn=input("Enter ISBN      : ")
					res=checkIsbn(isbn)
					if(res==0):
						print("Invalid ISBN No")
					else:
						if(res[-1]>=1):
							#print(rollno)
							#print(res)
							issueBook(rollno[1],res[0])
						else:
							print("Stock Not Available")
				else:
					print("You are Not Eligible to Request Book")
			elif(ch==2):
				roll=input("Enter Roll No : ")
				rollno=checkStudent(roll)
				if(rollno[0]!=0):
					print("Return Book")
					returnBooks(rollno[1],rollno[2])       
				else:
					print("No Records Found")
			elif(ch==3):
				qry="SELECT * FROM STUDENTS"
				printBookDetails('Student Details',qry)
			elif(ch==4):
				qry="SELECT students.NAME,students.ROLL,books.BNAME,trans.LOGS from trans inner join students on students.ID=trans.ID inner join books on books.BID=trans.BID where trans.status='No'"
				printBookDetails('Issue Book Details',qry)
			elif(ch==5):
				qry="SELECT students.NAME,students.ROLL,books.BNAME,trans.LOGS,trans.remarks from trans inner join students on students.ID=trans.ID inner join books on books.BID=trans.BID"
				printBookDetails('Transaction Details',qry)
			x=input("Do You Want To Continue (Y/N) : ")       
	elif(u==2):
		print('Welcome Student')
		x='y'
		while x=="Y" or x=='y':
			key=input("Enter The Keyword To Search : ")
			searchBooks(key)
			x=input("Do You Want To Continue or Exit Application (Y/N) : ")		
	else:
		print('Invalid User Name and Password')
	c=input('\n\nDo You Want To Continue : (Y/N)')


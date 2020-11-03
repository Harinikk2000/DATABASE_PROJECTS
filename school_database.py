import mysql.connector
import pandas as pd
from datetime import date 
import datetime #to get 2020-03-05
con=mysql.connector.connect(host="localhost",user="root",password="",database="school")
sql=con.cursor()

def check_db():
    a=True
    qry="SELECT count(SCHEMA_NAME) FROM information_schema.SCHEMATA  where SCHEMA_NAME='school';";
    sql.execute(qry)
    result=sql.fetchone()
    return result[0]
    

def create_db():
    if(check_db()==0):
        sql.execute('CREATE database IF NOT EXISTS school;')
    return True
    

    
def login(user):
    qry="select UID from users where UNAME=%s and UPASS=%s;"
    sql.execute(qry,user)
    result=sql.fetchone()        #returns only one result , and can use if or else statements
    if result is None:
        return 0
    else:
        return(result[0])
    
"""    
def add_staff1(name,tCODE,tPASS):
    qry="insert into add_staff (TNAME,TCODE,TPASS) values (%s,%s,%s)"
    sql.execute(qry)
    con.commit()
    print('success')
"""
#cannot pass as single variable, take as tuple
def add_staff1(add):
    qry="insert into add_staff (TNAME,TCODE,TPASS) values (%s,%s,%s)"
    sql.execute(qry,add)     #use argument during execution like 'add'
    con.commit()           #use 'commit' during insert,delete,update
    qry="insert into users (UNAME,UCODE,UPASS) values (%s,%s,%s)"
    sql.execute(qry,add)
    con.commit()
    print('success')
    
    
def add_staff_att(add1):   
    qry="insert into staff_att (stname,stcode) values (%s,%s)"
    sql.execute(qry,add1)
    con.commit()

def add_student(add):
    qry="insert into add_student (SNAME,ROLL,DOB2,STDD,SEC,FNAME,ADDRESS,PHONE,TC) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql.execute(qry,add)
    con.commit()
    print('success')

def pay_fee(pay): 
    qry="insert into pay_fee (ROLL2,SNAME2,CLASS2,SEC2,FEES2,BAL2) values (%s,%s,%s,%s,%s,%s)"
    sql.execute(qry,pay)
    con.commit()
    print('success')    
    
def fee_paid(paid2,roll2):
    qry="UPDATE PAY_FEE SET PAID2=PAID2+{j} WHERE roll2={i};".format(j=paid2,i=roll2)
    sql.execute(qry)
    con.commit()
    qry="UPDATE PAY_FEE SET BAL2=BAL2-PAID2 WHERE roll2={i};".format(i=roll2)
    sql.execute(qry)
    con.commit()   
    qry="select bal2 from pay_fee where roll2={i}".format(i=roll2)
    sql.execute(qry)
    result=sql.fetchone()
    return result
    print('success')
    
def fee(roll2):
    qry="SELECT * FROM PAY_FEE WHERE ROLL2={i};".format(i=roll2)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)                
###

def checkRoll(sname):
    qry="SELECT ROLL FROM add_student where sname='{r}'".format(r=sname)
    sql.execute(qry)
    result=sql.fetchone()
    if result is None:
        return 0
    else:
        return(result)    
"""
def checkRoll(sname):
    qry="SELECT ROLL FROM add_student where sname='%s';"
    sql.execute(qry)
    result=sql.fetchone()
    if result is None:
        return 0
    else:
        return(result)   
"""       
def addclass(add_class1):
    qry="insert into add_class (STD,SEC,TID,TPASS) values (%s,%s,%s,%s)"
    sql.execute(qry,add_class1)
    con.commit()
    print('success')
 
def add_exam(add):  
    print("good")
    qry="insert into exam (ENAME) values '%s' "
    sql.execute(qry,add)
    con.commit()
    
def checkc(tpass):
    print("ttt")
    qry="SELECT count(TID),tcode from add_staff where tpass={i}".format(i=tpass)
    sql.execute(qry)
    result=sql.fetchone()
    return result

def rollno(roll):
    qry="select count(SID),roll from add_student where roll={i}".format(i=roll)
    sql.execute(qry)
    result=sql.fetchone()
    return result

    if result is None:
        return 0
    else:
        return(result[0])    
        
def check_class(std,sec):
    qry="SELECT count(CID) FROM add_class where std={i} and sec='{j}';".format(i=std,j=sec) 
    #format is other easy way
    #use same name for argument and format variables
    
    #qry="select count(CID) from add_class where STD=%s and SEC=%s"    #cannot be used
    sql.execute(qry)   #no need of passing std,sec in execute,bcoz of using format in qry statement
    result=sql.fetchone()
    if result is None:
        return 0
    else:
        return(result[0])
        
        
def sid(roll):
    qry="select SID from add_student where roll={r};".format(r=roll)
    sql.execute(qry)
    result=sql.fetchone()
    if result is None:
        return 0
    else:
        return(result[0])
        
def sid1(stdd,sec):
    qry="select SID from add_student where stdd={r} and sec='{s}';".format(r=stdd,s=sec)
    sql.execute(qry)
    result=sql.fetchall()
    return(result)
    
def class1(add1):
    qry="insert into std1 (STD1,SECTION,ROLLNO,SID1,DOB1,SNAME1,ATD1) values (%s,%s,%s,%s,%s,%s,%s)"
    sql.execute(qry,add1)
    con.commit()
    print('success')    

def display(mes,qry):
    print(mes)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)  #to display in table format
    print(data)
   
def viewclass(STDD,SEC):   
    qry="select SID,SNAME,ROLL,DOB2,STDD,SEC,FNAME,ADDRESS,PHONE,TC FROM add_student where STDD={i} and SEC='{j}';".format(i=STDD,j=SEC)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)

def att(qry):
    sql.execute(qry)
    con.commit()
    print("success")
    
def att1(qry2):
    sql.execute(qry2)
    con.commit()
    print("success")
    
def view_staff(mes,qry):
    print(mes)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)
    qry1="SELECT TID,TCODE FROM ADD_STAFF"
    sql.execute(qry1)
    result=sql.fetchall()     
    return(result)
    
def details(SNAME,DOB2,STDD,SEC,FNAME,ADDRESS,PHONE,TC,roll):
    qry="update add_student set SNAME='{a}',DOB2='{c}',STDD={d},SEC='{e}',FNAME='{f}',ADDRESS='{g}',PHONE={h},TC='{i}' where roll={j};".format(a=SNAME,c=DOB2,d=STDD,e=SEC,f=FNAME,g=ADDRESS,h=PHONE,i=TC,j=roll)
    #qry="update add_student set sname='{i}' where roll={j}".format(i=sname,j=roll)
    sql.execute(qry)
    con.commit()
    
def details1(sname2,class2,sec2,fees2,bal2,roll2):
    qry="update pay_fee set sname2='{a}',class2={b},sec2='{c}',fees2={d},bal2={e} where roll2={f};".format(a=sname2,b=class2,c=sec2,d=fees2,e=bal2,f=roll2)
    sql.execute(qry)
    con.commit()
    print("success")
    
def details2(std1,section,dob1,sname1,rollno):
    qry="update std1 set std1={a},section='{b}',dob1='{c}',sname1='{d}' where rollno={e}".format(a=std1,b=section,c=dob1,d=sname1,e=rollno)
    sql.execute(qry)
    con.commit()
    print("success")

def mod1(tname,tpass,tcode):
    qry="update add_staff set tname='{a}',tpass={b} where tcode={c}".format(a=tname,b=tpass,c=tcode)
    sql.execute(qry)
    con.commit()
    
def mod2(uname,upass,ucode):
    qry="update users set uname='{a}',upass={b} where ucode={c}".format(a=uname,b=upass,c=ucode)
    sql.execute(qry)
    con.commit()   
    
def mod3(stname,stcode):
    qry="update staff_att set stname='{a}' where stcode={c}".format(a=stname,c=stcode)
    sql.execute(qry)
    con.commit()  

def view(stdd,sec):
    qry="select SID,ROLL,SNAME from add_student where stdd={a} and sec='{b}'".format(a=stdd,b=sec)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)
    qry1="select SID,ROLL from add_student where stdd={a} and sec='{b}'".format(a=stdd,b=sec)
    sql.execute(qry1)
    result=sql.fetchall()
    return result
    
def dis_att_stu(rollno):
    qry="select * from stud_att where rollno={a}".format(a=rollno)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)    
    
def dis_att_class(std1,section):
    qry="select * from stud_att where std1={a} and section='{b}'".format(a=std1,b=section)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)
 
def dis_att_date(std1,section,atdate1):
    qry="select * from stud_att where std1={a} and section='{b}' and atdate1='{c}'".format(a=std1,b=section,c=atdate1)
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)
    
def mod_stu_att(atd1,sid1,atdate1):
    qry="update stud_att set atd1='{a}' where sid1={b} and atdate1='{c}'".format(a=atd1,b=sid1,c=atdate1)
    sql.execute(qry)
    con.commit()
    print("success")
    
def mod_staff_att(atend,stcode,atdate):
    qry="update staff_att set atend='{a}' where stcode={b} and atdate='{c}'".format(a=atend,b=stcode,c=atdate)
    sql.execute(qry)
    con.commit()
    print("success")
    
def mark_stu(ex):
    qry="insert into marks (exid1,roll1,eng,math,sci) values (%s,%s,%s,%s,%s)"
    sql.execute(qry,ex)
    con.commit()
    print("success")
   
def mark_stu1(eng,math,sci,exid1,roll1):
    qry="update marks set eng={a},math={b},sci={c} where exid1={d} and roll1={e}".format(a=eng,b=math,c=sci,d=exid1,e=roll1)
    sql.execute(qry)
    con.commit()
    
    
def update_mark(exid1,roll1):
    qry="update marks set total=eng+math+sci,avg=total/3 where exid1={a} and roll1={b}".format(a=exid1,b=roll1)
    sql.execute(qry)
    con.commit() 
    
def collect(exid1,roll1):
    qry1="select total,avg from marks where exid1={a} and roll1={b}".format(a=exid1,b=roll1)
    sql.execute(qry1)
    result=sql.fetchall()  #while printing up[0][0]
    #result=sql.fetchone()   #while printing up[0]
    return result  
    print("success")
     
def up_mark(result1,grade,exid1,roll1):
    qry="update marks set result1='{c}',grade='{d}' where exid1={a} and roll1={b}".format(c=result1,d=grade,a=exid1,b=roll1)
    sql.execute(qry)
    con.commit()
    
def view_mark(stdd,sec):
    qry="select add_student.roll,add_student.sname,marks.exid1,marks.result1,marks.grade from add_student inner join marks on add_student.roll=marks.roll1 where add_student.stdd={a} and add_student.sec='{b}'".format(a=stdd,b=sec)
    print("  roll   name exid result grade")
    sql.execute(qry)
    result=sql.fetchall()
    data = pd.DataFrame(result)
    print(data)  

def check_cla(std,sec,tid,tpass):
    qry="select count(cid) from add_class where std={a} and sec='{b}' and tid={c} and tpass={d};".format(a=std,b=sec,c=tid,d=tpass)
    sql.execute(qry)
    result=sql.fetchone()
    return result
#-------------------------------------------------------------------------
check_db()
create_db()

abst=[]
aa=[]
all1=[]
al=[]
code=[]
c='Y'
while (c=='y' or c=='Y'):
    UNAME=input("Enter your name : ")
    UPASS=int(input("Enter your pass : "))
    user=(UNAME,UPASS)
    u=login(user)
    if(u==1):
        
        
        print("........................")
        print("Welcome ",UNAME,"...")
        print("........................")
        print("1.Add Staff")
        print("2.Add Student")
        print("3.Add Class")
        print("4.Display Students")
        print("5.Modify Student")
        print("6.Modify staff")
        print("7.View class")
        print("8.View Attendance")
        print("9.View Marks")
        print("10.View fees")
        print("11.display staff")
        print("........................\n")
        x='Y'
        while(x=='y' or x=='Y'):
            ch=int(input("Enter your choice 1-11 : "))
            if(ch==1):
                print("************")
                print("Add staff")
                print("************")
                name=input("Enter name of staff :")
                tCODE=int(input("Enter ucode :"))
                tPASS=int(input("Enter upass :"))
                add=(name,tCODE,tPASS)     #always insert as 'tuple'               
                add_staff1(add)            #then pass tuple to function
                add1=(name,tCODE)
                add_staff_att(add1)
                print("Staff added")
                
            elif(ch==2):
                print("************")
                print("Add STUDENT")
                print("************")
                name=input("Enter name of student : ")
                roll=input("Enter roll :")
                dob=input("Enter dob (dd-mm-yyyy) :")
                classs=input("Enter std :")
                sec=input("Enter sec :")
                fname=input("Enter father name :")
                addr=input("Enter addr :")
                phn=input("Enter phn :")
                tc=input("Enter (y/n) :")
                fee=int(input("Enter fee :"))
                bal=int(input("Enter bal :"))
                #cha=(classs,sec)
                cha=check_class(classs,sec)   #to check whether class and sec is available or not
                
                print(cha)
                #roll=1200
                
                if(cha==1):
                    
                    add=(name,roll,dob,classs,sec,fname,addr,phn,tc)
                    ad=add_student(add) 
                    print("student added")   
                    sid1=sid(roll)          #to add student in class by using their sid
                    #print(sid1)
                    add1=(classs,sec,roll,sid1,dob,name,'P')
                    class1(add1)
                    pay=(roll,name,classs,sec,fee,bal)
                    pay_fee(pay)
                    print("added")
                    aaa=checkRoll(name)                    
                    print(aaa[0])                                       
                else:
                    print("not found class or sec ")
                    
                    
            elif(ch==3):
                print("************")
                print("Add class")
                print("************")
                cname=input("Enter std")
                sec=input("Enter sec")
                teacher=input("Enter teacher id : ")
                pass1=input("Enter teacher pass : ")
                ca=(teacher)
                checkc(ca)     #to check whether teacher is present or not using id
                #print(ca[0])
                              
                if(ca[0]==0):
                    print("false")
                else:
                    print("true")
                    add_class1=(cname,sec,teacher,pass1)
                    addclass(add_class1)
                    print("added_class")
                    add1=(cname,sec)
                    print("good")
                     
            elif(ch==4):
                print("*********************")
                print("Display students list")
                print("*********************")
                qry="SELECT * FROM add_student ORDER BY STDD"   #using to short the code
                display('stu',qry)
            elif(ch==5):
                print("*********************")
                print("Modify student detail")
                print("*********************")
                roll=int(input("Enter the roll no of student : "))
                ro=rollno(roll)
                if(ro[0]==1):
                    name=input("Enter name of student : ")
                    dob=input("Enter dob (dd-mm-yyyy) :")
                    classs=input("Enter std :")
                    sec=input("Enter sec :")
                    fname=input("Enter father name :")
                    addr=input("Enter addr :")
                    phn=input("Enter phn :")
                    tc=input("Enter (y/n) :")
                    fee=int(input("Enter fee :"))
                    bal=int(input("Enter bal :"))             
                    print(ro[1])
                    details(name,dob,classs,sec,fname,addr,phn,tc,ro[1])                    
                    details1(name,classs,sec,fee,bal,ro[1])
                    details2(classs,sec,dob,name,ro[1])
                else:
                    print("Not found roll")
            elif(ch==6):
                print("*********************")
                print("Modify staff details ")
                print("*********************")
                code=int(input("Enter code of staff :"))
                caa=checkc(code)
                print(caa[0],caa[1])   #get count(TID),tcode of staff
                name=input("Enter name of staff :")
                tPASS=int(input("Enter upass :"))
                mod1(name,tPASS,caa[1])     
                mod2(name,tPASS,caa[1])
                mod3(name,caa[1])
                print("successfully modified")
                
            elif(ch==7):
                print("***********")
                print("VIEW CLASS")
                print("***********")
                std=input("Enter the STD :")
                sec=input("Enter the SEC :")
                viewclass(std,sec)            
            elif(ch==8):
                print("***************************")
                print("Display Student attendance")
                print("***************************")
                print("1.Student attendance ")
                print("2.Class attendance")
                print("3.Enter by date")
                attend=int(input("Enter 1 or 2 or 3 :"))
                if(attend==1):
                    rol1=int(input("Enter student roll no : "))                    
                    dis_att_stu(rol1)
                elif(attend==2):
                    std=int(input("Enter std :"))
                    sec=input("Enter section :")
                    dis_att_class(std,sec)
                elif(attend==3):
                    std=int(input("Enter std :"))
                    sec=input("Enter section :")
                    year=int(input("Enter year : "))
                    month=int(input("Enter month : "))
                    date=int(input("Enter date: "))
                    date1=datetime.date(year,month,date)       #to convert to date format,take as tuple
                    dis_att_date(std,sec,date1)
                else:
                    print("Wrong option")
              
            elif(ch==9):
                print("***********")
                print("View marks")
                print("***********")
                std=int(input("Enter std :"))
                sec=input("Enter section :")
                view_mark(std,sec)
            elif(ch==10):
                print("**********")
                print("View fees")
                print("**********")
                roll=int(input("Enter roll no of student :"))
                fee(roll)
            elif(ch==11):
                print("********************")
                print("Display staffs list")
                print("********************")
                qry="SELECT * FROM add_staff"
                display('staff',qry)
            else:
                print("Invalid choice")
            x=input("Do u want to continue admin ... (y/n) :")
    elif(u==2):
        print("........................")
        print("Welcome ",UNAME,"..")
        print("........................")
        print("1.Staff attendance")
        print("2.pay student fee")
        print("3.display students")
        print("4.display staff")
        print("5.modify staff attendance")
        print("........................\n")
        x='Y'
        while(x=='y' or x=='Y'):
            ch=int(input("Enter your choice 1-7 : "))
            if(ch==1):
                print("*****************")
                print("Staff attendance")         #
                print("*****************")
                qry="select TCODE,TPASS from add_staff"                
                a=view_staff("stt",qry)
                for i in range(0,len(a)):     #fetch tid,tcode of staff       
                    print(a[i][0])          #if we use fetchall, shd use a[i][j].. if fetchone can use a[i]
                    al.append(a[i][0])
                print(al)
                n=int(input("ENter n :"))
                print("Enter the code of staff to be absent :")
                for i in range(n):
                    i=int(input())
                    code.append(i)
                print(code)
                
                qry1="insert into staff_att (stcode,id1,atend,atdate) values "
                #att1('done',qry1)
                for i in range(0,len(al)):
                    t=0
                    for j in range(0,len(code)):
                        if(code[j]==al[i]):
                            t=1
                            break
                    if(t==1):
                        qry1=qry1+"({b},{c},'{a}',now()),".format(b=a[i][1],c=al[i],a='A')
                        
                    else:
                        qry1=qry1+"({b},{c},'{a}',now()),".format(b=a[i][1],c=al[i],a='P')
                        
                
                qry2=qry1[0:len(qry1)-1]
                att1(qry2)
                
            elif(ch==2):
                print("*********************")
                print("Pay fees of student ")
                print("*********************")
                rol=int(input("Enter roll no :"))
                fee=int(input("Enter the amt to be paid : "))               
                feee=fee_paid(fee,rol)
                print(feee[0])
            elif(ch==3):
                print("*********************")
                print("Display students list")
                print("*********************")
                qry="SELECT * FROM add_student ORDER BY STDD"
                display('stu details',qry)                
            elif(ch==4):
                print("*********************")
                print("Display staffs list")
                print("*********************")
                qry="SELECT * FROM add_staff"
                display('staff',qry)                
            elif(ch==5):
                print("****************************")
                print("Modify attendance of staff ")
                print("***************************")
                stcode=int(input("Enter stcode of staff : "))
                year=int(input("Enter year : "))
                month=int(input("Enter month : "))
                date=int(input("Enter date: "))
                date1=datetime.date(year,month,date)  
                att=input("mark as P or A :")
                #print(sid,date1,att)
                mod_staff_att(att,stcode,date1)                
            else:
                print("Invalid choice")
            x=input("Do u want to continue office ... (y/n) :")
            
            
    elif(u>=3):
        print("........................")
        print("Welcome ",UNAME,"..")
        print("........................")
        print("1.View class")
        print("2.Student attendance")
        print("3.Student marks")
        print("4.Add exam")
        print("5.Modify attendance of student")
        print("6.Modify marks of students")

        print("........................\n")
        x='Y'
        while(x=='y' or x=='Y'):
            ch=int(input("Enter your choice 1-7 : "))
            if(ch==1):
                print("************")
                print("VIEW CLASS")
                print("************")
                tcode=int(input("Enter tcode of staff : "))                              
                std=int(input("Enter the STD :"))
                sec=input("Enter the SEC :")
                cla=check_cla(std,sec,tcode,UPASS) 
                if(cla[0]==1):
                    viewclass(std,sec)
                else:
                    print("invalid tcode staff...")
            elif(ch==2):
                print("*******************")
                print("Student attendance ")
                print("*******************")
                tcode=int(input("Enter tcode of staff : "))                                              
                std=input("Enter the STD :")
                sec=input("Enter the SEC :")
                cla=check_cla(std,sec,tcode,UPASS)
                print(cla[0]) 
                if(cla[0]==1):                
                    s=view(std,sec)
                    print(s[0])
            
                    for i in range(0,len(s)):                
                        all1.append(s[i][0])
                    print(all1)
                    n=int(input("Enter no of stu absent : "))
                    print("Enter the sid of student to mark absent : ")
                    for i in range(n):
                        i=int(input())
                        abst.append(i)
                    print(abst)
                    
                    qry="insert into stud_att (STD1,SECTION,SID1,ROLLNO,ATD1,ATDATE1) values "
                    
                    for i in range(0,len(all1)):
                        t=0
                        for j in range(0,len(abst)):
                            if(abst[j]==all1[i]):
                                t=1
                                break
                        if(t==1):
                            qry=qry+"({b},'{c}',{st},{d},'{a}',now()),".format(b=std,c=sec,st=all1[i],d=s[i][1],a='A')
                            
                        else:
                            qry=qry+"({b},'{c}',{st},{d},'{a}',now()),".format(b=std,c=sec,st=all1[i],d=s[i][1],a='P')
                    print(qry[0:len(qry)-1])
                    qry=qry[0:len(qry)-1]    
                    att(qry)
                else:
                    print("invalid tcode staff...")
                
            elif(ch==3):
                print("*******************")
                print("Marks of students")  
                #for marks db, set grade,result as 'null' , since after entering marks, will calculate grade....
                print("*******************")
                print("VIEW CLASS")
                tcode=int(input("Enter tcode of staff : "))                              
                std=int(input("Enter the STD :"))
                sec=input("Enter the SEC :")
                cla=check_cla(std,sec,tcode,UPASS)
                #print(cla[0]) 
                if(cla[0]==1):                
                    exam=int(input("Enter exam id : "))
                    roll=int(input("Enter student roll : "))
                    eng=int(input("Enter eng mark : "))
                    math=int(input("Enter math mark : "))
                    sci=int(input("Enter sci mark : "))
                    ex=(exam,roll,eng,math,sci)
                    mark_stu(ex)
                    update_mark(exam,roll)
                    up=collect(exam,roll)
                    print(up[0][0],up[0][1])                
                    r='PASS'
                    if(eng>=35 and math>=35 and sci>=35):
                        r="PASS"
                    else:
                        r="FAIL"
                    print(r)
                    
                    grade='O'
                    if(up[0][1]>=90 and up[0][1]<=100):
                        grade='O'
                    elif(up[0][1]>=80 and up[0][1]<=89):
                        grade='A'
                    elif(up[0][1]>=70 and up[0][1]<=79):
                        grade='B'
                    elif(up[0][1]>=60 and up[0][1]<=69):
                        grade='C'
                    else:
                        grade='F'
                    print(grade)
                    up_mark(r,grade,exam,roll)
                else:
                    print("Invalid")
            elif(ch==4):
                print("**********")
                print("Add exam ")            
                print("**********")
                name=input("Enter exam name :")
                add=(name)
                add_exam(add)                
                                             
            elif(ch==5):
                print("*****************************")
                print("Modify attendance of student ")
                print("*****************************")
                tcode=int(input("Enter tcode of staff : "))                                              
                std=input("Enter the STD :")
                sec=input("Enter the SEC :")
                cla=check_cla(std,sec,tcode,UPASS)
                print(cla[0]) 
                if(cla[0]==1):                 
                    sid=int(input("Enter sid of student : "))
                    year=int(input("Enter year : "))
                    month=int(input("Enter month : "))
                    date=int(input("Enter date: "))
                    date1=datetime.date(year,month,date)  
                    att=input("mark as P or A :")
                    #print(sid,date1,att)
                    mod_stu_att(att,sid,date1)
                else:
                    print("Invalid")
            elif(ch==6):
                print("**************")
                print("Modify marks ")
                print("**************")
                tcode=int(input("Enter tcode of staff : "))                                              
                std=input("Enter the STD :")
                sec=input("Enter the SEC :")
                cla=check_cla(std,sec,tcode,UPASS)
                print(cla[0]) 
                if(cla[0]==1):
                    exam=int(input("Enter exam id : "))
                    roll=int(input("Enter student roll : "))
                    eng=int(input("Enter eng mark : "))
                    math=int(input("Enter math mark : "))
                    sci=int(input("Enter sci mark : "))               
                    mark_stu1(eng,math,sci,exam,roll)
                    update_mark(exam,roll)
                    up=collect(exam,roll)
                    print(up[0][0],up[0][1])                
                    r='PASS'
                    if(eng>=35 and math>=35 and sci>=35):
                        r="PASS"
                    else:
                        r="FAIL"
                    print(r)
                    
                    grade='O'
                    if(up[0][1]>=90 and up[0][1]<=100):
                        grade='O'
                    elif(up[0][1]>=80 and up[0][1]<=89):
                        grade='A'
                    elif(up[0][1]>=70 and up[0][1]<=79):
                        grade='B'
                    elif(up[0][1]>=60 and up[0][1]<=69):
                        grade='C'
                    else:
                        grade='F'
                    print(grade)
                    up_mark(r,grade,exam,roll)                
                else:
                    print("invalid")
            else:
                print("Invalid choice")
            x=input("Do u want to continue as staff... (y/n) :")

    else:
        print("Invalid uname or password")
    c=input("Do you want to continue (Y/N) : ")

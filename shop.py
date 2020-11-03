import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="shop")
#------------------------------------------------
#Fetch One
"""
    1.Login Check
    2.Customer Check
"""
def fetchOneData(sql):
    res=con.cursor()
    res.execute(sql)
    result=res.fetchone()
    return result

def fetchAllData(sql,col):  #to print customers,vendors,purchase,stock,sales infomation
    res=con.cursor()
    res.execute(sql)
    result=res.fetchall()
    #print(result)
    if len(result)==0: 
        return 0
    else:
        print("---------------------------------------------------------------------------------------------------------------")
        print("SNO",end="     ")
        for c in col:
             
             print(c,end="        ")
        print("\n----------------------------------------------------------------------------------------------------------------")
        x=0
        for row in result:
            x+=1
            print(x,end="    ")
            for i in range(len(row)):
                print(row[i],end="       ")
            print("")

#qry="insert into sales (CUID,BILL,PDATE,PID,PRICE,QTY,SGST,CGST,IGST,TOTAL) values ('"+str(cus[0])+"','"+bill+"',NOW(),'"+product[8]+"','"+product[3]+"','"+product[2]+"','"+product[4]+"','"+product[5]+"','"+product[6]+"','"+product[7]+"')"

def user(qry):  #add user,vendor,customers in db   
    res=con.cursor()
    res.execute(qry)
    con.commit()
    return "added success"

def calculateAmount(product,qty):
    #PNAME,PRICE,QTY,AMT,SGST,CGST,IGST,TOTAL 
    amt=int(product[2])*qty
    sgst=amt*(int(product[3])/100)
    cgst=amt*(int(product[4])/100)
    igst=amt*(int(product[5])/100)
    tot=amt+sgst+cgst+igst                                
    pro=[str(product[1]),str(product[2]),str(qty),str(amt),str(sgst),str(cgst),str(igst),str(tot),str(product[0])]
    return pro

def GenerateBillNo():
    sql="SELECT 2000+count(distinct(BILL)) as BILLNO FROM sales"
    res=con.cursor()
    res.execute(sql)
    result=res.fetchone()
    return str(result[0])
    
def saveSales(cart,cus):
    #CUID ,BILL,PDATE ,PID ,PRICE ,QTY ,SGST ,CGST ,IGST ,TOTAL
    #cus[0],GenerateBillNo(),NOW(),product[8],product[3],product[2],product[4],product[5],product[6],product[7]
    bill=GenerateBillNo()
    for product in cart:
        #Sales Table Insert
        qry="insert into sales (CUID,BILL,PDATE,PID,PRICE,QTY,SGST,CGST,IGST,TOTAL) values ('"+str(cus[0])+"','"+bill+"',NOW(),'"+product[8]+"','"+product[3]+"','"+product[2]+"','"+product[4]+"','"+product[5]+"','"+product[6]+"','"+product[7]+"')"
        res=con.cursor()
        res.execute(qry)
        #Stock Update(-)
        qry="update stock set qty=qty-"+product[2]+" where pid="+product[8]
        res=con.cursor()
        res.execute(qry)
        con.commit()
    

def billPrint(cart,cus):   
    print("****************************************SELLERS SUPER MARKET********************************************")
    aa="{:<15}{}"
    print(aa.format("Name: ",(cus[1])))
    print(aa.format("ADDRESS: ",(cus[2])))
    print(aa.format("",(cus[3])))
    print(aa.format("EMAIL: ",(cus[4])))
    print(aa.format("Pincode:",(cus[5])))
    print("*********************************************************************************************************")
    myformat = "{:<10}{:<15}{:<15}{:<10}{:<10}{:<10}{:<10}{:<10}{}{}"
    print(myformat.format("S.No","PRODUCT","UNIT","PRICE","AMOUNT","sgst","cgst","igst","","NET PRICE"))
    print("---------------------------------------------------------------------------------------------------------")

    for i in range(len(cart)):   
        total=0
        print(myformat.format(i+1,cart[i][0],cart[i][2],cart[i][1],cart[i][3],cart[i][4],cart[i][5],cart[i][6],"₹ ","{:10.2f}".format(float(cart[i][7])))) 
    for pro in cart:
        total=total+float(pro[7])
    total="{:.2f}".format((total))
    print("----------------------------------------------------------------------------------------------------------")
    print(myformat.format("","","","","","","","total amt:","₹ ",total))
    print("----------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t~~HAPPY SHOPPING~~")
    
#**********************************************************************************************************************        
#**********************************************************************************************************************
ch='N'
while(ch=='N' or ch=='n'):
    mes="""
        1.Login
        2.Customers
    """
    print(mes)
    c=int(input("Enter Your Choice: "))
    if c==1:
        name=input("Enter User Name     : ")
        password=input("Enter User Password : ")
        sql="SELECT NAME,ROLE FROM user_login where UNAME='"+name+"' and PASS='"+password+"'"
        a=fetchOneData(sql)
        ##print(a)
        if(a!=None):
            print("\t\t   *******************")
            print("\t\t   Welcome ",a[0].upper())
            print("\t\t   *******************")

            if(a[1].upper()=="ADMIN"):
                mes="""
                    1.user Registration
                    2.Sales Report
                    3.Purchase Report
                    4.Stock Report
                    5.Customer List
                    6.Vendor List
                   
                """
                print(mes)
                z='y'
                while(z=='y' or z=='Y'):
                    x=int(input("Select Your Choice : "))
                    if x==1:
                        print("User Registration")
                        name=input("Enter name : ")
                        uname=input("Enter uname : ")
                        password=input("Enter password : ")
                        role=input("Enter role : ")
                        qry="insert into user_login(NAME,UNAME,PASS,ROLE) values ('"+name+"','"+uname+"','"+password+"','"+role+"')"
                        u=user(qry)
                        print(u)
                    elif x==2:
                        print("Sales Report")
                        fdate=input("Enter From Date : ")
                        tdate=input("Enter To Date : ")
                        sql="SELECT customers.NAME, sales.BILL, DATE_FORMAT(sales.PDATE,'%d-%m-%Y') as PDATE, sum(PRICE) as PRICE, sum(SGST) as SGST, sum(CGST) as CGST, sum(IGST) as IGST, round(sum(TOTAL),2) as TOTAL FROM sales inner join customers on sales.cuid=customers.cuid where sales.PDATE between '"+fdate+"' and '"+tdate+"' group by sales.BILL order by sales.BILL;"
                        col=('NAME' ,'BILL' ,'PDATE' ,'PRICE' ,'SGST' ,'CGST' ,'IGST' ,'TOTAL')
                        fetchAllData(sql,col)
                        sql="select sum(total) from sales where pdate between '"+fdate+"' and '"+tdate+"';"
                        t=fetchOneData(sql)
                        print("Total amount for the product pruchased is : ",int(t[0]))
                    elif x==3:
                        print("Purchase Report")                       
                        fdate=input("Enter From Date : ")
                        tdate=input("Enter To Date : ")                        
                        #PUID, VID, PDATE, PID, PRICE, QTY, SGST, CGST, IGST, TOTAL
                        sql="SELECT vendor.NAME, DATE_FORMAT(purchase.PDATE,'%d-%m-%Y') as PDATE, product.pname , sum(purchase.PRICE) as PRICE, purchase.qty, sum(purchase.SGST) as SGST, sum(purchase.CGST) as CGST, sum(purchase.IGST) as IGST, round(sum(purchase.TOTAL),2) as TOTAL FROM purchase inner join vendor on purchase.vid=vendor.vid inner join product on purchase.pid=product.pid where purchase.PDATE between '"+fdate+"' and '"+tdate+"' group by purchase.vid order by purchase.vid;"
                        col=('NAME','PDATE' ,'PNAME','PRICE' ,'QTY','SGST' ,'CGST' ,'IGST' ,'TOTAL')
                        fetchAllData(sql,col)
                        sql="select sum(total) from purchase where pdate between '"+fdate+"' and '"+tdate+"';"
                        t=fetchOneData(sql)
                        print("Total amount for the product pruchased is : ",int(t[0]))
                    elif x==4:
                        print("Stock Report")  
                        sql="select product.pid,product.pname,stock.qty from product inner join stock on product.PID=stock.PID;"
                        col=('PID','PNAME','QTY')
                        fetchAllData(sql,col)
                    elif x==5:
                        print("Customer List")
                        col=('NAME','ADD1','ADD2','CITY','PINCODE','MOBILE','GST','EMAIL')                        
                        sql="select NAME,ADD1,ADD2,CITY,PINCODE,MOBILE,GST,EMAIL from customers;"
                        fetchAllData(sql,col)
                    elif x==6:
                        print("Vendor List")
                        col=('NAME','ADD1','ADD2','CITY','PINCODE','MOBILE','GST','EMAIL')                        
                        sql="select NAME,ADD1,ADD2,CITY,PINCODE,MOBILE,GST,EMAIL from vendor;"
                        fetchAllData(sql,col)                        
                    else:
                        z=input("Invalid choice""\n""Do you want to continue {Y|N}  : ")
                        
            elif(a[1].upper()=="SALES"):
                s='Y'
                while s=='Y' or s=='y':
                    mes="""
                        1.Add Customer Details
                        2.Edit Customer Details
                        3.Sales
                        4.Sales Report
                    """
                    print(mes)
                    x=int(input("Select Your Choice : "))
                    if x==1:
                        print("Add Customer Details")
                        #CUID, NAME, ADD1, ADD2, CITY, PINCODE, MOBILE, GST, EMAIL
                        name=input("Enter name of customer : ")
                        add1=input("Enter addr1 :")
                        add2=input("Enter addr2 :")
                        city=input("Enter city :")
                        pin=input("Enter pincode :")
                        mobile=input("Enter mobile no : ")
                        gst=input("Enter gst :")
                        email=input("Email")                   
                        qry="insert into customers (name,add1,add2,city,pincode,mobile,gst,email) values ('"+name+"','"+add1+"','"+add2+"','"+city+"','"+pin+"','"+mobile+"','"+gst+"','"+email+"');"
                        user(qry)
                    elif x==2:
                        print("Edit Customer Details")
                        id1=input("Enter cuid :")
                        name=input("Enter name of customer : ")
                        add1=input("Enter addr1 :")
                        add2=input("Enter addr2 :")
                        city=input("Enter city :")
                        pin=input("Enter pincode :")
                        mobile=input("Enter mobile no : ")
                        gst=input("Enter gst :")
                        email=input("Email")                   
                        qry="update customers set name='"+name+"',add1='"+add1+"',add2='"+add2+"',city='"+city+"',pincode='"+pin+"',mobile='"+mobile+"',gst='"+gst+"',email='"+email+"' where cuid="+id1
                        user(qry)
                    elif x==3:
                        print("Add Sales")
                             #PNAME,PRICE,QTY,AMT,SGST,CGST,IGST,TOTAL  
                        x=1
                        cart=[]
                        mobile=input("Enter Mobile No : ")
                        sql="SELECT * FROM customers where MOBILE='"+mobile+"'"
                        cus=fetchOneData(sql)
                        if(cus!=None):
                            while x==1:                              
                                pid=input("Enter Product ID :")
                                sql="SELECT PRODUCT.PID,PRODUCT.PNAME,PRODUCT.PRICE,PRODUCT.SGST,PRODUCT.CGST,PRODUCT.IGST,STOCK.QTY from product inner join stock on product.PID=stock.PID where product.PID="+pid
                                product=fetchOneData(sql)
                                print(product)
                                qty=int(input("Enter Qty :"))
                                if(product[6]==0):
                                    print("insufficient quantity")
                                elif(product[6]<qty):
                                    print("stock available :",int(product[6]))
                                    b=input("Do you want the current stock {Y|N} :")
                                    if(b=='Y' or b=='y'):
                                        cart.append(calculateAmount(product,product[6]))
                                else:
                                    cart.append(calculateAmount(product,qty))
                                x=int(input("Enter 1 to Add Product in Cart : "))                              
                            saveSales(cart,cus)
                            billPrint(cart,cus)
                        else:
                            print("Invalid User Details")
                    elif x==4:
                        print("Sales Report")
                        fdate=input("Enter From Date : ")
                        tdate=input("Enter To Date : ")
                        sql="SELECT customers.NAME, sales.BILL, DATE_FORMAT(sales.PDATE,'%d-%m-%Y') as PDATE, sum(PRICE) as PRICE, sum(SGST) as SGST, sum(CGST) as CGST, sum(IGST) as IGST, round(sum(TOTAL),2) as TOTAL FROM sales inner join customers on sales.cuid=customers.cuid where sales.PDATE between '"+fdate+"' and '"+tdate+"' group by sales.BILL order by sales.BILL;"
                        col=('NAME' ,'BILL' ,'PDATE' ,'PRICE' ,'SGST' ,'CGST' ,'IGST' ,'TOTAL')
                        c=fetchAllData(sql,col)
                        
                        sql="select sum(total) from sales where pdate between '"+fdate+"' and '"+tdate+"';"
                        t=fetchOneData(sql)
                        if(t[0]!=None):
                            print("Total amount for the product pruchased is : ",int(t[0]))
                    else:
                        print("Invalid Choice")
                    s=input("Enter Y To Continue Sales : ")
            elif(a[1].upper()=="STOCK"):
                mes="""
                    1.Add Vendors
                    2.Edit Vendor
                    3.Purchase
                    4.Stock Report
                    5.Add Category
                    6.Edit Category
                    7.Add Product
                    8.Edit Product
                    9.Purchase Report
                """
                print(mes)
                ch='y'
                while(ch=='y' or ch=='Y'):
                    x=int(input("Enter the choice : "))            
                    if(x==1):
                        print("Add Vendors")
                        name=input("Enter name of vendor : ")
                        add1=input("Enter addr1 :")
                        add2=input("Enter addr2 :")
                        city=input("Enter city :")
                        pin=input("Enter pincode :")
                        mobile=input("Enter mobile no : ")
                        gst=input("Enter gst :")
                        email=input("Email")                   
                        qry="insert into vendor (name,add1,add2,city,pincode,mobile,gst,email) values ('"+name+"','"+add1+"','"+add2+"','"+city+"','"+pin+"','"+mobile+"','"+gst+"','"+email+"');"
                        user(qry)
                    elif(x==2):
                        print("Edit Vendor")
                        id1=input("Enter vid :")
                        name=input("Enter name of customer : ")
                        add1=input("Enter addr1 :")
                        add2=input("Enter addr2 :")
                        city=input("Enter city :")
                        pin=input("Enter pincode :")
                        mobile=input("Enter mobile no : ")
                        gst=input("Enter gst :")
                        email=input("Email")                   
                        qry="update vendor set name='"+name+"',add1='"+add1+"',add2='"+add2+"',city='"+city+"',pincode='"+pin+"',mobile='"+mobile+"',gst='"+gst+"',email='"+email+"' where vid="+id1
                        user(qry)
                    elif(x==3):
                        print("Purchase")
                        #PUID, VID, PDATE, PID, PRICE, QTY, SGST, CGST, IGST, TOTAL
                        vid=input("Enter vid : ")
                        pid=input("Enter pid : ")
                        price=input("Enter price : ")
                        qty=input("Enter qty : ")
                        sgst=input("Enter sgst : ")
                        cgst=input("Enter cgst : ")
                        igst=input("Enter igst : ")
                        total=str((int(price)*int(qty))+int(sgst)+int(cgst)+int(igst))
                        qry="insert into purchase (VID, PDATE, PID, PRICE, QTY, SGST, CGST, IGST, TOTAL) values ('"+vid+"',now(),'"+pid+"','"+price+"','"+qty+"','"+sgst+"','"+cgst+"','"+igst+"','"+total+"');"
                        user(qry)
                        #SID, PID, QTY
                        sql="select qty from stock where pid='"+pid+"';"
                        p=fetchOneData(sql) 
                        q=str(int(p[0])+int(qty))
                        qry="update stock set qty='"+q+"' where pid="+pid
                        user(qry)
                    elif(x==4):
                        print("Stock Report")
                        sql="select product.pid,product.pname,stock.qty from product inner join stock on product.PID=stock.PID;"
                        col=('PID','PNAME','QTY')
                        fetchAllData(sql,col)                    
                    elif(x==5):
                        print("Add Category")
                        name=input("Add category name : ")
                        qry="insert into category (cname) values ('"+name+"');"
                        user(qry)                     
                    elif(x==6):
                        print("Edit Category")
                        cid=input("Enter cid : ")
                        cname=input("Add category name : ")
                        qry="update category set cname='"+cname+"' where cid="+cid
                        user(qry)                        
                    elif(x==7):
                        print("Add Product")
                        c=input("Enter category :")
                        #PID, PNAME, DES, CID, PRICE, SGST, CGST, IGST                           
                        pname=input("Enter pname : ")
                        des=input("enter des :")                        
                        price=input("Enter price : ")
                        sgst=input("Enter sgst : ")
                        cgst=input("Enter cgst : ")
                        igst=input("Enter igst : ")
                        stock=input("Enter stock : ")
                        sql="select cid from category where cname='"+c+"';"                       
                        cid=fetchOneData(sql)                        
                        #print(cid)                        
                        qry="insert into product (PNAME, DES, CID, PRICE, SGST, CGST, IGST) values ('"+pname+"','"+des+"','"+str(cid[0])+"','"+price+"','"+sgst+"','"+cgst+"','"+igst+"')"                       
                        user(qry)
                        sql="select pid from product where pname='"+pname+"';"                       
                        pid=fetchOneData(sql)   
                        qry="insert into stock (pid,qty) values ('"+str(pid[0])+"','"+stock+"');"
                        user(qry)
                        print("Successfully added")
                    elif(x==8):
                        print("Edit Product")
                        pid=input("Enter pid :")
                        pname=input("Enter pname : ")
                        des=input("enter des :")
                        price=input("Enter price : ")
                        sgst=input("Enter sgst : ")
                        cgst=input("Enter cgst : ")
                        igst=input("Enter igst : ") 
                        qry="update product set PNAME='"+pname+"', DES='"+des+"', CID='"+cid+"', PRICE='"+price+"', SGST='"+sgst+"', CGST='"+cgst+"', IGST='"+igst+"' where pid="+pid
                        user(qry)
                    elif(x==9):
                        print("Purchase Report")
                        fdate=input("Enter From Date : ")
                        tdate=input("Enter To Date : ")
                        #PUID, VID, PDATE, PID, PRICE, QTY, SGST, CGST, IGST, TOTAL
                        sql="SELECT vendor.NAME,purchase.VID, DATE_FORMAT(purchase.PDATE,'%d-%m-%Y') as PDATE, sum(PRICE) as PRICE, sum(SGST) as SGST, sum(CGST) as CGST, sum(IGST) as IGST, round(sum(TOTAL),2) as TOTAL FROM purchase inner join vendor on purchase.vid=vendor.vid where purchase.PDATE between '"+fdate+"' and '"+tdate+"' group by purchase.vid order by purchase.vid;"
                        col=('NAME','VID','PDATE' ,'PRICE' ,'SGST' ,'CGST' ,'IGST' ,'TOTAL')
                        fetchAllData(sql,col)                        
                    else:
                        print("Invalid choice")
                    ch=input("DO you want to continue {Y|N} :")
        else:
            print("Invalid User Details")
          
    ch=input("Are You Sure to Exit : ")


import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="data")
print("Database connecting...........")
#dsn='postgres://tjxiqyivvlzpwk:447243be38855370644e47a96171e5f09638409f8daded3c4f342a6498a60c12@ec2-54-147-107-18.compute-1.amazonaws.com:5432/dfp9fuo2f0cp7l'
mycursor = mydb.cursor()

pnr = 1024

def railresmenu():
    print("--------------------------------------------\nRailway Reservation System\n--------------------------------------------")
    print("1. Train Detail \n2. Reservation of Ticket \n3. Cancellation of Tickets \n4. Display PNR Status \n5. Quit")

    n = int(input("Enter your Choice :"))
    if n == 1:
        traindetail()
    elif n == 2:
        reservation()
    elif n == 3:
        cancel()
    elif n == 4 :
        display()
    elif n == 5:
        exit(0)
    else:
        print("-_- Wrong Choice -_-")

def traindetail():
    print("Train Details")
    ch='y'
    while (ch=='y'):
        l=[]
        name=input("enter train name :")
        l.append(name)
        tnum=int(input("enter train number :"))
        l.append(tnum)
        ac1=int(input("enter number of AC 1 class seats"))
        l.append(ac1)
        ac2=int(input("enter number of AC 2 class seats"))
        l.append(ac2)
        ac3=int(input("enter number of AC 3 class seats"))
        l.append(ac3)
        slp=int(input("enter number of sleeper class seats"))
        l.append(slp)
        train=(l)
        sql="insert into traindetail(tname,tnum,ac1,ac2,ac3,slp)values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,train)
        mydb.commit()
        print("insertion completed")
        print("Do you want to insert more train Detail")
        ch=input("enter yes/no")
        print('\n' *10) 
        print("===================================================================")
    railresmenu()

def reservation():
                global pnr
                l1=[]
                pname=input("enter passenger name=")
                l1.append(pname)
                age=input("enter age of passenger =")
                l1.append(age)
                trainno=input("enter train number")
                l1.append(trainno)
                np=int(input("Enter number of passanger:"))
                l1.append(np)
                print("select a class you would like to travel in")
                print("1.AC FIRST CLASS")
                print("2.AC SECOND CLASS")
                print("3.AC THIRD CLASS")
                print("4.SLEEPER CLASS")
                cp=int(input("Enter your choice:"))
                if(cp==1):
                                amount=np*1000
                                cls='ac1'
                elif(cp==2):
                                amount=np*800
                                cls='ac2'
                elif(cp==3):
                                amount=np*500
                                cls='ac3'
                else:
                                amount=np*350
                                cls='slp'
                l1.append(cls)           
                print("Total amount to be paid:",amount)
                l1.append(amount)
                pnr = pnr+1
                print("PNR Number:",pnr)
                print("status: confirmed")
                sts='conf'
                l1.append(sts)
                l1.append(pnr)
                train1=(l1)
                sql="insert into passengers(pname,age,trainno,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,train1)
                mydb.commit()
                print("insertion completed")
                print("Go back to menu")
                print('\n' *10)                 
                print("===================================================================")
                railresmenu()
               
def cancel():
                print("Ticket cancel window")
                pnr=input("enter PNR for cancellation of Ticket")
                pn=(pnr,) 
                sql="update passengers set status='deleted' where pnrno=%s"
                mycursor.execute(sql,pn)
                mydb.commit()
                print("Deletion completed")
                print("Go back to menu")
                print('\n' *10)                 
                print("===================================================================")
                railresmenu()
def display():
                print("PNR STATUS window")
                pnr=input("enter PNR NUMBER")
                pn=(pnr,) 
                sql="select * from passengers where pnrno=%s"
                mycursor.execute(sql,pn)
                res=mycursor.fetchall() 
                print("PNR STATUS are as follows : ")
                print("(pname,age,trainno, noofpas,cls,amt,status, pnrno)")
                for x in res: print(x)   
                #print("Deletion completed")
                print("Go back to menu")
                print('\n' *10)                 
                print("===================================================================")
                railresmenu()
railresmenu()


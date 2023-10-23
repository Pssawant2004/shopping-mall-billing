print(".                                ******************")
print("                                 * welcom to mall *")
print("                                 ******************\n\n")
def discount(m):
    m=m-(m*10/100)
    print("your total amount after discount is : ",m)
# Enter your username and passward.
a=str(input("Enter user Nmae : "))
b=str(input("enter passward : "))
if(a=="ghrcem" and b=="1234"):
    floor=[' 1. cloths ',' 2. sports ',' 3. food ',' 4.Grocery ',' 5. stationary ',' 6. theatre']
    print("_____________________________________________________________________________________")
    print("\n Following are the floors \n")
    print(floor)
    print("\n\n_____________________________________________________________________________________")

    #this Are the empty list where the amounts of product will get saved
    fp1=[]
    fp2=[]
    fp3=[]
    fp4=[]
    fp5=[]
    fp6=[]
    point=0
    #It is the sum of the elements of in the list respectively
    #  we declar the starting the value to be zero
    ts1=ts2=ts3=ts4=ts5=ts6=0
    
    #this is for in store recursion
    f1=f2=f3=f4=f5=f6=0
    a=0
    
    #from here you start entering in store 
    while(a==0):
         b=int(input("\n enter the floor number  : "))
         
         # CLOTHS SECTION
         if b==1:
             print("                You are entered in cloths section ")
             cl=[' 1. shirt ',' 2. Pant ',' 3.Top ',' 4. leggins ',' 5. kurta ',' 6. saari ']
             print(cl)
             while(f1==0):
                 pn=int(input("\n enter the product number : "))
                 if pn==1:
                     print(" you choose shirt")
                     q1=int(input("Enter quantity of shirts : "))
                     tip1= q1 * 400
                 if pn==2:
                     print(" you choose Pant")
                     q2=int(input("Enter quantity of Pant : "))
                     tip1= q2 * 300
                 if pn==3:
                     print(" you choose Top ")
                     q3=int(input("Enter quantity of Top : "))
                     tip1= q3 * 500
                 if pn==4:
                     print(" you choose leggins")
                     q4=int(input("Enter quantity of leggins : "))
                     tip1= q4 * 250
                 if pn==5:
                     print(" you choose kurta")
                     q5=int(input("Enter quantity of kurta : "))
                     tip1= q5 * 600
                 if pn==6:
                     print(" you choose saari")
                     q1=int(input("Enter quantity of saari : "))
                     tip1= q1 * 450    
                 tip1=tip1+(tip1*5/100)   
                 fp1.append(tip1)
                 point+=10
                 f1=int(input("If yoy want to continue in cloths section press 0 rather 1"))
             print(fp1)
             ts1=sum(fp1)
             print("the total amount is : ",ts1)            
             if(ts1>2000):
                discount(ts1)
             print("\n-----------------------------------------------------------------------------")       
         
         # SPORTS SECTION       
         if b==2:
             print("                     You entered in sports section")
             sl=[' 1. cricket Kit ',' 2. volleyball kit ',' 3. hocky kit ',' 4. badminton kit']
             print(sl)
             while(f2==0):
                 pn2=int(input("\n enter the product number : "))
                 if pn2==1:
                     print(" you choose cricket kit ")
                     q1=int(input("Enter quantity of cricket kit : "))
                     tip2= q1 * 4500
                 if pn2==2:
                     print(" you choose volleyball kit")
                     q2=int(input("Enter quantity of volleyball kit : "))
                     tip2= q2 * 1500
                 if pn2==3:
                     print(" you choose hocky kit ")
                     q3=int(input("Enter quantity of hocky kit : "))
                     tip2= q3 * 3000
                 if pn2==4:
                     print(" you choose badminton kit")
                     q4=int(input("Enter quantity of badminton kit : "))
                     tip2= q4 * 1000
                 tip2=tip2+(tip2*5/100)   
                 fp2.append(tip2)
                 point+=30
                 f2=int(input("If yoy want to continue in sports section press 0 rather 1"))
             print(fp2)
             ts2=sum(fp2)
             print("the total amount is : ",ts2)            
             if(ts2>20000):
                 discount(ts2)
                 
             print("\n-----------------------------------------------------------------------------")            
           #FOOD SECTION       
         if b==3:
             print("                            You entered in food section")
             fl=[' 1. pizza ',' 2. burger ',' 3. sandwich ',' 4. biryani ',' 5. maharashtra thali ']
             print(fl)
             while(f3==0):
                 pn3=int(input("\n enter the product number : "))
                 if pn3==1:
                     print(" you choose Pizza ")
                     q1=int(input("Enter quantity of pizza : "))
                     tip3= q1 * 300
                 if pn3==2:
                     print(" you choose burger")
                     q2=int(input("Enter quantity of burger : "))
                     tip3= q2 * 150
                 if pn3==3:
                     print(" you choose sandwich ")
                     q3=int(input("Enter quantity of sandwich : "))
                     tip3= q3 * 200
                 if pn3==4:
                     print(" you choose biryani")
                     q4=int(input("Enter quantity of biryani : "))
                     tip3= q4 * 200
                 if pn3==5:
                     print(" you choose sandwich ")
                     q3=int(input("Enter quantity of Maharashtra Thali : "))
                     tip3= q3 * 250   
                 tip3=tip3+(tip3*5/100)   
                 fp3.append(tip3)
                 point+=5
                 f3=int(input("If yoy want to continue in food section press 0 rather 1"))
             print(fp3)
             ts3=sum(fp3)
             print("the total amount is : ",ts3)            
             if(ts3>750):
                 discount(ts3)
         
             print("\n-----------------------------------------------------------------------------")    
         # GROCARY SECTION
         if b==4:
             print("                          You entered in grocary section")
             Gl=[' 1. sugar ',' 2. salt ',' 3. oil ',' 4. tea powder ',' 5.Rice ',' 6. soap']
             print(Gl)
             while(f4==0):
                 pn4=int(input("\n enter the product number : "))
                 if pn4==1:
                     print(" you choose sugar ")
                     q1=int(input("Enter quantity of sugar in Kg : "))
                     tip4= q1 * 35
                 if pn4==2:
                     print(" you choose salt")
                     q2=int(input("Enter quantity of salt in Kg : "))
                     tip4= q2 * 15
                 if pn4==3:
                     print(" you choose oil ")
                     q3=int(input("Enter quantity of oil in liter : "))
                     tip4= q3 * 200
                 if pn4==4:
                     print(" you choose tea powder")
                     q4=int(input("Enter quantity of tea power in kg : "))
                     tip4= q4 * 80
                 if pn4==5:
                     print(" you choose rice")
                     q4=int(input("Enter quantity of rice in kg : "))
                     tip4= q4 * 50   
                 if pn4==6:
                     print(" you choose soap")
                     q4=int(input("Enter quantity of soap : "))
                     tip4= q4 * 25   
                 tip4=tip4+(tip4*5/100)   
                 fp4.append(tip4)
                 point+=6
                 f4=int(input("If yoy want to continue in grocary section press 0 rather 1"))
             print(fp4)
             ts4=sum(fp4)
             print("the total amount is : ",ts4)            
             if(ts4>1000):
                 discount(ts4)
                 
                 print("\n-----------------------------------------------------------------------------")           
            #STATIONARY SECTION     
         if b==5:
             print("                       You entered in stationary section")
             stl=[' 1. notebooks ',' 2. compos box ',' 3. pen ',' 4. study table ',' 5.writing pad ']
             print(stl)
             while(f5==0):
                 pn5=int(input("\n enter the product number : "))
                 if pn5==1:
                     print(" you choose Notebook ")
                     q1=int(input("Enter quantity of Notebook : "))
                     tip5= q1 * 70
                 if pn5==2:
                     print(" you choose compos box")
                     q2=int(input("Enter quantity of compos box : "))
                     tip5= q2 * 200
                 if pn5==3:
                     print(" you choose pen ")
                     q3=int(input("Enter quantity of Pen : "))
                     tip5= q3 * 10
                 if pn5==4:
                     print(" you choose study table")
                     q4=int(input("Enter quantity of tea study table : "))
                     tip5= q4 * 900
                 if pn5==5:
                     print(" you choose writing pad")
                     q4=int(input("Enter quantity of writing pad : "))
                     tip5= q4 * 200   
                 tip5=tip5+(tip5*5/100)   
                 fp5.append(tip5)
                 point+=10
                 f5=int(input("If yoy want to continue in stationary section press 0 rather 1"))
             print(fp5)
             ts5=sum(fp5)
             print("the total amount is : ",ts5)            
             if(ts5>750):
                 discount(ts5)
        
                 print("\n-----------------------------------------------------------------------------")    
            #THEATER SECTION 
         if b==6:
             print("                         You entered in theatre section") 
             ml=[' 1. Fast and Furious 10 ',' 2. the kerla story ',' 3. IB71 ',' 4. 2018 ',' 5. evil dead rise ']
             print(ml)
             pn6=int(input("\n enter the product number : "))
             while(f6==0):
                 if pn6==1:
                     print(" you choose Fast and Furious 10 ")
                     q1=int(input("Enter quantity of Fast and Furious 10 tickets : "))
                     tip6= q1 * 350
                 if pn6==2:
                     print(" you choose the kerla story")
                     q2=int(input("Enter quantity of the kerla story tickets : "))
                     tip6= q2 * 280
                 if pn6==3:
                     print(" you choose IB71 ")
                     q3=int(input("Enter quantity of IB71 tickets : "))
                     tip6= q3 * 180
                 if pn6==4:
                     print(" you choose 2018")
                     q4=int(input("Enter quantity of 2018 tickets : "))
                     tip6= q4 * 180
                 if pn6==5:
                     print(" you choose Evil dead rise")
                     q4=int(input("Enter quantity of evil dead rise tickets : "))
                     tip6= q4 * 200   
                 tip6=tip6+(tip6*5/100)
                 fp6.append(tip6)
                 point+=40
                 f6=int(input("If yoy want to buy more tickrts then press 0 rather 1"))
             print(fp6)
             ts6=sum(fp6)             
             print("the total amount is : ",tip6) 
             print("\n-----------------------------------------------------------------------------")  
         a=int(input("\n If you want to continue shopping then press 0 rather press 1 : "))
            
         #YOUR TOTAL SPEND AMOUNT
    tat= ts1 + ts2 + ts3 + ts4 + ts5 + ts6
    print("\n  Today you spend total amount of rs.",tat)
  
    #Your total points are
    print("\n  Today your earning of points are :",point)
    print("\n\n                       =====================")
    print("                     ||    Have a good day    ||")
    print("                       =====================")
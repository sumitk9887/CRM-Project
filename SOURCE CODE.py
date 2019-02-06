print"                  w         w     eeeeeeeeee     ll                 cccccc         ooooo          mm       mm     eeeeeeeeee   "
print"                  w         w     e              ll               cc             oo     oo        m  m   m  m     e            "
print"                  w         w     e              ll             cc             oo         oo      m   m m   m     e            "
print"                  w    w    w     eeeeeeeee      ll            cc             oo           oo     m    m    m     eeeeeeeee    "
print"                  w   w  w  w     e              ll             cc             oo         oo      m         m     e            "
print"                  w  w    w w     e              ll               cc             oo     oo        m         m     e            "
print"                  ww       ww     eeeeeeeeee     lllllllllll        cccccc         ooooo          m         m     eeeeeeeeee   "
print
print
print"                                                          tttttttttttt          ooooo                                          "
print"                                                               tt             oo     oo                                        "
print"                                                               tt           oo         oo                                      "
print"                                                               tt          oo           oo                                     "
print"                                                               tt           oo         oo                                      "
print"                                                               tt             oo     oo                                        "
print"                                                               tt               ooooo                                          "
print
print"               ================================================================================================================"
print
print"                   v     v     gggggg                                                                                          "
print"                    v   v     g                                                                                                "
print"                     v v      g  gggg                                                                                          "
print"                      v        gggg g   PORTAL                                                                                 "
print"                                                                                             ....SERVICE AT YOUR DOORSTEP....  "
print
print"               ================================================================================================================"
print"                   E-mail  : https://vgservice.co.in/                                          Phone : 011-78496875     "
print"                                                                                               FAX   : +1 323 555 1234  "               
print
print"                   Address : Plot No 296, Udyog Vihar Industrial Area Phase 2, Gurgaon - 122016                         "
print
print"               ================================================================================================================"
print

import os
import pickle

#SIGN UP
    
class signup:
    def __init__(self):
        self.username=" "
        self.password=" "
        self.email=" "
        self.phone=" "

    #Stores Details of the user.
        
    def signin(self):
        self.username=raw_input("Select your id  ")
        print
        self.password=raw_input("Choose Your Password  ")
        print
        self.email=raw_input("Enter Your Email ID  ")
        print
        self.phone=int(raw_input("Enter Your Phone Number  "))
        print
        
    def printl(self):
        print self.username
        print self.password
        print self.email
        print self.phone



#REGISTER

class register:
    def __init__(self):

        self.complain=" "
        self.name=" "
        self.adress=" "
        self.mobile=0
        self.product=" "
        self.model=" "
        self.dop=" "
        self.status=" "
        
    def getdata(self):
        #Stores Complain number.
        self.complain=raw_input("Enter complain number  ")          
        print
        #Stores Customer name.
        self.name=raw_input("Enter Customer Name  ")                
        print
        #Stores Customer adress.
        self.adress=raw_input("Enter Customer Adress  ")            
        print
        #Stores Customer mobile number.
        self.mobile=int(raw_input("Enter Customer Mobile no.  "))   
        print
        #Stores Product.
        self.product=raw_input("Enter Product  ")                   
        print
        #Stores model. 
        self.model=raw_input("Enter model  ")                       
        print
        #Stores Date Of Purchase.
        self.dop=raw_input("Enter Date Of Purchase  ")              
        print
        #Stores Current Status
        self.status=raw_input("Enter Current Status ")
        print


    #Print The entered details
        
    def showdata(self):
        print "Complain Number""\t\t\t |  ",self.complain
        print
        print "Customer Name""\t\t\t |  ",self.name
        print
        print "Customer Adress""\t\t\t |  ",self.adress
        print
        print "Customer Mobile Number""\t\t |  ",self.mobile
        print
        print "Product""\t\t\t\t |  ",self.product
        print
        print "Model Number""\t\t\t |  ",self.model
        print
        print "Date of purchase""\t\t |  ",self.dop
        print
        print "Current Status""\t\t\t |  ",self.status
        



                

#MAIN PROGRAM
           
#Importing the time module                    
from datetime import datetime
import time            

p="true"
while p=="true":
    
    #Main Menu
    
    print
    print"\t\t\t\t\t\t\t\t    MAIN MENU"
    print
    print
    print"\t\t\t\t\t\t\t\tPress 1 for Login"
    print"\t\t\t\t\t\t\t\tPress 2 for SignUp"
    print"\t\t\t\t\t\t\t\tPress 3 for Exit"
    print
    print
    
    ch=int(raw_input("Enter your choice  "))
    print
    print
    if ch==1:
        
        #Calling the login class.
        s=signup()
        a=raw_input("Enter ID  ")
        f=open("binary.dat","rb+")
        try:
            while True:
                s=pickle.load(f)
                if a==s.username:
                    print
                    b=raw_input("Enter the password ") #Asking For Password
                    
                    if b==s.password:
                        #Both Id and Password is correct then
                        

                        print"\t\t\t\t\t\t\t\tLogin sucessfully"
                        print
                        print
                        raw_input("\t\t\t\t\t\t\t\tPress Enter to continue..")
                        print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\tLOADING.",
                        time.sleep(1)       
                        print ("."),
                        time.sleep(1)
                        print ("."),
                        time.sleep(1)
                        print ("."),
                        time.sleep(1)
                        print (".")
                        time.sleep(1)
                        print
                        print
                        h="true"
                        while h=="true":   
                            print
                            print
                            print"\t\t\t\t\t\t\t\tEnter 1 To Register a Complain"
                            print
                            print"\t\t\t\t\t\t\t\tEnter 2 To Update the Complain"
                            print
                            print"\t\t\t\t\t\t\t\tEnter 3 To Search For Details Of a Complain"
                            print
                            print"\t\t\t\t\t\t\t\tEnter 4 To Update Complain Status"
                            print
                            print"\t\t\t\t\t\t\t\tEnter 5 To Exit"
                            print
                            print
                            op=int(raw_input("Enter Your Choice ")) #Asking For The User Choice
                            print
                            time.sleep(1)
                            if op==1:
                            
                            #To Register
        
                                r=register()
                                i="work"
                                while i=="work":
                                
                                    r=register()    #Object Of Register Class
                                    r.getdata()     #Calling getdata() Function of Register Class
                                    f1=open("register.dat","ab+")
                                    pickle.dump(r,f1)
                                    f1.close()

                                    print "Complain Has Been Sucessfully Registered"
                                    print

                                    #Printing The Summary
                                    
                                    raw_input("\t\t\t\t\t\t\t\tPress Enter For The Summary")
                                    print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\tLOADING.",
                                    time.sleep(1)
                                    print ("."),
                                    time.sleep(1)
                                    print ("."),
                                    time.sleep(1)
                                    print ("."),
                                    time.sleep(1)
                                    print
                                    f1=open("register.dat","rb+")
                                    try:
                                        r=pickle.load(f1)
                                        r.showdata()
                                        print
                                        print"Registered Date and Time is:"
                                        
                                        #Print the current date and time
                                        
                                        print  datetime.now().strftime('%Y-%m-%d %H:%M:%S')     
                                    except EOFError:
                                        f1.close()

                                
                                    print"\t\t\t\t\t\t\t\tEnter 1 Reguster A New Call"
                                    print
                                    print"\t\t\t\t\t\t\t\tEnter 2 Go Back To The Menu"
                                    print
                                    z=int(raw_input("Enter your choice "))
                                    if z==1:                            
                                        pass
                                    else:
                                        i="stop"
                            elif op==2:

                                #Updating The Details
                                
                                l="true"
                                while l=="true":
                                    try:
                                        i="true"
                                        while i=="true":
                                            r=register()
                                            file2=open("new register.dat","ab+")
                                            x=raw_input("Enter Complain Number To Update Details  ")
                                            file1=open("register.dat","rb+")
                                            r=pickle.load(file1)
                                            if r.complain==x:
                                                print                                        
                                                print "\t\t\t\t\t\t\t\t What You Want To Update"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 1 For Complain Number"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 2 For Customer Name"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 3 For Customer Address "
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 4 For Customer Mobile Number"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 5 For Product is"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 6 For Model Number"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 7 For Date of purchase"
                                                print
                                        
                                                ch=int(raw_input("Enter Your Choice  "))

                                                #Updating Complain Number
                                                
                                                if ch==1:
                                                    val=raw_input("Enter New Complain Number  ")
                                                    r.complain=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"

                                                #Updating Customer Name
                                                    
                                                elif ch==2:
                                                    val=raw_input("Enter New Customer Name  ")
                                                    r.name=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"

                                                #Updating Customer Address
                                                    
                                                elif ch==3:
                                                    val=raw_input("Enter New Customer Address  ")
                                                    r.adress=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"
                              

                                                #Updating Customer Mobile no.
                                                    
                                                elif ch==4:
                                                    val=raw_input("Enter New Customer Mobile no.  ")
                                                    r.mobile=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"
                                                #Updating Product
                                                    
                                                elif ch==5:
                                                    val=raw_input("Enter New Product  ")
                                                    r.product=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"

                                                #Updating Model
                                                    
                                                elif ch==6:
                                                    val=raw_input("Enter New Model  ")
                                                    r.model=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"

                                                #Updating Date Of Purchase
                                                    
                                                elif ch==7:
                                                    val=raw_input("Enter New Date Of Purchase  ")
                                                    r.dop=val
                                                    pickle.dump(r,file2)
                                                    file2.close()
                                                    file1.close()
                                                    z="in"

                                                else:
                                                    file2.close()
                                                    file1.close()
                                                    z="out"
                                                    print"Incorrect Choice Please Choose A Valid option"

                                                if z=="in":
                                                    
                                                    os.remove("register.dat")
                                                    os.rename("new register.dat","register.dat")
                                                    file2=open("register.dat","rb")
                                                    try:
                                                        r=pickle.load(file2)
                                                        print
                                                        print
                                                        print
                                                        raw_input("\t\t\t\t\t\t\t\tPress Enter To See The Details After Upgradation ")
                                                        print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tLOADING.",
                                                        time.sleep(1)
                                                        print ("."),
                                                        time.sleep(1)
                                                        print ("."),
                                                        time.sleep(1)
                                                        print ("."),
                                                        time.sleep(1)
                                                        print (".")
                                                        time.sleep(1)
                                                        print
                                                        print
                                                        r.showdata()
                                                    except EOFError:
                                                        file2.close()
                                                        
                                                print
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 1 To Cotinue Updating"
                                                print
                                                print "\t\t\t\t\t\t\t\tEnter 2 To Go Back To The Main Menu"
                                                print
                                                print 
                                                choice=int(raw_input("Enter Your Choice  "))
                                                if choice==1:
                                                    pass
                                                elif choice==2:
                                                    i="fasle"
                                                    l="false"
                                                else:
                                                    print " Wrong option"
                                            else:
                                                #If The Complain Number Is Not Registered
                                                
                                                print"\t\t\t\t\t\t\t\tComplain Number Is not valid,Please Choose A Valid Complain Number To Update Details" 
                                                print
                                                print"\t\t\t\t\t\t\t\tEnter 1 To Re-enter"
                                                print
                                                print"\t\t\t\t\t\t\t\tEnter 2 To Exit"
                                                luck=int(raw_input("Enter Your Choice  "))
                                                if luck==1:
                                                    pass
                                                else:
                                                    i="false"
                                                    l="false"
                                    except EOFError:
                                        file1.close()

                            #Searching For Details
                                        
                            elif op==3:
                                f2=open("register.dat","rb+")
                                complain=raw_input("Enter Complain Number To Search Details  ")
                                try:
                                    r=register()
                                    r=pickle.load(f2)
                                    if complain==r.complain:
                                        try:
                                            r.showdata()
                                            
                                            raw_input("\t\t\t\t\t\t\t\tPress Enter To Continue..")
                                            print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tLOADING.",
                                            time.sleep(1)
                                            print ("."),
                                            time.sleep(1)
                                            print ("."),
                                            time.sleep(1)
                                            print ("."),
                                            time.sleep(1)
                                            print (".")
                                            time.sleep(1)
                                            print
                                            print
      
                                        except EOFError:
                                            f2.close()
                                except:
                                    pass

                            #Cancelling The Complain
                            elif op==4:
                                
                                try:
                                                          
                                    r=register()
                                    file2=open("new register.dat","ab+")
                                    x=raw_input("Enter Complain Number To Update Status of  ")
                                    file1=open("register.dat","rb+")
                                    r=pickle.load(file1)
                                    if r.complain==x:
                                        val=raw_input("Enter Current Status  ")
                                        r.status=val
                                        pickle.dump(r,file2)
                                        file2.close()
                                        file1.close()
                                        print 
                                        print"\t\t\t\t\t\t\t\tStatus Updated Sucessfully"
                                        print

                                        #Renaming The Files
                                               
                                        os.remove("register.dat")
                                        os.rename("new register.dat","register.dat")
                                        file2.close()
                                except EOFError:
                                    
                                    pass            

                            elif op==5:
                                h="false"
  

                    else:
                        print"\t\t\t\t\t\t\t\tIncorrect Password"
                else:
                    print"ID Is Not Registered,Kindly Register First"
        except EOFError:
            
            f.close()
    elif ch==2:

        #SignUp
        
        s=signup()
        print "\t\t\t\t\t\t\t\tWelcome to the Sign Up page"
        print
        raw_input("\t\t\t\t\t\t\t\tPress Enter To Continue..")
        print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tLOADING.",
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print ("."),
        time.sleep(1)
        print (".")
        time.sleep(1)
        print
        print
        s=signup()
        s.signin()
        f=open("binary.dat","ab+")
        pickle.dump(s,f)
        f.close()
    
        print "\t\t\t\t\t\t\t\tYou Are Sucessfully Registered,Kindly LOGIN"
        print
        raw_input("\t\t\t\t\t\t\t\tPress Enter To Go To Main Menu ")
    elif ch==3:
        exit()

    else:
        print"Incorrect Option"

#==================================FUNCTIONS====================================

#===============
def func1():
    a = str(input("Enter 1 or 2 : "))
    if a == "1" :
        state = "lost phone search"
        ##print("you have entered", a,"i.e.", state)
        err1 = False
        proceed(state)
    elif a == "2":
        state = "buy new phone"
        ##print("you have entered", a,"i.e.", state)
        err1 = False
        proceed(state)
    else :
        print("please enter only '1' or '2'")
        func1()
#===============
def proceed(x):
    ##print(x,": STATEEEEEEEEE")
    print("Before going further we would need to know you.Please enter the details mentioned below.")
    
    if err2 == True :
        name = input("Your Name : ")
        adres = input("Address : ")
        mb_no = str(input("Your Alternate Mobile Number : "))
    if len(str(mb_no)) !=10:
        print("please enter a valid mobile number")
        mb_no = reproceed()
        #mb_no = reproceed()
    ##print(x)
    if x == "lost phone search" :
        ##print(mb_no)
        lostPhone(name)
    else :
        #mb_no = reproceed()
        ##print(mb_no)
        newPhone(name)
       
#===============
def reproceed():
    wow = 0
    x = None
    x = str(input("Your Alternate Mobile Number : "))
    if len(x) !=10:
        print("please enter a valid mobile number")
        reproceed()
    elif len(x) == 10 :
        #for i in x:
        #    print(i)
        #    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' :
        #        #return int(x)
        #       wow +=1
        #    else :
        #        print("Please enter INTEGERS ONLY")
        #        x = None
        #        reproceed()
        #if wow == 10 :
        return int(x)
    else :
        return 0000000000
#===============
def lostPhone(name):
    ##print("Lost Phone")
    print("Select what you want to do next")
    print("1. regain info [type 1]")
    print("2. track location [type 2]")
    print("3. ring [type 3]")
    print("4. Back up all info & erase all data [type 4]")
    print("5. unlock your device [type 5]")
    y = int(input())

    if y == 1 :
        print("The request has been sent, your info will be stored to your samsung account cloud")
    elif y == 2 :
        print(name , "your phone was ast detected at Pathan chowk near Chuna Bhatti Road at 4:41 AM Jan 31st")
    elif y == 3 :
        print(name , "your phone will ring for 1 minute even if it is on DnD or Silent mode.")
    elif y == 4 :
        print(name , "your device is currently not connected to a network, try again later")
    elif y == 5 :
        print(name , "your device is now unlocked.")
#===============
def newPhone(name):
    print("Sorry", name,"we are out of stock right now. We will soon be back with greater deals and discounts.")
    
#=============================================================================

#intitiallise code...
print("Welcome to the Phone finding agency")
print("How would you like us to help you?")
print("Search for my lost phone (1)")
print("Buy a new phone (2)")
state = "" 
err1 = True
err2 = True
name = None
adres = None
mb_no = None
y = None
func1()

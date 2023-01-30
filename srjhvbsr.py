
#==================================FUNCTIONS====================================

#===============
def func1():
    a = str(input("Enter 1 or 2 : "))
    if a == "1" :
        state = "lost phone search"
        print("you have entered", a)
        err1 = False
        proceed()
    elif a == "2":
        state = "buy new phone"
        print("you have entered", a)
        err1 = False
        proceed()
    else :
        print("please enter only '1' or '2'")
        func1()
#===============
def proceed():
    print("Before going further we would need to know you.Please enter the details mentioned below.")
    
    if err2 == True :
        name = input("Your Name : ")
        adres = input("Address : ")
        mb_no = str(input("Your Alternate Mobile Number : "))
    if len(str(mb_no)) !=10:
        
        print("please enter a valid mobile number")
        mb_no = reproceed()
        mb_no = reproceed()
    if state == "lost phone search" :
        
        print(mb_no)
        lostPhone()
    else :
        #mb_no = reproceed()
        print(mb_no)
        newPhone()
       
#===============
def reproceed():
    x = None
    x = int(input("Your Alternate Mobile Number x: "))
    if len(str(x)) !=10:
        print("please enter a valid mobile number")
        reproceed()
    return x
#===============
def lostPhone():
    print("Lost Phone")
#===============
def newPhone():
    print("New Phone")
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
func1()

    
    



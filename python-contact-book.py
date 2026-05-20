# Welcome to Contact Book
# Practice Project for Python Dictionaries and Modular programming using Functions
print("-----------------------------------------")
print("         WELCOME TO CONTACTS             ")
print("-----------------------------------------")

contact = {} #Empty Dictionary where contacts will be stored

def menu(): # Menu Module
    print("----------------")
    print("      MENU      ")
    print("----------------")
    print()
    print("1. ADD CONTACT")
    print("2. VIEW CONTACTS")
    print("3. SEARCH CONTACT")
    print("4. DELETE CONTACT")
    print("5. EXIT")
    print()
    choice = int(input("Enter Your Choice: "))
    if choice ==1:
        func1()
    elif choice ==2:
        func2()
    elif choice ==3:
        func3()
    elif choice ==4:
        func4()
    else: # Exit 
        print()
        print("----------------------------")
        print("THANK YOU FOR USING CONTACTS")
        print("----------------------------")
        exit()
    
def func1(): # Add new contacts module
    print()
    print()
    print("------------")
    print("NEW CONTACT:")
    print("------------")
    print()
    name = input("Enter Name: ")
    print()
    num = int(input("Emter Contact Number: "))
    print()
    contact[name]=num
    print("----------------------------------")
    print(f"Contact {name} Saved Successfully")
    print("----------------------------------")
    print()
    print()
    menu()

def func2(): # View all contacts module
    print()
    print()
    print("-------------------")
    print("ALL SAVED CONTACTS: ")
    print("-------------------")
    for name in contact:
        print()
        print(f"{name} ----- {contact[name]}")
        print("-------------------------------")
    print()
    print()
    menu()

def func3(): # Search contacts module
    print()
    print()
    print("----------------")
    print("CONTACT SEARCH:")
    print("----------------")
    print()
    name = input("Enter Name To Search: ")
    if name in contact:
        print()
        print("-------------")
        print("Contact Found")
        print("-------------")
        print()
        print("-----------------------------")
        print(f"{name} ----- {contact[name]}")
        print("-----------------------------")
    else:
        print()
        print("-----------------")
        print("Contact Not Found")
        print("-----------------")
    print()
    print()
    menu()
        

def func4(): # Delete contacts module
    print()
    print()
    print("---------------")
    print("DELETE CONTACT:")
    print("---------------")
    print()
    name = input("Enter Name of Contact to be Deleted: ")
    if name in contact:
        del contact[name]
        print()
        print("----------------------------")
        print("Contact Deleted Successfully")
        print("----------------------------")
    else:
        print()
        print("----------------------")
        print("Contact Does Not Exist")
        print("----------------------")
    print()
    print()
    menu()
    
    
menu()
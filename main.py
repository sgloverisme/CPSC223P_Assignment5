from contacts import * 
import json
contacts = Contacts(filename = 'c.dat')

while True:
    print("*** TUFFY TITAN CONTACT MAIN MENU")
    print()
    print("1. Add contact\n")
    print("2. Modify contact\n")
    print("3. Delete contact\n")
    print("4. Print contact list\n")
    print("5. Set contact filename\n")
    print("6. Exit the program\n")
    print()

    choice=int(input("Enter menu choice: "))
    print()

    if choice == 1: #----------------Adding Contacts 
        i =input("Enter Phone Number: ")
        fn = input("Enter First Name: ")
        ln= input("Enter the Last Name: ")
        r=contacts.add_contact(id=i, first_name=fn, last_name=ln)
        if r=="error" :
            print("Phone Number already exists")
        else:
            contacts.sort_contacts()
            print("Added: " + r[0] + " " + r[1] + ".")
        print()
    elif choice==2: #-----------------modifying contacts
        i =input("Enter Phone Number: ")
        fn = input("Enter First Name: ")
        ln= input("Enter the Last Name: ")
        r=contacts.modify_contact(id=i, first_name=fn, last_name=ln)
        if r=="error" :
            print("Phone Number does not exists")
        else:
            print("Modfied: " + r[0] + " " + r[1] + ".")
        print()
    elif choice==3: #----------------deleting contact
        i =input("Enter Phone Number: ")
        r=contacts.delete_contact(id=i)
        if r=="error" :
            print("Invalid Phone Number")
        else:
            print("Deleted: " + r[0] + " " + r[1] + ".")
        print()
    elif choice==4: #----------------Printing contact list
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for key in contacts.data:
            print(f'{contacts.data[key][1]} 22{contacts.data[key][0]:22} {key:12}')
        print()
    elif choice==5: #--------------save filename
        fn= input("Enter new filename: ")
        contacts = Contacts(filename=fn)
        print()
    elif choice ==6: #--------------------exit program 
        break
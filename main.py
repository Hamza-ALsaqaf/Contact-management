from ContactModule import *

# Create an instance of ContactManager
contactmanager=ContactManager()
while True:
    choice =  input("\n\nContact Manager\n1.Add Contact\n2.Remove Contact.\n3.Search Contact \n4.Display Contact\n5.Exit\nEnter your Choice:\n\n")
    if choice == "1":
        # Add contact
        name=input("Enter Name: ")
        phone=input("Enter Phone Number: ")
        email=input("Enter Email Address: ")
        contact=Contact(name,phone,email)
        contactmanager.add_contact(contact)
        
    elif choice == "2":
        # Remove contact
        name=input("Enter Name of Contact That Want to Remove it: ")
        contactmanager.remove_contact(name)
    elif choice == "3":
        # Search contact
        name=input("Enter Name of Contact That Want to search it: ")
        contactmanager.search(name)
        
    elif choice == "4":
        # Display contacts
        contactmanager.display_contacts()
        
    elif choice == "5":
        # Exit the program
        break
    
    else :
        print("Error try again")


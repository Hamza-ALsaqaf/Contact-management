class Contact :
    def __init__(self,name,phone,email) -> None:
        # Constructor method to initialize Contact object
        self.name=name 
        self.phone=phone 
        self.email=email
    def __str__(self) -> str:
        # String representation of Contact object
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    def __init__(self) -> None:
        # Constructor method to initialize ContactManager object
        self.contactslist=[]
    
    def add_contact(self,contact):
        # Method to add a contact to the contact list
        self.contactslist.append(contact)
    
    def search(self,name):
        # Method to search for a contact by name
        if len(self.contactslist)!=0:
            for contact in self.contactslist:
                if contact.name.upper()==name.upper():
                    return contact
        else:
            #not found
            return None
    def remove_contact(self,name):
        # Method to remove a contact by name
        foundContact=self.search(name)
        if foundContact!=None:
            self.contactslist.remove(foundContact)
        else:
            #not found
            return None
    def display_contacts(self):
        # Method to display all contacts
        if len(self.contactslist)!=0:
            for contact in self.contactslist:
                print(contact)
                print("-"*50)
        else:
            #contact list is Empty
            print("No contacts found")








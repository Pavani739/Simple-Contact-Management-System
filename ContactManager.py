class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        self.contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.\n")
            return
        print("Contact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
        print()

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            self.contacts[name] = {"Phone": phone, "Email": email}
            print(f"Contact '{name}' updated successfully!\n")
        else:
            print("Contact not found.\n")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!\n")
        else:
            print("Contact not found.\n")

    def run(self):
        while True:
            print("\nContact Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.update_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    ContactManager().run()

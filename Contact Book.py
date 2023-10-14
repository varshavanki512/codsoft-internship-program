class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print
            (f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        matching_contacts = []
        for contact in self.contacts:
            query_lower = query.lower()
            contact_info = contact.name.lower() + contact.phone_number

            if query_lower in contact_info:
                matching_contacts.append(contact)
        return matching_contacts

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                break

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                break


def main():
    contact_manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully!")
        elif choice == '2':
            contact_manager.view_contact_list()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            matching_contacts = contact_manager.search_contact(query)
            if matching_contacts:
                print("\nMatching Contacts:")
                for idx, contact in enumerate(matching_contacts, start=1):
                    print
                (f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact
            (new_name, new_phone_number, new_email, new_address)
            contact_manager.update_contact(name, new_contact)
            print("Contact updated successfully!")
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
            print("Contact deleted successfully!")
        elif choice == '6':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

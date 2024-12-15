contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if contact['name'] == search_term or contact['phone'] == search_term]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if contact['name'] == search_term or contact['phone'] == search_term:
            print("Enter new details (leave blank to keep current value):")
            name = input(f"Enter new name [{contact['name']}]:") or contact['name']
            phone =input(f"Enter new phone number [{contact['phone']}]:") or contact['phone']
            email = input(f"Enter new email [{contact['email']}]: ") or contact['email']
            address = input(f"Enter new address [{contact['address']}]: ") or contact['address']
            contact.update({'name': name, 'phone': phone, 'email': email, 'address': address})
            print("Contact updated successfully.")
            return
        print("Contact not found.")

def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    global contacts
    contacts = [contact for contact in contacts if not (contact['name'] == search_term or contact['phone'] == search_term)]
    print("Contact delete successfully.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
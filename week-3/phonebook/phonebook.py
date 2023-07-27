phonebook = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print("Error: Contact already exists.")
    else:
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added.")

def delete_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Error: Contact not found.")

def search_contact():
    name = input("Enter contact name: ")
    if name in phonebook:
        print(f"Phone number: {phonebook[name]}")
    else:
        print("Error: Contact not found.")

def print_contacts():
    for name, number in phonebook.items():
        print(f"{name}: {number}")

while True:
    print("\nPhonebook")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. Print all contacts")
    print("5. Quit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print_contacts()
    elif choice == '5':
        break

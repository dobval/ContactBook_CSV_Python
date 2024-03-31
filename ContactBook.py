import csv  # For CSV files

# blank contacts list
contacts = []
# field names for contact dictionary
field_names = [
    "Name",
    "Phone",
    "Email",
    "Company",
    "Other Phone",
    "Melody",
    "Group",
]  # TO DO: ADD OPTIONS


def display_menu():
    print("Contact Book Menu")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. Import CSV")
    print("0. Exit (Autoexport)")


def add_contact():
    contact = {}  # new dictionary for each contact
    for field in field_names:
        y = input("{}: ".format(field))
        contact.update({field: y})
    contacts.append(contact)
    print("Contact added successfully!")


def search_contact():
    search_term = input("Enter the name/phone/email of the contact to search: ")
    found_contacts = []
    for contact in contacts:
        if (
            search_term.lower() in contact["Name"].lower()
            or search_term.lower() in contact["Phone"].lower()
            or search_term.lower() in contact["Email"].lower()
        ):
            found_contacts.append(contact)

    if found_contacts:
        print("Matching contacts found:")
        for contact in found_contacts:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("-------------------")
    else:
        print("No matching contacts found.")


def update_contact():
    name = input("Enter the name of the contact to update: ")
    found_contact = None
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            found_contact = contact
            break

    if found_contact:
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name: ")
        found_contact["Phone"] = input("Enter the new phone number: ")
        found_contact["Email"] = input("Enter the new email: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.")


def display_all_contacts():
    if contacts:
        print("All Contacts:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


def list_groups():
    unique_groups = set()
    if contacts:
        for contact in contacts:
            group = contact.get("group", "Other")
        print("Contact Groups: ")
        for group in unique_groups:
            print(group)


def export_to_file():
    with open("ContactsExport.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(contacts)


def import_from_file():
    try:
        with open("ContactsExport.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(row)
    except Exception as errorname:
        print(errorname)
        print("Your CSV file should be named ContactsExport.csv")


# Main program loop
while True:
    display_menu()
    choice = input(
        "Enter your choice (1-6): "
    )  # SHOULD BE INPUT (CHANGED ONLY FOR FDIBA PCs, PYTHON 2.7)

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        import_from_file()
    elif choice == "0":
        print("Exiting the program...")
        export_to_file()
        break
    else:
        print("Invalid choice. Please enter a valid option.")

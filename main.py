list_contact = [
    {
        "nik": "1234567890", 
        "name": "John Doe",
        "phone": "555-1234"
        
    },
    {
        "nik": "0987654321", 
        "name": "Aane Smith",
        "phone": "555-5678"
    }
]

def create_contact():
    nik = input("Enter contact NIK: ")
    name = input("Enter contact name: ").title()
    phone = input("Enter contact phone number: ")
    contact = {
        "nik": nik, 
        "name": name, 
        "phone": phone
    }
    list_contact.append(contact)
    print("Contact added successfully.")
    
def contact_table():
    sorted_contacts = sorted(list_contact, key=lambda x: x['name'])
    print(f"\n{'NIK':<10} | {'Name':<20} | {'Phone':<15}")
    print("-" * 50)
    
    for contact in sorted_contacts:
        print(f"{contact['nik']:<10} | {contact['name']:<20} | {contact['phone']:<15}")

def edit_contact():
    nik = input("Enter the NIK of the contact to edit: ")
    for contact in list_contact:
        if contact["nik"] == nik:
            new_nik = input("Enter new NIK: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            contact["nik"] = new_nik
            contact["name"] = new_name
            contact["phone"] = new_phone
            print("Contact updated successfully.")
            return
    print("Contact not found.")
    
def menu():
    print("test")

def main():
    
    menu()
    create_contact()
    # edit_contact()
    contact_table()
    
main()





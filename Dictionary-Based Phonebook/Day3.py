phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780"
}

def add_contact(name, number):
    if name in phonebook:
        print("Contact already exists!")
    else:
        phonebook[name] = number
        print("Contact added!")

def search_contact(name):
    # Partial search (bonus)
    found = False
    for key in phonebook:
        if name.lower() in key.lower():
            print(key, ":", phonebook[key])
            found = True
    if not found:
        print("Contact not found!")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")

# Example usage
add_contact("ROHAN", "9999999999")
search_contact("RI")
delete_contact("AMIT")

print("\nFinal Phonebook:", phonebook)

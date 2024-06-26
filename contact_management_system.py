import re
contacts_dictionary = {}
def command_line_interface():
    phone_regex = r"^\d{3}-\d{3}-\d{4}$"
    name_regex = r"^\b[A-Z]{1}[a-z]+\b\s\b[A-Z]{1}[a-z]+\b$"
    email_regex = r"^[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    txt_regex = r"^[A-Za-z0-9_\-]+\.{1}(txt){1}$"
    print("Welcome to our Contact Management System!")
    while True:
        main_menu = input("Menu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export (or overwitre) contacts to a new text file\n7. Append updates to anexisting text file backup\n8. Import contacts from a text file\n9. Quit\nEnter number for selected menu option here: ")
        if main_menu == "1":
            add_phone_number = input("Please enter the phone number for your new contact here: ")
            add_name = input("Please enter the name for your new contact here: ")
            add_email = input("Please enter the email address for your new contact here: ")
            try:
                if re.match(phone_regex, add_phone_number) and re.match(name_regex, add_name) and re.match(email_regex, add_email):
                    add_contact(add_phone_number, add_name, add_email)
                else:
                    print("Please ensure all inputs have been entered in a valid format. Phone numbers should be 'xxx-xxx-xxxx' with 0-9 digits, emails should be 'username@domain.com', names should be 'First Last'")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "2":
            edit_id = input("To find the appropriate contact card we are looking to edit, please enter their phone number: ")
            edit_field = input("What field would you like to edit: ")
            new_info_value = input("What new information are you replacing the existing value with: ")
            try:
                if re.match(phone_regex, edit_id):
                    edit_contact(edit_id, edit_field, new_info_value)
                else:
                    print("Invalid phone number format. Please enter as 'xxx-xxx-xxxx' with 0-9 digits")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "3":
            delete_id = input("PLease enter the phone number for the contact you would like to delete: ")
            try:
                if re.match(phone_regex, delete_id):
                    delete_contact(delete_id)
                else:
                    print("Invalid phone number format. Please enter as 'xxx-xxx-xxxx' with 0-9 digits")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "4":
            search_id = input("Please enter the phone number for the contact you are searching for: ")
            try:
                if re.match(phone_regex, search_id):
                    search_contact(search_id)
                else:
                    print("Invalid phone number format. Please enter as 'xxx-xxx-xxxx' with 0-9 digits")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "5":
            display_all_contacts()
        elif main_menu == "6":
            export_name = input("Please enter a valid name for your new .txt file: ")
            try:
                if re.match(txt_regex, export_name):
                    contacts_export(export_name)
                else:
                    print("Please use a valid file format. Acceptable characters for name are A-Z upper and lowercase, 0-9, _ and -. Please avoid spaces. All files must end in .txt ")
            except Exception as e:
                print(f"Processing Error: {e}")                                       
        elif main_menu == "7":
            append_name = input("Please enter the name of the existing text file you wish to append to in valid .txt format: ")
            try:
                if re.match(txt_regex, append_name):
                    contacts_append(append_name)
                else:
                    print("Please use a valid file format. Acceptable characters for name are A-Z upper and lowercase, 0-9, _ and -. Please avoid spaces. All files must end in .txt ")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "8":
            import_name = input("Please enter the name or path of the txt file you are looking to import: ")
            try:
                if re.match(txt_regex, import_name):
                    contact_import(import_name)
                else:
                    print("Please use a valid file format. Acceptable characters for name are A-Z upper and lowercase, 0-9, _ and -. Please avoid spaces. All files must end in .txt ")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "9":
            print("Thank you for using our Contact Management System!")
            break
        else:
            print("Please enter a valid menu option numbered 1 through 9")



def add_contact(phone_number, name, email):
    global contacts_dictionary
    contacts_dictionary.update({phone_number: {"Name": name, "Phone Number": phone_number, "Email": email}})
    while True:
        add_category = input("Would you like to add a new category (Y/N): ")
        if add_category.upper() == "Y":
            new_category = input("What is the title of the new category: ").title()
            category_value = input("For this contact, what is this category's information: ")
            contacts_dictionary[phone_number].update({new_category:category_value})
        elif add_category.upper() == "N":
            break
        else:
            print("Please enter a valid response (Y or N)")
    print("Your contact has been added!")
    for key, value in contacts_dictionary[phone_number].items():
        print(f"{key}: {value}")
    # print(contacts_dictionary)
    return contacts_dictionary

def edit_contact(id, field, new_info):
    global contacts_dictionary
    try:
        if field.lower() == "phone number":
            contacts_dictionary[new_info] = {"Name": contacts_dictionary[id]["Name"], "Phone Number": new_info, "Email": contacts_dictionary[id]["Email"]}
            del contacts_dictionary[id] 
        elif field.lower() == "name":
            contacts_dictionary[id]["Name"] = new_info
        elif field.lower() == "email":
            contacts_dictionary[id]["Email"] = new_info
        else:
            while True:
                confirm_field = input("Please confirm you are trying to edit or add a manually entered field (Y/N): ").upper()
                if confirm_field == "Y":
                    contacts_dictionary[id].update({field:new_info})
                    break
                elif confirm_field == "N":
                    print("Contacts have not been altered, please check your inputs to ensure a valid field has been entered.")
                    break
                else:
                    print("Invalid entry, please enter Y or N")
        print(f"Contact with initial phone number {id}, has had {field} edited for new value: {new_info}")
        # print(contacts_dictionary)
        return contacts_dictionary
    except KeyError:
        print("Please ensure the original phone number entered to locate the desired contact is valid and was previously added.")

def delete_contact(delete_id):
    global contacts_dictionary
    try:
        del contacts_dictionary[delete_id]
        # print(contacts_dictionary)
        return contacts_dictionary
    except KeyError:
        print("Please ensure the original phone number entered for the contact you wish to delete has been previously added.")

def search_contact(search_id):
    global contacts_dictionary
    try:
        for key in contacts_dictionary.keys():
            if search_id == key:
                for inner_key, value in contacts_dictionary[search_id].items():
                    print(f"{inner_key}: {value}")
    except KeyError:
        print("Please ensure the original phone number entered for the contact you are searching for has been previously added.")                

def display_all_contacts():
    global contacts_dictionary
    for index, contact_id in enumerate(contacts_dictionary.keys(), 1):
        print(f"Contact #{index}.")
        for inner_key, value in contacts_dictionary[contact_id].items():
            print(f"{inner_key}: {value}")
        print("\n")

def contacts_export(export_file):
    global contacts_dictionary
    try:
        with open(export_file, "w") as file:
            for index, contact_id in enumerate(contacts_dictionary.keys(), 1):
                file.write(f"|Contact #{index}.")
                for inner_key, value in contacts_dictionary[contact_id]:
                    file.write(f"{inner_key}: {value}")
    except OSError:
        print("Operating System Error")
    except Exception as e:
        print(f"General Error: {e}")

def contacts_append(append_file):
    global contacts_dictionary
    try:
        with open(append_file, "a+") as file:
            for line in file:
                contact_id = line.strip().split("|")
            for index, key in enumerate(contacts_dictionary.keys(), 1):
                if key not in contact_id:
                    file.write(f"|Contact #{index}.")
                    for inner_key, value in contacts_dictionary[key]:
                        file.write(f"{inner_key}: {value}")
    except FileNotFoundError:
        print("Please enter a file or path that already exists so new contacts can be appended to it.")
    except OSError:
        print("Operating System Error")
    except Exception as e:
        print(f"General Error: {e}")

def contact_import(import_file):
    global contacts_dictionary
    try:
        with open(import_file, "r") as file:
            for line in file:
                contact_id =line.strip().split("|")
            for key in contacts_dictionary.keys():
                if key not in contact_id:                
    except FileNotFoundError:
        print("Please enter a file or path that already exists to import.")
    except OSError:
        print("Operating System Error")
    except Exception as e:
        print(f"General Error: {e}")

command_line_interface()
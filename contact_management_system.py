import re
contacts_dictionary = {}
def command_line_interface():
    phone_regex = r"^\d{3}-\d{3}-\d{4}$"
    name_regex = r"^[A-Z][a-zA-Z'-]+ [A-Z][a-zA-Z'-]+$"
    email_regex = r"^[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    txt_regex = r"^[\w\-/]+\.txt$"
    print("Welcome to our Contact Management System!")
    while True:
        main_menu = input("Menu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export (or overwitre) contacts to a new text file\n7. Import contacts from a text file\n8. Quit\nEnter number for selected menu option here: ")
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
        # elif main_menu == "7":
        #     append_name = input("Please enter the name of the existing text file you wish to append to in valid .txt format: ")
        #     try:
        #         if re.match(txt_regex, append_name):
        #             contacts_append(append_name)
        #         else:
        #             print("Please use a valid file format. Acceptable characters for name are A-Z upper and lowercase, 0-9, _ and -. Please avoid spaces. All files must end in .txt ")
        #     except Exception as e:
        #         print(f"Processing Error: {e}")
        elif main_menu == "7":
            import_name = input("Please enter the name or path of the txt file you are looking to import: ")
            try:
                if re.match(txt_regex, import_name):
                    contact_import(import_name)
                else:
                    print("Please use a valid file format. Acceptable characters for name are A-Z upper and lowercase, 0-9, _ and -. Please avoid spaces. All files must end in .txt ")
            except Exception as e:
                print(f"Processing Error: {e}")
        elif main_menu == "8":
            print("Thank you for using our Contact Management System!")
            break
        else:
            print("Please enter a valid menu option numbered 1 through 8")

'''
The command_line_interface function houses the overall backbone of this project including the main_menu input variable which allows users to choose how they want to begin building and interacting with their contact management system.
This function houses the regex pattern we will use to validate the inputs and formatting of phone numbers, emails, names, and txt file naming. The main menu functions within a while loop that can only be broken if the user inputs 8, which is the option number for quit.
It uses a series of if/elif tests to determine if the user wants to choose options for adding, editing, deleting, searching, or viewing all contacts. It also has elif statement for exporting and importing contacts through .txt file handling.
Our command_line_interface uses re.match() to validate it's inputs with the earlier defined regex patterns and if the inputs pass validation they are used as arguments for our various functions built in to the program. This feature is also housed in try, except blocks to catch any unexpected exceptions that can be categorized as general procesing errors, related to our use of regex.
Each regex nested if statement has an else print statement that follows it that will point out what the acceptable input parameters are so users do not continue to make the same errors multiple times. 
'''



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

'''
The add_contact function takes in 3 arguments that will be in every contact: phone_number, name, and email. Positionally I chose phone_number first as that was the parameter I wanted to use as the key for the outer portion of contacts_dictionary.
First we identify that contacts_dictionary is global as all of our functions will reference and return to it. I then use the .update method to set up the general structure of our nested dictionary.
I follow that with a while loop that allows users to add their own categories with the input of new_category as the nested key and the input of category_value as the nested value.
I then use conatcts_dictionary[phone_number] to direct inside the nested dictionary and use .update to add on this new key-value pair. Lastly I use a for loop with the .items() method to print off every key:value pair for our new contact and then return our updated contacts_dictionary.
'''

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

'''
edit_contact works by taking in the parameters of id to reference which contact we are editing, field to identify which ke-value pair we are editing, and new info to assign the new nested value for this category.
First we make the contacts_dictionary global and then in a try except block we use a series of if-elif tests to identify if name, email, or phone number is being edited. If phone number is the choice we have to reassign the whole dictionary entry as both the inner value and outer key will be changed.
After assigning these new values we are also sure to delete the old contact so there is no duplicate with incorrect information.
The assignment of contacts_dictionary[id][inner key] for name and email is simpler as none of the key's are changed and we can just assign a new inner value.
Lastly the else block will use a while loop to ask users to confirm they are trying to edit or add an additional manually entered field. If they confirm it we direct inside the appropriate id for the contact we are editing ad use the .update method with (field:new_info) as the inner kay:value pair.
Then we break the loop. Alternatively if the user types N instead of Y they are not confirming a manual field and we break the loop before any of the data structure is changed by the error.
The else statement identifies invalid entries and requests the user to enter Y or N instead.
After the data structure has been changed regardless of field, we print an f-strng to show our user what change has been made and for what contact as confirmation. We then return the new updated contacts_dictionary.
We also have an exception built in if there is a KeyError where a phone number is entered for a contact that is not in the dictionary already.
'''

def delete_contact(delete_id):
    global contacts_dictionary
    try:
        del contacts_dictionary[delete_id]
        # print(contacts_dictionary)
        return contacts_dictionary
    except KeyError:
        print("Please ensure the original phone number entered for the contact you wish to delete has been previously added.")

'''
delete_contact works by taking the argument of delete_id and locating the entire item for a single outer key. Once it locates this contact's phone number it will run a simple del keyword to remove that single contact from the dictionary and all of its' inner key:value pairs.
We then return the updted contacts_dictionary without that contact in it. This function, like the previous edit function, has a try-except block for KeyError if a phone number is entered in the valid format but has not been entered into our dictionary yet.
'''

def search_contact(search_id):
    global contacts_dictionary
    try:
        for key in contacts_dictionary.keys():
            if search_id == key:
                for inner_key, value in contacts_dictionary[search_id].items():
                    print(f"{inner_key}: {value}")
    except KeyError:
        print("Please ensure the original phone number entered for the contact you are searching for has been previously added.")                

'''
search_contact works by taking in a searh_id that is the phone number of the contact we are trying to locate. It uses the global contacts_dictionary and is in a try-except block to catch any KeyErrors if the user tries to find a contact for a phone number that has not yet been entered.
Within the try block we use a for loop and the .keys() method to locate the search_id as an outer key. We then iterate through the inner key:value pair using a nested for loop and the .items() method, printing our search results in an f-string.  
'''

def display_all_contacts():
    global contacts_dictionary
    for index, contact_id in enumerate(contacts_dictionary.keys(), 1):
        print(f"Contact #{index}.")
        for inner_key, value in contacts_dictionary[contact_id].items():
            print(f"{inner_key}: {value}")
        print("\n")

'''
display_all_contacts also uses the global contacts_dictionary but takes no arguments as it will print the whole dictionary. First we iterate through the enumerate of the outer dictionary using the .keys() method inside the built in fucntion.
We start our index at one and print an f-string with the contact's index number. Within this for loop we then use a nested for loop with inner key, value and the .items() method for each inner dictionary of each outer key.
Inside the inner dictionaries we print off every key:value pair for that contact. Once both for loops have been fully iterated through, our entire dictionary should be printed in a formatted appearance in the terminal.  
'''
# def contacts_export(export_file):
#     global contacts_dictionary
#     try:
#         with open(export_file, "w") as file:
#             for index, contact_id in enumerate(contacts_dictionary.keys(), 1):
#                 file.write(f"Contact #{index}: \n")
#                 for inner_key, value in contacts_dictionary[contact_id].items():
#                     file.write(f"{inner_key}: {value}\n")
#     except OSError:
#         print("Operating System Error")
#     except Exception as e:
#         print(f"General Error: {e}")

def contacts_export(export_file):
    global contacts_dictionary
    try:
        with open(export_file, "w") as file:
            for index, contact_id in enumerate(contacts_dictionary.keys(), 1):
                file.write(f"Contact #{index}:\n")
                for inner_key, value in contacts_dictionary[contact_id].items():
                    file.write(f"{inner_key}: {value}\n")
                file.write("\n")
    except OSError:
        print("Operating System Error")
    except Exception as e:
        print(f"General Error: {e}")

'''
contacts_export works by exporting the global contacts_dictionary into a .txt file that is named through the argument that is passed through this function. In a try-except block that can catch general errors as well as OS errors, we begin the try block using the with open keyword in write ("w") mode.
once we've opened this new document we are writing and have referenced it as file, we begin looping through each part of our dictionary to transfer its data to the new file.
We start with a for loop that enumerates our outer dictionary keys so we can number and index each contact we export using the file.write() method. We then loop through the inner dictionary for each conact_id uisng a nested for loop and the .items() method.
In this nested for loop we use file.write() method again to write our inner_key:value pair to the new .txt file. Lastly we go back out to our original for loop and print off a final file.write(\n) so our ictionary entries are fully iterated through and can be stored to our new exported file.
'''

# def contacts_append(append_file):
#     global contacts_dictionary
#     try:
#         with open(append_file, "a+") as file:
#             for line in file:
#                 contact_id = line.strip().split("|")
#             for index, key in enumerate(contacts_dictionary.keys(), 1):
#                 if key not in contact_id:
#                     file.write(f"Contact #{index}.")
#                     for inner_key, value in contacts_dictionary[key].items():
#                         file.write(f"{inner_key}: {value}")
#     except FileNotFoundError:
#         print("Please enter a file or path that already exists so new contacts can be appended to it.")
#     except OSError:
#         print("Operating System Error")
#     except Exception as e:
#         print(f"General Error: {e}")

'''
Saint says we need Flask for this
'''

def contact_import(import_file):
    global contacts_dictionary
    phone_regex = r"^\d{3}-\d{3}-\d{4}$"
    name_regex = r"^[A-Z][a-zA-Z'-]+ [A-Z][a-zA-Z'-]+$"
    email_regex = r"^[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    phone_id = ""
    try:
        with open(import_file, "r") as file:
            for line in file:
                import_items = line.strip().split(":")
            for item in import_items:
                if item not in contacts_dictionary:
                    if re.match(phone_regex, item):
                        item = phone_id
                        contacts_dictionary[phone_id] = {"Phone Number": phone_id}
                    if re.match(name_regex, item):
                        contacts_dictionary[phone_id].update({"Name": item})
                    if re.match(email_regex, item):
                        contacts_dictionary[phone_id].update({"Email": item})           
    except FileNotFoundError:
        print("Please enter a file or path that already exists to import.")
    except OSError:
        print("Operating System Error")
    except Exception as e:
        print(f"General Error: {e}")

command_line_interface()
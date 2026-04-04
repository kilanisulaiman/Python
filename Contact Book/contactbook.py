import json
import os
import time

def create_contactFile():

    if not os.path.isfile(fileName):
        try:
            with open(fileName, "x", encoding="utf-8") as f:
                json.dump({}, f)

        except PermissionError:
            print("Creating contactFile failed --> Error: Permission not granted")

        except FileExistsError:
            print("\n")

        except OSError as e:
            print(f"OS Error: {e}")


def append_contactFile(data : dict):
    if not os.path.isfile(fileName):
        print(f"Error: File {fileName} not found")

    if not os.access(fileName, os.R_OK):
        print(f"Error: file {fileName} has no access permission")

    try:
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(data, file, indent = 4)

    except PermissionError:
        print("Failed to append: Permission not granted")

    except OSError as e:
        print(f"OS Error: {e.strerror} ")


def access_contactFile():
    if not os.path.isfile(fileName):
        print(f"Error: {fileName} File is not found")
        return {}

    if not os.access(fileName, os.R_OK):
        print(f"ERROR: file {fileName} has No READ permission")
        return {}
    
    if os.path.getsize(fileName) == 0:
        with open(fileName, "w", encoding = "utf-8") as f:
            json.dump({}, f)

    try:
        with open(fileName, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as e:
        print("Broken Line Syntax")
        print("line:", e.lineno, ", column:", e.colno)
        print(e.msg)
        return {}

    except UnicodeError:
        print("Error: File is not UTF-8 suported")
        return {}

    except OSError as e:
        print(f"OS Error: {e}")
        return {}


def main():

    create_contactFile()

    header = "Your Contact Book Program"
    print(header.center(45, "_"))
    while True:
        print(
            " 1. View contact\n 2. Add contact\n 3. Edit contact\n 4. Clear contact\n 5. Delete contact\n 6. Exit "
        )
        user: str = input("Select a number: ").strip()
        print("")
        if user == "1":
            view_contact()
        elif user == "2":
            add_contact()
        elif user == "3":
            edit_contact()
        elif user == "4":
            clear_contact()
        elif user == "5":
            delete_contact()
        elif user == "6":
            print("Have a nice day...")
            break
        else:
            print("Invalid input \n")


def view_contact():
    print("View all contact".center(45, "_"))
    i = 0
    if contactBook:
        loading()
        for name, info in contactBook.items():
            i += 1
            print(f" {i}. {name} info: ")
            for key, value in info.items():
                print(f"\t {key} : {value}")
        print("")
    else:
        print("Your contact list is empty \n")


def add_contact():
    print("Add contact".center(45, "_"))
    while True:
        try:
            number = int(input("How many contact do you want to add: "))
            if number < 0:
                print("Value cannot be less than one 1 \n")
                continue
            elif number == 0:
                print("You didn't add any contact \n")
                break
            else:
                for i in range(number):
                    name = input(f"Contact {i+1} Name: ").strip().capitalize()
                    contactBook[name] = {}
                    contactBook[name]["phone number"] = input(f"{name} Number: ")
                    contactBook[name]["mail"] = input(f"{name} mail: ")
                    contactBook[name]["gender"] = input(f"{name} gender: ")
                    print("")

                append_contactFile(contactBook)   
                print("Contacts successfully added !!\n")
            break
        except ValueError:
            print("Invalid input \n")


def edit_contact():
    print("Edit contact".center(45, "_"))
    userName = input("Enter contact Name: ").capitalize().strip()
    if userName in contactBook.keys():
        while True:
            try:
                number = int(input("How many info do you want to edit \n[gender, phone number, mail]: "))
                if (number < 0) or (number > 3):
                    print(f"Only 3 info are available \n")
                    continue
                if number == 0:
                    print("Yod didn't edit anything \n")
                    break
                option: list[str] = ["gender", "mail", "phone number"]
                for i in range(number):
                    info = input(f"info {i+1}: ").strip().lower()
                    if info in option:
                        newInfo: str = input(f"{userName} {info}: ").strip()
                        contactBook[userName][info] = newInfo
                    else:
                        print(f"{info} not available____ \n")

                    append_contactFile(contactBook)

                print("Contact edited successfully !!! \n")
                break
            except ValueError:
                print("Invalid input \n")
    else:
        print(f"{userName} is not in the contact list \n")


def clear_contact():
    print("Clear contact book".center(45, "_"))
    user: str = (input("Clear your contact list \n are you sure YES/NO: ").strip().lower())
    if user == "yes":
        contactBook.clear()
        with open(fileName, "w", encoding="utf-8") as f:
            json.dump(contactBook, f)
        for i in range(101):
            load = f"Clearing list: {i}% completed"
            print(load, end="\r", flush=True)
            time.sleep(0.02)

        print("Contact Book Cleared..............\n")


def delete_contact():
    print("Delete Contact".center(45, "_"))
    user = input("Enter contact Name: ").capitalize()

    if user in contactBook.keys():
        del contactBook[user]
        append_contactFile(contactBook)
        print("Contact deleted successfully !!! \n")
    else:
        print(f"{user} is not in the contact list \n")


def loading():
    print("")
    for count in range(101):
        load = f"Loading list : {count}% completed"
        print(load, end="\r", flush=True)
        time.sleep(0.02)
    print(" " * 45, end="\r")


fileName = "contactBook.json"
contactBook = access_contactFile()
main()

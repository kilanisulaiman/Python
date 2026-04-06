
import json
import os
import time


FILE_NAME = "contact_book.json"


def create_contact_file():
    if os.path.isfile(FILE_NAME):
        return
    try:
        with open(FILE_NAME, "x", encoding="utf-8") as f:
            json.dump({}, f)
    except PermissionError:
        print("Error: Cannot create contact file — permission denied.")
    except FileExistsError:
        pass
    except OSError as e:
        print(f"OS Error while creating file: {e}")


def write_contact_file(data: dict):
    if not os.path.isfile(FILE_NAME):
        print(f"Error: '{FILE_NAME}' not found. Cannot save contacts.")
        return
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except PermissionError:
        print("Error: Cannot write to contact file — permission denied.")
    except OSError as e:
        print(f"OS Error while writing file: {e.strerror}")


def load_contact_file() -> dict:
    if not os.path.isfile(FILE_NAME):
        print(f"Error: '{FILE_NAME}' not found.")
        return {}
    if os.path.getsize(FILE_NAME) == 0:
        write_contact_file({})
        return {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print("Error: Contact file is corrupted (invalid JSON).")
        print(f"  Line {e.lineno}, column {e.colno}: {e.msg}")
        print("  Backing up corrupted file as 'contact_book.json.bak'.")
        os.replace(FILE_NAME, FILE_NAME + ".bak")
        # Write directly — FILE_NAME no longer exists so write_contact_file would fail
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump({}, f)
        return {}
    except UnicodeDecodeError:
        print("Error: Contact file is not valid UTF-8.")
        return {}
    except OSError as e:
        print(f"OS Error while reading file: {e}")
        return {}


def loading_bar(label: str = "Loading"):
    for count in range(101):
        print(f"{label}: {count}% completed", end="\r", flush=True)
        time.sleep(0.01)
    print(" " * 50, end="\r")


def section_header(title: str):
    print(title.center(45, "_"))


def view_contact(contact_book: dict):
    section_header("View All Contacts")
    if not contact_book:
        print("Your contact list is empty.\n")
        return
    loading_bar("Loading list")
    for i, (name, info) in enumerate(contact_book.items(), start=1):
        print(f" {i}. {name}")
        for key, value in info.items():
            print(f"\t{key}: {value}")
    print()


def add_contact(contact_book: dict):
    section_header("Add Contact")
    while True:
        try:
            count = int(input("How many contacts do you want to add: ").strip())
        except ValueError:
            print("Invalid input. Enter a whole number.\n")
            continue
        if count < 0:
            print("Value must be 1 or greater.\n")
            continue
        if count == 0:
            print("No contacts added.\n")
            return
        for i in range(count):
            name = input(f"Contact {i + 1} name: ").strip().capitalize()
            if not name:
                print("Name cannot be empty. Skipping this contact.\n")
                continue
            if name in contact_book:
                print(f"'{name}' already exists. Skipping to avoid overwrite.\n")
                continue
            phone = input(f"{name} phone number: ").strip()
            mail = input(f"{name} email: ").strip()
            gender = input(f"{name} gender: ").strip()
            print()
            contact_book[name] = {
                "phone number": phone,
                "mail": mail,
                "gender": gender,
            }
        write_contact_file(contact_book)
        print("Contacts saved successfully.\n")
        return


def edit_contact(contact_book: dict):
    section_header("Edit Contact")
    name = input("Enter contact name: ").strip().capitalize()
    if name not in contact_book:
        print(f"'{name}' is not in the contact list.\n")
        return
    valid_fields = ["gender", "mail", "phone number"]
    print(f"Editable fields: {valid_fields}")
    while True:
        try:
            count = int(input("How many fields do you want to edit: ").strip())
        except ValueError:
            print("Invalid input. Enter a whole number.\n")
            continue
        if count < 0 or count > len(valid_fields):
            print(f"Enter a number between 0 and {len(valid_fields)}.\n")
            continue
        if count == 0:
            print("You didn't edit anything.\n")
            return
        for i in range(count):
            field = input(f"Field {i + 1}: ").strip().lower()
            if field not in valid_fields:
                print(f"'{field}' is not a valid field. Choose from: {valid_fields}\n")
                continue
            new_value = input(f"New {field} for {name}: ").strip()
            contact_book[name][field] = new_value
        write_contact_file(contact_book)
        print("Contact updated successfully.\n")
        return


def delete_contact(contact_book: dict):
    section_header("Delete Contact")
    name = input("Enter contact name: ").strip().capitalize()
    if name not in contact_book:
        print(f"'{name}' is not in the contact list.\n")
        return
    confirm = input(f"Delete '{name}'? YES/NO: ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.\n")
        return
    del contact_book[name]
    write_contact_file(contact_book)
    print("Contact deleted successfully.\n")


def clear_contact(contact_book: dict):
    section_header("Clear Contact Book")
    confirm = input("This will delete ALL contacts. Are you sure? YES/NO: ").strip().lower()
    if confirm != "yes":
        print("Cancelled.\n")
        return
    contact_book.clear()
    write_contact_file(contact_book)
    loading_bar("Clearing list")
    print("Contact book cleared.\n")


def main():
    create_contact_file()
    contact_book = load_contact_file()

    print("Your Contact Book".center(45, "_"))

    actions = {
        "1": ("View contacts",  lambda: view_contact(contact_book)),
        "2": ("Add contact",    lambda: add_contact(contact_book)),
        "3": ("Edit contact",   lambda: edit_contact(contact_book)),
        "4": ("Clear contacts", lambda: clear_contact(contact_book)),
        "5": ("Delete contact", lambda: delete_contact(contact_book)),
        "6": ("Exit",           None),
    }

    while True:
        print()
        for key, (label, _) in actions.items():
            print(f" {key}. {label}")
        choice = input("\nSelect a number: ").strip()
        print()
        if choice == "6":
            print("Have a nice day.")
            break
        if choice not in actions:
            print("Invalid input.\n")
            continue
        actions[choice][1]()


if __name__ == "__main__":
    main()



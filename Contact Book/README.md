# Contact Book

A command-line contact management program written in Python. Stores contacts locally in a JSON file.

---

## Features

- Add one or multiple contacts at once
- View all saved contacts
- Edit individual contact fields
- Delete a specific contact
- Clear the entire contact book
- Auto-repairs empty or corrupted JSON files
- Backs up corrupted data before resetting

---

## Requirements

- Python 3.10 or higher
- No third-party libraries — standard library only

---

## How to Run

```bash
python contact_book.py
```

---

## Menu Options

| Option | Action                        |
|--------|-------------------------------|
| 1      | View all contacts             |
| 2      | Add contact(s)                |
| 3      | Edit a contact                |
| 4      | Clear the entire contact book |
| 5      | Delete a specific contact     |
| 6      | Exit                          |

---

## Contact Fields

Each contact stores three fields:

- `phone number`
- `mail`
- `gender`

---

## Data Storage

Contacts are saved in a file called \`contact_book.json\` in the same directory as the script.

This file is created automatically on first run. Do not delete it while the program is running.

If the file is corrupted, the program will back it up as \`contact_book.json.bak\` and start fresh automatically.

---


## .gitignore

The `.gitignore` file tells Git which files to exclude from the repository.

The following files are excluded from this project:

- `contact_book.json` — contains your personal contact data
- `contact_book.json.bak` — backup of a corrupted contact file

These files are local only and will never be pushed to GitHub.


---

## Project Structure

```
contact-book/
├── contact_book.py   # main program
├── README.md         # this file
└── .gitignore
```

---

## Author

KILANI SULAIMAN.  
GitHub: [@kilanisulaiman](https://github.com/kilanisulaiman)


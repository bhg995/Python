from tkinter import *
from tkinter import messagebox
import string, secrets
import pyperclip
import json
import os


def generate_password():
    min_length = 12
    min_lowercase = 2
    min_uppercase = 2
    min_numbers = 2
    min_symbols = 2

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = '!#$%&(_^?)*+@[]{}:;<>,.'

    password_list = (
        [secrets.choice(lower) for _ in range(min_lowercase)] +
        [secrets.choice(uppercase) for _ in range(min_uppercase)] +
        [secrets.choice(numbers) for _ in range(min_numbers)] +
        [secrets.choice(symbols) for _ in range(min_symbols)]
    )

    remaining = min_length - len(password_list)
    all_of_it = lower + uppercase + numbers + symbols
    password_list += [secrets.choice(all_of_it) for _ in range(remaining)]

    secrets.SystemRandom().shuffle(password_list)

    password = "".join(password_list)

    # Copy to clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="New Password", message="The password has been copied to clipboard.")


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Incomplete", message="Fill all the fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The details: \n\nEmail: {email} "
                                                      f"\nPassword: {password} \nOK?")
        if is_ok:
            if not os.path.exists("data.json"):
                with open("data.json", "w") as data_file:
                    json.dump([], data_file)  # Create empty list if file doesn't exist

            # Read existing data from file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

            # Save new entry
            data.append({
                "website": website,
                "email": email,
                "password": password
            })

            # Write updated data back to the file
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            # Clear input fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=400, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

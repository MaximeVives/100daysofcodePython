from tkinter import *
from tkinter.messagebox import *
import random

import pyperclip as pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    return "".join(password_list)


def load_password(password):
    password.delete(0, END)
    password.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file(website, email, password):
    if confirm_options(website, email, password):
        new_data = {
            website.get(): {
                "email": email.get(),
                "password": password.get(),
            }
        }
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
            pyperclip.copy(password.get())
            showinfo("Mot de passe copié", "Le mot de passe a été copié")

            clear_entries([website, email, password])
            website.focus()

    else:
        showinfo("Mot de passe non sauvegardé", "Le mot de passe n'a pas été sauvegardé")


def clear_entries(entries):
    for entry in entries:
        entry.delete(0, END)


def confirm_options(website, email, password):
    if website.get() == "" or email.get() == "" or password.get() == "":
        showerror(title="Données non complètes", message="Tous les champs n'ont pas été complétés")
        return False
    return True


# ---------------------------- SEARCH --------------------------------- #

def search(website):
    user_search = website.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        showerror(title="Pas de mot de passe", message="Il n'y a pas encore de mot de passe enregistré.")

    else:
        if user_search not in data:
            showerror(title="Recherche échouée", message=f"Il n'y a pas de correspondance dans la Base de données pour '{user_search}'.")
        else:
            email = data[user_search]["email"]
            password = data[user_search]["password"]

            showinfo(title=user_search, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
            showinfo("Mot de passe copié", "Le mot de passe a été copié")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website :")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/username :")
email_label.grid(row=2, column=0)

password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=49)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
search_password_button = Button(text="Search", command=lambda: search(website_entry), width=15)
search_password_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=lambda: load_password(password_entry), width=15)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=lambda: save_file(website_entry, email_entry, password_entry))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

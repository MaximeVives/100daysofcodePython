from tkinter import *
from tkinter.messagebox import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

import pyperclip as pyperclip

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
        try:
            with(open("data.txt", "a")) as f:
                f.write(f"{website.get()}, {email.get()}, {password.get()}\n")

            pyperclip.copy(password.get())
            showinfo("Mot de passe copié", "Le mot de passe a été copié")

            clear_entries([website, email, password])
            website.focus()
        except FileNotFoundError:
            showerror(title="Fichier non créé", message="Le fichier n'a pas pu être créé, merci de réessayer.")
    else:
        showinfo("Mot de passe non sauvegardé", "Le mot de passe n'a pas été sauvegardé")


def clear_entries(entries):
    for entry in entries:
        entry.delete(0, END)


def confirm_options(website, email, password):
    if website.get() == "" or email.get() == "" or password.get() == "":
        showerror(title="Données non complètes", message="Tous les champs n'ont pas été complétés")
        return False
    return askokcancel(title="Confirmer la sauvegarde ?", message="Voulez-vous enregistrer ce mot de passe ?")


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
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=lambda: load_password(password_entry))
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=lambda: save_file(website_entry, email_entry, password_entry))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

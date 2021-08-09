from const import BACKGROUND_COLOR, WAITING_TIME
from tkinter import *
from tkinter.messagebox import showinfo
import pandas as pd
from random import choice

# ====================== MODEL ========================== #

words = {}
try:
    get_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    initial_data = pd.read_csv("data/french_words.csv")
    words = initial_data.to_dict(orient="records")
else:
    words = get_words.to_dict(orient="records")


current_card = {}


def get_a_word():
    global current_card

    current_card = choice(words)
    card.itemconfigure(title, text="French", fill="black")
    card.itemconfigure(word, text=current_card["French"], fill="black")
    card.itemconfigure(card_bg, image=bg_french)
    window.after(WAITING_TIME, func=flip_card)


def flip_card():
    card.itemconfigure(title, text="English", fill="white")
    card.itemconfigure(word, text=current_card["English"], fill="white")
    card.itemconfigure(card_bg, image=bg_english)


def know_word():
    if len(words) == 0:
        showinfo("Plus de mot", "Tous les mots ont été appris")
    else:
        words.remove(current_card)
        word_to_learn = pd.DataFrame(words)
        word_to_learn.to_csv("data/words_to_learn.csv", index=False)
        get_a_word()


# ======================= VIEW ========================== #
window = Tk()

window.title("Flashy")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(WAITING_TIME, func=flip_card)

bg_french = PhotoImage(file="images/card_front.png")
bg_english = PhotoImage(file="images/card_back.png")

card = Canvas(bg=BACKGROUND_COLOR, height=525, width=800, highlightthickness=0)
card_bg = card.create_image(0, 0, image=bg_french, anchor="nw")
card.grid(row=0, column=0, columnspan=2)

title = card.create_text(400, 163, text="French", font=("Arial", 40, "italic"))
word = card.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

get_a_word()

fail_image = PhotoImage(file="images/wrong.png")
fail = Button(image=fail_image, highlightthickness=0, command=get_a_word)
fail.grid(row=1, column=0)

success_image = PhotoImage(file="images/right.png")

success = Button(image=success_image, highlightthickness=0, command=know_word)
success.grid(row=1, column=1)

window.mainloop()

from tkinter import *
import pandas
import random
timer = None
BACKGROUND_COLOR = "#B1DDC6"
word_num = 0

# ----------------------IMPORTING DATA -------------------- #
data = pandas.read_csv("data/french_words.csv")
french_words = data.French.to_list()
english_translation = data.English.to_list()

#-------------------------FUNCTIONS-------------------------#


def new_word():
    global word_num
    next_fr_word = random.choice(french_words)
    flashcard.itemconfig(flashcard_img, image=card_front_img)
    flashcard.itemconfig(title_text, text="French")
    flashcard.itemconfig(word_text, text=next_fr_word)
    word_num = french_words.index(next_fr_word)
    count_down(3)
    print(len(french_words))
    print(len(english_translation))


#After a set amount of time flash card flips over to reveal the english equivalent
def count_down(count):
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        print(count)
    elif count == 0:
        card_flip()


def card_flip():
    global timer
    global word_num
    window.after_cancel(timer)
    flashcard.itemconfig(flashcard_img, image=card_back_img)
    flashcard.itemconfig(title_text, text="English")
    eng_word = english_translation[word_num]
    flashcard.itemconfig(word_text, text=eng_word)


def know_it():
    global word_num
    french_words.remove(french_words[word_num])
    english_translation.remove(english_translation[word_num])
    new_word()


# ------------------------UI SETUP------------------------- #

# Window
window = Tk()
window.title("Flashcard Learner")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Canvas
flashcard = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_img = flashcard.create_image(400, 263, image=card_front_img)
flashcard.grid(row=0, column=0, columnspan=2)
title_text = flashcard.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = flashcard.create_text(400, 253, text="Word", font=("Arial", 50, "bold"))

# Labels


# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, command=know_it)
right_button.grid(row=1, column=1)


new_word()

window.mainloop()


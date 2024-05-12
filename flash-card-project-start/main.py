import random
from tkinter import *

import pandas

current_word = {}
BACKGROUND_COLOR = "#B1DDC6"
french_dict = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_dict = original_data.to_dict(orient="records")
else:
    french_dict = data.to_dict(orient="records")





def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(french_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_img_front, image=front_img)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English",fill= "white")
    canvas.itemconfig(card_word, text=current_word["English"], fill= "white")
    canvas.itemconfig(canvas_img_front, image=back_image)

def known():
    french_dict.remove(current_word)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()









window = Tk()
window.title("FLASHY")
window.config(padx=55, pady=55, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")


front_img = PhotoImage(file="images/card_front.png")
canvas_img_front = canvas.create_image(400, 263, image=front_img)

card_word = canvas.create_text(400, 256, text="", font=("Ariel", 60, "bold"))
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(row=1, column=0)


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=known)
right_button.grid(row=1, column=1)




next_card()
window.mainloop()


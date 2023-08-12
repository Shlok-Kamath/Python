from random import randint
from tkinter import *
from pandas import DataFrame, read_csv

BACKGROUND_COLOR = "#B1DDC6"


def change():
    global random_int, data_dic, total_range
    random_int = randint(1, total_range)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    new_word = data_dic["French"][random_int]
    canvas.itemconfig(word_text, text=new_word, fill="black")
    window.after(3000, flip)


def flip():
    global random_int, data_dic
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    word = data_dic["English"][random_int]
    canvas.itemconfig(word_text, text=word, fill="white")


def remove_element():
    global data_dic, random_int, total_range
    data_dic["French"].pop(random_int)
    data_dic["English"].pop(random_int)
    total_range -= 1
    new_data = DataFrame(data_dic)
    new_data.to_csv("data/words_to_learn.csv")
    change()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

canvas_image = canvas.create_image(400, 263, image=card_front_image)

language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Trouve", font=("Ariel", 60, "bold"))

try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
data_dic = DataFrame.to_dict(data)
random_int = 0
total_range: int = len(data_dic["French"]) - 1

wrong_button = Button(image=wrong_image, highlightthickness=0, command=change)
wrong_button.grid(row=2, column=2)

right_button = Button(image=right_image, highlightthickness=0, command=remove_element)
right_button.grid(row=2, column=0)

window.mainloop()

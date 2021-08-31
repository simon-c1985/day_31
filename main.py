import tkinter as tk
import pandas as pd
from random import choice

TITLE_FONT = ('Book Antqua', 40, 'italic')
WORD_FONT = ('Book Antqua', 60, 'bold')
BACKGROUND_COLOR = "#B1DDC6"
learn_russian = []
learn_english = []

window = tk.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pd.read_csv('./data/to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('./data/english_words.csv')
finally:
    english_words = [word for word in data['English']]
    russian_words = [word for word in data['Русский']]
    words = data.to_dict(orient='records')
    index = 0
    data_csv = {}


def create_csv_data():
    global data_csv
    # for ind in range(len(english_words) - 1):
    #     data_csv[english_words[ind]] = russian_words[ind]
    df = pd.DataFrame({'English': english_words,
                       'Русский': russian_words

                       })
    df.to_csv('./data/to_learn.csv', index=False)


def next_card():
    global index, timer
    window.after_cancel(timer)
    try:
        index = choice(range(len(english_words) - 1))
        canvas.itemconfig(front_img, image=front_card_img)
        canvas.itemconfig(language_text, text='English', fill='black')
        # canvas.itemconfig(word_text, text=f"{words[index]['English']}", fill='black')
        canvas.itemconfig(word_text, text=f'{english_words[index]}', fill='black')
        timer = window.after(3000, press_no_button)
    except IndexError:
        canvas.itemconfig(language_text, text="WARNING!!!", fill='red')
        canvas.itemconfig(word_text, text="No words to learn!", fill='green')


def press_yes_button():
    english_words.remove(english_words[index])
    russian_words.remove(russian_words[index])
    create_csv_data()
    next_card()


def press_no_button():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(front_img, image=back_card_img)
    canvas.itemconfig(language_text, text='Русский', fill='white')
    canvas.itemconfig(word_text, text=f'{russian_words[index]}', fill='white')
    timer = window.after(5000, next_card)


timer = window.after(1000, next_card)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = tk.PhotoImage(file='./images/card_front.png')
back_card_img = tk.PhotoImage(file='./images/card_back.png')
front_img = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)

yes_button_img = tk.PhotoImage(file='./images/right.png')
yes_button = tk.Button(image=yes_button_img, highlightthickness=0, fg=BACKGROUND_COLOR, bd=0,
                       activebackground=BACKGROUND_COLOR, command=press_yes_button)
yes_button.grid(column=1, row=1)

no_button_img = tk.PhotoImage(file='./images/wrong.png')
no_button = tk.Button(image=no_button_img, highlightthickness=0, fg=BACKGROUND_COLOR, bd=0,
                      activebackground=BACKGROUND_COLOR, command=press_no_button)
no_button.grid(column=0, row=1)

language_text = canvas.create_text(400, 150, text='Title', font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text='Word', font=WORD_FONT)

canvas.mainloop()

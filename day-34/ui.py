from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,
                             bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='Amazon acquired Twitch', fill=THEME_COLOR,
                                                     font=("arial", 20, 'italic'))
        self.canvas.grid(padx=20, pady=20, row=1, columnspan=2, sticky="esew")

        self.score_text = Label(text='Score: 0',  bg=THEME_COLOR, fg="white", font=(
            "Arial", 10, 'bold'))

        self.score_text.grid(padx=20, pady=20, row=0, column=1)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image)
        self.true_button.grid(padx=20, pady=20, row=2, column=0)

        self.wrong_button = Button(image=self.false_image)
        self.wrong_button.grid(padx=20, pady=20, row=2, column=1)

        self.window.mainloop()

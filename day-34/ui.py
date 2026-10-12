from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR)
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="White",
            highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Amazon acquired Twitch',
            fill=THEME_COLOR,
            font=("arial", 20, 'italic')
        )
        self.canvas.grid(
            padx=20,
            pady=20,
            row=1,
            columnspan=2,
            sticky="esew")

        self.score_text = Label(
            text='Score: 0',
            bg=THEME_COLOR,
            fg="white",
            font=(
                "Arial",
                10,
                'bold'))

        self.score_text.grid(padx=20, pady=20, row=0, column=1)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=self.true_image,
            command=self.true_pressed
        )
        self.true_button.grid(padx=20, pady=20, row=2, column=0)

        self.false_button = Button(
            image=self.false_image,
            command=self.false_pressed
        )
        self.false_button.grid(padx=20, pady=20, row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def update_score(self):
        new_score = self.quiz.score
        self.score_text.config(text=f"Score: {new_score}")

    def check_remain_question(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            end_text = f"You've completed the quiz!\n\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=end_text)
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(0, self.color_change_green)
        self.window.after(500, self.color_change_white)
        if is_right:
            self.update_score()
            if self.quiz.still_has_questions():
                self.get_next_question()
            else:
                self.check_remain_question()
        else:
            self.window.after(0, self.color_change_red)
            self.window.after(500, self.color_change_white)
            if self.quiz.still_has_questions():
                self.get_next_question()
            else:
                self.check_remain_question()

    def color_change_green(self):
        self.canvas.config(bg="Green")

    def color_change_white(self):
        self.canvas.config(bg="White")

    def color_change_red(self):
        self.canvas.config(bg="Red")

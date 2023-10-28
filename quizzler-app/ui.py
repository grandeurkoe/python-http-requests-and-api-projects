from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUIZ_FONT = ("Arial", 15, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=("Arial", 11, "bold italic"),
                                 fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.question_canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125, font=QUIZ_FONT, width=260, text="Quiz "
                                                                                                        "Questions",
                                                              fill=THEME_COLOR)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, borderwidth=0, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, borderwidth=0, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        self.question_canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.question_canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def is_true(self):
        if self.quiz.check_answer("True"):
            self.question_canvas.configure(bg="green")
        else:
            self.question_canvas.configure(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.windows.after(ms=1000, func=self.get_next_question)

    def is_false(self):
        if self.quiz.check_answer("False"):
            self.question_canvas.configure(bg="green")
        else:
            self.question_canvas.configure(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.windows.after(ms=1000, func=self.get_next_question)

import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
SCORE_FONT = ('Arial', 11, 'normal')
QUESTION_FONT = ('Arial', 18, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.minsize(width=400, height=500)
        self.window.config(padx=20, pady=20,
                           background=THEME_COLOR)
        self.window.resizable(width=False, height=False)

        self.score_label = tkinter.Label(text='Score: 0',
                                         fg='white',
                                         background=THEME_COLOR,
                                         font=SCORE_FONT,
                                         highlightthickness=False)
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(background='white', width=360, height=250)
        self.canvas_text = self.canvas.create_text(180,
                                                   125,
                                                   width=320,
                                                   text='Here we will add the question',
                                                   font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.true_image = tkinter.PhotoImage(file='images/true.png')
        self.true = tkinter.Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)

        self.false_image = tkinter.PhotoImage(file='images/false.png')
        self.false = tkinter.Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))
        # self.get_next_question()

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('wrong'))
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background='lightgreen')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)

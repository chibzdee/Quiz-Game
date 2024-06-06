from tkinter import * # type: ignore
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

true_button = "C:/Users/PT WORLD/OneDrive/Desktop/100 days of python code/Day34/images/true.png"
false_button = "C:/Users/PT WORLD/OneDrive/Desktop/100 days of python code/Day34/images/false.png"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("arial", 15))
        self.score.grid(column=8, row=0)

        self.canvas = Canvas(width=500, height=250)
        self.question = self.canvas.create_text(250, 125, width=200,  text="", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=9, pady=20)

        self.true_image = PhotoImage(file=true_button)
        self.true = Button(image=self.true_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)
        
        self.false_image = PhotoImage(file=false_button)
        self.false = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=8, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():            
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)

        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
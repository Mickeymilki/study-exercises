import tkinter as tk

class TestSystemApp:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0

        self.window = tk.Tk()
        self.window.title("Test System")
        
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", command=lambda i=i: self.check_answer(i))
            button.pack()
            self.answer_buttons.append(button)

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.load_questions()
        self.display_question()

        self.window.mainloop()

    def load_questions(self):
        # Read questions from file and populate self.questions list
        with open("04.29_test\questions.txt", "r") as file:
            lines = file.readlines()
            question = ""
            answers = []
            for line in lines:
                line = line.strip()
                if line.startswith("q:"):
                    if question:
                        self.questions.append((question, answers))
                    question = line[2:]
                    answers = []
                elif line.startswith("+"):
                    answers.append(line)
                else:
                    answers.append(line)

            if question:
                self.questions.append((question, answers))

    def display_question(self):
        question, answers = self.questions[self.current_question_index]
        self.question_label.config(text=question)
        for i, answer in enumerate(answers):
            self.answer_buttons[i].config(text=answer)

    def check_answer(self, answer_index):
        question, answers = self.questions[self.current_question_index]
        if answers[answer_index].startswith("+"):
            self.correct_answers += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        total_questions = len(self.questions)
        percentage = (self.correct_answers / total_questions) * 100
        result_text = f"Правильных ответов: {self.correct_answers}/{total_questions}\nПроцент: {percentage:.2f}%"
        self.result_label.config(text=result_text)

app = TestSystemApp()
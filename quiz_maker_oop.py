import tkinter as tk
from tkinter import messagebox

class QuizMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Maker")
        self.root.geometry("400x450")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter your quiz question:").pack(pady=5)
        self.question_entry = tk.Entry(self.root, width=50)
        self.question_entry.pack()

        self.entries = {}
        for option in ['a', 'b', 'c', 'd']:
            tk.Label(self.root, text=f"Choice {option}:").pack()
            entry = tk.Entry(self.root, width=50)
            entry.pack()
            self.entries[option] = entry

        tk.Label(self.root, text="Correct answer (a, b, c, d):").pack(pady=5)
        self.correct_answer = tk.Entry(self.root, width=10)
        self.correct_answer.pack()
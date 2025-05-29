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

        tk.Button(self.root, text="Save Question", command=self.save_question,
                  bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)

    def save_question(self):
        question = self.question_entry.get()
        choices = {key: entry.get() for key, entry in self.entries.items()}
        answer = self.correct_answer.get().lower()

        if not question or not all(choices.values()) or not answer:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if answer not in choices:
            messagebox.showerror("Input Error", "Correct answer must be one of: a, b, c, d")
            return

        quiz_entry = (
            f"Question: {question}\n"
            + "\n".join(f"{k}) {v}" for k, v in choices.items())
            + f"\nAnswer) {answer}\n---\n"
        )

import tkinter as tk
from tkinter import messagebox
import random


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices  # Dict with keys 'a', 'b', 'c', 'd'
        self.answer = answer.lower()

    def is_correct(self, selected_option):
        return selected_option == self.answer
class QuizLoader:
    @staticmethod
    def load_from_file(filename):
        questions = []
        try:
            with open(filename, 'r') as file:
                content = file.read().strip()
                entries = content.split('---\n')
                for entry in entries:
                    lines = entry.strip().split('\n')
                    if len(lines) < 6:
                        continue  # skip incomplete entries
                    q_text = lines[0][len("Question: "):]
                    choices = {
                        'a': lines[1][3:],
                        'b': lines[2][3:],
                        'c': lines[3][3:],
                        'd': lines[4][3:]
                    }
                    answer = lines[5][len("Answer) "):].strip().lower()
                    questions.append(Question(q_text, choices, answer))
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} not found.")
        return questions
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

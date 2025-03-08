import tkinter as tk
from tkinter import messagebox
import random

# Sample advice list
advice_list = [
    "Stay positive and keep pushing forward!",
    "Take breaks and take care of yourself.",
    "Every day is a new opportunity to grow.",
    "Don’t be afraid to express your emotions.",
    "Learn from mistakes and move on.",
    "Happiness comes from within.",
    "Believe in yourself and your journey."
]

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Diary & Advice")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f8ff")
        
        self.label = tk.Label(root, text="My Diary", font=("Arial", 16, "bold"), bg="#f0f8ff")
        self.label.pack(pady=10)
        
        self.text_area = tk.Text(root, font=("Arial", 12), width=40, height=10)
        self.text_area.pack(pady=10)
        
        self.save_button = tk.Button(root, text="Save Entry", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.save_entry)
        self.save_button.pack(pady=5)
        
        self.advice_button = tk.Button(root, text="Get Advice", font=("Arial", 12), bg="#2196F3", fg="white", command=self.show_advice)
        self.advice_button.pack(pady=5)
    
    def save_entry(self):
        entry = self.text_area.get("1.0", tk.END).strip()
        if entry:
            with open("diary_entries.txt", "a") as file:
                file.write(entry + "\n---\n")
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Diary entry saved!")
        else:
            messagebox.showwarning("Warning", "Diary entry cannot be empty!")
    
    def show_advice(self):
        random_advice = random.choice(advice_list)
        messagebox.showinfo("Advice", random_advice)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()


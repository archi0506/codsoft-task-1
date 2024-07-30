import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry('400x400')

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List", font=('Helvetica', 16))
        self.title_label.pack(pady=10)

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(pady=10)

        self.listbox = tk.Listbox(self.tasks_frame, width=40, height=10)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.mark_button = tk.Button(root, text="Mark as Completed", command=self.mark_task)
        self.mark_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def mark_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks[selected_task_index] += " (completed)"
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
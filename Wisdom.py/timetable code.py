import tkinter as tk
from tkinter import messagebox
import random

# Sample study habit tracker
study_log = []

# Main App Window
root = tk.Tk()
root.title("StudySync - Student Planner")
root.geometry("600x600")

subjects = {}

# Add Subject and Topic
def add_subject():
    subject = subject_entry.get()
    topic = topic_entry.get()
    if subject and topic:
        subjects.setdefault(subject, []).append(topic)
        subject_entry.delete(0, tk.END)
        topic_entry.delete(0, tk.END)
        update_subject_list()
    else:
        messagebox.showwarning("Missing Info", "Please enter both subject and topic.")

# Generate Timetable
def generate_timetable():
    timetable.delete(1.0, tk.END)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        timetable.insert(tk.END, f"{day}:\n")
        for _ in range(2):  # 2 sessions per day
            subject = random.choice(list(subjects.keys()))
            topic = random.choice(subjects[subject])
            timetable.insert(tk.END, f"  - {subject}: {topic}\n")
        timetable.insert(tk.END, "\n")

# Update Subject List
def update_subject_list():
    subject_list.delete(0, tk.END)
    for subject, topics in subjects.items():
        subject_list.insert(tk.END, f"{subject}: {', '.join(topics)}")

# Log Study Habit
def log_study():
    study_log.append(1)
    messagebox.showinfo("Logged", "Study session recorded!")

# Show Stats
def show_stats():
    total_sessions = len(study_log)
    streak = len(study_log[-5:]) if total_sessions >= 5 else total_sessions
    messagebox.showinfo("Stats", f"Total Sessions: {total_sessions}\nRecent Streak: {streak}")

# UI Layout
tk.Label(root, text="Subject").pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

tk.Label(root, text="Topic").pack()
topic_entry = tk.Entry(root)
topic_entry.pack()

tk.Button(root, text="Add Subject & Topic", command=add_subject).pack()

tk.Label(root, text="Subjects Added").pack()
subject_list = tk.Listbox(root, height=5)
subject_list.pack()

tk.Button(root, text="Generate Timetable", command=generate_timetable).pack()
timetable = tk.Text(root, height=10, width=60)
timetable.pack()

tk.Button(root, text="Log Study Session", command=log_study).pack()
tk.Button(root, text="Show Study Stats", command=show_stats).pack()

root.mainloop()

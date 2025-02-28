import streamlit as st
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        file.writelines([task + "\n" for task in tasks])

# Streamlit UI
st.title("✅ To-Do List Web App")
st.subheader("Stay Organized with Your Tasks!")

tasks = load_tasks()

# Task Input
new_task = st.text_input("Enter a new task:")
if st.button("➕ Add Task"):
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        st.experimental_rerun()

# Display Tasks
st.write("### 📌 Your Tasks:")
if tasks:
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([0.8, 0.2])
        col1.write(f"✔️ {task}")
        if col2.button("❌", key=i):
            tasks.pop(i)
            save_tasks(tasks)
            st.experimental_rerun()
else:
    st.write("🎉 No tasks! Enjoy your day!")

st.write("---")
st.write("🚀 Built with Streamlit | #Python #Streamlit #WebApp")


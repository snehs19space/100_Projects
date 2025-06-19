import streamlit as st
import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def main():
    st.title("📝 To-Do List")

    tasks = load_tasks()

    with st.form("add_task_form"):
        new_task = st.text_input("New Task")
        submitted = st.form_submit_button("Add Task")
        if submitted and new_task:
            tasks.append({"task": new_task, "completed": False, "timestamp": str(datetime.now())})
            save_tasks(tasks)
            st.experimental_rerun()

    for i, t in enumerate(tasks):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        if t["completed"]:
            col1.markdown(f"~~{t['task']}~~")
        else:
            col1.markdown(t["task"])
        if col2.button("Edit", key=f"edit_{i}"):
            new_text = st.text_input("Edit task", value=t["task"], key=f"input_{i}")
            if new_text:
                t["task"] = new_text
                save_tasks(tasks)
                st.experimental_rerun()
        if col3.button("✅" if not t["completed"] else "↩️", key=f"done_{i}"):
            t["completed"] = not t["completed"]
            save_tasks(tasks)
            st.experimental_rerun()

if __name__ == "__main__":
    main()


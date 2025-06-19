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

    with st.form("task_form"):
        new_task = st.text_input("New Task")
        delete_task = st.text_input("Delete Task (by text)")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if new_task:
                tasks.append({"task": new_task, "completed": False, "timestamp": str(datetime.now())})
            if delete_task:
                tasks = [t for t in tasks if t["task"] != delete_task]
            save_tasks(tasks)
            st.rerun()

    for i, t in enumerate(tasks):
        col1, col2, col3, col4 = st.columns([0.5, 0.2, 0.2, 0.1])
        if t["completed"]:
            col1.markdown(f"<span style='color:gray'><s>{t['task']}</s></span>", unsafe_allow_html=True)
        else:
            col1.markdown(f"<span style='color:#2b8a3e'>{t['task']}</span>", unsafe_allow_html=True)

        if col2.button("Edit", key=f"edit_{i}"):
            new_text = st.text_input("Edit task", value=t["task"], key=f"input_{i}")
            if new_text:
                t["task"] = new_text
                save_tasks(tasks)
                st.rerun()

        if col3.button("✅" if not t["completed"] else "↩️", key=f"done_{i}"):
            t["completed"] = not t["completed"]
            save_tasks(tasks)
            st.rerun()

        if col4.button("🗑️", key=f"delete_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()

if __name__ == "__main__":
    main()

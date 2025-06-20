import streamlit as st
import json
from datetime import datetime, date

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
    completed_count = sum(1 for t in tasks if t["completed"])
    st.info(f"✅ Completed Tasks: {completed_count} / {len(tasks)}")

    if "new_task_input" not in st.session_state:
        st.session_state.new_task_input = ""
    if "due_date_input" not in st.session_state:
        st.session_state.due_date_input = date.today()

    with st.form("add_task_form"):
        new_task = st.text_input("New Task", key="new_task_input")
        due_date = st.date_input("Due Date", value=st.session_state.due_date_input, key="due_date_input")
        submitted = st.form_submit_button("Add Task")
        if submitted and new_task:
            tasks.append({
                "task": new_task,
                "completed": False,
                "timestamp": str(datetime.now()),
                "due_date": str(due_date)
                })
        save_tasks(tasks)
        new_task = st.text_input("New Task", key="new_task_input")
        due_date = st.date_input("Due Date", value=st.session_state.due_date_input, key="due_date_input")
        

    for i, t in enumerate(tasks):
        col1, col2, col3, col4 = st.columns([0.5, 0.2, 0.15, 0.15])

        task_display = f"{t['task']} (Due: {t.get('due_date', 'N/A')})"
        if t["completed"]:
            col1.markdown(f"<span style='color:gray'><s>{task_display}</s></span>", unsafe_allow_html=True)
        else:
            col1.markdown(f"<span style='color:#2b8a3e'>{task_display}</span>", unsafe_allow_html=True)

        if col2.button("✏️", key=f"edit_{i}"):
            new_text = st.text_input("Edit task", value=t["task"], key=f"input_{i}")
            if new_text:
                t["task"] = new_text
                save_tasks(tasks)
                st.rerun()

        if col3.button("✅" if not t["completed"] else "↩️", key=f"done_{i}"):
            t["completed"] = not t["completed"]
            save_tasks(tasks)
            st.rerun()

        if col4.button("Delete", key=f"delete_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()

if __name__ == "__main__":
    main()

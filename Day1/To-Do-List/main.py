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

    if "new_task" not in st.session_state:
        st.session_state.new_task = ""
    if "due_date" not in st.session_state:
        st.session_state.due_date = date.today()
    if "edit_task_index" not in st.session_state:
        st.session_state.edit_task_index = None
    if "edit_task_text" not in st.session_state:
        st.session_state.edit_task_text = ""

    with st.form("add_task_form"):
        st.session_state.new_task = st.text_input("New Task", value=st.session_state.new_task)
        st.session_state.due_date = st.date_input("Due Date", value=st.session_state.due_date)
        submitted = st.form_submit_button("Add Task")
        if submitted and st.session_state.new_task:
            tasks.append({
                "task": st.session_state.new_task,
                "completed": False,
                "timestamp": str(datetime.now()),
                "due_date": str(st.session_state.due_date)
            })
            save_tasks(tasks)
            st.session_state.new_task = ""
            st.session_state.due_date = date.today()
            st.rerun()

    for i, t in enumerate(tasks):
        col1, col2, col3, col4 = st.columns([0.5, 0.2, 0.15, 0.15])

        task_display = f"{t['task']} (Due: {t.get('due_date', 'N/A')})"
        if t["completed"]:
            col1.markdown(f"<span style='color:gray'><s>{task_display}</s></span>", unsafe_allow_html=True)
        else:
            col1.markdown(f"<span style='color:#2b8a3e'>{task_display}</span>", unsafe_allow_html=True)

        if col2.button("✏️", key=f"edit_btn_{i}"):
            st.session_state.edit_task_index = i
            st.session_state.edit_task_text = t["task"]

        if st.session_state.edit_task_index == i:
            new_text = st.text_input("Edit task", value=st.session_state.edit_task_text, key=f"edit_input_{i}")
            if st.button("Save", key=f"save_{i}"):
                tasks[i]["task"] = new_text
                st.session_state.edit_task_index = None
                st.session_state.edit_task_text = ""
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

import streamlit as st
import functions

todos = functions.open_json()


def add_todo():
    if st.session_state["new_todo"] != '':
        todo = st.session_state["new_todo"]
        todos.append(todo)
        functions.dump_json(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    todo_key = f"{todo}{index}"
    checkbox = st.checkbox(label=todo, key=todo_key)
    if checkbox:
        todos.pop(index)
        functions.dump_json(todos)
        del st.session_state[todo_key]
        st.experimental_rerun()

st.text_input(label="Add:", label_visibility="hidden",
              placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

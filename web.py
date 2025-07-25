import streamlit as st
import functions

todos = functions.get_todos("todos.txt")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("To <b>add</b> a todo type it in and press enter", unsafe_allow_html=True)
st.write("To <b>delete</b> a todo press the checkbox on the todo", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


import streamlit as st
import functions
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My First To Do App")
st.subheader("Welcome to my To Do list")
st.write("My To Do list helps me to improve my learning process")

# st.checkbox("Learn Python fundamentals")
# st.checkbox("Master Python advanced level")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a Todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')



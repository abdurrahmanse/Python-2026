import streamlit as st

with st.chat_message("user"):
    st.write("What is a variable?")

with st.chat_message("assistant"):
    st.write(
        "A variable is a container that holds a value. It can be used to store data and manipulate it throughout a program. In programming, variables are essential for storing information that can change during the execution of a program."
    )

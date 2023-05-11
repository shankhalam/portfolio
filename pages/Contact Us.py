import streamlit as st

st.header("Contact Us")

with st.form(key='email_form'):
    email = st.text_input("Enter your Email")
    message = st.text_area("Enter your Message")
    button = st.form_submit_button("Submit")
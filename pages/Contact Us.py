import streamlit as st
from send_mail import send_mail

st.header("Contact Us")

with st.form(key='email_form'):
    email = st.text_input("Enter your Email")
    raw_message = st.text_area("Enter your Message")
    message = f"""\
Subject: New Message from Portfolio Website

From: {email}
{raw_message}    
"""
    button = st.form_submit_button("Submit")

    if button:
        send_mail(message)
        st.info("Your message send successfully.Get back you soon.")
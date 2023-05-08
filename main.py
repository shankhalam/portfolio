import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Shan Khalam")
    content = """
    I am Shan Khalam, a software developer at Swophistic Software Solutions. Although I graduated as a pharmacist 
    from Kerala University, my passion for programming led me to my current position. I mainly specialize in Python 
    and possess a strong understanding of Angular and Ionic frameworks. I am particularly interested in developing 
    desktop and web applications. Additionally, I enjoy creating both dynamic and static websites using WordPress and 
    Bootstrap.
    """
    st.info(content)

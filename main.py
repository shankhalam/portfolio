import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Shan Khalam")
    content = """
    I am Shan Khalam, a Software Developer at Swophistic Software Solutions. Although I graduated as a pharmacist 
    from Kerala University, my passion for programming led me to my current position. I mainly specialize in Python 
    and possess a strong understanding of Angular and Ionic frameworks. I am particularly interested in developing 
    desktop and web applications. Additionally, I enjoy creating both dynamic and static websites using WordPress and 
    Bootstrap.
    """
    st.info(content)

content2 = """Below you can find some Apps which i made from Python. Feel free to contact for more information about 
any of the apps."""
st.write(content2)

df = pandas.read_csv('data.csv', sep=';')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row['image'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])



import streamlit as st

st.set_page_config(page_title="My mega-webpage", page_icon="🚀", layout="wide")

st.title("Welcome to my webpage🙃")

tab1, tab2 = st.tabs(["About Me", "My tool"])

with tab1:
    st.header("Get to know the autor")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn.britannica.com/36/147936-050-8E84B614/Dwayne-Johnson.jpg", width=200)
    with col2:
        st.subheader("Yo, im future python dev")
        st.write("Im studying in the IT Step Academy")
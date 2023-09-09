import streamlit as st

st.write(
    f'<div style="text-align: center;"><h1>Contact</h1></div>',
    unsafe_allow_html=True
)
st.divider()

column1, column2, column3 = st.columns(3)


with column1:
    st.image("assets/gmailjpg.jpg", width=50)
    st.write("[Gmail](mailto:ferreyralorenzo2@gmail.com)")

with column2:
    st.image("assets/linkedin.png", width=50)
    st.write("[LinkedIn](https://www.linkedin.com/in/lorenzo-ferreyra/)")

with column3:
    st.image("assets/git.png", width=50)
    st.write("[GitHub](https://github.com/LorenzoFerreyra)")
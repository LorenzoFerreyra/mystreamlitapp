import streamlit as st


st.set_page_config(page_title="Lorenzo Ferreyra",
                   page_icon="👋",
                   )

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #333333;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("This is Lorenzo's personal website.")
st.divider()
st.sidebar.success("Welcome!")

st.write("""
         Hi there!
         My name is Lorenzo Ferreyra, a data analyst based in Argentina with experience in a number of industries.
         This website serves as a platform for showcasing my projects and tech blogs.
         If you're looking for data consultancy services, feel free to connect with me!
         I'm here to help you make informed data-driven decisions.
         """)

st.divider()

def pie_de_pagina():

    column1, column2, column3 = st.sidebar.columns(3)


    with column1:
        st.image("assets/gmailjpg.jpg", width=50)
        st.write("[Gmail](mailto:ferreyralorenzo2@gmail.com)")

    with column2:
        st.image("assets/linkedin.png", width=50)
        st.write("[LinkedIn](https://www.linkedin.com/in/lorenzo-ferreyra/)")

    with column3:
        st.image("assets/git.png", width=50)
        st.write("[GitHub](https://github.com/LorenzoFerreyra)")
pie_de_pagina()







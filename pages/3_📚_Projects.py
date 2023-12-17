import streamlit as st

st.write(
    f'<div style="text-align: center;"><h1>My projects</h1></div>',
    unsafe_allow_html=True
)
st.divider()
st.markdown("#### Things I worked on")

# Proyecto 1
st.image("assets/social_data.jpg", caption="Shiny App for analyzing social data in R", use_column_width=True)
st.markdown("[GitHub Repo](https://github.com/LorenzoFerreyra/shinyapp)")

# Proyecto 2
st.image("assets/is-crypto-dead.jpeg", caption="Crypto Tracker Web App in Python + Django", use_column_width=True)
st.markdown("[GitHub Repo](https://github.com/esgaelramos/YourMoneyTrackerMail) | [Sitio web](https://mymoneyup.tech/)")
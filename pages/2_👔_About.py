import streamlit as st

st.write(
    f'<div style="text-align: center;"><h1>About me</h1></div>',
    unsafe_allow_html=True
)
st.divider()


st.markdown("#### The essentials")

st.text("education")
st.markdown("* BA in Sociology (computationally oriented), 2019-2024. Universidad de Flores")
st.markdown("* BA in English, 2015-2019. Instituto Almirante Brown")
st.text("work")
st.markdown("* Data Analyst, 2023-present (Aardvark Partners, USA)")
st.markdown("* Junior Data Analyst, 2022 (Qendar, Argentina)")
st.markdown("* English Translator & Interpreter, 2020-2021 (Freelance, Argentina)")

st.write("[Download CV!](assets/Lorenzo_Ferreyra_CV_2023.pdf)", unsafe_allow_html=True)
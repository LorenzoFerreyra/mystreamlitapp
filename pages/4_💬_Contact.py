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


st.header(":mailbox: Get in touch with me!")


contact_form = """
<form action="https://formsubmit.co/332d019338e1abc0ad41921a21a97e07" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
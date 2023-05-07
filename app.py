import streamlit as st
from PIL import Image

st.set_page_config(page_title="Henry Junior Yiga | Portfolio", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style.css.txt")

img_contact_form = Image.open("lab_pic.jpg")

with st.container():
    st.subheader("About Me")
    st.markdown("""I am a tri-lingual passionate research scientist with a background in biochemistry and a passion for data science and computer programming. Fluent in English, French, and Spanish, I love adventure, travel, reading, and writing. In fact, I recently published a children's graphics book that sensitizes readers about COVID-19 and future pandemics. If you're interested in the book, feel free to reach out to me at `nafti.yiga@gmail.com`.""")
    st.markdown("""In addition to my writing and research work, I have developed expertise in data analysis and programming. I use tools such as Python, R, and Power BI to analyze and visualize data, and I have completed several projects in the areas of machine learning, data mining, and statistical analysis. My experience in data science complements my biochemistry research, and enables me to extract meaningful insights from complex datasets, and to develop predictive models that can aid in drug discovery and protein engineering.""")
    st.markdown("""I hold a Master's degree in Biochemistry, and I have been working on research projects related to molecular biology, drug discovery, and protein engineering. I am currently working on getting my thesis published, and you can find a copy to it on my Github [Masters Thesis](https://github.com/naftie22/My-Website/raw/main/Yiga-Henry-Junior-Memoir[1681].pdf). If you would like to learn more about my research or my data science projects, feel free to reach out to me via my [LinkedIn profile](https://linkedin.com/in/henry-junior-yiga-6b691b231) or [Github](https://github.com/naftie22).""")

with st.container():
    image_column, = st.columns(1)
    with image_column:
        st.image(img_contact_form)
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/nafti.yiga@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placehoder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

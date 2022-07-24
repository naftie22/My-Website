import streamlit as st
from PIL import Image



st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)
local_css("style.css.txt")

img_contact_form = Image.open("programmer-working-with-program-code-picture-id1075599562-1.jpg")

with st.container():

	st.subheader("Hi, Iam Henry Junior Yiga :wave:")
	st.title(" A Tech Enthusiast from Uganda")
	st.write("lam a scientist and public health expert with scientific, programming and language skills.")
	st.write("To find out more about me i have shared a link to my linkedin account below")
	st.write("I am also passionate about tech and have skills in python,Django,C#,ASP.NETCORE,Git and mySQL my github is shared below.")
	st.write(" Learn more on linkedin > (https://linkedin.com/in/henry-junior-yiga-6b691b231)")
	st.write(" Learn more on github > (https://github.com/naftie22)")

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("What I do")
		st.write("##")
		st.write(
			"""
			Am a tri-lingual passionate biochemist(Masters Degree) fluent in English, French and Spanish.
			I love adventure, travel reading & writing. I recently published a children's graphics book sensitising about
			covid-19 and future pandemics. If interested in the book reach out to me 'nafti.yiga@gmail.com' 
			 I also picked up interest in tech and programming; with skills in python and C# with their respective frameworks and some of my projects so far 
			can be found on my github account whose link i put above.
		
			"""
		)
	with right_column:
		st.empty()

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

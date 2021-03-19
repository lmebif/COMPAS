import streamlit as st
import time
from annotated_text import annotated_text as at

my_placeholder = st.empty()

if my_placeholder:
	a = st.checkbox('Arrest me',value=False)

	if a:
		st.write("You've been arrested.")
		#time.sleep(2)
		st.write("Officer Gary will ask you a few questions that you must answer truthfully.")
		#time.sleep(2)
		st.spinner()

		with st.spinner(text='Officer Gary will be with you any second'):
			st.success('Officer Gary enters the room')
			#time.sleep(2)
			at(("I am officer Gary and I need you to answer the following questions:","","#faa"))
			#time.sleep(2)
			at(("How old are you?","","#faa"))
			#time.sleep(1)
			
			age = st.slider('Enter your age',min_value=0)

			#time.sleep(3)


			s = "Aha, so you're " + str(age) + " years old. Did your parents ever tell you how big a dumb-dumb you are?"

			at((s,"","#faa"))

			s = "Okay, now tell me how many of your friends smoke weed"

			at((s,"","#faa"))

			friends = st.slider("Number of pot-head friends",min_value=0,max_value=10)

			s = "Was one of your parents ever sent to jail or prison?"

			at((s,"","#faa"))

			parents_y = st.checkbox("Yes")
			if not parents_y:
				parents_n = st.checkbox("No")

			s = "How often do you get in fights at school?"

			at((s,"","#faa"))

			fights = st.slider("Fights per day",min_value=0,max_value=10)

			s = "Now, I will read a few statements out loud. You just have to tell me whether you agree or disagree"

			at((s,"","#faa"))

			s = "Statement 1:"
			s1 = "A hungry person has a right to steal"
			at((s,"","#faa"),(s1,"","#fea"))

			agree_1 = st.selectbox('Statement 1',['Agree', 'Disagree'])

			st.write('\n'*5)

			s = "Statement 2:"
			s1 = "If people make me angry or make me lose my temper, I can be dangerous"
			at((s,"","#faa"),(s1,"","#fea"))

			agree_2 = st.selectbox('Statement 2',['Agree', 'Disagree'])

			s = "Statement 3:"
			s1 = "Pineapple is a socially acceptable pizza topping"
			at((s,"","#faa"),(s1,"","#fea"))

			agree_3 = st.selectbox('Statement 3',['Agree', 'Disagree'])


			
			f = age + friends + fights + int(bool(agree_1)) + int(bool(agree_2)) + int(bool(agree_3))


			score = f%8+2

			s = "You're risk score is " + str(score)

			at((s,"","#faa"))


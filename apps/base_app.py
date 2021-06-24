"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Where was Thuto used ?")

	# st.text("We worked with Toyota where they had") 
	# st.text("a problem of identifying the most") 
	# st.text("suitable product to adverstise")
	# st.text("since they have wide range of products.")

	st.markdown("""
We worked with Toyota where they had a problem of identifying the most
suitable product to advertise since they have a wide range of products and  customers

We were tasked to build a model that can accuratley classify which products 
to show customer based on their beleives towards climate change.

""")




	  


	
	tweet_text = st.text_area("","Enter tweet so it can classified")

	if st.button("Classify"):
			# Transforming user input with vectorizer
			#vect_text = tweet_cv.transform([tweet_text]).toarray()
			tweet_text = [tweet_text]
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/ovr.pkl"),"rb"))
			prediction = predictor.predict(tweet_text)
			#st.image('hybrid1.2.png', width=500)
			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			#st.success("Text Categorized as: {}".format(prediction))

			#st.title(prediction[0])

			if (prediction[0] == -1) :
				st.title("Based on tweet you don't believe in climate-change")
				st.subheader("Have a look at some gas cars available from Toyota")
				st.image('a1.png', width=500)
				st.image('a2.png', width=500)
				st.image('a3.png', width=500)
				
				
			elif (prediction[0]==0) :
				st.title("Based on tweet you're nuetral towards climate-change")
				st.subheader("Take a look at some Hybrid cars available from Toyota")
				st.image('h1.png', width=500)
				st.image('h2.png', width=500)
				st.image('h3.png', width=500)
				
			else :
				#st.image('img.jpg', width=60)
				st.title("Based on tweet you believe in  climate-change")
				st.subheader("Take a look at some Electric cars available from Toyota")
				st.image('p1.png', width=500)
				st.image('p2.png', width=500)
				
				
# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()

#streamlit run base_app.py
#user_tweet = 'climate change was man made' #negative
#user_tweet = 'believe in global warming climate change' #nuetral
#user_tweet = 'climate change australia donald trump' #pro

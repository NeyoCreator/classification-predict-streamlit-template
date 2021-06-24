import streamlit as st


def research_page():
    header = st.beta_container()
    body = st.beta_container()
    body2 = st.beta_container()
    body3 = st.beta_container()
    body4 = st.beta_container()
   
    col1,col2 = st.beta_columns(2) #Two containers

   
    with header:
        st.title("Research")


    with body:
         st.text("The research based on Toyota project")
         st.text("where we had identify the correct products to adverstise")
         st.text("to twitter users based on beliefs they held on ")
         st.text("cimate change")
         #st.image('pro.png', width=500)


       
    with body2:
        st.text("                                                                        ")
        st.title("Overview of data")
        st.text(" This was the seniment in which we had ") 
        st.text("to classify our text into.")
        st.text("-1 : User does not believe in climate change")
        st.text("0  : User is neutral towards climate change")
        st.text("1  : User is believes in climate change")
        st.text("2  : User is believes in climate change and links factual news")
        st.image('bar_graph_overall.png', width=500)

    with body3:
         st.title("Exploring Wordclouds")
         st.text("We used word-clouds to view the")
         st.text("the most frequent words within the dataset")
         st.text("to give us a better understanding of how our")
         st.text("data looks.")
         st.image('word_cloud.png', width=700)


    with body4:
         st.title("Exploring Hashtags")
         st.text("We extracted and viewed the most frequent Hashtags.")
         st.text("Since hashtags reach a wider audience they can give ")
         st.text("us better insight into the concensus of our customers")
         st.markdown("**Anti-climate change #Hashtags**")
         st.image('negative_bar.png', width=500)
         st.markdown("**Pro-climate change #Hashtags**")
         st.image('positive_bar.png', width=500)

         
import streamlit as st


def about_page():
    header = st.beta_container()
    body = st.beta_container()
    body2 = st.beta_container()
   
    col1,col2 = st.beta_columns(2) #Two containers
   
    with header:
        st.title("How does it work?")


    with body:

         st.markdown(""" It receives a customers social media data such as twitter posts,
         tries find patterns within the data and classifies it
         based on a given sentiment.


         
         """)
         
         st.image('pro.png', width=500)


       
    with body2:
        st.text("                                                                        ")
        st.title("Why do we use it?")
    
        st.markdown(""" To give companies a better understanding to what their clients want, as a result we
        strenghthen the relationship between the customer and the company.
         
         """)

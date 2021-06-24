import streamlit as st


def about_page():
    header = st.beta_container()
    body = st.beta_container()
    body2 = st.beta_container()
    body3 = st.beta_container()
    images =st.beta_container()

    col1,col2 = st.beta_columns(2) #Two containers

   
   
   
   

   
   
    with header:
        st.title("How does it work?")


    with body:
         st.text("It gets a customers social media data")
         st.text("finds patterns within the data and")
         st.text("classifies it based on a given")
         st.text("sentiment.")
         st.image('pro.png', width=500)


    # with header:
    #     st.title("Why do we do what we do?")


    # with body:
    #     st.text(" To give companies better understanding") 
    #     st.text("to what thier clients want.")

       

        

    with body2:
        st.text("                                                                        ")
        st.title("Why do we do what we do?")
        st.text(" To give companies better understanding") 
        st.text("to what thier clients want.")

        st.text("                                                                        ")
        st.markdown("**Contacts **")
        st.text("email us on: classificationMM2@dataexperts.co.za")
        st.text("Tel: 0154 222 972")
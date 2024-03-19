import streamlit as st
import helper
import pickle
st.header("Duplicate Question Pair")
st.subheader("please enter both the question to check both have same meaning or not")
model = pickle.load(open('model.pkl','rb'))
q1 = st.text_input("Enter Question 1")
q2 = st.text_input("Enter Question 2")

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.write('The meanings of the two questions are same.')
    else:
        st.write('The meanings of the two questions are different.')

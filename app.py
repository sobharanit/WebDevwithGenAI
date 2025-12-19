import streamlit as st
import google.generativeai as genai
st.title("Final FDP Session Task 19thDec2025")
user_input = st.text_input("Aske me Anything:")

genai.configure(api_key="AIzaSyC1sNIcsVB--wiVjkC_k_BnIvpci1i6LBA")
model = genai.GenerativeModel("models/gemini-2.5-flash")
 
if user_input:
    response = model.generate_content(user_input)
    st.write("response from genai")
    st.write(response.text)
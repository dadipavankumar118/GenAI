import streamlit as st
from openai import OpenAI

f = open(r'C:\Users\pavan\Data_Science_Internship\Projects\Project-3(GenAI App - AI Code Reviewer)\GenAI App_AI Code Reviewer_API_Key.txt')
OPENAI_API_KEY = f.read()

st.title("AI Code Reviewer")
st.subheader("Finds bugs and errors in code and rewritting the corrrected code")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_area("Enter a Code")

if st.button("Generate") == True:
    st.snow()
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)
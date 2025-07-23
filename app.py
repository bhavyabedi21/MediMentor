import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configuring the Key and initiating the model
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))
model = genai.GenerativeModel('gemini-2-pro') 

# Sidebar
st.sidebar.subheader("Calculate your BMI")
weight = st.sidebar.text_input("Enter your weight (in kgs):")
height = st.sidebar.text_input("Enter your height (in cms):")
result=""
bmi_submit = st.sidebar.button("Calculate BMI")
def BMI(weight,height):
    result = (float(weight)/(float(height)/100)**2)
    return result
if bmi_submit:
    result = round(BMI(weight,height),4)
    st.sidebar.write("Your BMI is:")
    st.sidebar.markdown(f":green[{result} kg/m^2]")
else:
    st.sidebar.write("Your BMI is:")
    st.sidebar.markdown("")

notes = f'''
The BMI value can be interpreted as:
* Underweight: BMI < 18.5
* Normal Weight: BMI 18.5 - 24.9
* Overweight: BMI 25 - 29.9
* Obese: BMI > 30
'''
st.sidebar.write(notes)
st.sidebar.markdown("👨‍💻 Created by: :blue[Bhavya Bedi]")


# Designing the Front End (right side)
st.header("🧑‍⚕️ MediMentor:blue[.ai]: Your Trusted Health Advisor",divider="green")
input = st.text_input("Hi! I am your Health Advisor 💊. Ask me about your Health, Diseases, and Fitness only ⚕️")

def guide_me(input):
    if input!= '':
        prompt = f'''Act as a Dietician, Health Coach, and Expert and address
        the queries, questions, apprehensions related to health, fitness, diseases, 
        and things associated with it with empathy towards the user. Any query or question that is 
        not related to health, pass the following message - "I am a Heathcare advisor. I can only answer questions related to Health, Fitness, and Diet."
        If someone asks about the medicine for any ailment, just pass the message -
        "I am an AI model and cannot answer question related to diagnosis and medicine. Please reachout to a Physician"
        '''
        response = model.generate_content(prompt+input).text
        return (response)
    else:
        return st.write("Please write the question you want to ask")
    

submit = st.button("🚀 Get AI-Powered Insights")
if submit:
    response = guide_me(input)
    st.markdown("### ✨ Generated Output")
    st.write(response)

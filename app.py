import streamlit as st

st.title("✈️ Flight Booking Chatbot")

# Simple chat UI
user_input = st.text_input("Ask me about flights:")

def chatbot_response(query):
    # Replace this with your actual logic from Colab
    if "flight" in query.lower():
        return "Sure! Where do you want to go?"
    return "I can help you book flights!"

if user_input:
    response = chatbot_response(user_input)
    st.write("🤖:", response)

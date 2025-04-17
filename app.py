# app.py

import streamlit as st
from helpers import get_ai_response, suggest_activity

# Set page configuration for Streamlit app
st.set_page_config(page_title="MindSpace 🌿", page_icon="🌿", layout="centered")

# Optional: Logo and Header
#st.image("assets/logo.png", width=200)  # Optional: Add your logo here
st.title("🌿 Welcome to MindSpace – Your Digital Wellness Buddy 🌿")

# App description
st.markdown("""
Hey there! Let's check in with your mood and screen time. I'm here to help you reset and feel your best ✨.
We’re all about balance, not disconnecting.
""")

# User inputs
mood = st.text_input("How are you feeling right now?", "e.g., stressed, anxious, happy, bored")
screen_time = st.slider("How many hours have you been on your phone today?", 0, 12, 1)

# Get personalized advice and activity suggestion when the button is clicked
if st.button("Get My Reset Plan 💬"):
    with st.spinner("Talking to your wellness buddy..."):
        # Call helper function to get advice from Azure OpenAI
        advice = get_ai_response(mood, screen_time)
        # Get a random mindful activity suggestion
        activity = suggest_activity()

        # Display the advice and suggested activity
        st.success("Here's your personalized wellness plan 👇")
        st.markdown(f"**🧠 Wellness Advice:**\n\n{advice}")
        st.markdown(f"**🎨 Reset Suggestion:**\n\n{activity}")
        
        # Additional friendly reminder
        st.markdown("\n*Remember, it's all about balance. Let's keep it chill and reset whenever you need!* 🌿")

# Footer with helpful links
st.markdown("""
---  
MindSpace is here for you. Need help? [Reach out to mental health professionals](https://www.mentalhealth.gov).
""")

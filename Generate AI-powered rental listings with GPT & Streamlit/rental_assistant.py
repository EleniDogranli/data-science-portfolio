import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Rental Assistant", page_icon="🏠")

st.title("🏠 AI Rental Assistant")
st.write("Provide the characteristics of your property and get a ready-made rental ad!")

# Φόρμα εισόδου
with st.form("property_form"):
    location = st.text_input("📍 Location", "Athens, Greece - Koukaki")
    property_type = st.selectbox("🏢 Property Type", ["Studio", "1-bedroom apartment", "2-bedroom apartment", "Loft"])
    size_sqm = st.number_input("📏 Square Meters", min_value=10, max_value=300, value=45)
    features = st.multiselect("✔️ Services", ["Balcony", "AC", "Furnished", "Wi-Fi", "Near metro", "Pets allowed", "Washing machine"])
    submit = st.form_submit_button("🎯 Create an Ad")

# Όταν πατηθεί το κουμπί
if submit:
    with st.spinner("🧠 Create an ad via GPT..."):

        # Δημιουργία prompt
        prompt = f"""
You are an expert real estate assistant.

Suggest a monthly rent range (in €) and create a rental listing title and description based on the following property info:

Location: {location}
Property type: {property_type}
Size: {size_sqm} sqm
Features: {", ".join(features)}

Return the response in the following format:
---
Rent Estimate: €[min]–[max]
Title: ...
Description: ...
---
"""

        # Call GPT
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        # show results
        st.success("✅ Your ad has been created!")
        st.markdown(response.choices[0].message.content)

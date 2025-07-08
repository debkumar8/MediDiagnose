import streamlit as st
import requests

st.title("🩺 AI Medical Diagnostics Assistant")

symptom_input = st.text_area("Describe your symptoms") # what ever text we written here, it will  go the below button and will hit the url

if st.button("Get Diagnosis"):
    state_input = {
        "input": symptom_input,
        "symptom_area": "",    # These are blank 
        "diagnosis": ""
    }
    
    
    try:
        response = requests.post(
            "https://medidiag.onrender.com/diagnose/invoke", 
            headers={"Content-Type": "application/json"},
            json={"input": state_input}
        )

        # 🔍 DEBUG: Show full raw content before parsing
        st.code(f"Status Code: {response.status_code}")
        st.code(f"Raw Text: {response.text}")

        data = response.json()  # This fails if .text is not valid JSON

        st.subheader("Symptom Area Detected:")
        st.write(data.get("symptom_area", "N/A"))

        st.subheader("AI Diagnosis Suggestion:")
        st.write(data.get("diagnosis", "N/A"))

    except Exception as e:
        st.error(f"❌ Failed to get diagnosis:\n{e}")

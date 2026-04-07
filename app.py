import streamlit as st
import joblib
import json
import numpy as np
from form import show_form

# Page setup
st.set_page_config(page_title="Cardiovascular Risk Coach", page_icon="❤️")
st.title("❤️ Cardiovascular Risk Coach")

# Load model and deployment info
@st.cache_resource
def load_model():
    model = joblib.load('models/best_model.pkl')
    with open('models/feature_names.json', 'r') as f:
        features = json.load(f)
    with open('models/deployment_info.json', 'r') as f:
        info = json.load(f)
    return model, features, info

model, feature_names, deployment_info = load_model()
threshold = deployment_info['threshold']

# Session state init
if "patient_data" not in st.session_state:
    st.session_state.patient_data = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show form if no data yet
if st.session_state.patient_data is None:
    if show_form():
        st.rerun()
else:
    # Show patient data
    with st.expander("📋 Patient Data"):
        st.write(f"Name: {st.session_state.patient_data['name']}")
        st.write(f"Sex: {'Male' if st.session_state.patient_data['male'] == 1 else 'Female'}")
        st.write(f"Age: {st.session_state.patient_data['age']} years")
        st.write(f"Total cholesterol: {st.session_state.patient_data['totChol']} mg/dL")
        st.write(f"Hypertension: {'Yes' if st.session_state.patient_data['prevalentHyp'] == 1 else 'No'}")
        st.write(f"Cigarettes per day: {st.session_state.patient_data['cigsPerDay']}")
    
    st.markdown("---")
    st.subheader("Risk Assessment")
    
    # Prepare features for prediction
    features = np.array([[
        st.session_state.patient_data['male'],
        st.session_state.patient_data['age'],
        st.session_state.patient_data['totChol'],
        st.session_state.patient_data['prevalentHyp'],
        st.session_state.patient_data['cigsPerDay']
    ]])
    
    # Predict risk
    risk_score = model.predict_proba(features)[0][1]
    risk_percent = risk_score * 100
    risk_level = "High Risk" if risk_score >= threshold else "Low Risk"
    
    st.metric("10-Year Cardiovascular Risk", f"{risk_percent:.1f}%")
    st.subheader(f"Assessment: {risk_level}")
    
    if risk_level == "High Risk":
        st.warning("Your estimated risk is elevated. Consider discussing prevention strategies with your doctor.")
    else:
        st.success("Your estimated risk is low. Keep up with healthy habits!")
    
    st.markdown("---")
    st.subheader("💬 Talk to your coach")
    
    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # If chat is empty, coach starts with a greeting
    if len(st.session_state.messages) == 0:
        with st.chat_message("assistant"):
            with st.spinner("Preparing your personalized recommendations..."):
                from coach import call_coach
                first_message = call_coach(st.session_state.patient_data, [])
                st.markdown(first_message)
                st.session_state.messages.append({"role": "assistant", "content": first_message})
    
    # User input
    if prompt := st.chat_input("Write your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                from coach import call_coach
                reply = call_coach(st.session_state.patient_data, st.session_state.messages)
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
    
    # Reset button
    if st.button("🔄 New Patient"):
        st.session_state.patient_data = None
        st.session_state.messages = []
        st.rerun()
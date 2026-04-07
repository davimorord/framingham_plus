import streamlit as st

def show_form():
    with st.form("risk_form"):
        st.subheader("Patient Information")
        
        name = st.text_input("Full name")
        
        col1, col2 = st.columns(2)
        with col1:
            male = st.selectbox("Sex", ["Female", "Male"])
            age = st.number_input("Age (years)", 20, 100, 50)
        with col2:
            totChol = st.number_input("Total cholesterol (mg/dL)", 100, 400, 200)
            prevalentHyp = st.selectbox("Hypertension", ["No", "Yes"])
            cigsPerDay = st.number_input("Cigarettes per day", 0, 60, 0)
        
        submitted = st.form_submit_button("Calculate Risk")
        
        if submitted:
            st.session_state["patient_data"] = {
                "name": name,
                "male": 1 if male == "Male" else 0,
                "age": age,
                "totChol": totChol,
                "prevalentHyp": 1 if prevalentHyp == "Yes" else 0,
                "cigsPerDay": cigsPerDay
            }
            st.success(f"Data saved for {name}")
            return True
    return False
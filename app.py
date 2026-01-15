import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model/churn_model.pkl")
columns = joblib.load("model/columns.pkl")

st.title("Customer Churn Prediction System")

tenure = st.slider("Tenure",0,72)
monthly = st.slider("Monthly Charges",0,200)
contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
internet = st.selectbox("Internet Service",["DSL","Fiber optic","No"])
tech = st.selectbox("Tech Support",["Yes","No"])

input_data = {
    "tenure":tenure,
    "MonthlyCharges":monthly,
    "Contract_"+contract:1,
    "InternetService_"+internet:1,
    "TechSupport_"+tech:1
}

df = pd.DataFrame([input_data])
df = df.reindex(columns=columns, fill_value=0)

if st.button("Predict Churn"):
    pred = model.predict(df)[0]
    if pred==1:
        st.error("High Risk Customer ❌")
    else:
        st.success("Low Risk Customer ✅")

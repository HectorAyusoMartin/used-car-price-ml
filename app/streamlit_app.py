import streamlit as st
import sys
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_PATH))

from src.predict import predict_price


st.set_page_config(
    page_title="Used Car Price Predictor",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #556B5D;
}
</style>
""", unsafe_allow_html=True)

st.title("Second-Hand Vehicle Price Predictor")
st.write("Estimate the selling price of a second-hand vehicle.")


st.caption("Machine Learning project for used car valuation")


name = st.text_input("Vehicle Name", "Maruti Swift Dzire VDI")

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2014
)

km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=145500
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner History",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)


if st.button("Predict Price"):

    input_data = {
        "name": name,
        "year": year,
        "km_driven": km_driven,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner
    }

    prediction = predict_price(input_data)

    st.subheader("Estimated Price")
    st.success(f"{prediction:,.0f}")
    st.markdown("---")
    st.caption("Developed by Héctor Ayuso Martín")
    st.caption("LinkedIn: https://www.linkedin.com/in/hector-ayuso-martin/")   
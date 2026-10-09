import base64
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


APP_DIR = Path(__file__).resolve().parent

# Show the local background image.
bg_image = base64.b64encode((APP_DIR / "bg.jpg").read_bytes()).decode()
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255,255,255,.78), rgba(255,255,255,.78)),
                    url("data:image/jpeg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the saved model pipeline and species label encoder.
model = joblib.load(APP_DIR / "Model" / "penguin_model.pkl")
label_encoder = joblib.load(APP_DIR / "Model" / "label_encoder.pkl")

st.title("Penguin Species Predictor")
st.write("Enter the penguin's measurements to predict its species.")

with st.form("prediction_form"):
    island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
    sex = st.selectbox("Sex", ["Female", "Male"])
    culmen_length = st.number_input("Culmen length (mm)", 32.4, 56.0, 44.0)
    culmen_depth = st.number_input("Culmen depth (mm)", 13.0, 21.4, 17.0)
    flipper_length = st.number_input("Flipper length (mm)", 175, 235, 200)
    body_mass = st.number_input("Body mass (g)", 2830, 6317, 4000)
    predict = st.form_submit_button("Predict species")

if predict:
    penguin = pd.DataFrame(
        [[island, culmen_length, culmen_depth, flipper_length, body_mass, sex]],
        columns=[
            "island",
            "culmen_length_mm",
            "culmen_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
            "sex",
        ],
    )
    encoded_species = model.predict(penguin)
    species = label_encoder.inverse_transform(encoded_species)[0]
    st.success(f"Predicted species: {species}")

# streamlit run app.py
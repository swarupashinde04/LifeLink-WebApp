import streamlit as st
import pandas as pd
import os

st.title("❤️ Donor Registration")
st.write("Fill in your details to register as a blood donor.")

# CSV File
donors_file = "data/donors.csv"

# Create CSV if it doesn't exist
if not os.path.exists(donors_file):
    pd.DataFrame(columns=[
        "Name",
        "Age",
        "BloodGroup",
        "Phone",
        "Location",
        "Available"
    ]).to_csv(donors_file, index=False)

# Load donors
donors = pd.read_csv(donors_file)

# Form
name = st.text_input("Full Name")
age = st.number_input("Age", min_value=18, max_value=65, step=1)
blood = st.selectbox(
    "Blood Group",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)
phone = st.text_input("Phone Number")
location = st.text_input("Location")

if st.button("Register Donor"):

    # Clean Inputs
    name = name.strip().title()
    location = location.strip().title()
    phone = phone.strip()

    # Validation
    if not name:
        st.error("❌ Please enter your name.")

    elif len(phone) != 10 or not phone.isdigit():
        st.error("❌ Phone number must contain exactly 10 digits.")

    elif not location:
        st.error("❌ Please enter your location.")

    elif phone in donors["Phone"].astype(str).values:
        st.error("❌ This phone number is already registered.")

    else:

        new_donor = pd.DataFrame([{
            "Name": name,
            "Age": age,
            "BloodGroup": blood,
            "Phone": phone,
            "Location": location,
            "Available": "Yes"
        }])

        donors = pd.concat([donors, new_donor], ignore_index=True)
        donors.to_csv(donors_file, index=False)

        st.success("✅ Donor Registered Successfully!")
        st.balloons()
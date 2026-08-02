import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Emergency Request", page_icon="🚑")

st.title("🚑 Emergency Blood Request")
st.write("Fill in the details to raise an emergency blood request.")

st.divider()

with st.form("request_form"):

    patient = st.text_input("Patient Name")

    blood = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    hospital = st.text_input("Hospital Name")

    city = st.text_input("City")

    units = st.number_input(
        "Units Required",
        min_value=1,
        max_value=10,
        value=1
    )

    urgency = st.radio(
        "Urgency",
        ["Critical", "Within 2 Hours", "Today"]
    )

    phone = st.text_input("Contact Number")

    notes = st.text_area("Additional Notes (Optional)")

    submitted = st.form_submit_button("🚨 Submit Request")

if submitted:

    request = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Patient": patient,
        "Blood Group": blood,
        "Hospital": hospital,
        "City": city,
        "Units": units,
        "Urgency": urgency,
        "Phone": phone,
        "Notes": notes,
        "Status": "Searching"
    }

    file = "data/requests.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
    else:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([request])], ignore_index=True)
    df.to_csv(file, index=False)

    st.success("✅ Emergency Request Submitted Successfully!")

    st.info("🤖 AI is searching for the best available donors...")
# -----------------------------
# AI DONOR MATCHING
# -----------------------------

donor_file = "data/donors.csv"

if os.path.exists(donor_file):

    donors = pd.read_csv(donor_file)

    # Blood group match
    matched = donors[
        (donors["BloodGroup"] == blood) &
        (donors["Available"] == "Yes")
    ].copy()

    if matched.empty:

        st.error("❌ No matching donors available.")

    else:

        # AI Score
        matched["Score"] = 50

        # Same city bonus
        matched.loc[
            matched["Location"].str.lower() == city.lower(),
            "Score"
        ] += 20

        # Young donors bonus
        matched.loc[
            matched["Age"] < 35,
            "Score"
        ] += 10

        # Availability bonus
        matched["Score"] += 20

        matched = matched.sort_values(
            by="Score",
            ascending=False
        )

        st.success("🏆 Best Donor Matches")


        medals = ["🥇", "🥈", "🥉"]

        for i, (_, donor) in enumerate(matched.head(3).iterrows()):

           medal = medals[i] if i < 3 else "⭐"

           st.markdown(f"""
<div style="
    background:white;
    border-left:8px solid #d32f2f;
    padding:20px;
    margin-bottom:18px;
    border-radius:15px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
">

<h3 style="color:#222222;">{medal} {donor['Name']}</h3>

<p style="color:#333333;">🩸 <b>Blood Group:</b> {donor['BloodGroup']}</p>

<p style="color:#333333;">📍 <b>Location:</b> {donor['Location']}</p>

<p style="color:#333333;">📞 <b>Phone:</b> {donor['Phone']}</p>

<p style="color:#d32f2f;"><b>⭐ AI Score:</b> {donor['Score']}/100</p>

</div>
""", unsafe_allow_html=True)
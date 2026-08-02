import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 LifeLink Dashboard")

# -------------------------
# LOAD DATA
# -------------------------

donors_file = "data/donors.csv"
requests_file = "data/requests.csv"

if os.path.exists(donors_file):
    donors = pd.read_csv(donors_file)
else:
    donors = pd.DataFrame()

if os.path.exists(requests_file):
    requests = pd.read_csv(requests_file)
else:
    requests = pd.DataFrame()

# -------------------------
# METRICS
# -------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("❤️ Total Donors", len(donors))

with col2:
    st.metric("🚑 Emergency Requests", len(requests))

with col3:
    available = 0
    if not donors.empty:
        available = len(donors[donors["Available"] == "Yes"])

    st.metric("✅ Available Donors", available)

st.divider()

# -------------------------
# RECENT DONORS
# -------------------------

st.subheader("❤️ Registered Donors")

if donors.empty:
    st.info("No donors registered yet.")
else:
    st.dataframe(donors, use_container_width=True)

st.divider()

# -------------------------
# RECENT REQUESTS
# -------------------------

st.subheader("🚑 Emergency Requests")

if requests.empty:
    st.info("No emergency requests yet.")
else:
    st.dataframe(requests, use_container_width=True)
st.divider()

st.subheader("🔄 Update Donor Availability")

if not donors.empty:

    donor_names = donors["Name"].tolist()

    selected_donor = st.selectbox(
        "Select Donor",
        donor_names
    )

    new_status = st.selectbox(
        "Availability",
        ["Yes", "No"]
    )

    if st.button("Update Availability"):

        donors.loc[
            donors["Name"] == selected_donor,
            "Available"
        ] = new_status

        donors.to_csv(
            donors_file,
            index=False
        )

        st.success("✅ Availability Updated!")

        st.rerun()

else:
    st.info("No donors available.")
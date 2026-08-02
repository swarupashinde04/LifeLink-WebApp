import streamlit as st

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="LifeLink",
    page_icon="🩸",
    layout="wide"
)

# -------------------------------
# LOAD CSS
# -------------------------------
def load_css():
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------------
# HERO SECTION
# -------------------------------

st.markdown("""
<div class="hero">

<h1>🩸 LifeLink</h1>

<h3>AI-Powered Emergency Blood Response System</h3>

<p>
Connecting patients, blood donors and hospitals
through an intelligent emergency response platform.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------
# BUTTONS
# -------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("❤️ Register as Donor", use_container_width=True):
        st.switch_page("pages/donor_registration.py")

with col2:
    if st.button("🩸 Request Blood", use_container_width=True):
        st.switch_page("pages/emergency_request.py")

with col3:
    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/dashboard.py")

st.write("")
st.write("")

# -------------------------------
# FEATURE CARDS
# -------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
❤️ Verified Donors

Find trusted blood donors.
""")

with c2:
    st.info("""
🚑 Emergency Requests

Raise emergency blood requests instantly.
""")

with c3:
    st.info("""
🤖 AI Recommendation

Rank donors by availability and eligibility.
""")

st.write("")
st.divider()

st.caption("----------------------------------------------------------------------------------------------------------  Built with ❤️ by Team Swarupa ----------------------------------------------------------------------------------------------------")
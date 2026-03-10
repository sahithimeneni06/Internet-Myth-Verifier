import streamlit as st
from services.verifier import verify_claim

st.set_page_config(
    page_title="Internet Myth Verification Agent",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 Internet Myth Verification Agent")

st.write(
"""
This AI agent verifies internet claims by searching multiple sources
and reasoning about the evidence.
"""
)

# input box
claim = st.text_input(
    "Enter a claim to verify:",
    placeholder="Example: Drinking cold water causes heart attack"
)

# button
verify_button = st.button("Verify Claim")

if verify_button:

    if claim.strip() == "":
        st.warning("Please enter a claim.")
    else:

        with st.spinner("Analyzing claim..."):

            verdict = verify_claim(claim)

        st.subheader("📌 Result")

        st.success(verdict)

        st.subheader("🧾 Claim")

        st.write(claim)
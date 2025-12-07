import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FEMA Disaster Relief Dashboard")

import urllib.request, os, time

url = "https://storage.googleapis.com/info_450/IndividualAssistanceHousingRegistrantsLargeDisasters%20(1).csv"
filename = "fema_disaster_data.csv"

start = time.time()
print(f"Downloading {filename}...")
urllib.request.urlretrieve(url, filename)
st.title("FEMA Disaster Relief Dashboard")

# --- Load FEMA dataset ---
df = pd.read_csv("fema_disaster_data.csv", nrows=300000)
st.subheader("Data Preview")
st.write(df.head())

# --- Histogram of Repair Amount ---
st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(
    df,
    x="repairAmount",
    nbins=30,
    title="Distribution of Repair Amounts"
)
st.plotly_chart(fig_hist)

# --- Boxplot of Repair Amount by TSA Eligibility ---
st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(
    df,
    x="tsaEligible",
    y="repairAmount",
    title="Repair Amount by TSA Eligibility",
    labels={
        "tsaEligible": "TSA Eligible (1 = Yes, 0 = No)",
        "repairAmount": "Repair Amount"
    }
)
st.plotly_chart(fig_box)

# --- Optional text summary ---
st.markdown(
    "*Insight:* Compare the central tendency and spread of repair amounts "
    "for TSA-eligible vs. non-eligible households."
)

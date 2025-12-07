import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.request
import time
import os

st.title("FEMA Disaster Relief Dashboard")

# URL to the dataset
url = "https://storage.googleapis.com/info_450/IndividualAssistanceHousingRegistrantsLargeDisasters%20(1).csv"
filename = "fema_disaster_data.csv"

# Download CSV only if it doesn't exist locally
if not os.path.exists(filename):
    start = time.time()
    st.info(f"Downloading dataset ({filename})...")
    urllib.request.urlretrieve(url, filename)
    st.success(f"Downloaded {filename} in {time.time() - start:.2f} seconds!")

# Load the dataset
df = pd.read_csv("/content/fema_disaster_data.csv", nrows=300000)

# --- Data preview ---
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
    labels={"tsaEligible": "TSA Eligible (1=Yes, 0=No)",
            "repairAmount": "Repair Amount"}
)
st.plotly_chart(fig_box)

# --- Insight ---
st.markdown(
    "**Insight:** TSA-eligible households tend to show different repair cost patterns. "
    "Compare the spread and median values between the groups."
)

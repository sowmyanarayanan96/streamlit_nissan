import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import requests

st.set_page_config(layout='wide')

# CSS for custom styling including navbar
st.markdown("""
    <style>
        .stAppHeader {
        background-color: #09355D; /* Change this to your preferred color */
        color: white;
        font-size: 24px;
        text-align: center;
        padding: 40px;
    }
    .main-container {
        padding: 0;
    }
    .navbar {
        background-color: #002855;
        color: white;
        padding: 10px;
        font-family: 'Arial', sans-serif;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar h1 {
        margin: 0;
        padding: 0;
        font-size: 24px;
    }
    .navbar div {
        display: flex;
        gap: 15px;
    }
    .navbar button {
        background-color: #004e89;
        border: none;
        color: white;
        padding: 8px 16px;
        text-align: center;
        font-size: 16px;
        border-radius: 4px;
        cursor: pointer;
    }
    .navbar button:hover {
        background-color: #0066cc;
    }
    .metric-card {
        padding: 10px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
        text-align: center;
    }
    .metric-label {
        font-weight: bold;
        font-size: 18px;
        color: #333;
    }
    .metric-value {
        font-size: 32px;
        color: #007bff;
    }
    .metric-delta {
        font-size: 14px;
        color: green;
    }
    </style>
""", unsafe_allow_html=True)

# Top navigation bar
st.markdown("""
    <div class="navbar">
        <h1></h1>
        
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("NISSAN Motor Corporation")
    # st.header("Navigation")
    st.write("Dashboard")
    st.write("VIN Management")
    st.write("Supplier")
    st.write("Settings")

# Header Title
st.title("SRN - Supplier Risk Navigator System")

# def fetch_regions():

#     api_url = "http://127.0.0.1:8000/getdata"
#     response = requests.get(api_url)
    
#     if response.status_code==200:
#         data= response.json()
#         regions_data = data.get("details",[])
#         return regions_data
#     else:
#         st.error(f"Failed to fetch regions:{response.status_code}")
#         return[]
    
# regions = fetch_regions()
col1, col2, col3, col4, col5 = st.columns(5)
        
with col1:
    # st.selectbox("Claim Region", regions if regions else ["No regions available"])
    st.selectbox("claim Region",["No Selection","USA","NAA","SWEDAN","MEXICO","INDIA","JAPAN","TOKYO"])
with col2:
    st.selectbox("Supplier Name", ["All", "Supplier A", "Supplier B"])
with col3:
    st.selectbox("Parts Name", ["All", "Part A", "Part B"])
with col4:
    st.selectbox("Vehicle Model", ["All", "Model A", "Model B"])

with col5:
    st.selectbox("Report Frequency", ["Last Month", "Last Year", "Custom"])

# Metric Cards Section
st.markdown("### Key Metrics")

# Create columns for the metric cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Claim Count</div>
        <div class="metric-value">354</div>
        <div class="metric-delta">8.5% up</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Claim Amount</div>
        <div class="metric-value">$3,298</div>
        <div class="metric-delta">2.3% up</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Recovery Amount</div>
        <div class="metric-value">$6,458.87</div>
        <div class="metric-delta">6% up</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Parts Amount</div>
        <div class="metric-value">$27,000</div>
        <div class="metric-delta">32% up</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Labour Amount</div>
        <div class="metric-value">$358.43</div>
        <div class="metric-delta">65% up</div>
    </div>
    """, unsafe_allow_html=True)

# Bar Chart - Claim Volume Analysis
col1, col2 = st.columns(2)

with col1:
    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Claim Count": np.random.randint(50, 400, size=12)
    })
    fig = px.bar(data, x="Month", y="Claim Count", title="Claim Volume Analysis")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Map Visualization
    st.markdown("### Hotspot Region Analysis")
    locations = pd.DataFrame({
        'lat': np.random.uniform(25, 50, 5),
        'lon': np.random.uniform(-100, -70, 5)
    })
    st.map(locations)

col1, col2 = st.columns(2)
with col1:
    # Top Issue Supplier - Pie Chart
    st.markdown("### Top Issue Supplier")
    supplier_data = pd.DataFrame({
        "Supplier": ["", "Supplier B", "Supplier C", "Supplier D"],
        "Issue Count": [150, 100, 50, 75]
    })
    fig2 = px.pie(supplier_data, names="Supplier", values="Issue Count", title="Top Issue Supplier")
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    # Issue Category - Pie Chart
    st.markdown("### Top Issue Category")
    issue_category_data = pd.DataFrame({
        "Category": ["Die Pusher Fails", "Process Failure", "No Labels", "Insert Direction", "Mittla"],
        "Issue Count": [30, 25, 20, 15, 10]
    })
    fig3 = px.pie(issue_category_data, names="Category", values="Issue Count", title="Top Issue Category")
    st.plotly_chart(fig3, use_container_width=True)


# # Root Cause Analysis - Progress Bars
# st.markdown("### Root Cause Analysis")
# st.write("Weakened Tab in Sunvisor Clip")
# st.progress(0.95)
# st.write("Lamp assy-rr comb, RH with Dim Light")
# st.progress(0.92)
# st.write("Wrong Emblem")
# st.progress(0.89)

col1,col2 = st.columns(2)

with col1:
    # Root Cause Analysis - Progress Bars
    st.markdown("### Root Cause Analysis")
    st.write("Weakened Tab in Sunvisor Clip")
    st.progress(0.95)
    st.write("Lamp assy-rr comb, RH with Dim Light")
    st.progress(0.92)
    st.write("Wrong Emblem")
    st.progress(0.89)

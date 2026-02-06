"""Overview page - Dashboard with key metrics and charts"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests


def get_mock_data():
    """Generate mock data for demo purposes"""
    return {
        "total_sessions": 24,
        "active_sessions": 5,
        "total_checkins": 342,
        "checkins_today": 45,
        "success_rate": 94.2,
        "avg_response_time": 245  # ms
    }


def show_overview(backend_url):
    """Display overview dashboard with metrics and charts"""
    st.title("📊 Overview Dashboard")
    st.markdown("---")
    
    # TODO: Replace mock data with actual backend API calls
    data = get_mock_data()
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📚 Total Sessions", data["total_sessions"], f"{data['active_sessions']} active")
    
    with col2:
        st.metric("✅ Check-ins Today", data["checkins_today"], "+12 from yesterday")
    
    with col3:
        st.metric("🎯 Success Rate", f"{data['success_rate']}%", "↗️ +2.1%")
    
    with col4:
        st.metric("⚡ Avg Response Time", f"{data['avg_response_time']}ms", "↘️ -15ms")
    
    st.markdown("---")
    
    # Charts Row
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Check-ins by Hour")
        # Mock data
        hours = list(range(8, 18))
        checkins = [12, 15, 18, 22, 19, 25, 28, 24, 20, 15]
        
        fig = go.Figure(data=[
            go.Bar(x=hours, y=checkins, marker_color='#1f77b4')
        ])
        fig.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Verification Status")
        # Mock data
        statuses = ['Verified', 'Pending', 'Failed']
        counts = [315, 20, 7]
        colors = ['#2ecc71', '#f39c12', '#e74c3c']
        
        fig = go.Figure(data=[
            go.Pie(labels=statuses, values=counts, marker=dict(colors=colors))
        ])
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📝 Recent Check-ins")
    
    # Mock table data
    recent_data = {
        "Check-in ID": ["CHK001", "CHK002", "CHK003", "CHK004", "CHK005"],
        "Student ID": ["STU123", "STU456", "STU789", "STU012", "STU345"],
        "Session": ["Math 101 - Lec 1", "Physics 201 - Lab", "Chem 150 - Lec 2", "Bio 101 - Lec 3", "Math 101 - Lec 1"],
        "Timestamp": ["2024-01-28 09:15", "2024-01-28 09:22", "2024-01-28 09:30", "2024-01-28 10:05", "2024-01-28 10:12"],
        "Status": ["✅ Verified", "✅ Verified", "⚠️ Pending", "✅ Verified", "❌ Failed"],
        "Risk Score": [0.05, 0.08, 0.32, 0.04, 0.78]
    }
    
    df = pd.DataFrame(recent_data)
    st.dataframe(df, use_container_width=True, hide_index=True)


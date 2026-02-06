"""
SAIV Instructor Dashboard - Module 4

This is the skeleton implementation for the Observability module.
Students must implement the instructor dashboard with session management,
attendance monitoring, and metrics visualization.
"""
# pip install streamlit 
# pip install streamlit-option-menu
# streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
# run tasks

from streamlit_option_menu import option_menu           # pip install streamlit-option-menu
import streamlit as st
import os

# Import page modules
from pages import overview, metrics, check_ins, sessions, audit_logs

# This hides the native Streamlit sidebar multi-page links
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="SAIV Instructor Dashboard",
    page_icon="📊",
    layout="wide"
)

# Environment variables
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://localhost:9090")

with st.sidebar:
    selected = option_menu(
        menu_title="SAIV Dashboard", 
        menu_icon="speedometer2",
        options=["Overview", "Sessions", "Check-ins", "Audit Logs","Metrics", "Student's View"], 
        icons=[
            "grid-1x2",      # Overview (Dashboard layout)
            "clock-history", # Sessions (Time-based activity)
            "patch-check",   # Check-ins (Verified/Attendance)
            "file-earmark-text", # Audit Logs (Records/Documents)
            "graph-up",      # Metrics (Growth/Data)
            "person-video3"  # Student's View (Person/Interface view)
            ], 
        default_index=0,
    )

if selected == "Overview":
    overview.render()

elif selected == "Sessions":
    sessions.render()

elif selected == "Check-ins":
    check_ins.render()

elif selected == "Audit Logs":
    audit_logs.render()

elif selected == "Metrics":
    metrics.render()

elif selected == "Student's View":
    st.header("Student View")
    st.write("Coming soon...")

# =============================================================================
# TODO: Implement the following pages/features
# =============================================================================

# -----------------------------------------------------------------------------
# Authentication
# -----------------------------------------------------------------------------
# - Login form for instructors
# - JWT token management
# - Session persistence

# -----------------------------------------------------------------------------
# Overview Page
# -----------------------------------------------------------------------------
# - Total sessions (active/inactive)
# - Total check-ins & success rate
# - Recent check-ins table
# - Check-ins by hour chart
# - Verification status pie chart

# -----------------------------------------------------------------------------
# Sessions Management
# -----------------------------------------------------------------------------
# - View all sessions with details
# - Create new sessions with geofence config
# - View check-ins per session
# - CSV export for gradebook

# -----------------------------------------------------------------------------
# Check-ins View
# -----------------------------------------------------------------------------
# - Filter by session, verification status
# - Real-time updates
# - CSV export for gradebook integration
# - Attendance data with all signals

# -----------------------------------------------------------------------------
# Audit Logs
# -----------------------------------------------------------------------------
# - Browse system events
# - Filter by event type, user, action
# - Color-coded by severity
# - Export audit trail

# -----------------------------------------------------------------------------
# Metrics Dashboard
# -----------------------------------------------------------------------------
# - API response times (p95 latency)
# - Request rates
# - Success rates
# - Risk score distribution
# - High-risk alerts
# - System health status

# =============================================================================
# CSV Export Format
# =============================================================================
# Required columns:
# - Check-in ID, Student ID, Session ID
# - Timestamp, Verification Status
# - Risk Score, Liveness Score, Face Match Score
# - GPS Coordinates (latitude, longitude)

# Placeholder content

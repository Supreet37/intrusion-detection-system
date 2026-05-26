# components/sidebar.py
# Sidebar component with model information

import streamlit as st
from utils.constants import EXPECTED_FEATURES

def render_sidebar():
    """Render the sidebar with model information."""
    
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/security-checked--v1.png", width=80)
        st.title("🛡️ Model Info")
        st.markdown("---")
        
        st.markdown("### 🤖 Algorithm")
        st.code("""
        Model: LightGBM
        Type: Binary Classifier
        Objective: binary
        Boosting: gbdt
        Trees: 100
        Leaves: 31
        """, language="text")
        
        st.markdown("### 📊 Features Used")
        st.markdown(f"**Total features:** {len(EXPECTED_FEATURES)}")
        
        with st.expander("View all features"):
            for feat in EXPECTED_FEATURES:
                st.caption(f"• {feat}")
        
        st.markdown("---")
        st.markdown("### ⚡ Threat Indicators")
        
        st.markdown("""
        | Risk Level | Indicators |
        |:---|:---|
        | 🔴 **High** | IP score > 0.7<br>Login attempts > 10 |
        | 🟡 **Medium** | Unusual hours<br>Failed logins > 3 |
        | 🟢 **Low** | Weak encryption<br>Unknown browser |
        """)
        
        st.markdown("---")
        st.caption("Built with LightGBM | Real-time IDS")
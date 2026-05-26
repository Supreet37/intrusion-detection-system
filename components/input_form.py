# components/input_form.py
# User input form component

import streamlit as st
from utils.constants import (
    PROTOCOL_OPTIONS, ENCRYPTION_OPTIONS, BROWSER_OPTIONS,
    INPUT_CONSTRAINTS, PROTOCOL_LABELS, ENCRYPTION_LABELS, BROWSER_LABELS
)

def render_input_form() -> dict:
    """
    Render the input form and return collected data.
    
    Returns:
        Dictionary with all user inputs
    """
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    raw_input = {}
    
    with col1:
        st.subheader("🌐 Network Features")
        
        # Network Packet Size
        nc = INPUT_CONSTRAINTS['network_packet_size']
        raw_input['network_packet_size'] = st.number_input(
            "📦 Packet Size (bytes)",
            min_value=nc['min'],
            max_value=nc['max'],
            value=nc['default'],
            step=nc['step'],
            help="64-1500 bytes. Unusual sizes may indicate attacks."
        )
        
        # Protocol Type
        raw_input['protocol_type'] = st.selectbox(
            "🔌 Protocol Type",
            options=PROTOCOL_OPTIONS,
            format_func=lambda x: PROTOCOL_LABELS.get(x, x),
            index=0,
            help="TCP: reliable, UDP: faster, ICMP: diagnostics (often abused)"
        )
        
        # Encryption Used
        raw_input['encryption_used'] = st.selectbox(
            "🔐 Encryption",
            options=ENCRYPTION_OPTIONS,
            format_func=lambda x: ENCRYPTION_LABELS.get(x, x),
            index=0,
            help="AES is secure. DES is weak. None is risky."
        )
        
        # IP Reputation Score
        ic = INPUT_CONSTRAINTS['ip_reputation_score']
        raw_input['ip_reputation_score'] = st.slider(
            "🌍 IP Reputation Score",
            min_value=ic['min'],
            max_value=ic['max'],
            value=ic['default'],
            step=ic['step'],
            help="0 = trusted, 1 = highly suspicious"
        )
    
    with col2:
        st.subheader("👤 User Behavior")
        
        # Login Attempts
        lc = INPUT_CONSTRAINTS['login_attempts']
        raw_input['login_attempts'] = st.number_input(
            "🔑 Login Attempts",
            min_value=lc['min'],
            max_value=lc['max'],
            value=lc['default'],
            step=lc['step'],
            help="High values may indicate brute-force attacks"
        )
        
        # Failed Logins
        fc = INPUT_CONSTRAINTS['failed_logins']
        raw_input['failed_logins'] = st.number_input(
            "❌ Failed Logins",
            min_value=fc['min'],
            max_value=fc['max'],
            value=fc['default'],
            step=fc['step'],
            help="Multiple failures followed by success = suspicious"
        )
        
        # Session Duration
        sc = INPUT_CONSTRAINTS['session_duration']
        raw_input['session_duration'] = st.number_input(
            "⏱️ Session Duration (seconds)",
            min_value=sc['min'],
            max_value=sc['max'],
            value=sc['default'],
            step=sc['step'],
            help="Very long sessions may indicate unauthorized persistence"
        )
        
        # Unusual Time Access
        raw_input['unusual_time_access'] = st.selectbox(
            "🕐 Access Time",
            options=[0, 1],
            format_func=lambda x: "✅ Normal Hours (9-5)" if x == 0 else "⚠️ Unusual Hours",
            index=0,
            help="Access outside normal business hours"
        )
        
        # Browser Type
        raw_input['browser_type'] = st.selectbox(
            "🌐 Browser Type",
            options=BROWSER_OPTIONS,
            format_func=lambda x: BROWSER_LABELS.get(x, x),
            index=0,
            help="Unknown browsers may indicate bots/scripts"
        )
    
    # Failed Login Ratio (with auto-calculation option)
    st.subheader("📊 Advanced Metrics")
    
    ratio_source = st.radio(
        "Failed Login Ratio",
        options=["Auto-calculate", "Manual Entry"],
        horizontal=True,
        index=0
    )
    
    if ratio_source == "Auto-calculate":
        if raw_input['login_attempts'] > 0:
            ratio = raw_input['failed_logins'] / raw_input['login_attempts']
            st.info(f"📐 Calculated ratio: **{ratio:.3f}** (failed / total)")
            raw_input['failed_login_ratio'] = ratio
        else:
            st.warning("Cannot calculate: Login attempts is 0")
            raw_input['failed_login_ratio'] = 0.0
    else:
        rc = INPUT_CONSTRAINTS['failed_login_ratio']
        raw_input['failed_login_ratio'] = st.number_input(
            "Failed Login Ratio",
            min_value=rc['min'],
            max_value=rc['max'],
            value=rc['default'],
            step=rc['step'],
            help="Manual ratio value (failed/total)"
        )
    
    return raw_input
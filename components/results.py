# components/results.py
# Results display component

import streamlit as st
import pandas as pd
from utils.constants import RISK_THRESHOLDS

def render_results(prediction_result: dict, raw_input: dict):
    """
    Render prediction results with visual feedback.
    
    Args:
        prediction_result: Dictionary from model.predict()
        raw_input: Original user inputs for risk analysis
    """
    
    st.markdown("---")
    
    is_attack = prediction_result['prediction'] == 1
    prob_attack = prediction_result['probability_attack']
    
    if is_attack:
        # Attack detected - Red styling
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #ff4b4b, #cc0000);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 0 30px #ff4b4b;
        ">
            <h1 style="color: white; margin: 0;">🚨 INTRUSION DETECTED!</h1>
            <p style="color: white; font-size: 2rem; margin: 0.5rem 0;">
                Threat Probability: {prob_attack:.2%}
            </p>
            <p style="color: #ffcccc;">Confidence: {prediction_result['confidence']:.2%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Action recommendations
        with st.expander("🛡️ Recommended Actions", expanded=True):
            st.markdown("""
            - 🚫 **Immediately block** the source IP address
            - 📋 **Review authentication logs** for unusual patterns
            - 🔔 **Alert security team** for incident response
            - 🔍 **Enable enhanced monitoring** on affected systems
            - 📝 **Document the incident** for future reference
            """)
    
    else:
        # Normal traffic - Green styling
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #00cc66, #009944);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 0 20px #00cc66;
        ">
            <h1 style="color: white; margin: 0;">✅ ACTIVITY NORMAL</h1>
            <p style="color: white; font-size: 1.5rem; margin: 0.5rem 0;">
                Threat Probability: {prob_attack:.2%}
            </p>
            <p style="color: #ccffcc;">Confidence: {prediction_result['confidence']:.2%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("No immediate action required. Continue monitoring as usual.")
    
    # Risk Factor Analysis (displayed for both, more detailed when attack)
    if prob_attack > 0.3 or is_attack:
        st.subheader("📊 Risk Factor Analysis")
        
        risk_factors = []
        warnings = []
        
        # IP Reputation
        ip_score = raw_input.get('ip_reputation_score', 0)
        if ip_score > RISK_THRESHOLDS['high_ip_score']:
            risk_factors.append(f"⚠️ **High IP reputation score**: {ip_score:.2f}")
        elif ip_score > 0.4:
            warnings.append(f"📈 **Elevated IP score**: {ip_score:.2f}")
        
        # Login attempts
        login_attempts = raw_input.get('login_attempts', 0)
        if login_attempts > RISK_THRESHOLDS['high_login_attempts']:
            risk_factors.append(f"⚠️ **Excessive login attempts**: {login_attempts}")
        
        # Failed logins
        failed = raw_input.get('failed_logins', 0)
        if failed > RISK_THRESHOLDS['high_failed_logins']:
            risk_factors.append(f"⚠️ **Multiple failed logins**: {failed}")
        
        # Failed ratio
        ratio = raw_input.get('failed_login_ratio', 0)
        if ratio > RISK_THRESHOLDS['high_failed_ratio']:
            risk_factors.append(f"⚠️ **High failure ratio**: {ratio:.2f}")
        
        # Unusual time
        if raw_input.get('unusual_time_access', 0) == 1:
            risk_factors.append("⚠️ **Access at unusual hours** (outside 9 AM - 5 PM)")
        
        # Packet size anomalies
        packet_size = raw_input.get('network_packet_size', 512)
        if packet_size < RISK_THRESHOLDS['low_packet_size']:
            risk_factors.append(f"⚠️ **Unusually small packet**: {packet_size} bytes")
        elif packet_size > RISK_THRESHOLDS['high_packet_size']:
            risk_factors.append(f"⚠️ **Unusually large packet**: {packet_size} bytes")
        
        # Encryption
        encryption = raw_input.get('encryption_used', 'AES')
        if encryption != 'AES':
            risk_factors.append(f"⚠️ **Weak/no encryption**: {encryption}")
        
        # Browser
        browser = raw_input.get('browser_type', 'Chrome')
        if browser == 'Unknown':
            risk_factors.append("⚠️ **Unknown browser type** - possible bot/script")
        
        # Display risk factors
        if risk_factors:
            st.warning("**Identified Risk Factors:**")
            for factor in risk_factors:
                st.markdown(factor)
        else:
            st.info("No specific risk factors identified, but probability is elevated.")
        
        if warnings:
            with st.expander("ℹ️ Additional Observations"):
                for warning in warnings:
                    st.caption(warning)

def render_feature_importance(model):
    """Display feature importance chart if available."""
    if hasattr(model, 'feature_importances_'):
        st.subheader("🔬 Model Feature Importance")
        st.caption("Features that most influence predictions (global model perspective)")
        
        from utils.constants import EXPECTED_FEATURES
        importances = model.feature_importances_
        
        # Create DataFrame for top features
        importance_df = pd.DataFrame({
            'Feature': EXPECTED_FEATURES,
            'Importance': importances
        }).sort_values('Importance', ascending=False).head(12)
        
        st.bar_chart(importance_df.set_index('Feature'))
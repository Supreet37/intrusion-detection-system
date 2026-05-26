# app.py
# Main Streamlit application

import streamlit as st
from utils.model_loader import load_model, predict, get_feature_importance
from utils.feature_engineer import validate_inputs
from components.sidebar import render_sidebar
from components.input_form import render_input_form
from components.results import render_results, render_feature_importance
from utils.constants import INPUT_CONSTRAINTS

# Page configuration
st.set_page_config(
    page_title="Cybersecurity Intrusion Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #00ffcc;
        text-align: center;
        background: linear-gradient(90deg, #0f0c29, #302b63, #24243e);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .stButton button {
        width: 100%;
        background-color: #00ffcc;
        color: #0f0c29;
        font-weight: bold;
        font-size: 1.2rem;
    }
    hr {
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Render sidebar
render_sidebar()

# Main content
st.markdown('<div class="main-header">🛡️ Cybersecurity Intrusion Detection System</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 1.5rem;">
    <p style="font-size: 1.1rem;">
        Enter network traffic and user behavior details below. The model will analyze 
        patterns and determine if the activity is <span style="color:#00ffcc;">normal</span> 
        or a <span style="color:#ff4b4b;">potential attack</span>.
    </p>
</div>
""", unsafe_allow_html=True)

# Load model
model, expected_features = load_model()

# Render input form
user_input = render_input_form()

# Prediction button
col_empty, col_button, col_empty2 = st.columns([1, 2, 1])
with col_button:
    predict_clicked = st.button("🚀 ANALYZE NETWORK TRAFFIC", use_container_width=True)

# Make prediction when button is clicked
if predict_clicked:
    # Validate inputs
    validation = validate_inputs(user_input, INPUT_CONSTRAINTS)
    
    if not validation['valid']:
        for error in validation['errors']:
            st.error(f"❌ {error}")
    else:
        with st.spinner("Analyzing traffic patterns..."):
            # Make prediction
            result = predict(user_input, model, expected_features)
            
            # Display results
            render_results(result, user_input)
            
            # Show feature importance
            render_feature_importance(model)
            
            # Optional: Show raw probabilities in expander
            with st.expander("📊 Detailed Prediction Metrics"):
                st.metric("Normal Probability", f"{result['probability_normal']:.4f}")
                st.metric("Attack Probability", f"{result['probability_attack']:.4f}")
                st.metric("Confidence", f"{result['confidence']:.4f}")

# Footer
st.markdown("---")
st.caption("🔒 This model is based on a cybersecurity intrusion detection dataset. For demonstration and research purposes only.")
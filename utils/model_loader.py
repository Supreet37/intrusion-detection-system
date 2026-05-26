# utils/model_loader.py
# Handles model loading and prediction

import pickle
import streamlit as st
import pandas as pd
from .feature_engineer import encode_input, create_dataframe

@st.cache_resource
def load_model():
    """
    Load the LightGBM model and feature columns from pickle files.
    Returns tuple of (model, feature_columns)
    """
    try:
        with open('lgbm_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('model_columns.pkl', 'rb') as f:
            model_columns = pickle.load(f)
        return model, model_columns
    except FileNotFoundError as e:
        st.error(f"""
        ❌ Model file not found: {e.filename}
        
        Please ensure both files are in the same directory as the app:
        - `lgbm_model.pkl`
        - `model_columns.pkl`
        """)
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

def predict(raw_input: dict, model, expected_features: list) -> dict:
    """
    Make a prediction using the loaded model.
    
    Args:
        raw_input: User-friendly input dictionary
        model: Loaded LightGBM model
        expected_features: List of expected feature names
    
    Returns:
        Dictionary with 'prediction', 'probability', 'confidence'
    """
    # Encode the input
    encoded = encode_input(raw_input)
    
    # Create DataFrame
    df = create_dataframe(encoded)
    
    # Get prediction
    prediction = int(model.predict(df)[0])
    probabilities = model.predict_proba(df)[0]
    
    return {
        'prediction': prediction,  # 0 = normal, 1 = attack
        'probability_attack': probabilities[1],
        'probability_normal': probabilities[0],
        'confidence': max(probabilities)  # Highest probability
    }

def get_feature_importance(model):
    """Return feature importance if available."""
    if hasattr(model, 'feature_importances_'):
        return model.feature_importances_
    return None
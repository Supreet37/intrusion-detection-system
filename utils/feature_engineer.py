# utils/feature_engineer.py
# Handles feature encoding and DataFrame creation

import pandas as pd
from .constants import (
    EXPECTED_FEATURES, PROTOCOL_ENCODING, ENCRYPTION_ENCODING,
    BROWSER_ENCODING
)

def encode_input(raw_data: dict) -> dict:
    """
    Convert user-friendly input into model-expected feature dictionary.
    
    Args:
        raw_data: Dictionary with keys: protocol_type, encryption_used, 
                  browser_type, and numeric fields
    
    Returns:
        Dictionary with all expected feature names as keys
    """
    encoded = {}
    
    # Copy numeric fields
    numeric_fields = [
        'network_packet_size', 'login_attempts', 'session_duration',
        'ip_reputation_score', 'failed_logins', 'unusual_time_access',
        'failed_login_ratio'
    ]
    for field in numeric_fields:
        encoded[field] = raw_data.get(field, 0)
    
    # Encode protocol
    protocol = raw_data.get('protocol_type', 'TCP')
    protocol_encoding = PROTOCOL_ENCODING.get(protocol, PROTOCOL_ENCODING['TCP'])
    encoded.update(protocol_encoding)
    
    # Encode encryption
    encryption = raw_data.get('encryption_used', 'AES')
    encryption_encoding = ENCRYPTION_ENCODING.get(encryption, ENCRYPTION_ENCODING['AES'])
    encoded.update(encryption_encoding)
    
    # Encode browser
    browser = raw_data.get('browser_type', 'Chrome')
    browser_encoding = BROWSER_ENCODING.get(browser, BROWSER_ENCODING['Chrome'])
    encoded.update(browser_encoding)
    
    return encoded

def create_dataframe(encoded_data: dict) -> pd.DataFrame:
    """
    Create a DataFrame in the exact order expected by the model.
    
    Args:
        encoded_data: Dictionary with all expected features
    
    Returns:
        DataFrame with columns in EXPECTED_FEATURES order
    """
    # Ensure all expected features are present
    for feature in EXPECTED_FEATURES:
        if feature not in encoded_data:
            encoded_data[feature] = 0
    
    # Create DataFrame with correct column order
    df = pd.DataFrame([encoded_data])[EXPECTED_FEATURES]
    
    return df

def get_missing_features(encoded_data: dict) -> list:
    """Return list of missing expected features."""
    return [f for f in EXPECTED_FEATURES if f not in encoded_data]

def validate_inputs(raw_data: dict, constraints: dict) -> dict:
    """
    Validate user inputs against constraints.
    
    Returns:
        Dictionary with 'valid' boolean and 'errors' list
    """
    errors = []
    
    for field, constraint in constraints.items():
        if field in raw_data:
            value = raw_data[field]
            if value < constraint['min']:
                errors.append(f"{field} cannot be less than {constraint['min']}")
            if value > constraint['max']:
                errors.append(f"{field} cannot be greater than {constraint['max']}")
    
    # Special validation: failed_logins cannot exceed login_attempts
    if raw_data.get('failed_logins', 0) > raw_data.get('login_attempts', 0):
        errors.append("Failed logins cannot exceed total login attempts")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    }
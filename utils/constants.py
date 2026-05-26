# utils/constants.py
# All configuration constants, mappings, and thresholds

# Feature names as expected by the model
EXPECTED_FEATURES = [
    'network_packet_size', 'login_attempts', 'session_duration',
    'ip_reputation_score', 'failed_logins', 'unusual_time_access',
    'protocol_type_TCP', 'protocol_type_UDP', 'encryption_used_DES',
    'browser_type_Edge', 'browser_type_Firefox', 'browser_type_Safari',
    'browser_type_Unknown', 'failed_login_ratio'
]

# Protocol mappings
PROTOCOL_OPTIONS = ['TCP', 'UDP', 'ICMP']
PROTOCOL_ENCODING = {
    'TCP': {'protocol_type_TCP': 1, 'protocol_type_UDP': 0},
    'UDP': {'protocol_type_TCP': 0, 'protocol_type_UDP': 1},
    'ICMP': {'protocol_type_TCP': 0, 'protocol_type_UDP': 0},
}

# Encryption mappings
ENCRYPTION_OPTIONS = ['AES', 'DES', 'None']
ENCRYPTION_ENCODING = {
    'AES': {'encryption_used_DES': 0},
    'DES': {'encryption_used_DES': 1},
    'None': {'encryption_used_DES': 0},
}

# Browser mappings
BROWSER_OPTIONS = ['Chrome', 'Firefox', 'Edge', 'Safari', 'Unknown']
BROWSER_ENCODING = {
    'Chrome': {'browser_type_Edge': 0, 'browser_type_Firefox': 0, 'browser_type_Safari': 0, 'browser_type_Unknown': 0},
    'Firefox': {'browser_type_Edge': 0, 'browser_type_Firefox': 1, 'browser_type_Safari': 0, 'browser_type_Unknown': 0},
    'Edge': {'browser_type_Edge': 1, 'browser_type_Firefox': 0, 'browser_type_Safari': 0, 'browser_type_Unknown': 0},
    'Safari': {'browser_type_Edge': 0, 'browser_type_Firefox': 0, 'browser_type_Safari': 1, 'browser_type_Unknown': 0},
    'Unknown': {'browser_type_Edge': 0, 'browser_type_Firefox': 0, 'browser_type_Safari': 0, 'browser_type_Unknown': 1},
}

# Input field constraints
INPUT_CONSTRAINTS = {
    'network_packet_size': {'min': 64, 'max': 1500, 'default': 512, 'step': 10},
    'login_attempts': {'min': 1, 'max': 50, 'default': 3, 'step': 1},
    'session_duration': {'min': 0.5, 'max': 10000.0, 'default': 300.0, 'step': 50.0},
    'ip_reputation_score': {'min': 0.0, 'max': 1.0, 'default': 0.3, 'step': 0.01},
    'failed_logins': {'min': 0, 'max': 20, 'default': 0, 'step': 1},
    'failed_login_ratio': {'min': 0.0, 'max': 5.0, 'default': 0.0, 'step': 0.1},
}

# Risk thresholds
RISK_THRESHOLDS = {
    'high_ip_score': 0.7,
    'high_login_attempts': 10,
    'high_failed_logins': 3,
    'high_failed_ratio': 0.5,
    'low_packet_size': 80,
    'high_packet_size': 1400,
}

# Display labels
PROTOCOL_LABELS = {
    'TCP': 'TCP (Transmission Control Protocol)',
    'UDP': 'UDP (User Datagram Protocol)',
    'ICMP': 'ICMP (Internet Control Message Protocol)',
}

ENCRYPTION_LABELS = {
    'AES': 'AES (Strong Encryption)',
    'DES': 'DES (Weak Encryption)',
    'None': 'None (Unencrypted - Risky)',
}

BROWSER_LABELS = {
    'Chrome': 'Chrome',
    'Firefox': 'Firefox',
    'Edge': 'Edge',
    'Safari': 'Safari',
    'Unknown': 'Unknown / Bot',
}
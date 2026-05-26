# 🛡️ Cybersecurity Intrusion Detection System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A machine learning-based intrusion detection system that analyzes network traffic and user behavior to identify potential cyber attacks in real-time.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a **LightGBM classifier** that detects cybersecurity intrusions by analyzing:

- **Network features** (packet size, protocol type, encryption, IP reputation)
- **User behavior features** (login attempts, session duration, failed logins)
- **Contextual features** (access time, browser type)

The system provides a user-friendly web interface where security analysts can input network traffic parameters and receive instant threat assessments with probability scores.

## ✨ Features

| Feature | Description |
|:---|:---|
| 🔍 **Real-time Detection** | Instant analysis of network traffic patterns |
| 📊 **14 Input Features** | Comprehensive coverage of network & behavioral metrics |
| 🎯 **Probability Scoring** | Confidence percentage for each prediction |
| ⚠️ **Risk Factor Analysis** | Identifies specific suspicious indicators |
| 📈 **Feature Importance** | Visualizes which factors influenced the decision |
| 🎨 **User-friendly UI** | Intuitive interface with color-coded results |

## 📊 Dataset

The model is trained on a cybersecurity intrusion detection dataset containing:

### Network-Based Features
- `network_packet_size` - Packet size in bytes (64-1500)
- `protocol_type` - TCP, UDP, or ICMP
- `encryption_used` - AES, DES, or None
- `ip_reputation_score` - Trust score (0-1)

### User Behavior Features
- `login_attempts` - Number of login tries
- `failed_logins` - Failed authentication attempts
- `session_duration` - Session length in seconds
- `browser_type` - Chrome, Firefox, Edge, Safari, or Unknown
- `unusual_time_access` - Access during off-hours (0/1)
- `failed_login_ratio` - Ratio of failed to total attempts

### Dataset Statistics
- **Total Records:** 9,537
- **Attack Samples:** ~20% (imbalanced, real-world scenario)
- **Features:** 14 (after one-hot encoding)

## 🤖 Model

### LightGBM Classifier

| Parameter | Value |
|:---|:---|
| Algorithm | LightGBM Gradient Boosting |
| Objective | Binary Classification |
| Number of Trees | 100 |
| Max Leaves | 31 |
| Learning Rate | 0.1 |
| Feature Importance Type | Split |

### Performance Metrics
- **Accuracy:** ~95% on test set
- **Precision:** High (low false positives)
- **Recall:** High (detects most attacks)
- **F1-Score:** Balanced performance

## 💻 Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/intrusion-detection-system.git
cd intrusion-detection-system

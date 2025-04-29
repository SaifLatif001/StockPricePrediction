import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the list of stocks
stocks = [
    'RELIANCE.BO', 'COALINDIA.BO', 'TCS.BO', 'HDFCBANK.BO', 'INFY.BO', 'ICICIBANK.BO', 'SBIN.BO', 'HINDUNILVR.BO',
    'ITC.BO', 'LT.BO', 'KOTAKBANK.BO', 'BAJFINANCE.BO', 'AXISBANK.BO', 'MARUTI.BO', 'ASIANPAINT.BO', 'TITAN.BO',
    'SUNPHARMA.BO', 'HCLTECH.BO', 'WIPRO.BO', 'ULTRACEMCO.BO', 'TECHM.BO', 'POWERGRID.BO', 'NTPC.BO', 'BAJAJFINSV.BO',
    'NESTLEIND.BO', 'TATASTEEL.BO', 'JSWSTEEL.BO', 'GRASIM.BO', 'ADANIENT.BO', 'ADANIPORTS.BO', 'DIVISLAB.BO',
    'HINDALCO.BO', 'DRREDDY.BO', 'CIPLA.BO', 'BRITANNIA.BO', 'SBILIFE.BO', 'EICHERMOT.BO', 'INDUSINDBK.BO',
    'HEROMOTOCO.BO', 'UPL.BO', 'BPCL.BO', 'ONGC.BO', 'M&M.BO', 'BAJAJ-AUTO.BO', 'TATAMOTORS.BO', 'APOLLOHOSP.BO',
    'HDFCLIFE.BO', 'BHARTIARTL.BO', 'SHREECEM.BO', 'TATACONSUM.BO', 'DABUR.BO', 'PIDILITIND.BO', 'HAVELLS.BO'
]

# Custom CSS for webpage-like styling
st.markdown("""
<style>
    /* Reset default margins and padding */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* Background for the entire app */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
    }

    /* Navigation bar styling */
    .navbar {
        background-color: #ffffff;
        padding: 15px 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
    }

    .navbar-brand {
        font-size: 1.5em;
        font-weight: bold;
        color: #1e3c72;
    }

    .navbar-links a {
        color: #1e3c72;
        text-decoration: none;
        margin: 0 15px;
        font-size: 1.1em;
        transition: color 0.3s ease;
    }

    .navbar-links a:hover {
        color: #d81b60;
    }

    /* Hero section styling */
    .hero {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-position: center;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero-text {
        color: #ffffff;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    /* Main content container */
    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Card styling for predictions and plots */
    .card {
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    .card-title {
        color: #d81b60;
        font-size: 1.5em;
        margin-bottom: 15px;
    }

    /* Dropdown styling */
    .stSelectbox {
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 10px;
    }

    .stSelectbox div {
        color: #1e3c72;
        font-size: 1.1em;
    }

    /* Table styling */
    .stDataFrame {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Plot styling */
    .stPlotlyChart, .stPyplot {
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Footer styling */
    .footer {
        background-color: #1e3c72;
        color: #ffffff;
        text-align: center;
        padding: 15px;
        position: relative;
        bottom: 0;
        width: 100%;
        margin-top: 30px;
    }

    .footer-text {
        font-size: 1em;
    }

    .footer-text a {
        color: #ffeb3b;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .footer-text a:hover {
        color: #d81b60;
    }
</style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">Stock Predictor</div>
    <div class="navbar-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero section with your name
st.markdown("""
<div class="hero">
    <div class="hero-text">Stock Price Prediction by Saif Latif</div>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Create two columns for dropdowns
col1, col2 = st.columns([1, 1])

with col1:
    # Dropdown to select model (XGBoost or LSTM)
    model_type = st.selectbox("Select Model", ["XGBoost", "LSTM"], key="model_select")

with col2:
    # Dropdown to select stock
    ticker = st.selectbox("Select a Stock", stocks, key="stock_select")

# Load predictions based on selected model
if model_type == "XGBoost":
    prediction_path = f"predictions_xgb/{ticker}_2025_predictions.csv"
elif model_type == "LSTM":
    prediction_path = f"predictions/{ticker}_2025_predictions.csv"
else:
    prediction_path = None

if os.path.exists(prediction_path):
    # Load the predictions
    predictions_df = pd.read_csv(prediction_path)

    # Display predictions in a card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="card-title">Predictions for {ticker} in 2025 ({model_type})</div>', unsafe_allow_html=True)
    st.write(predictions_df.head(10))  # Show first 10 rows
    st.markdown('</div>', unsafe_allow_html=True)

    # Plot the predictions in a card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Predicted Prices Plot</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='white')
    ax.plot(predictions_df['Date'], predictions_df['Predicted_Price'], label='Predicted Price', color='#ff6f00', linewidth=2)
    ax.set_title(f'{ticker} Predicted Prices for 2025 ({model_type})', fontsize=14, color='#d81b60')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price (INR)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', alpha=0.7, color='#bdbdbd')
    ax.set_facecolor('#f5f5f5')
    ax.legend()
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # Placeholder for model performance metrics in a card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Model Performance Metrics</div>', unsafe_allow_html=True)
    st.markdown(f'<div>Performance metrics for {model_type} are not available in this version.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error(f"No predictions found for {ticker} with {model_type} model.")

# Close main content
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-text">
        © 2025 Stock Price Prediction Project by Saif Latif | Powered by Streamlit | <a href="https://github.com/SaifLatif001/StockPricePrediction" target="_blank">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)
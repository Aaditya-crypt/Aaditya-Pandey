
# Time Series Analysis for Bitcoin Price Prediction using Prophet

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Usage](#usage)
- [Models](#models)
- [Conclusion](#conclusion)

## Overview
This project aims to predict future Bitcoin prices using time series analysis techniques. The project leverages Prophet, a forecasting model developed by Facebook, to capture trends and seasonality in historical Bitcoin price data. The model is designed to forecast future prices based on historical data obtained from Yahoo Finance.

## Dataset
The dataset used for this project is the historical Bitcoin price data retrieved from Yahoo Finance. It contains daily records of Bitcoin's open, high, low, close prices, volume, and adjusted close price.

## Features
- **Data Collection**: Fetching Bitcoin price data using `yfinance`.
- **Data Preprocessing**: Cleaning and preparing the data for analysis.
- **Feature Engineering**: Adding new features such as moving averages, daily returns, and volatility.
- **Model Training**: Training the Prophet model to predict future Bitcoin prices.
- **Model Evaluation**: Evaluating model performance using metrics like Mean Absolute Percentage Error (MAPE) and Mean Squared Error (MSE).

## Usage
1. Clone the repository from your preferred source control platform.
2. Install the required packages using `pip install -r requirements.txt`.
3. Download the Bitcoin price data using the `yfinance` library, or place a pre-downloaded CSV file in the `data` directory.
4. Run the script to preprocess the data and train the Prophet model.
5. Run the script to make predictions and visualize the results.

## Models
- **Prophet**: A robust time series forecasting model that handles seasonality, trends, and holidays.
- **ARIMA**: A basic time series forecasting model that is also evaluated for comparison.
- **LSTM (Optional)**: A deep learning model for forecasting, which may be tested as a future extension of this project.

## Conclusion
This project demonstrates the use of time series analysis for forecasting Bitcoin prices using Prophet. Future improvements could involve experimenting with additional models like SARIMA or deep learning methods like LSTM, as well as fine-tuning hyperparameters for enhanced predictive accuracy.

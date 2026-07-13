# 📈 End-to-End Sales Forecasting & Demand Intelligence System

A complete **Time Series Forecasting & Demand Intelligence** project developed as part of the **Week 3 & Week 4 Data Science Internship**.

This project analyzes historical retail sales data, forecasts future demand using multiple forecasting models, detects anomalies, segments products based on demand behavior, and provides an interactive Streamlit dashboard for business decision-making.

---

# 🚀 Project Objectives

- Analyze retail sales trends
- Forecast future sales demand
- Compare multiple forecasting models
- Detect unusual sales spikes and drops
- Segment products using Machine Learning
- Build an interactive business dashboard
- Generate actionable business insights

---

# 📂 Project Structure

```text
SalesForecasting_PrashantAhuja/
│
├── app.py
├── analysis.ipynb
├── train.csv
├── vgsales.csv
├── requirements.txt
├── README.md
│
├── charts/
│
├── outputs/
│
└── models/
```

---

# 📊 Dataset

### Primary Dataset

**Superstore Sales Dataset**

Contains four years of historical retail sales including:

- Orders
- Customers
- Products
- Categories
- Regions
- Profit
- Discount
- Shipping Information

---

### Supplementary Dataset

**Video Game Sales Dataset**

Used for:

- Multi-source data analysis
- Data merging
- Anomaly detection demonstration

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Seaborn
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit

---

# 📌 Project Workflow

## Task 1

### Data Loading & Exploration

- Data Cleaning
- Missing Value Analysis
- Duplicate Removal
- Feature Engineering
- Revenue Analysis
- Shipping Analysis
- Seasonality Analysis

---

## Task 2

### Time Series Analysis

- Monthly Sales Trend
- Seasonal Decomposition
- Trend Analysis
- Residual Analysis
- Stationarity Testing
- Augmented Dickey-Fuller Test
- Differencing

---

## Task 3

### Sales Forecasting

Implemented three forecasting models:

- SARIMA
- Facebook Prophet
- XGBoost Regressor

Compared using:

- MAE
- RMSE
- MAPE

Automatically selected the best performing model.

---

## Task 4

### Category & Region Forecasting

Forecasts generated for:

- Furniture
- Technology
- Office Supplies
- West Region
- East Region

---

## Task 5

### Anomaly Detection

Implemented two anomaly detection methods:

- Isolation Forest
- Z-Score

Compared both approaches and identified abnormal sales weeks.

---

## Task 6

### Product Demand Segmentation

Used:

- StandardScaler
- K-Means Clustering
- PCA

Demand Segments:

- High Volume, Stable Demand
- Growing Demand
- Low Volume, High Volatility
- Declining Demand

---

## Task 7

### Interactive Streamlit Dashboard

The dashboard includes four pages:

### 📊 Sales Overview

- KPI Cards
- Yearly Sales
- Monthly Sales Trend
- Region & Category Filters

### 📈 Forecast Explorer

- Best Model
- Forecast Horizon
- Segment Forecasts
- Model Performance

### 🚨 Anomaly Report

- Isolation Forest Results
- Weekly Sales
- Anomaly Comparison

### 📦 Product Demand Segments

- PCA Visualization
- Cluster Summary
- Stocking Recommendations

---

# 📈 Forecasting Models

| Model | Purpose |
|--------|----------|
| SARIMA | Statistical Time Series Forecasting |
| Prophet | Business Time Series Forecasting |
| XGBoost | Machine Learning Forecasting |

---

# 📊 Machine Learning Techniques

- Time Series Forecasting
- Isolation Forest
- K-Means Clustering
- PCA
- Feature Engineering
- Time Series Decomposition

---

# 📁 Generated Outputs

The project automatically generates:

- Forecast Reports
- Cleaned Dataset
- Weekly Sales
- Monthly Sales
- Cluster Reports
- Anomaly Reports
- Comparison Reports

---

# 📸 Generated Charts

- Revenue by Category
- Monthly Sales Trend
- Regional Sales Growth
- Time Series Decomposition
- SARIMA Forecast
- Prophet Forecast
- XGBoost Forecast
- Isolation Forest
- Z-Score Detection
- Product Clusters
- Elbow Method

---

# ▶️ Run the Project

## Clone Repository

```bash
git clone https://github.com/Prabhu0712/SalesForecasting_PrashantAhuja.git
```

## Move to Project Folder

```bash
cd SalesForecasting_PrashantAhuja
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Launch Dashboard

```bash
streamlit run app.py
```

---

# 📌 Results

- ✔ Comprehensive Sales Analysis
- ✔ Three Forecasting Models Compared
- ✔ Automatic Best Model Selection
- ✔ Product Demand Segmentation
- ✔ Sales Anomaly Detection
- ✔ Interactive Business Dashboard

---

# 🎯 Business Impact

This project helps retail businesses:

- Improve inventory planning
- Reduce overstocking
- Minimize stock-outs
- Forecast future demand
- Detect unusual sales patterns
- Support data-driven decision making

---

# 👨‍💻 Developer

**Prashant Ahuja**

B.Tech Computer Science Engineering

Manav Rachna International Institute of Research and Studies (MRIIRS)

---

# ⭐ Acknowledgements

- Kaggle Superstore Sales Dataset
- Kaggle Video Game Sales Dataset
- Streamlit
- Scikit-learn
- Statsmodels
- Facebook Prophet
- XGBoost

---

## 📜 License

This project is developed for educational and internship purposes.

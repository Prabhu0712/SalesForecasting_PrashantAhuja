# ==============================================================================
# End-to-End Sales Forecasting & Demand Intelligence System
# Streamlit Dashboard
# Student : Prashant Ahuja
# ==============================================================================

import os
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go

# ==============================================================================
# Page Configuration
# ==============================================================================

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# Global Styling (CSS)
# ==============================================================================
# NOTE: This is pure styling — no app logic was changed here. It's safe on
# Streamlit Cloud since it only injects CSS, no external assets are loaded.

st.markdown(
    """
    <style>
        /* ---------- Fonts ---------- */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        }

        /* ---------- Overall page ---------- */
        .stApp {
            background: radial-gradient(circle at top left, #131722 0%, #0b0d13 55%, #0a0b10 100%);
        }
        .block-container {
            padding-top: 1.6rem;
            padding-bottom: 2.5rem;
            max-width: 1250px;
        }

        /* ---------- Scrollbar ---------- */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #0f1117;
        }
        ::-webkit-scrollbar-thumb {
            background: #2f3646;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #4C8BF5;
        }

        /* ---------- Headings ---------- */
        h1, h2, h3 {
            font-family: 'Poppins', 'Inter', sans-serif;
        }
        h1 {
            font-weight: 700;
            font-size: 2.1rem;
            padding-bottom: 0.5rem;
            background: linear-gradient(90deg, #4C8BF5 0%, #7FB2FF 45%, #4C8BF5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            border-bottom: 3px solid #4C8BF5;
            margin-bottom: 1.4rem;
            letter-spacing: 0.3px;
        }
        h2, h3 {
            font-weight: 600;
            color: #E8ECF7;
        }
        h3 {
            border-left: 4px solid #4C8BF5;
            padding-left: 0.6rem;
            margin-top: 1.2rem;
        }

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #171b26 0%, #12151e 100%);
            border-right: 1px solid #262b36;
        }
        section[data-testid="stSidebar"] h1 {
            -webkit-text-fill-color: #4C8BF5;
            background: none;
            border-bottom: none;
            font-size: 1.35rem;
            margin-bottom: 0.8rem;
        }
        section[data-testid="stSidebar"] .stRadio label {
            font-size: 0.95rem;
            padding: 0.15rem 0;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] > label {
            background: #1b2030;
            border: 1px solid #262b36;
            border-radius: 10px;
            padding: 0.55rem 0.8rem;
            margin-bottom: 0.4rem;
            transition: all 0.2s ease-in-out;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
            border-color: #4C8BF5;
            background: #202940;
            transform: translateX(3px);
        }

        /* ---------- Metric cards ---------- */
        div[data-testid="stMetric"] {
            background: linear-gradient(135deg, #1b2030 0%, #1f2637 100%);
            border: 1px solid #2a3040;
            border-radius: 16px;
            padding: 1.1rem 1.3rem;
            box-shadow: 0 4px 14px rgba(0,0,0,0.3);
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }
        div[data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            border-color: #4C8BF5;
            box-shadow: 0 8px 20px rgba(76,139,245,0.25);
        }
        div[data-testid="stMetricLabel"] {
            font-weight: 600;
            opacity: 0.8;
            text-transform: uppercase;
            font-size: 0.78rem;
            letter-spacing: 0.6px;
        }
        div[data-testid="stMetricValue"] {
            color: #7FB2FF;
            font-weight: 700;
            font-family: 'Poppins', sans-serif;
        }

        /* ---------- Buttons ---------- */
        .stButton > button, .stDownloadButton > button {
            background: linear-gradient(90deg, #4C8BF5, #3f6fd1);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1.2rem;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 3px 10px rgba(76,139,245,0.25);
        }
        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(76,139,245,0.4);
        }

        /* ---------- Selectbox / Slider / Inputs ---------- */
        div[data-baseweb="select"] > div {
            background-color: #1b2030;
            border-radius: 10px;
            border: 1px solid #2a3040;
        }
        .stSlider > div > div > div > div {
            background-color: #4C8BF5;
        }

        /* ---------- Dataframes / Tables ---------- */
        div[data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #262b36;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }

        /* ---------- Info / alert boxes ---------- */
        div[data-testid="stAlert"] {
            border-radius: 14px;
            border-left: 4px solid #4C8BF5;
        }

        /* ---------- Plotly chart container ---------- */
        div[data-testid="stPlotlyChart"] {
            background: #12151f;
            border: 1px solid #232838;
            border-radius: 16px;
            padding: 0.8rem;
            box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        }

        /* ---------- Divider spacing ---------- */
        hr {
            margin: 1.4rem 0;
            border-color: #232838;
        }

        /* ---------- Fade-in on every page load / page switch ---------- */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(14px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .block-container {
            animation: fadeInUp 0.5s ease-out;
        }

        /* ---------- Hero header (top of each page) ---------- */
        .hero-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            background: linear-gradient(120deg, #1b2030 0%, #171b26 100%);
            border: 1px solid #262b36;
            border-radius: 18px;
            padding: 1.1rem 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        }
        .hero-icon {
            font-size: 2.1rem;
            background: linear-gradient(135deg, #4C8BF5, #7FB2FF);
            width: 58px;
            height: 58px;
            min-width: 58px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(76,139,245,0.35);
        }
        .hero-title {
            font-family: 'Poppins', sans-serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: #F1F4FA;
            margin: 0;
            line-height: 1.2;
        }
        .hero-subtitle {
            color: #93A0BE;
            font-size: 0.92rem;
            margin-top: 0.15rem;
        }

        /* ---------- Footer ---------- */
        .footer-box {
            text-align: center;
            padding: 1.8rem 1rem 0.6rem 1rem;
            opacity: 0.9;
        }
        .footer-box h3 {
            color: #4C8BF5;
            border-left: none;
            padding-left: 0;
            margin-bottom: 0.3rem;
            font-size: 1.15rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# Project Paths
# ==============================================================================
# Using the script's own directory keeps this portable between local runs
# and Streamlit Community Cloud, where the working directory is the repo root.

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(PROJECT_PATH, "train.csv")
OUTPUT_PATH = os.path.join(PROJECT_PATH, "outputs")


def require_file(path, friendly_name):
    """Stops the app gracefully with a clear message if a required data
    file hasn't been uploaded to the repo — this is the #1 reason a
    Streamlit Cloud deploy shows a blank/error page."""
    if not os.path.exists(path):
        st.error(
            f"⚠️ Required file **{friendly_name}** was not found at:\n\n"
            f"`{path}`\n\n"
            f"Make sure it's committed to your GitHub repo (in the same "
            f"folder structure) before deploying to Streamlit Cloud."
        )
        st.stop()
    return path


@st.cache_data
def load_csv(path):
    """Cached CSV reader — avoids re-reading the same file from disk on
    every widget interaction (Streamlit reruns the whole script on each
    one, e.g. moving the forecast horizon slider)."""
    return pd.read_csv(path)

# ==============================================================================
# Load Data
# ==============================================================================

@st.cache_data
def load_data():

    sales = load_csv(
        require_file(DATA_PATH, "train.csv")
    )

    sales["Order Date"] = pd.to_datetime(
        sales["Order Date"],
        dayfirst=True
    )

    sales["Ship Date"] = pd.to_datetime(
        sales["Ship Date"],
        dayfirst=True
    )

    return sales

sales = load_data()

# ==============================================================================
# Sidebar
# ==============================================================================

st.sidebar.title("📈 Navigation")

page = st.sidebar.radio(

    "Select Page",

    [

        "Sales Overview",

        "Forecast Explorer",

        "Anomaly Report",

        "Product Demand Segments"

    ]

)

st.sidebar.markdown("---")

st.sidebar.write("End-to-End Sales Forecasting")

st.sidebar.write("Week 3 & Week 4 Internship Project")

# ==============================================================================
# Reusable hero header (used at the top of every page)
# ==============================================================================

PAGE_META = {
    "Sales Overview": ("📊", "Sales Overview Dashboard", "High-level KPIs, yearly & monthly trends, and regional drill-downs."),
    "Forecast Explorer": ("📈", "Forecast Explorer", "Compare model performance and explore segment-level forecasts."),
    "Anomaly Report": ("🚨", "Anomaly Detection Report", "Weekly sales with anomalies flagged via Isolation Forest vs Z-Score."),
    "Product Demand Segments": ("📦", "Product Demand Segmentation", "Cluster products by demand behaviour and recommended stocking strategy."),
}

def render_header(page_name):
    icon, title, subtitle = PAGE_META[page_name]
    st.markdown(
        f"""
        <div class="hero-header">
            <div class="hero-icon">{icon}</div>
            <div>
                <p class="hero-title">{title}</p>
                <p class="hero-subtitle">{subtitle}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def scroll_to_top():
    """Scroll the main Streamlit viewport back to the top after a page
    change. Retries a few times because Streamlit may still be laying
    out the new page's content the instant this first runs."""
    components.html(
        """
        <script>
            (() => {
                const doc = window.parent && window.parent.document ? window.parent.document : document;

                const scrollAll = () => {
                    const containers = [
                        doc.querySelector('section.main'),
                        doc.querySelector('[data-testid="stAppViewContainer"]'),
                        doc.querySelector('[data-testid="stMain"]'),
                        doc.querySelector('.main'),
                        doc.querySelector('.block-container'),
                        doc.documentElement,
                        doc.body
                    ].filter(Boolean);

                    containers.forEach((el) => {
                        try {
                            el.scrollTop = 0;
                            if (el.scrollTo) el.scrollTo(0, 0);
                        } catch (e) {}
                    });

                    try { window.parent.scrollTo(0, 0); } catch (e) {}
                    try { window.scrollTo(0, 0); } catch (e) {}
                };

                scrollAll();
                setTimeout(scrollAll, 50);
                setTimeout(scrollAll, 200);
                setTimeout(scrollAll, 500);
            })();
        </script>
        """,
        height=0,
    )


if "active_page" not in st.session_state:
    st.session_state.active_page = page

if st.session_state.active_page != page:
    st.session_state.active_page = page
    scroll_to_top()
elif "initialized" not in st.session_state:
    st.session_state.initialized = True
    scroll_to_top()

# ==============================================================================
# PAGE 1
# ==============================================================================

if page == "Sales Overview":

    render_header(page)

    total_sales = sales["Sales"].sum()

    total_orders = sales["Order ID"].nunique()

    total_customers = sales["Customer ID"].nunique()

    avg_order = sales["Sales"].mean()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Total Sales",
        f"${total_sales:,.0f}"
    )

    c2.metric(
        "Orders",
        total_orders
    )

    c3.metric(
        "Customers",
        total_customers
    )

    c4.metric(
        "Average Order Value",
        f"${avg_order:.2f}"
    )

    st.markdown("---")

    sales["Year"] = sales["Order Date"].dt.year

    yearly = (

        sales

        .groupby("Year")["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.bar(

        yearly,

        x="Year",

        y="Sales",

        title="Total Sales by Year",

        text_auto=".2s",

        color_discrete_sequence=["#4C8BF5"]

    )

    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    sales["Month"] = sales["Order Date"].dt.to_period("M").astype(str)

    monthly = (

        sales

        .groupby("Month")["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.line(

        monthly,

        x="Month",

        y="Sales",

        markers=True,

        title="Monthly Sales Trend",

        color_discrete_sequence=["#4C8BF5"]

    )

    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    left,right = st.columns(2)

    with left:

        region = st.selectbox(

            "Select Region",

            sorted(

                sales["Region"].unique()

            )

        )

    with right:

        category = st.selectbox(

            "Select Category",

            sorted(

                sales["Category"].unique()

            )

        )

    filtered = sales[

        (sales["Region"]==region)

        &

        (sales["Category"]==category)

    ]

    fig = px.bar(

        filtered,

        x="Sub-Category",

        y="Sales",

        color="Sub-Category",

        title="Sales by Sub-Category"

    )

    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.dataframe(

        filtered.head(20),

        use_container_width=True

    )

# ==============================================================================
# PAGE 2
# ==============================================================================

elif page == "Forecast Explorer":

    render_header(page)

    comparison_path = require_file(
        os.path.join(OUTPUT_PATH, "model_comparison.csv"),
        "outputs/model_comparison.csv"
    )

    comparison = load_csv(comparison_path)

    st.subheader("Model Performance")

    st.dataframe(

        comparison,

        use_container_width=True

    )

    selected = st.selectbox(

        "Select Forecast Segment",

        [

            "Furniture",

            "Technology",

            "Office Supplies",

            "West",

            "East"

        ]

    )

    horizon = st.slider(

        "Forecast Horizon (Months)",

        1,

        3,

        3

    )

    forecast_path = require_file(
        os.path.join(OUTPUT_PATH, "segment_forecasts.csv"),
        "outputs/segment_forecasts.csv"
    )

    forecast = load_csv(forecast_path)

    forecast = forecast[

        forecast["Segment"]==selected

    ]

    forecast = forecast.head(horizon)

    fig = px.line(

        forecast,

        x="Date",

        y="Forecast",

        markers=True,

        title=f"{selected} Forecast",

        color_discrete_sequence=["#4C8BF5"]

    )

    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.dataframe(

        forecast,

        use_container_width=True

    )

    best = comparison.sort_values(

        "RMSE"

    ).iloc[0]

    c1,c2,c3 = st.columns(3)

    c1.metric(

        "Best Model",

        best["Model"]

    )

    c2.metric(

        "MAE",

        round(best["MAE"],2)

    )

    c3.metric(

        "RMSE",

        round(best["RMSE"],2)

    )

# ==============================================================================
# PAGE 3
# ==============================================================================

elif page == "Anomaly Report":

    render_header(page)

    anomaly_path = require_file(
        os.path.join(OUTPUT_PATH, "anomaly_comparison.csv"),
        "outputs/anomaly_comparison.csv"
    )

    anomaly = load_csv(anomaly_path)

    anomaly["Week"] = pd.to_datetime(
        anomaly["Week"]
    )

    iso_report_path = require_file(
        os.path.join(OUTPUT_PATH, "isolation_forest_report.csv"),
        "outputs/isolation_forest_report.csv"
    )

    iso_report = load_csv(iso_report_path)

    iso_report["Week"] = pd.to_datetime(
        iso_report["Week"]
    )

    st.subheader("Weekly Sales")

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=anomaly["Week"],

            y=anomaly["Weekly Sales"],

            mode="lines",

            name="Weekly Sales",

            line=dict(color="#4C8BF5")

        )

    )

    fig.add_trace(

        go.Scatter(

            x=iso_report["Week"],

            y=iso_report["Weekly Sales"],

            mode="markers",

            marker=dict(

                size=10,

                color="#FF4B4B"

            ),

            name="Anomalies"

        )

    )

    fig.update_layout(

        title="Isolation Forest Anomaly Detection",

        xaxis_title="Week",

        yaxis_title="Weekly Sales",

        template="plotly_dark",

        plot_bgcolor="rgba(0,0,0,0)",

        paper_bgcolor="rgba(0,0,0,0)"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.subheader("Detected Anomalies")

    st.dataframe(

        iso_report,

        use_container_width=True

    )

    st.markdown("---")

    st.subheader("Isolation Forest vs Z-Score")

    st.dataframe(

        anomaly,

        use_container_width=True

    )

# ==============================================================================
# PAGE 4
# ==============================================================================

elif page == "Product Demand Segments":

    render_header(page)

    segments_path = require_file(
        os.path.join(OUTPUT_PATH, "product_segments.csv"),
        "outputs/product_segments.csv"
    )

    segments = load_csv(segments_path)

    summary_path = require_file(
        os.path.join(OUTPUT_PATH, "cluster_summary.csv"),
        "outputs/cluster_summary.csv"
    )

    summary = load_csv(summary_path)

    fig = px.scatter(

        segments,

        x="PCA1",

        y="PCA2",

        color="Demand Segment",

        hover_name="Sub-Category",

        title="Product Demand Clusters"

    )

    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.subheader("Product Segments")

    st.dataframe(

        segments,

        use_container_width=True

    )

    st.subheader("Cluster Summary")

    st.dataframe(

        summary,

        use_container_width=True

    )

    st.markdown("---")

    st.subheader("Recommended Stocking Strategy")

    st.info(

        """
**High Volume, Stable Demand**
- Maintain high inventory.
- Regular replenishment.

**Growing Demand**
- Increase inventory gradually.
- Monitor monthly demand.

**Low Volume, High Volatility**
- Keep minimum stock.
- Reorder only when required.

**Declining Demand**
- Reduce inventory.
- Avoid overstocking.
        """

    )

# ==============================================================================
# FOOTER
# ==============================================================================

st.markdown("---")

st.markdown(
    """
<div class='footer-box'>

### End-to-End Sales Forecasting & Demand Intelligence System

Developed by **Prashant Ahuja**

MRIIRS | B.Tech CSE | Week 3 & Week 4 Internship Project

</div>
""",
unsafe_allow_html=True
)

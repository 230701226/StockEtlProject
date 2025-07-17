# Data Pipeline & Visualization using Python
📊 StockETL – Internship Task Documentation
COMPANY: CodTech IT Solutions
NAME: Pooja A K
DOMAIN: Data Science
DURATION: 4 Weeks
MENTOR: Neela Santosh

DESCRIPTION OF TASK
I developed a fully automated StockETL Data Pipeline and deployed a visual dashboard using Streamlit, focused on processing and analyzing historical stock data for multiple companies.

The project automates the ETL (Extract, Transform, Load) process for over 30 stock tickers, generating meaningful financial metrics and interactive visualizations.

Key capabilities include:

Batch-wise ingestion of raw CSV files (one per stock)
 Preprocessing: date parsing, handling missing values, and feature engineering (returns, volatility)
 Statistical feature scaling (StandardScaler)
 Export to clean, processed dataset (processed_data.csv)
 Insight generation: trend lines, volatility, and rolling averages
 Deployment of full dashboard via Streamlit.io

TECHNOLOGIES USED
Tool	Purpose
Python	Core programming and logic
pandas	Reading, preprocessing, and aggregation
scikit-learn	Feature scaling (StandardScaler)
matplotlib	Data visualization for trends and patterns
Streamlit	Building and deploying interactive dashboard

DEPLOYMENT METHODS
Local ETL Execution (Python Script)
Tested and executed via:

bash
Copy
Edit
python run_pipeline.py
Reads raw stock CSVs from /data

Generates processed_data.csv in /output

Stores logs in etl_log.txt

Supports over 15,000 rows of processed stock data

Shows summary stats in summary.md

🌐 Online Deployment via Streamlit.io
Live dashboard hosted on:
🔗 StockETL Dashboard – Hugging Face Spaces

Features include:

 Upload and explore processed stock data

 Dynamic visualizations: price trends, volume distribution, returns

 Ticker-wise filtering, timeline selection

 Time-series plots using matplotlib

 Download processed output

⚠ Note: Only online deployment via Streamlit.io was used. Offline deployment via Docker was explored but not submitted due to time constraints.

 SAMPLE OUTPUT
 ETL Output Table
Stock Symbol	Date	Close	Volume	Return	Volatility
INFY	2023-01-01	140.23	12,450,000	0.0023	0.015
TCS	2023-01-02	3450.45	9,320,000	-0.0015	0.009

 Visual Snapshots

<img width="1784" height="906" alt="Screenshot 2025-07-17 191024" src="https://github.com/user-attachments/assets/b1b2cefe-c926-4ee5-bab5-98a05724a4d0" />
<img width="1295" height="623" alt="Screenshot 2025-07-17 191044" src="https://github.com/user-attachments/assets/91fbf150-0ca7-4cde-84e2-504df40193c6" />
<img width="1263" height="829" alt="Screenshot 2025-07-17 191055" src="https://github.com/user-attachments/assets/24fbfb50-c614-4c3e-ba94-f25fad60c6b1" />
<img width="1795" height="840" alt="Screenshot 2025-07-17 191114" src="https://github.com/user-attachments/assets/47b73cfa-a781-40f1-abc3-f4c090dedc9f" />



🏁 CONCLUSION
This project demonstrates:

 Strong data engineering with custom ETL
 Feature engineering for stock market analytics
 Visual storytelling through interactive dashboards
 Production-grade deployment using Streamlit.io

It’s a valuable addition to my portfolio, showcasing my ability to create scalable data workflows and insightful user interfaces for financial analytics.

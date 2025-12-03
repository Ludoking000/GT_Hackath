# TrendSpotter — Automated Insight Engine
### Hackathon Problem Code: H-001 — The Automated Insight Engine

TrendSpotter is an AI-driven system that automatically ingests marketing datasets, analyzes performance trends, detects insights, generates charts, and produces a multi-page PDF report with an executive summary.

This project solves **H-001: The Automated Insight Engine**, which requires building an automated system that:
- Accepts data from multiple sources
- Cleans and transforms it
- Extracts insights
- Generates visualizations
- Creates a report

---

## Problem Statement (H-001)

Businesses generate large amounts of marketing performance data but often struggle to interpret:
- Key performance trends
- Which metrics are improving or declining
- What actions should be taken based on the data

This system automatically:
1. Ingests a dataset (default or user-provided)
2. Cleans and preprocesses the data
3. Extracts KPIs
4. Performs trend analysis (upward, downward, or stable)
5. Generates charts
6. Creates a professional PDF report
7. Produces an AI-generated executive summary

---

## Features

### 1. Multi-Dataset Support
- Accepts **CSV or Excel files**
- User can pass a dataset path, or use the included default dataset

### 2. Automated Data Ingestion
- Auto-detects file type
- Auto-parses date columns
- Cleans missing values

### 3. KPI Extraction
Automatically computes:
- Total and average Clicks
- Impressions
- Engagement Score
- ROI
- Acquisition Cost

### 4. Trend Detection
Detects whether metrics are:
- Strong upward trend
- Mild upward trend
- No significant change
- Mild downward trend
- Strong downward trend

### 5. Chart Generation
Automatically generates and saves:
- Clicks over time
- Impressions over time
- Engagement Score over time
- Top 10 Campaigns by Impressions
- ROI by Channel

Charts are saved in:
Output/



### 6. AI Executive Summary (GPT)
Uses GPT-4o-mini to generate a polished business narrative including:
- Overall performance summary
- Key improvements and declines
- Risk indicators
- Recommendations

### 7. Professional PDF Report
Includes:
- KPI summary
- Trend insights
- Takeaways
- Executive summary
- Embedded charts
Saved at:
Output/report.pdf


---

## Dataset Information

### Default Dataset Used
data/raw/marketing_campaign_dataset.xlsx
(https://www.kaggle.com/datasets/guelmaniloubna/marketing-campaign-dataset)

Contains:
- Date  
- Campaign  
- Company  
- Channel  
- Impressions  
- Clicks  
- Engagement Score  
- ROI  
- Acquisition Cost  
- Target Audience  

Users can replace this with their own dataset.

---

## How Users Can Load Their Own Dataset

### Run with a custom CSV or Excel file:
python src/pipeline.py --dataset "path/to/yourfile.csv"

### Run using the default dataset:
python src/pipeline.py


---

## Folder Structure

GT_Hackath/
│── data/
│ └── raw/
│ └── marketing_campaign_dataset.xlsx
│── src/
│ ├── preprocessing.py
│ ├── analysis.py
│ ├── insights.py
│ ├── gpt_insights.py
│ ├── report_generator.py
│ └── pipeline.py
│── Output/
│ └── report.pdf
│── Screenshots/
│── README.md
│── requirements.txt


---

## How to Run

### 1. Install dependencies:
pip install -r requirements.txt

### 2. Set OpenAI API key:
setx OPENAI_API_KEY "your_api_key_here"

Restart VS Code after setting this.

### 3. Run the pipeline:
python src/pipeline.py


### 4. Run with a custom dataset:
python src/pipeline.py --dataset "data/raw/custom.xlsx"



---

## Output Generated

### 1. PDF Report
Located at:
Output/report.pdf

### 2. Charts
Saved in:
Output/

### Example Insights:
Clicks: ↑ Strong upward trend (+12.45%)
Impressions: ↓ Mild downward trend (-3.22%)
Engagement Score: ↓ Strong downward trend (-15.21%)
ROI: ↑ Strong upward trend (+8.55%)

TOP TAKEAWAYS:
• Clicks are rising significantly — strong audience engagement.
• Impressions are falling — consider expanding audience targeting.
• ROI is improving — marketing efficiency increasing.

---

## Tech Stack

- Python  
- Pandas  
- Matplotlib  
- ReportLab  
- OpenAI GPT-4o-mini  
- CLI Argument Parser  

---

## Future Improvements

- Spike and anomaly detection  
- Interactive dashboard UI  
- SQL/Database ingestion  
- Automated email delivery  

---

## Conclusion

TrendSpotter fulfills all requirements of **H-001: The Automated Insight Engine** by providing:
- End-to-end automated analytics
- Flexible dataset input
- KPI + trend insights
- AI-generated summaries
- Fully formatted reports

This tool is ready for real-world marketing intelligence use.


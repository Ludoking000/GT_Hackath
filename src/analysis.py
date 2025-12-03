import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_basic_analysis(df):
    summary = df.describe(include="all")

    kpis = {}
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        kpis[col] = {
            "min": df[col].min(),
            "max": df[col].max(),
            "mean": df[col].mean(),
            "sum": df[col].sum()
        }

    return {
        "summary": summary,
        "kpis": kpis,
        "df_for_trends": df
    }




def generate_charts(df):
    chart_paths = []
    os.makedirs("Output", exist_ok=True)

    # Ensure Date is datetime if present
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Month"] = df["Date"].dt.to_period("M").astype(str)
    else:
        # fallback: create artificial month groups every 30 rows
        df["Month"] = (df.index // 30).astype(str)

    # ---------------------------------------
    # 1. Clicks per Month
    # ---------------------------------------
    if "Clicks" in df.columns:
        monthly_clicks = df.groupby("Month")["Clicks"].mean()

        plt.figure(figsize=(10,5))
        monthly_clicks.plot(marker="o", linewidth=3, color="#007acc")
        plt.title("Average Clicks per Month", fontsize=14)
        plt.xlabel("Month")
        plt.ylabel("Clicks")
        path = "Output/clicks_monthly.png"
        plt.savefig(path, bbox_inches="tight")
        plt.close()
        chart_paths.append(path)

    # ---------------------------------------
    # 2. Impressions per Month
    # ---------------------------------------
    if "Impressions" in df.columns:
        monthly_impressions = df.groupby("Month")["Impressions"].mean()

        plt.figure(figsize=(10,5))
        monthly_impressions.plot(marker="o", linewidth=3, color="#00a65a")
        plt.title("Average Impressions per Month", fontsize=14)
        plt.xlabel("Month")
        plt.ylabel("Impressions")
        path = "Output/impressions_monthly.png"
        plt.savefig(path, bbox_inches="tight")
        plt.close()
        chart_paths.append(path)

    # ---------------------------------------
    # 3. Engagement by Customer Segment
    # ---------------------------------------
    if "Engagement_Score" in df.columns and "Customer_Segment" in df.columns:
        seg_engagement = df.groupby("Customer_Segment")["Engagement_Score"].mean()

        plt.figure(figsize=(10,5))
        seg_engagement.plot(kind="bar", color="#ff9900")
        plt.title("Engagement Score by Customer Segment", fontsize=14)
        plt.ylabel("Engagement Score")
        plt.xticks(rotation=45, ha="right")
        path = "Output/engagement_by_segment.png"
        plt.savefig(path, bbox_inches="tight")
        plt.close()
        chart_paths.append(path)

    # ---------------------------------------
    # 4. ROI by Company
    # ---------------------------------------
    if "ROI" in df.columns and "Company" in df.columns:
        company_roi = df.groupby("Company")["ROI"].mean()

        plt.figure(figsize=(10,5))
        company_roi.plot(kind="bar", color="#9933ff")
        plt.title("Average ROI by Company", fontsize=14)
        plt.ylabel("ROI")
        plt.xticks(rotation=45, ha="right")
        path = "Output/roi_by_company.png"
        plt.savefig(path, bbox_inches="tight")
        plt.close()
        chart_paths.append(path)

    return chart_paths

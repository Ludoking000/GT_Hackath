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



def generate_charts(df, output_dir="Output"):
    """Generate trend charts + bar charts and save them as PNG."""

    os.makedirs(output_dir, exist_ok=True)

    chart_paths = []

    # -------- 1. Spend over time --------
    for col in df.columns:
        if "date" in col.lower():
            date_col = col
            break
    else:
        date_col = None

    if date_col:
        df_sorted = df.sort_values(date_col)

        if "spend" in df.columns:
            plt.figure(figsize=(8, 4))
            plt.plot(df_sorted[date_col], df_sorted["spend"], marker="o")
            plt.title("Spend Over Time")
            plt.xlabel("Date")
            plt.ylabel("Spend")
            path = os.path.join(output_dir, "spend_over_time.png")
            plt.savefig(path)
            plt.close()
            chart_paths.append(path)

        if "impressions" in df.columns:
            plt.figure(figsize=(8, 4))
            plt.plot(df_sorted[date_col], df_sorted["impressions"], marker="o", color="green")
            plt.title("Impressions Over Time")
            plt.xlabel("Date")
            plt.ylabel("Impressions")
            path = os.path.join(output_dir, "impressions_over_time.png")
            plt.savefig(path)
            plt.close()
            chart_paths.append(path)

    # -------- 2. Bar chart: Top campaigns --------
    for possible_col in ["campaign", "campaign_name", "ad_name", "adgroup"]:
        if possible_col in df.columns:
            campaign_col = possible_col
            break
    else:
        campaign_col = None

    if campaign_col and "spend" in df.columns:
        top_campaigns = df.groupby(campaign_col)["spend"].sum().nlargest(10)

        plt.figure(figsize=(8, 4))
        top_campaigns.plot(kind="bar")
        plt.title("Top Campaign Spend")
        plt.xlabel("Campaign")
        plt.ylabel("Total Spend")
        path = os.path.join(output_dir, "top_campaigns.png")
        plt.savefig(path)
        plt.close()
        chart_paths.append(path)

    return chart_paths

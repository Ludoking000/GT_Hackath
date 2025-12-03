import pandas as pd

def percentage_change(series):
    """Return percentage change between first and last values."""
    if len(series) < 2:
        return 0
    start = series.iloc[0]
    end = series.iloc[-1]
    if start == 0:
        return 0
    return ((end - start) / start) * 100


def trend_direction(pct):
    """Convert percentage change into readable ASCII arrows."""
    if pct > 10:
        return f"↑ Strong upward trend (+{pct:.2f}%)"
    elif pct > 0:
        return f"↑ Mild upward trend (+{pct:.2f}%)"
    elif pct < -10:
        return f"↓ Strong downward trend ({pct:.2f}%)"
    elif pct < 0:
        return f"↓ Mild downward trend ({pct:.2f}%)"
    else:
        return f"→ No significant change ({pct:.2f}%)"


def generate_insights(result):
    summary = result["summary"]
    kpis = result["kpis"]
    df = result.get("df_for_trends")

    insights = []
    insights.append("KEY METRICS SUMMARY:\n")

    # KPI values
    for metric, values in kpis.items():
        insights.append(
            f"{metric}: Total = {values['sum']:.2f}, Average = {values['mean']:.2f}"
        )

    insights.append("\nTREND ANALYSIS:\n")

    # Check trends only if df exists and has Date
    if df is not None and "Date" in df.columns:
        df = df.sort_values("Date")
        trend_metrics = ["Clicks", "Impressions", "Engagement_Score", "ROI", "Acquisition_Cost"]

        for metric in trend_metrics:
            if metric in df.columns:
                series = df[metric].reset_index(drop=True)
                pct = percentage_change(series)
                direction = trend_direction(pct)
                insights.append(f"{metric}: {direction}")

    insights.append("\nTOP TAKEAWAYS:")

    # Example takeaways
    if df is not None:
        if "Clicks" in df.columns and percentage_change(df["Clicks"]) > 10:
            insights.append("• Clicks are rising significantly — strong audience engagement.")

        if "Impressions" in df.columns and percentage_change(df["Impressions"]) < -10:
            insights.append("• Impressions are falling — consider expanding audience targeting.")

        if "ROI" in df.columns and percentage_change(df["ROI"]) > 10:
            insights.append("• ROI is improving — marketing efficiency increasing.")

        if "Acquisition_Cost" in df.columns and percentage_change(df["Acquisition_Cost"]) > 5:
            insights.append("• Acquisition cost is rising — campaigns may be getting expensive.")

    return "\n".join(insights)

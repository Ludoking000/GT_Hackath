import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel(path) if path.endswith(".xlsx") else pd.read_csv(path)

    # ---- FIX COLUMN NAMES ----
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Fix truncated names manually
    rename_map = {
        "Impressio": "Impressions",
        "Impression": "Impressions",
        "Engageme": "Engagement_Score",
        "Engagement": "Engagement_Score",
        "Channel_U": "Channel",
        "Campaign_": "Campaign_Name"
    }
    df = df.rename(columns=rename_map)

    # ---- PARSE DATE COLUMN ----
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # ---- CLEAN NUMERIC COLUMNS ----
    numeric_cols = ["Clicks", "Impressions", "Engagement_Score", "ROI", "Acquisition_Cost", "Conversion"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "")
                .str.replace("$", "")
                .astype(float)
                .fillna(0)
            )

    return df

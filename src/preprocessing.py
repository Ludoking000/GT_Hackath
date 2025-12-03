import pandas as pd

def load_and_clean_data(path):
    """Loads CSV or Excel and performs automatic cleaning."""

    # Auto detect file type
    if path.endswith(".xlsx") or path.endswith(".xls"):
        df = pd.read_excel(path)
    elif path.endswith(".csv"):
        df = pd.read_csv(path)
    else:
        raise ValueError("Unsupported file type. Upload CSV or Excel.")

    df = df.drop_duplicates()
    df = df.ffill().bfill()

    # Auto-detect date columns
    for col in df.columns:
        if "date" in col.lower() or "day" in col.lower() or "time" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            except:
                pass

    return df

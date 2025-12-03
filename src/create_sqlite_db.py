import pandas as pd
import sqlite3
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Load dataset
df = pd.read_excel("data/raw/marketing_campaign_dataset.xlsx")

# Create SQLite DB
conn = sqlite3.connect("data/marketing.db")

# Save dataframe as a SQL table
df.to_sql("marketing_data", conn, if_exists="replace", index=False)

conn.close()

print("\n🎉 SQLite Database Created Successfully!")
print("📁 Path: data/marketing.db")
print("📄 Table: marketing_data\n")

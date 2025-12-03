import pandas as pd

df = pd.read_excel("data/raw/marketing_campaign_dataset.xlsx")
df.to_csv("data/raw/marketing_campaign_dataset.csv", index=False)

print("CSV saved as data/raw/marketing_campaign_dataset.csv")

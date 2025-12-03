import os

# -----------------------------
# Folder Structure
# -----------------------------
folders = [
    "data/raw",
    "data/processed",
    "src",
    "notebooks",
    "Output",
    "Screenshots"
]

files_with_content = {
    "requirements.txt": (
        "pandas\n"
        "numpy\n"
        "matplotlib\n"
        "seaborn\n"
        "python-pptx\n"
        "reportlab\n"
        "openpyxl\n"
        "pillow\n"
        "scikit-learn\n"
    ),

    "README.md": (
        "# 🚀 TrendSpotter: Automated Insight Engine\n\n"
        "Template repository for the GroundTruth Mini AI Hackathon.\n\n"
        "This repo contains:\n"
        "- Automated data ingestion\n"
        "- Data analysis pipeline\n"
        "- AI-powered insight generation\n"
        "- Auto-generated PDF reports\n\n"
        "## 📁 Repository Structure\n"
        "This will be updated during the hackathon.\n\n"
        "## 🚀 How to Run\n"
        "```\n"
        "python src/pipeline.py\n"
        "```\n"
    ),

    "src/__init__.py": "",

    "src/preprocessing.py": (
        "def load_and_clean_data(file_path):\n"
        "    \"\"\"\n"
        "    Placeholder: loads CSV and returns cleaned dataframe.\n"
        "    Actual logic will be added during hackathon.\n"
        "    \"\"\"\n"
        "    import pandas as pd\n"
        "    df = pd.read_csv(file_path)\n"
        "    return df\n"
    ),

    "src/analysis.py": (
        "def generate_basic_analysis(df):\n"
        "    \"\"\"\n"
        "    Placeholder for summary statistics & charts.\n"
        "    \"\"\"\n"
        "    summary = df.describe(include='all')\n"
        "    return summary\n"
    ),

    "src/insights.py": (
        "def generate_insights(summary):\n"
        "    \"\"\"\n"
        "    Placeholder for LLM-generated insights.\n"
        "    \"\"\"\n"
        "    return 'Insights will be generated here using AI.'\n"
    ),

    "src/report_generator.py": (
        "def create_pdf_report(output_path, insights, charts=None):\n"
        "    \"\"\"\n"
        "    Placeholder for PDF report generator.\n"
        "    \"\"\"\n"
        "    from reportlab.pdfgen import canvas\n"
        "    c = canvas.Canvas(output_path)\n"
        "    c.drawString(100, 750, 'Automated Insight Report')\n"
        "    c.drawString(100, 720, insights)\n"
        "    c.save()\n"
    ),

    "src/pipeline.py": (
        "from preprocessing import load_and_clean_data\n"
        "from analysis import generate_basic_analysis\n"
        "from insights import generate_insights\n"
        "from report_generator import create_pdf_report\n\n"
        "def run_pipeline(input_csv, output_pdf):\n"
        "    df = load_and_clean_data(input_csv)\n"
        "    summary = generate_basic_analysis(df)\n"
        "    insights = generate_insights(summary)\n"
        "    create_pdf_report(output_pdf, insights)\n\n"
        "if __name__ == '__main__':\n"
        "    run_pipeline('data/raw/sample.csv', 'Output/report.pdf')\n"
    ),

    "notebooks/EDA.ipynb": "",
    "Output/placeholder.txt": "Output files will be stored here.",
    "Screenshots/placeholder.txt": "Screenshots will be placed here."
}

# -----------------------------
# Create folders
# -----------------------------
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# -----------------------------
# Create files with content
# -----------------------------
for filepath, content in files_with_content.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("🎉 Repository skeleton created successfully!")

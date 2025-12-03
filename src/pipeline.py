import argparse
import os

from preprocessing import load_and_clean_data
from db_loader import load_from_sql
from analysis import generate_basic_analysis, generate_charts
from insights import generate_insights
from gpt_insights import generate_gpt_summary
from report_generator import create_pdf_report


def parse_arguments():
    parser = argparse.ArgumentParser(description="Automated Insight Engine Pipeline")

    # File-based dataset
    parser.add_argument(
        "--dataset",
        type=str,
        default="data/raw/marketing_campaign_dataset.xlsx",
        help="Path to CSV or Excel dataset"
    )

    # Database ingestion
    parser.add_argument("--db", type=str, help="SQLAlchemy DB connection string")
    parser.add_argument("--table", type=str, help="Table name to load from SQL")
    parser.add_argument("--query", type=str, help="Custom SQL query")

    return parser.parse_args()


def load_data(args):
    """
    Handles both file-based and SQL-based data ingestion.
    """

    # --- SQL Path ---
    if args.db:
        print(f"📥 Loading dataset from SQL database: {args.db}")

        df = load_from_sql(
            db_url=args.db,
            table=args.table,
            query=args.query
        )
        print("✔ SQL Data Loaded")
        return df

    # --- File Path ---
    print(f"📥 Loading dataset from file: {args.dataset}")
    df = load_and_clean_data(args.dataset)
    print("✔ Excel/CSV Data Loaded")
    return df


def main():
    # ---------------------------------------------------------
    # PARSE ARGUMENTS
    # ---------------------------------------------------------
    args = parse_arguments()

    # ---------------------------------------------------------
    # LOAD DATA (CSV/Excel or SQL)
    # ---------------------------------------------------------
    df = load_data(args)

    # ---------------------------------------------------------
    # ANALYSIS: KPIs + Summary
    # ---------------------------------------------------------
    print("📊 Running basic analysis...")
    result = generate_basic_analysis(df)
    print("✔ KPIs Calculated")

    # ---------------------------------------------------------
    # INSIGHTS: Trends + Takeaways
    # ---------------------------------------------------------
    print("🧠 Generating raw insights...")
    raw_insights = generate_insights(result)
    print("✔ Trend Insights Generated")

    # ---------------------------------------------------------
    # GPT EXECUTIVE SUMMARY
    # ---------------------------------------------------------
    print("🤖 Generating executive summary (GPT)...")
    try:
        gpt_summary = generate_gpt_summary(raw_insights)
    except Exception as e:
        print("⚠ GPT Error:", e)
        gpt_summary = "Executive Summary unavailable (GPT Error)."

    final_insights = (
        raw_insights +
        "\n\nEXECUTIVE SUMMARY:\n" +
        gpt_summary
    )
    print("✔ Executive Summary Added")

    # ---------------------------------------------------------
    # CHART GENERATION
    # ---------------------------------------------------------
    print("📈 Generating charts...")
    chart_paths = generate_charts(df)
    print(f"✔ Charts Generated: {chart_paths}")

    # Ensure output folder exists
    os.makedirs("Output", exist_ok=True)

    # ---------------------------------------------------------
    # PDF REPORT GENERATION
    # ---------------------------------------------------------
    print("📄 Building PDF report...")
    create_pdf_report("Output/report.pdf", final_insights, chart_paths)
    print("✔ PDF Created at Output/report.pdf")

    print("\n🎉 Pipeline completed successfully!\n")


if __name__ == "__main__":
    main()

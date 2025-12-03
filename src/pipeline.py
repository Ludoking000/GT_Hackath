import argparse
from preprocessing import load_and_clean_data
from analysis import generate_basic_analysis, generate_charts
from insights import generate_insights
from report_generator import create_pdf_report
from gpt_insights import generate_gpt_summary

def run_pipeline(input_path=None):
    # If user didn't supply a file, use default dataset
    if input_path is None:
        print("⚠️ No dataset provided. Using default marketing dataset.")
        input_path = "data/raw/marketing_campaign_dataset.xlsx"
    else:
        print(f"📂 Using user-provided dataset: {input_path}")

    # Load + clean data
    df = load_and_clean_data(input_path)

    # KPI/statistics analysis
    result = generate_basic_analysis(df)

    # Text insights
   
    raw_insights = generate_insights(result)
    gpt_summary = generate_gpt_summary(raw_insights)

    final_insights = (
        raw_insights +
        "\n\nEXECUTIVE SUMMARY:\n" +
        gpt_summary
    )


    # Generate charts
    chart_paths = generate_charts(df)

    # Generate PDF
    create_pdf_report("Output/report.pdf", final_insights, chart_paths)


    print("\n🎉 Pipeline completed successfully!")
    print("✔ Data Loaded")
    print("✔ KPIs Calculated")
    print("✔ Insights Generated")
    print("✔ Charts Generated:", chart_paths)
    print("✔ PDF Report saved at Output/report.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Insight Engine")

    parser.add_argument(
        "--dataset",
        type=str,
        default=None,
        help="Path to CSV or Excel file"
    )

    args = parser.parse_args()

    run_pipeline(args.dataset)

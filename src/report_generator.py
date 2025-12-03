from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap
import os

PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT_MARGIN = 40
TOP_MARGIN = 750
LINE_HEIGHT = 16
MAX_WIDTH = 520   # safe printable width

def draw_wrapped_text(c, text, x, y, max_width=MAX_WIDTH):
    """
    Automatically wraps long text so it doesn't overflow the PDF page.
    Returns the final y-position after writing the wrapped lines.
    """
    lines = text.split("\n")

    for line in lines:
        wrapped_lines = wrap(line, width=100)  # Adjust width for wrapping
        for wrapped in wrapped_lines:
            c.drawString(x, y, wrapped)
            y -= LINE_HEIGHT

    return y


def create_pdf_report(output_path, insights_text, chart_paths):
    c = canvas.Canvas(output_path, pagesize=letter)

    # -------------------------------
    # PAGE 1 — INSIGHTS + EXEC SUMMARY
    # -------------------------------
    y = TOP_MARGIN
    c.setFont("Helvetica-Bold", 16)
    c.drawString(LEFT_MARGIN, y, "Automated Insight Report")
    y -= 30

    c.setFont("Helvetica", 12)

    # Add insights with wrapped text
    y = draw_wrapped_text(c, insights_text, LEFT_MARGIN, y)

    c.showPage()

    # -------------------------------
    # PAGE 2+ — CHARTS
    # -------------------------------
    for path in chart_paths:
        if os.path.exists(path):
            c.drawImage(path, 40, 200, width=520, height=350)
            c.showPage()

    c.save()

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from textwrap import wrap
import os

PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT = 50
RIGHT = 550
TOP = 750
LINE = 16
WRAP_WIDTH = 95  # affects wrapping quality

def draw_header(c, title):
    c.setFont("Helvetica-Bold", 20)
    c.drawString(LEFT, TOP, title)
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(LEFT, TOP - 5, RIGHT, TOP - 5)

def draw_section_title(c, title, y):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(LEFT, y, title)
    return y - 25

def draw_wrapped(c, text, y):
    c.setFont("Helvetica", 11)
    lines = text.split("\n")
    for line in lines:
        wrapped = wrap(line, WRAP_WIDTH)
        for w in wrapped:
            c.drawString(LEFT, y, w)
            y -= LINE
    return y - 10

def clean_text(text):
    replace = {
        "**": "",
        "*": "",
        "###": "",
        "#": ""
    }
    for k, v in replace.items():
        text = text.replace(k, v)
    return text.strip()

def create_pdf_report(output_path, insights_text, chart_paths):
    c = canvas.Canvas(output_path, pagesize=letter)

    # CLEAN text
    insights_text = clean_text(insights_text)

    # ---------------- PAGE 1 ------------------
    draw_header(c, "Automated Insight Report")
    y = TOP - 50

    # SECTION 1: Key Metrics + Trends + Takeaways
    y = draw_section_title(c, "Summary Insights", y)
    y = draw_wrapped(c, insights_text, y)

    c.showPage()

    # ---------------- PAGE 2+ (Charts) ------------------
    for path in chart_paths:
        if os.path.exists(path):
            c.setFont("Helvetica-Bold", 16)
            c.drawString(LEFT, TOP, "Visual Charts")
            c.drawImage(path, 50, 250, width=500, height=400)
            c.showPage()

    c.save()

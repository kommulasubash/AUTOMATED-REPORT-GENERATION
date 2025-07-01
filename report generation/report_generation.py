import pandas as pd
from fpdf import FPDF

# Load data
data = pd.read_csv("data.csv")

# Analyze data
average_score = data['Score'].mean()
top_scorer = data.loc[data['Score'].idxmax()]

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Student Score Report", ln=True, align='C')

pdf.ln(10)
pdf.set_font("Arial", '', 12)

# Add data table
pdf.cell(0, 10, "Student Scores:", ln=True)
for index, row in data.iterrows():
    pdf.cell(0, 10, f"{row['Name']}: {row['Score']}", ln=True)

pdf.ln(5)

# Add summary
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Summary:", ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(0, 10, f"Top Scorer: {top_scorer['Name']} ({top_scorer['Score']})", ln=True)

# Save PDF
pdf.output("report.pdf")

print("PDF report generated as report.pdf")

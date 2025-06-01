import csv
from fpdf import FPDF

# Function to read CSV data
def read_csv(filename):
    data = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convert Quantity and Price to int/float
            row['Quantity'] = int(row['Quantity'])
            row['Price'] = float(row['Price'])
            data.append(row)
    return data

# Function to analyze data: total quantity, total sales per product, grand total sales
def analyze_data(data):
    for item in data:
        item['Total Sales'] = item['Quantity'] * item['Price']
    grand_total = sum(item['Total Sales'] for item in data)
    total_quantity = sum(item['Quantity'] for item in data)
    return grand_total, total_quantity

# Function to generate PDF report
def generate_pdf(data, grand_total, total_quantity, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Sales Report", ln=True, align='C')
    
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Total Products Sold: {total_quantity}", ln=True)
    pdf.cell(0, 10, f"Grand Total Sales: ${grand_total:.2f}", ln=True)
    pdf.ln(10)
    
    # Table headers
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, "Product", 1)
    pdf.cell(40, 10, "Quantity", 1)
    pdf.cell(40, 10, "Price ($)", 1)
    pdf.cell(50, 10, "Total Sales ($)", 1)
    pdf.ln()
    
    # Table data
    pdf.set_font("Arial", '', 12)
    for item in data:
        pdf.cell(50, 10, item['Product'], 1)
        pdf.cell(40, 10, str(item['Quantity']), 1)
        pdf.cell(40, 10, f"{item['Price']:.2f}", 1)
        pdf.cell(50, 10, f"{item['Total Sales']:.2f}", 1)
        pdf.ln()
    
    pdf.output(output_file)
    print(f"PDF report generated successfully: {output_file}")

# Main execution
if __name__ == "__main__":
    filename = "sales_data.csv"
    output_pdf = "sales_report.pdf"
    
    data = read_csv(filename)
    grand_total, total_quantity = analyze_data(data)
    generate_pdf(data, grand_total, total_quantity, output_pdf)

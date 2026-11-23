# Customer Segmentation Using RFM Analysis
**HCL Data Analyst Project | ABES Engineering College**

This package contains the analysis performed on the uploaded UCI Online Retail workbook.

## Actual run summary
- Raw rows: 541,909
- Eligible rows after cleaning: 392,692
- Customers: 4,338
- Snapshot date: 2011-12-10
- Eligible revenue: GBP 8,887,208.89

## Project contents
- `data/processed/`: actual cleaned transaction data, customer-level RFM, segment summary, data-quality report, country revenue, top customers, audit sample and Excel results workbook.
- `python/rfm_analysis.py`: reproducible pipeline.
- `sql/`: Oracle table, view and validation scripts.
- `powerbi/`: DAX measures and dashboard instructions.
- `charts/`: actual output charts.
- `docs/Actual_Findings.md`: findings from this run.

## Reproduce
Install dependencies:
```bash
pip install pandas numpy openpyxl matplotlib
```
Run:
```bash
python python/rfm_analysis.py --input "Online Retail.xlsx" --output "data/processed/reproduced"
```

## Oracle note
Oracle SQL Developer is a client, not the database itself. You need access to an Oracle database (for example an institutional Oracle instance or an eligible Oracle Cloud service) to execute the SQL scripts. If you do not have that access, use the supplied Python customer-level CSV in Power BI and label Oracle execution as pending rather than claiming it ran.

## Power BI
Import `data/processed/customer_rfm.csv`, create the measures in `powerbi/DAX_Measures.txt`, and follow `powerbi/Dashboard_Guide.md`. Save the resulting report as `Customer_RFM_Analysis.pbix`.

## Dataset attribution
Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33. Dataset period: 01-Dec-2010 to 09-Dec-2011.

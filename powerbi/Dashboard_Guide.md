# Power BI Dashboard — 3 pages

## Data source
For the fastest build, import `data/processed/customer_rfm.csv` (or connect to Oracle view `VW_CUSTOMER_RFM_SEGMENTS` after Oracle setup). Use GBP as the currency label. The source period is historical (2010–2011).

## Page 1: Executive Overview
- KPI cards: Total Customers, Total Revenue, Average Customer Value, Average Recency Days
- Donut chart: Legend=SEGMENT, Values=CustomerID (Distinct count)
- Bar chart: Axis=SEGMENT, Values=MONETARY (Sum)
- Bar chart: Axis=COUNTRY, Values=MONETARY (Sum), Top N=10
- Slicers: COUNTRY and SEGMENT

## Page 2: Segment Analysis
- Matrix: SEGMENT, customer count, revenue, customer share, revenue share, average recency
- Scatter chart: X=RECENCY, Y=MONETARY, Size=FREQUENCY, Legend=SEGMENT
- Slicers: COUNTRY, SEGMENT

## Page 3: Customer Explorer
- Table: CUSTOMER_ID, COUNTRY, LAST_PURCHASE, RECENCY, FREQUENCY, MONETARY, RFM_SCORE, SEGMENT
- Drill-through by CUSTOMER_ID
- Add a back button

## Formatting
Use a clean light background, consistent segment colors, GBP formatting, clear titles, and footer:
"Source: UCI Online Retail dataset (01-Dec-2010 to 09-Dec-2011)."
Save as `Customer_RFM_Analysis.pbix`.

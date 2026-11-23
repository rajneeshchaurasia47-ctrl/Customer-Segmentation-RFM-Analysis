# Actual Findings — Run on Uploaded Online Retail.xlsx

## Data profile
- Raw transaction rows: 541,909
- Exact duplicate rows removed: 5,268
- Rows with missing CustomerID: 135,080
- Cancellation invoice rows: 9,288
- Rows with quantity <= 0: 10,624
- Rows with unit price <= 0: 2,517
- Eligible transaction rows after cleaning: 392,692
- Identified customers: 4,338
- Snapshot date: 10 Dec 2011
- Eligible revenue: GBP 8,887,208.89

## Segment results
            SEGMENT  CUSTOMERS     REVENUE  AVG_CUSTOMER_VALUE  AVG_RECENCY_DAYS  CUSTOMER_SHARE_PCT  REVENUE_SHARE_PCT
          Champions        942 5743329.230         6096.952473         13.003185           21.715076          64.624668
    Loyal Customers        504  916856.701         1819.160121         37.442460           11.618257          10.316588
            At Risk        662  827189.821         1249.531452        151.063444           15.260489           9.307645
        Hibernating       1072  523208.532          488.067660        217.469216           24.711849           5.887209
Potential Loyalists        481  500152.230         1039.817526         17.301455           11.088059           5.627776
    Needs Attention        541  332848.720          615.247172         52.859519           12.471185           3.745256
      New Customers        136   43623.660          320.762206         18.544118            3.135085           0.490859

## Interpretation
Champions represent 21.72% of identified customers and contribute 64.62% of eligible revenue. This indicates that revenue is concentrated among a relatively small high-value group in this historical dataset.

At Risk customers: 662; Hibernating customers: 1072. These groups are candidates for carefully tested win-back and reactivation campaigns.

## Important limitations
- This is historical data from 2010–2011; do not describe it as current market behaviour.
- Customers with missing CustomerID cannot be included in customer-level RFM.
- RFM is descriptive rule-based segmentation, not a churn prediction model.
- Segment definitions and quintile cut-offs are project rules.
- Currency is treated as GBP based on the dataset's UK retailer context; verify currency convention in the dataset citation/metadata before final presentation.

"""Reproducible RFM analysis pipeline for the UCI Online Retail dataset."""
from pathlib import Path
import argparse
import pandas as pd
import numpy as np

def ntile_ascending(frame, metric):
    ordered = frame[["CustomerID", metric]].sort_values([metric, "CustomerID"], kind="mergesort")
    n = len(ordered); q, rem = divmod(n, 5); scores = []
    for pos in range(n):
        bucket = pos // (q + 1) + 1 if pos < (q + 1) * rem else rem + (pos - (q + 1) * rem) // q + 1
        scores.append(bucket)
    return pd.Series(scores, index=ordered.index).reindex(frame.index).astype(int)

def segment(row):
    r, f, m = int(row.R_SCORE), int(row.F_SCORE), int(row.M_SCORE)
    if r >= 4 and f >= 4 and m >= 4: return "Champions"
    if r >= 3 and f >= 4: return "Loyal Customers"
    if r >= 4 and f >= 2: return "Potential Loyalists"
    if r >= 4 and f == 1: return "New Customers"
    if r <= 2 and f >= 3: return "At Risk"
    if r <= 2 and f <= 2: return "Hibernating"
    return "Needs Attention"

def run(input_file, output_dir):
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    raw = pd.read_excel(input_file, engine="openpyxl")
    raw.columns = [str(c).strip() for c in raw.columns]
    required = {"InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"}
    if required - set(raw.columns): raise ValueError(f"Missing columns: {sorted(required-set(raw.columns))}")
    df = raw.drop_duplicates().copy()
    df["InvoiceNo"] = df.InvoiceNo.astype(str).str.strip()
    df["InvoiceDate"] = pd.to_datetime(df.InvoiceDate, errors="coerce")
    for c in ["Quantity","UnitPrice","CustomerID"]: df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["InvoiceNo","InvoiceDate","Quantity","UnitPrice","CustomerID"])
    df = df[~df.InvoiceNo.str.upper().str.startswith("C")]
    df = df[(df.Quantity > 0) & (df.UnitPrice > 0)].copy()
    df["CustomerID"] = df.CustomerID.astype("int64")
    df["Revenue"] = df.Quantity * df.UnitPrice
    df["Country"] = df.Country.fillna("Unknown").astype(str).str.strip()
    snapshot = df.InvoiceDate.max().normalize() + pd.Timedelta(days=1)
    rfm = df.groupby("CustomerID", as_index=False).agg(
        LAST_PURCHASE=("InvoiceDate","max"), FREQUENCY=("InvoiceNo","nunique"),
        MONETARY=("Revenue","sum"),
        COUNTRY=("Country",lambda s:s.mode().iloc[0] if not s.mode().empty else "Unknown"))
    rfm["RECENCY"] = (snapshot-rfm.LAST_PURCHASE.dt.normalize()).dt.days
    rfm["R_SCORE"] = 6-ntile_ascending(rfm,"RECENCY")
    rfm["F_SCORE"] = ntile_ascending(rfm,"FREQUENCY")
    rfm["M_SCORE"] = ntile_ascending(rfm,"MONETARY")
    rfm["RFM_SCORE"] = rfm.R_SCORE.astype(str)+rfm.F_SCORE.astype(str)+rfm.M_SCORE.astype(str)
    rfm["SEGMENT"] = rfm.apply(segment,axis=1)
    rfm["SNAPSHOT_DATE"] = snapshot.strftime("%Y-%m-%d")
    rfm["LAST_PURCHASE"] = rfm.LAST_PURCHASE.dt.strftime("%Y-%m-%d %H:%M:%S")
    rfm.to_csv(out/"customer_rfm.csv",index=False)
    summary = rfm.groupby("SEGMENT",as_index=False).agg(
        CUSTOMERS=("CustomerID","nunique"),REVENUE=("MONETARY","sum"),
        AVG_CUSTOMER_VALUE=("MONETARY","mean"),AVG_RECENCY_DAYS=("RECENCY","mean"))
    summary["CUSTOMER_SHARE_PCT"] = summary.CUSTOMERS/rfm.CustomerID.nunique()*100
    summary["REVENUE_SHARE_PCT"] = summary.REVENUE/rfm.MONETARY.sum()*100
    summary.to_csv(out/"segment_summary.csv",index=False)
    print(f"Customers={rfm.CustomerID.nunique():,}; Revenue=GBP {rfm.MONETARY.sum():,.2f}; Snapshot={snapshot.date()}")
if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True); ap.add_argument("--output",default="data/processed")
    a=ap.parse_args(); run(a.input,a.output)

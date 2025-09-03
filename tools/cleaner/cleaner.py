import sys
import pandas as pd 
import re
df = pd.read_csv("./sample_data/testdata.csv")

def parse_date(x):
    return pd.to_datetime(x, errors="coerce").date()

def to_cents(x):
    s = str(x).replace("$","").replace(",","").strip()
    try:
        return int(round(float(s) * 100))
    except:
        return None

def clean_desc(s):
    s = "" if pd.isna(s) else str(s)
    return re.sub(r"\s+", " ", s).strip()

def normalize_merchant(s: str) -> str:
    """
    Normalize merchant names for grouping.
    Examples:
      "LOWES #01538*" → "lowes"
      "365 MARKET L 888 432-3299" → "market l"
      "SQ *BUN'D UP MARYLAND" → "bun'd up maryland"
    """
    if not isinstance(s, str):
        return ""

    s = s.lower()                       # lowercase
    s = re.sub(r"\d+", "", s)           # remove digits
    s = re.sub(r"[^a-z\s&'\-]", " ", s) # keep letters, space, &, ', -
    s = re.sub(r"\s+", " ", s)          # collapse spaces
    return s.strip()

# 1) get CSV path from command-line
if len(sys.argv) < 2:
    print("Usage: python cleaner.py <csv_file>")
    sys.exit(1)


csv_path = sys.argv[1]

# 2) read CSV
df = pd.read_csv(csv_path)

date_col = "Post Date"          # canonical date
txn_date_col = "Transaction Date"  # optional keep
desc_col = "Description"
amt_col  = "Amount"
category_provided = "Category"

out = pd.DataFrame({
    "posted_at": df[date_col].apply(parse_date),
    "description_raw": df[desc_col].apply(normalize_merchant),
    "amount_cents": df[amt_col].apply(to_cents),
    # optional: keep original transaction date too
    "txn_date": df[txn_date_col].apply(parse_date),
    "category" : df[category_provided],
})

out["account_name"] = "Chase_7046"
out["currency"] = "USD"


print(out.dtypes)
print(out.head(5))
print("nulls:\n", out.isna().sum())
print("amount range (cents):", out["amount_cents"].min(), out["amount_cents"].max())


from pathlib import Path

# make sure output folder exists
out_dir = Path("cleaned_data")
out_dir.mkdir(exist_ok=True)

# save the normalized dataset
out_file = out_dir / "normalized_transactions.csv"
out.to_csv(out_file, index=False)

print(f"✅ Saved normalized CSV to {out_file}")

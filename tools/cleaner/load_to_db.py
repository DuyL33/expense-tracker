# import standard stuff
import pandas as pd
from pathlib import Path
from db_utils import get_connection, insert_transaction

# path to the cleaned CSV
cleaned_csv = Path(r"C:\Users\Duy\Desktop\expense-tracker\tools\cleaner\cleaned_data\normalized_transactions.csv")

# read cleaned CSV
df = pd.read_csv(cleaned_csv)

# connect to database
conn = get_connection()
cur = conn.cursor()

# iterate and insert
for _, row in df.iterrows():
    t = {
        "Transaction Date": row["txn_date"],
        "Post Date": row["posted_at"],
        "Description": row["description_raw"],
        "Category": row["category"],
        "Type": "debit" if row["amount_cents"] < 0 else "credit",  # example
        "Amount_cents": int(row["amount_cents"]) if pd.notna(row["amount_cents"]) else 0,
        "Memo": None,
    }
    insert_transaction(cur, t)

# commit & close
conn.commit()
cur.close()
conn.close()

print("✅ All cleaned transactions inserted into the database!")

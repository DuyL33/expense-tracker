import sys
import pandas as pd 

df = pd.read_csv("./sample_data/testdata.csv")

# 1) get CSV path from command-line
if len(sys.argv) < 2:
    print("Usage: python cleaner.py <csv_file>")
    sys.exit(1)


csv_path = sys.argv[1]

# 2) read CSV
df = pd.read_csv(csv_path)

# 3) show first 5 rows
print(df.head())
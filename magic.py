# Calculate the average of results
import sys
import pandas as pd

csvs = sys.argv[1:]
magics = [pd.read_csv(c) for c in csvs]
magics[0]['item_cnt_month'] = sum(list(m['item_cnt_month'] for m in magics)) / len(csvs)
magics[0].to_csv('output.csv', index=False)

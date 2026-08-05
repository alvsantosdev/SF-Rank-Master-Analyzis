import pandas as pd
import sqlite3

df_matches = pd.read_csv('../data/raw/sf6_matches_04_27.csv', low_memory=False)

df_matches.drop_duplicates(inplace=True)

conn = sqlite3.connect('../data/Processed/sf.db')

df_matches.to_sql('matches', conn, if_exists="replace", index=False)





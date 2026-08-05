import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../data/Processed/sf.db')

with open('../sql/mr_wr.sql') as f:
    query = f.read()

df = pd.read_sql(query, conn)

picks_char = (df['p1_char'].value_counts( )).add(df['p2_char'].value_counts( ), fill_value=0)

rate = { }

for character in picks_char.index:

    char = df[(df['p1_char'] == character) & (df['p1_result'] == 'True')]

    wins = char['p1_char'].value_counts()


    char = df[(df['p2_char'] == character) & (df['p2_result'] == 'True')]

    wins += char['p2_char'].value_counts()

    win_rate = ((wins / picks_char[character]) * 100).round(2)

    rate[character] = win_rate[character]


rate_order =  dict(sorted(rate.items(), key=lambda item: item[1], reverse=False))

fig, ax = plt.subplots(figsize=(10 , 6))

bars = ax.barh(
    rate_order.keys(),
    rate_order.values()

)
ax.bar_label(
        bars,
        padding=5
)
ax.set_title('winrate_character_UMaster')
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Char')
ax.grid(axis="x", alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.savefig('../reports/figure/winrate_fig/winrateUMaster.png')




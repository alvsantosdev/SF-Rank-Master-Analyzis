import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('../data/Processed/sf.db')

with open('../sql/character.sql') as f:
    query = f.read()

df_char = pd.read_sql(query, conn)

chars = pd.concat([df_char['p1_char'], df_char['p2_char']])

df_result = (
    chars.value_counts()
         .reset_index()
)

df_result.columns = ['character', 'count']

fig, ax = plt.subplots(figsize=(10, 8))

bars = ax.barh(
    df_result["character"],
    df_result["count"]
)


ax.invert_yaxis()


ax.set_title(
    "Character Popularity in Street Fighter 6",
    fontsize=18,
    weight="bold",
    pad=15
)


ax.text(
    0,
    1.02,
    "Total picks considering both Player 1 and Player 2",
    transform=ax.transAxes,
    fontsize=11,
    color="gray"
)


ax.set_xlabel("Number of Picks")
ax.set_ylabel("")


ax.grid(axis="x", alpha=0.3)


ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


ax.bar_label(
    bars,
    padding=4,
    fontsize=9
)

plt.tight_layout()

plt.savefig(
    "../reports/figure/popularityChar.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()






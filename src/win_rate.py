import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../data/Processed/sf.db')

with open('../sql/win_rate.sql') as f:
    query = f.read()

df = pd.read_sql(query, conn)

picks_char = (
    df['p1_char'].value_counts()
    .add(df['p2_char'].value_counts(), fill_value=0)
)

rate = {}

for character in picks_char.index:

    wins_p1 = df[
        (df['p1_char'] == character) &
        (df['p1_result'] == 'True')
    ]['p1_char'].count()

    wins_p2 = df[
        (df['p2_char'] == character) &
        (df['p2_result'] == 'True')
    ]['p2_char'].count()

    wins = wins_p1 + wins_p2

    rate[character] = round((wins / picks_char[character]) * 100, 2)

rate = (
    pd.Series(rate)
      .sort_values(ascending=True)
)

fig, ax = plt.subplots(figsize=(10, 8))

bars = ax.barh(
    rate.index,
    rate.values,
    color="#3B82F6"
)


labels = [f"{x:.2f}%" for x in rate.values]

ax.bar_label(
    bars,
    labels=labels,
    padding=4,
    fontsize=9
)

ax.axvline(
    x=50,
    color="red",
    linestyle="--",
    linewidth=1.5,
    label="50%"
)

ax.legend()

ax.set_title(
    "Character Win Rate",
    fontsize=18,
    weight="bold",
    pad=15
)

ax.set_xlabel("Win Rate (%)")
ax.set_ylabel("")

ax.grid(axis="x", alpha=0.3)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


ax.set_xlim(rate.min() - 0.5, rate.max() + 0.6)

plt.tight_layout()

plt.savefig(
    "../reports/figure/winrate_fig/winrate.png",
    dpi=300,
    bbox_inches="tight"
)

























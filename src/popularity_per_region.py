
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('../data/Processed/sf.db')

with open('../sql/character_popularity_per_country.sql') as f:
    query = f.read()

df = pd.read_sql(query, conn)

df.rename(columns={'p1_home':'Country', 'p1_char':'Character'}, inplace=True)

df['percentage_picks'] = (df['picks'] / df.groupby('Country')['picks'].transform('sum') * 100).round(2)

for character in df['Character'].unique():

    char = df.loc[df['Character'] == character ]

    char['total_picks_per_country'] = df.groupby('Country')['picks'].transform('sum')

    median = char['total_picks_per_country'].median()

    char = char[char['total_picks_per_country']>= median]

    char = char.sort_values(by = 'percentage_picks', ascending=False)

    df_final = char.head(10)

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(
        df_final['Country'],
        df_final['percentage_picks'],
        color="#3B82F6"
    )

    labels = [
        f"{perc:.2f}% (N={total:,})"
        for perc, total in zip(
            df_final['percentage_picks'],
            df_final['total_picks_per_country']
        )
    ]

    ax.bar_label(
        bars,
        labels=labels,
        padding=4,
        fontsize=9
    )

    ax.set_title(
        f"Top 10 Countries by {character} Pick Rate",
        fontsize=16,
        fontweight="bold",
        pad=12
    )

    ax.set_xlabel("Pick Rate (%)", fontsize=11)
    ax.set_ylabel("")

    ax.invert_yaxis()

    ax.grid(axis="x", linestyle="--", alpha=0.3)


    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)


    ax.set_xlim(
        0,
        df_final['percentage_picks'].max() * 1.20
    )

    plt.tight_layout()

    plt.savefig(
        f'../reports/figure/{character}.png',
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)
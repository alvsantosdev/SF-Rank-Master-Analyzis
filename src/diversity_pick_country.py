import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../data/Processed/sf.db')

with open('../sql/diversity_country.sql') as f:
    query = f.read()

df = pd.read_sql(query, conn)

df.rename(columns={'p1_home':'Country', 'p1_char':'Character'}, inplace=True)

df['percentage_picks'] = (df['picks'] / df.groupby('Country')['picks'].transform('sum') * 100).round(2)

df['total_picks'] = df.groupby('Country')['picks'].transform('sum')

median = df.groupby('Country')['picks'].sum().median()

df_filter= df[df['total_picks'] >= median].copy()

vari = df_filter.groupby('Country')['percentage_picks'].var().reset_index(name = 'variance')

vari['variance'] = vari['variance'].round(2)

vari = vari.sort_values('variance')

fig, ax =  plt.subplots(figsize = (10, 8))

bars = ax.barh(
    vari['Country'].head(10),
    vari['variance'].head(10)
)

ax.bar_label(
bars,
padding = 5
)

ax.set_title('Country Variance Picks')
ax.set_xlabel('Variance (%)')
ax.set_ylabel('Country')
ax.grid(axis="x", alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xlim(0, max(vari['variance'].head(10)) * 1.1)

plt.savefig('../reports/figure/Country_Variance')












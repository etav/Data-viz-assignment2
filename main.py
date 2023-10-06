import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# vizspiratrion: https://www.fs.usda.gov/ccrc/education/climate-primer/current-climate-change

df = pd.read_csv('/Users/ernest/PycharmProjects/Data_Viz/Data-viz-assignment2/ExcelFormattedGISTEMPData2CSV.csv')
df['Variance'] = df['Glob']

# inspect dtypes
df.dtypes

# create rolling mean
df['rolling_mean'] = df['Glob'].rolling(window=5).mean()

# create plot
sns.lineplot(x='Year', y='Variance', data=df, label='Global Temperature Variance', color='#4D7C86',
             linewidth=1).set_title('Global Average Temperature Variation (1880-2020)')

fig = sns.lineplot(x='Year', y='rolling_mean', data=df,
                   label='5 Year Rolling Mean',
                   color='#4D7C86',
                   linewidth=3)
# plotting settings
plt.legend(loc='upper left', frameon=False)


# add horizontal line to scatterplot
plt.axhline(y=0, color='black',  linewidth=.5)

# save figure

plt.savefig('global temperature variance.png')

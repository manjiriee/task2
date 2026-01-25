import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv('Unemployment in India.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Extract Year and Month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Create Covid flag
df['Covid_Period'] = df['Date'].apply(
    lambda x: 'Pre-Covid' if x < pd.to_datetime('2020-03-01') else 'During/Post-Covid'
)

# Line Plot
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate Over Time')
plt.savefig("line_plot.png")
plt.show()

# Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(x='Covid_Period', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Impact of Covid-19 on Unemployment Rate')
plt.savefig("box_plot_covid.png")
plt.show()

# Bar Plot
monthly_trend = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
plt.figure(figsize=(10,5))
sns.barplot(x=monthly_trend.index, y=monthly_trend.values)
plt.title('Average Unemployment Rate by Month')
plt.savefig("bar_plot_month.png")
plt.show()

# Heatmap
if 'Region' in df.columns:
    heatmap_data = df.pivot_table(
        index='Region',
        columns='Month',
        values='Estimated Unemployment Rate (%)'
    )
    plt.figure(figsize=(12,6))
    sns.heatmap(heatmap_data, cmap='coolwarm')
    plt.title('Unemployment Rate Heatmap by Region and Month')
    plt.savefig("heatmap_region.png")
    plt.show()

# Histogram
plt.figure(figsize=(8,5))
sns.histplot(df['Estimated Unemployment Rate (%)'], bins=20, kde=True)
plt.title('Distribution of Unemployment Rates')
plt.savefig("histogram_distribution.png")
plt.show()
import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns

print("Generating EDA Charts in the background...")

try:
    df = pd.read_csv("credit_data.csv")
except FileNotFoundError:
    print("Error: credit_data.csv not found. Run main.py first!")
    exit()

plt.figure(figsize=(10, 6))
sns.histplot(df['credit_amount'], kde=True, color='blue')
plt.title('Distribution of Credit Amount')
plt.savefig('section3_histogram.png')
print("✅ Saved: section3_histogram.png")

plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('section4_heatmap.png')
print("✅ Saved: section4_heatmap.png")

print("All charts generated successfully! Check your folder sidebar.")
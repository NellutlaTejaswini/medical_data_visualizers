import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
# Replace 'your_dataset.csv' with the actual filename or path to your dataset
df = pd.read_csv('your_dataset.csv')

# Filter data based on conditions
filtered_df = df[
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] > df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] > df['weight'].quantile(0.975))
]

# Create a correlation matrix
correlation_matrix = filtered_df.corr()

# Plot the correlation matrix using seaborn's heatmap
mask = correlation_matrix < 1.0  # Mask the upper triangle to remove self-correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', mask=mask)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

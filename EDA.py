import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

print("Dataset Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# 🔹 1. Basic Statistics
print("\nSummary Statistics:")
print(df.describe())

# 🔹 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 🔹 3. Word Count Analysis (for text column)
df['word_count'] = df.iloc[:, 0].apply(lambda x: len(str(x).split()))

print("\nWord Count Added:")
print(df.head())

# 🔹 4. Plot Word Count Distribution
plt.figure()
plt.hist(df['word_count'], bins=20)
plt.title("Word Count Distribution")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.show()

# 🔹 5. Most Frequent Words
from collections import Counter

all_words = " ".join(df.iloc[:, 0]).split()
word_freq = Counter(all_words)

# Get top 10 words
common_words = word_freq.most_common(10)

words = [w[0] for w in common_words]
counts = [w[1] for w in common_words]

# 🔹 6. Bar Chart for Top Words
plt.figure()
plt.bar(words, counts)
plt.title("Top 10 Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
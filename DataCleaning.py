import pandas as pd
import re

# Load dataset (change file name)
df = pd.read_csv("your_dataset.csv")

print("Original Data:")
print(df.head())
print("\nMissing Values:\n", df.isnull().sum())

# 🔹 1. Remove duplicates
df.drop_duplicates(inplace=True)

# 🔹 2. Handle missing values
df.fillna("Unknown", inplace=True)

# 🔹 3. Select text columns only
text_columns = df.select_dtypes(include=['object']).columns

# 🔹 4. Clean text columns
for col in text_columns:
    df[col] = df[col].str.lower()  # lowercase
    df[col] = df[col].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', str(x)))  # remove special chars
    df[col] = df[col].apply(lambda x: re.sub(r'\s+', ' ', x).strip())  # remove extra spaces

# 🔹 5. Remove stopwords
stopwords = ["the", "is", "in", "and", "to", "of", "for", "on", "with"]

for col in text_columns:
    df[col] = df[col].apply(
        lambda x: " ".join([word for word in x.split() if word not in stopwords])
    )

print("\nCleaned Data:")
print(df.head())

# Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)

print("✅ Data cleaning completed successfully!")
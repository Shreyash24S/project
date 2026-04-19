import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset (replace with your CSV)
data = {
    "Review": [
        "food is very good and tasty",
        "delivery is slow and bad",
        "excellent service and good quality",
        "very bad experience",
        "fast delivery and good packaging",
        "food quality is poor"
    ]
}

df = pd.DataFrame(data)

# 🔹 Step 1: Create sentiment labels
# 1 = Positive, 0 = Negative
df["Sentiment"] = df["Review"].apply(
    lambda x: 1 if "good" in x or "excellent" in x else 0
)

print("Dataset:")
print(df)

# 🔹 Step 2: Convert text to numerical form
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Review"])

y = df["Sentiment"]

# 🔹 Step 3: Train model
model = MultinomialNB()
model.fit(X, y)

# 🔹 Step 4: Predict sentiment of new reviews
new_reviews = [
    "delivery was bad",
    "food is excellent and tasty"
]

new_X = vectorizer.transform(new_reviews)
predictions = model.predict(new_X)

# 🔹 Step 5: Analyze results
for review, pred in zip(new_reviews, predictions):
    if pred == 1:
        print(review, "→ Positive")
    else:
        print(review, "→ Negative")

# 🔹 Step 6: Product Improvement Insights
positive = df[df["Sentiment"] == 1]
negative = df[df["Sentiment"] == 0]

print("\nPositive Feedback:")
print(positive["Review"])

print("\nNegative Feedback:")
print(negative["Review"])
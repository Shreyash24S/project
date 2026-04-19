import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Assume first column contains text
X = df.iloc[:, 0]

# Dummy labels (for practical purpose)
# 1 = Positive, 0 = Negative
y = [1 if "good" in str(text) else 0 for text in X]

# 🔹 Convert text to numerical form
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 🔹 Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# 🔹 Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# 🔹 Predict
y_pred = model.predict(X_test)

# 🔹 Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# 🔹 Test with new data
sample = ["this product is very good"]
sample_vec = vectorizer.transform(sample)

prediction = model.predict(sample_vec)

if prediction[0] == 1:
    print("Positive Sentiment")
else:
    print("Negative Sentiment") 
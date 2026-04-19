import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Create sample dataset (you can replace with your own CSV)
data = {
    "Likes": [10, 50, 30, 200, 150, 80, 300, 20],
    "Shares": [2, 10, 5, 40, 30, 15, 60, 3],
    "Comments": [1, 5, 3, 20, 15, 8, 25, 2]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 🔹 Feature selection (structure-based metrics)
X = df[["Likes", "Shares", "Comments"]]

# 🔹 Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔹 Apply K-Means clustering
kmeans = KMeans(n_clusters=2, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nClustered Data:")
print(df)

# 🔹 Interpret clusters
print("\nCluster 0 → Low Engagement")
print("Cluster 1 → High Engagement")
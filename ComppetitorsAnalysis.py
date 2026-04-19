import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace with your CSV)
data = {
    "Brand": ["Zomato", "Swiggy", "Zomato", "Swiggy", "Zomato", "Swiggy"],
    "Likes": [100, 150, 120, 130, 140, 160],
    "Shares": [20, 25, 22, 28, 24, 30],
    "Comments": [10, 15, 12, 18, 14, 20]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 🔹 Group by brand
grouped = df.groupby("Brand").mean()

print("\nAverage Engagement:")
print(grouped)

# 🔹 Plot comparison (Likes)
plt.figure()
grouped["Likes"].plot(kind="bar")
plt.title("Average Likes Comparison")
plt.ylabel("Likes")
plt.show()

# 🔹 Plot comparison (Shares)
plt.figure()
grouped["Shares"].plot(kind="bar")
plt.title("Average Shares Comparison")
plt.ylabel("Shares")
plt.show()

# 🔹 Plot comparison (Comments)
plt.figure()
grouped["Comments"].plot(kind="bar")
plt.title("Average Comments Comparison")
plt.ylabel("Comments")
plt.show()
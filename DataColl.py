import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Reddit URL to scrape
url = "https://old.reddit.com/r/technology/"

# Strong headers (important for Reddit)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Send request
response = requests.get(url, headers=headers, verify=False)

# Check response
print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Extract post titles and links
posts = []
for post in soup.select("a.title"):
    posts.append({
        "Post Title": post.get_text(),
        "Post Link": "https://reddit.com" + post.get("href", "")
    })

# Create DataFrame
df = pd.DataFrame(posts)

# Display results
print(df.head())

# Save to CSV
df.to_csv("reddit_data.csv", index=False)

print("✅ Data scraped successfully!")

# import requests
# import pandas as pd
# import time
# import warnings
# warnings.filterwarnings("ignore")

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
# }

# def scrape_reddit(url, pages=3):
   
#     url = url.strip("/")
#     url = url.replace("old.reddit.com", "www.reddit.com")
#     if not url.startswith("http"):
#         url = "https://www.reddit.com/r/" + url
#     json_url = url + ".json?limit=25"

#     posts = []
#     after  = None  # pagination token

#     for page in range(pages):
#         page_url = json_url + (f"&after={after}" if after else "")
#         print(f"Scraping page {page + 1} → {page_url}")

#         response = requests.get(page_url, headers=HEADERS, verify=False)

#         if response.status_code != 200:
#             print(f" Error: Status {response.status_code}")
#             break

#         data = response.json()

#         children = data["data"]["children"]
#         if not children:
#             print("No more posts found.")
#             break

#         for child in children:
#             p = child["data"]
#             posts.append({
#                 "title"       : p.get("title",       "N/A"),
#                 "score"       : p.get("score",        "N/A"),
#                 "upvote_ratio": p.get("upvote_ratio", "N/A"),
#                 "num_comments": p.get("num_comments", "N/A"),
#                 "author"      : p.get("author",       "N/A"),
#                 "subreddit"   : p.get("subreddit",    "N/A"),
#                 "url"         : p.get("url",          "N/A"),
#                 "posted_at"   : pd.to_datetime(p.get("created_utc"), unit="s"),
#                 "post_link"   : "https://reddit.com" + p.get("permalink", ""),
#                 "flair"       : p.get("link_flair_text", "N/A"),
#                 "is_video"    : p.get("is_video",     False),
#             })

#         # Pagination
#         after = data["data"].get("after")
#         if not after:
#             print("No more pages.")
#             break

#         time.sleep(1)

#     return posts



# url = "https://www.reddit.com/r/technology/"

# data = scrape_reddit(url, pages=3)

# if data:
#     df = pd.DataFrame(data)
#     print("\nSample Data:")
#     print(df[["title", "score", "num_comments", "author"]].head(10))
#     df.to_csv("reddit_output.csv", index=False)
#     print(f"\n Done! {len(df)} posts saved to reddit_output.csv")
# else:
#     print("No data scraped.")
import requests
from datetime import datetime
import os
import json
import time

#Fetching top stories ID's

id_url="https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}
try:
  response=requests.get(id_url,headers=headers)
  print("HTTP Status Code:", response.status_code)
  if(response.status_code==200):
    id_data=response.json()
  else:
    print("Failed to get datat from api(id)")
except Exception as e:
  print(f"Exception occured as {e}")

#define cateogories

categories = {
      "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
      "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
      "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
      "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
      "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

#function to categorize

def categorize_story(title):
    title = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return None

category_counts={
    "technology":0,
    "worldnews":0,
    "sports":0,
    "science":0,
    "entertainment":0
} 


stories=[]

for id in id_data:
    
    story_url=f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    try:
      response=requests.get(story_url,headers=headers)
      story_data=response.json()
      if story_data and "title" in story_data:
        print(story_data["title"])
        stories.append(story_data)
 
    except Exception as e:
      print(f"Exception occured as {e}")



all_stories=[]
for story in stories[:500]:
  title=story.get("title")
  category=categorize_story(title)
  if category and category_counts[category]<25:
    story={
        "post_id":story.get("id"),
        "title":story.get("title"),
        "category":category,
        "score":story.get("score"),
        "num_comments":story.get("descendants"),
        "author":story.get("by"),
        "collected_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    }
    all_stories.append(story)
    category_counts[category]+=1
    if category_counts[category] == 25:
                print(f"{category} category completed. Waiting 2 seconds...")
                time.sleep(2)


if not os.path.exists("data"):
         os.makedirs("data")
date_str=datetime.now().strftime("%Y%m%d")
filename=f"data/trends_{date_str}.json"
with open(filename,"w") as file:
  json.dump(all_stories,file,indent=4)

print(f"Total stories collected: {len(all_stories)}")
print(f"Data saved to {filename}")
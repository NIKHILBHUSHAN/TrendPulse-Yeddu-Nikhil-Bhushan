import matplotlib.pyplot as plt
import pandas as pd
import os

df=pd.read_csv("data/trends_analysed_260414.csv")

if not os.path.exists("output"):
    os.makedirs("output")
sorted=df.sort_values("score",ascending=False).head(10)
sorted["title"] = sorted["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

#horizontalbar garaph

plt.barh(sorted["title"],sorted["score"])
plt.xlabel("score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score ")
plt.savefig("output/chart1_top_stories.png")
plt.show()

category=df["category"].value_counts().to_dict()
colors={
    "technology":"red",
    "worldnews":"blue",
    "sports":"orange",
    "science":"green",
    "entertainment":"skublue"

}

#bargraph

plt.bar(category.keys(),category.values(),color=["red","green","blue","orange","green","skyblue"])
plt.xlabel("Categroies")
plt.ylabel("No of stories")
plt.title("Stories per Category")
plt.savefig("output/chart2_categories.png")
plt.show()

#scatter plot

popular=df[df["is_popular"]==True]
notpopualr=df[df["is_popular"]==False]

plt.scatter(popular["score"],popular["num_comments"],color="red",marker="o",label="popular")
plt.scatter(notpopualr["score"],notpopualr["num_comments"],color="green",marker="x",label="not popular")

plt.title("Score vs Comments")
plt.xlabel("score")
plt.ylabel("comments")
plt.legend()
plt.savefig("output/chart3_scatter.png")
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))


sorted_df = df.sort_values("score", ascending=False).head(10).copy()

sorted_df["title"] = sorted_df["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

axes[0].barh(sorted["title"], sorted["score"])
axes[0].set_title("Top 10 Stories")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")


category_counts = df["category"].value_counts()

colors = ["red", "blue", "orange", "green", "skyblue"]

axes[1].bar(category_counts.index, category_counts.values, color=colors)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

axes[2].scatter(popular["score"], popular["num_comments"], color="red", label="Popular")
axes[2].scatter(notpopualr["score"], notpopualr["num_comments"], color="green", label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()

plt.tight_layout()
plt.savefig("output/dashboard.png")
plt.show()
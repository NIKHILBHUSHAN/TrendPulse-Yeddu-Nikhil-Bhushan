import pandas as pd
import numpy as np
from datetime import datetime

#load dataset
df=pd.read_csv("data/trends_260414.csv")
print(df.head())

print("shape fo dataframe  :",df.shape)
print("avergae scores acorss all stories:",df["score"].mean())
print("avergae comments acorss all stories:",df["num_comments"].mean())

#numpy analysis
print("Numpy Analysis")
score=df["score"]
mean=np.mean(score)
median=np.median(score)
standard_deviation=np.std(score)
highest_score=np.max(score)
lowest_score=np.min(score)

'''category_count=df["category"].value_counts()
print(category_count.idxmax())'''
category_count=df["category"].value_counts().to_dict()
category_values=np.array(list(category_count.values()))
max_index=np.argmax(category_values)
keys=list(category_count.keys())

x=df.sort_values("num_comments",ascending=False)



print("Mean score:",mean)
print("Meadian score:",median)
print("Standard devaition:",standard_deviation)
print("Max score:",highest_score)
print("Min score:",lowest_score)
print(f"Most stories in:{keys[max_index]}({np.max(category_values)}stories)")
print(f"Most commented story: {x.iloc[0,1]} - {x.iloc[0,4]} comments")

#add new columns

df["enagagement"]=df["num_comments"]/(df["score"]+1)
df["is_popular"]=df["score"]>mean

#save analyzed data to a new .csv file

date_str=datetime.now().strftime("%y%m%d")
filename=f"data/trends_analysed_{date_str}.csv"
df.to_csv(filename,index=False)
print(f"saved to {filename}")


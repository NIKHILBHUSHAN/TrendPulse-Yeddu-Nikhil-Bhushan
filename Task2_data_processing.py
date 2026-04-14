import pandas as pd
from datetime import datetime

#loads json 
df=pd.read_json("data/trends_20260414.json")

#count no of rows
print("No of rows loaded from data/trends_20260414.json:",len(df))

# remove any rows with the same post_id
remove_duplicates=df.drop_duplicates("post_id")
print("After rremoving duplicates:",len(remove_duplicates))

# drop rows where post_id, title, or score is missing
remove_missing_values=remove_duplicates.dropna(subset=["post_id","title","score","num_comments"])
print("After removing nulls:",len(remove_missing_values))

#make sure score and num_comments are integers
remove_missing_values["score"]=remove_missing_values["score"].astype(int)
remove_missing_values["num_comments"]=remove_missing_values["num_comments"].astype(int)

#remove stories where score is less than 5
remove_low_quality=remove_missing_values[remove_missing_values["score"]>=5]
print("after removing low scores:",len(remove_low_quality))

# strip extra spaces from the title column
final_dataframe=remove_low_quality.copy()
final_dataframe["title"]=final_dataframe["title"].str.strip()

#A quick summary: how many stories per category
print("Stories per category:")
print(final_dataframe["category"].value_counts())

date_str=datetime.now().strftime("%y%m%d")
filename=f"data/trends_{date_str}.csv"

final_dataframe.to_csv(filename,index=False)

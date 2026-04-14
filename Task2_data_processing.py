import pandas as pd
from datetime import datetime
df=pd.read_json("data/trends_20260414.json")
print("No of rows loaded from data/trends_20260414.json:",len(df))

remove_duplicates=df.drop_duplicates("post_id")
print("After rremoving duplicates:",len(remove_duplicates))

remove_missing_values=remove_duplicates.dropna(subset=["post_id","title","score","num_comments"])
print("After removing nulls:",len(remove_missing_values))

remove_missing_values["score"]=remove_missing_values["score"].astype(int)
remove_missing_values["num_comments"]=remove_missing_values["num_comments"].astype(int)


remove_low_quality=remove_missing_values[remove_missing_values["score"]>=5]
print("after removing low scores:",len(remove_low_quality))


final_dataframe=remove_low_quality.copy()
final_dataframe["title"]=final_dataframe["title"].str.strip()

print("Stories per category:")
print(final_dataframe["category"].value_counts())

date_str=datetime.now().strftime("%y%m%d")
filename=f"data/trends_{date_str}.csv"

final_dataframe.to_csv(filename,index=False)

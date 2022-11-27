import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://Lokesh100:<ind100#meC>@cluster0.gb2w07a.mongodb.net/?retryWrites=true&w=majority")
DATA_FILE_PATH='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME="aps"
COLLECTION_NAME='SENSOR'
if __name__=='__main__':
   df=pd.read_csv(DATA_FILE_PATH)
   print(f'rows and columns:{df.shape}')
   # convert dataframe to JSON so that we can dump these records in Mongodb
   df.reset_index(drop=True,inplace=True)
   json_record=list(json.loads(df.T.to_json()).values())
   print(json_record[0])
   client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


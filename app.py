import pymongo
import pandas as pd
import json
client=pymongo.MongoClient("")
db=Client['app']
Collections=db['Sensor']
Data_file_path='/config/workspace/aps_failure_training_set1.csv.1'
if __name__=='__main__':
    df=pd.read_csv(Data_file_path)
    print(df.head())
    print(f'rows & columns:{df.shape}')
    # convert dataframe to Json to dump to Mongodb
    df.reset_index(drop=True,inplace=True)
    print(df)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client['aps']['SENSOR'].insert_many(json_record)

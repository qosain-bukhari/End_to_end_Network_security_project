import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            logger.info(f"Reading CSV file: {file_path}")
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            logger.info(f"CSV converted to JSON, total records: {len(records)}")
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            logger.info(f"Inserting {len(records)} records into MongoDB: {database}.{collection}")
            client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = client[database]
            coll = db[collection]
            result = coll.insert_many(records)
            logger.info(f"Inserted {len(result.inserted_ids)} records successfully")
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "Network_data/phisingData.csv"
    DATABASE = "QosainBukhari"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(f"Total Records: {len(records)}")
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"Inserted Records: {no_of_records}")

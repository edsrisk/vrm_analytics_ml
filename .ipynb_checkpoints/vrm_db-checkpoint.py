import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime

client = MongoClient("mongodb://localhost:27017/", connect=True)

db = client['vrm_db'] # with this we don't need to manually create a database in MongoDB

def insert_servicetype(service_dict):
    collection = db['service_type']
    return print(collection.insert_one(service_dict).inserted_id)

def insert_contractscoring(contract_scoring_dict):
    collection = db.contract_scoring
    return print(collection.insert_one(contract_scoring_dict).inserted_id)

def insert_vendorscoring(vendor_scoring_dict):
    collection = db.vendor_scoring
    return print(collection.insert_one(vendor_scoring_dict).inserted_id)

def insert_enhancedoversight(enhanced_oversight_dict):
    collection = db.enhanced_oversight
    collection.insert_one(enhanced_oversight_dict)
    #return print(collection.insert_one(enhanced_oversight_dict).inserted_id)


def insert_scoringmodel(scoring_model_dict):
    collection = db.revised_scoring_model
    collection.insert_one(scoring_model_dict)
    #return print(collection.insert_one(scoring_model_dict).inserted_id)
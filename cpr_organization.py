# Import libraries and dependencies for MongoDB
import pymongo
from pymongo import MongoClient # Library to make connection with MongoClient

client = MongoClient() # Connect to the default host and port

# Another connection option - 1: Specify the host and port explicitly
client = MongoClient('localhost', 27017)

# Option 2: Connect by using the MongoDB URI Format
client = MongoClient('mongodb://localhost:27017/')

# Create the database in MongoDB (eg, CPR Soccer Organization which will contains all the cpr teams)
db = client.cpr_database

# Another option for creating the database
# db = client['cpr_database']

# Get a collection: A collection is a list of teams in the cpr organization, i.e. orange, reds, legends, old_boys, etc
collection = db.old_boys # Create the collection here if you are creating a players dictionary

# Or using the dictionary style access
# collection = db['old_boys']

# Insert DataFrame or documents in python file: Create a function
def insert_old_boys(old_boys_dict):
    collection = db.old_boys # collection done in the fuction if you are importing the players table from another python file
    
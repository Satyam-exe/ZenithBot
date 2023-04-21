import datetime
import os

import pymongo
import pytz
from dotenv import load_dotenv, find_dotenv

is_dotenv_loaded = load_dotenv(dotenv_path=find_dotenv(filename='.env'))

host = os.environ.get('MONGODB_HOST')
username = os.environ.get('MONGODB_USERNAME')
password = os.environ.get('MONGODB_PASSWORD')


client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority")

db = client['zenithbot']
chat_col = db['chat']
music_col = db['music']


def insert_chat_to_db(query, reply):
    chat_col.insert_one({
        'query': query,
        'reply': reply,
        'datetime': datetime.datetime.now(pytz.timezone('Asia/Kolkata')),
        'is_revoked': False
    })
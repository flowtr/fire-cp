import os
from firstclass_dotenv import Dotenv
import pymongo
import logging

from pymongo.database import Database
import coloredlogs

from pymongo.mongo_client import MongoClient

logging.basicConfig(level=logging.DEBUG, format="%(asctime)-15s %(message)s")
coloredlogs.install()
logger = logging.getLogger("flowtr.panel")

dotenv = Dotenv()
try:
    dotenv.load()
except:
    logger.error("Could not load .env file, using defaults")

PORT = os.getenv("PORT", 6969)

DB_URI = os.getenv("DB_URI", "mongodb://localhost")
mongo: Database = None

try:
    mongo = pymongo.MongoClient(DB_URI).get_database("panel")
    logger.info("Connected to database.")
except:
    logger.error(f"Could not connect to mongodb at {DB_URI}")

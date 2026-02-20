
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_ID = os.getenv("PROJECT_ID")
    DATASET_ID = os.getenv("DATASET_ID")
    TABLE_ID = os.getenv("TABLE_ID")
    ASTEROIDS_BUCKET = os.getenv("ASTEROIDS_BUCKET")

settings = Settings()
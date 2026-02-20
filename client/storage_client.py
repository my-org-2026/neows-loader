from google.cloud import storage
from utils.settings import settings

class GCSClient:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(settings.ASTEROIDS_BUCKET)

    def download_csv_as_text(self, source_blob_name):
        blob = self.bucket.blob(source_blob_name)
        return blob.download_as_text()

from client.storage_client import GCSClient
from utils.settings import settings
from loader.asteroids_loader import BigQuery
from utils.logger import logger
import pandas as pd
import io

def main(request):
        request_json = request.get_json(silent=True)
        file_path = request_json.get("file_path")

        if not file_path:
            return {"error": "file_path is required"}, 400

        try:
            gcs = GCSClient()
            csv_content = gcs.download_csv_as_text(file_path)

            if not csv_content:
                return {"error": f"CSV file at {file_path} is empty or missing"}, 400

            csv_buffer = io.StringIO(csv_content)
            df = pd.read_csv(csv_buffer, dtype=str)

            loader = BigQuery()
            logger.info("Start loading data to bigquery")
            loader.load_data(df, settings.PROJECT_ID, settings.DATASET_ID, settings.TABLE_ID)
            logger.info("Loaded successfully")

            return {
                "message": "Load complete",
                "rows_loaded": len(df),
                "file_path": file_path
            }

        except Exception as e:
            return {"error": str(e)}, 500

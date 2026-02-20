
from google.cloud import bigquery
from utils.settings import settings
from utils.logger import logger

class BigQuery:
    def __init__(self):
        self.client = bigquery.Client(project=settings.PROJECT_ID)

    def load_data(self, df, project_id, dataset_id, table_id):
        table = f"{project_id}.{dataset_id}.{table_id}"
        job = self.client.load_table_from_dataframe(df, table)
        job.result()

        logger.info("Loaded", job.output_rows, "rows.")

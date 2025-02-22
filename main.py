from src.projectAlpha import logger

from src.projectAlpha.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="data ingestion"

try:
    logger.info(f">>>> stage {STAGE_NAME} started  <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>> stage {STAGE_NAME} completed  <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

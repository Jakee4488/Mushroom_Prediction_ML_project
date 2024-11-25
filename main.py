from GDP_Prediction import logger
from GDP_Prediction.pipeline.Data_ingestion import DataIngestionTrainingPipeline


#
STAGE_NAME="Data Ingestion"

try:
        logger.info(f"Running {STAGE_NAME} stage")
        ingestion_pipeline = DataIngestionTrainingPipeline()
        ingestion_pipeline.main()
        logger.info(f"Completed {STAGE_NAME} stage")
except Exception as e:  
        logger.error(f"Failed to run {STAGE_NAME} stage")
        logger.error(e)
        raise e
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>>>>Running {STAGE_NAME} Started<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>Running {STAGE_NAME} Completed<<<<<<\n\n x==========x==========x==========x\n")
except Exception as e:
    logger.error(e)
    raise e
from src.DataScience_Proj1 import logger
from src.DataScience_Proj1.pipeline.data_ingestion_pipelie import DataIngestionTrainingPipeline
from src.DataScience_Proj1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DataScience_Proj1.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.DataScience_Proj1.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.DataScience_Proj1.pipeline.model_eval_pipeline import ModelEvaluationPipeline

STAGE_NAME='Data Ingestion Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Evaluation'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
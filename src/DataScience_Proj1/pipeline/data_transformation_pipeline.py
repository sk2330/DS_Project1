from src.DataScience_Proj1.config.configuration import ConfigurationManager
from src.DataScience_Proj1.components.data_transformation import DataTransformation
from src.DataScience_Proj1 import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1] ##-1 indicates whether the status is true or false
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            print(e)
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
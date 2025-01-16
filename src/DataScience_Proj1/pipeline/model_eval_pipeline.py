from src.DataScience_Proj1.config.configuration import ConfigurationManager
from src.DataScience_Proj1.components.model_eval import ModelEvaluation
from src.DataScience_Proj1 import logger
from pathlib import Path

STAGE_NAME='Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_eval_config=config.get_model_eval_cofig()
        model_eval_config=ModelEvaluation(config=model_eval_config)
        model_eval_config.log_into_mlflow()
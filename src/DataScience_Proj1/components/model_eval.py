from src.DataScience_Proj1 import logger
from pathlib import Path
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.DataScience_Proj1.utils.common import save_json
from src.DataScience_Proj1.entity.config_entity import ModelEvaluationConfig

os.environ['MLFLOW_TRACKING_URI']='https://dagshub.com/saikiven03/DS_Project1.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME']='saikiven03'
os.environ['MLFLOW_TRACKING_PASSWORD']='7c0e76b0f174dd060d5f14dafb6d79494ef83cfa'

##Model evaluation
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import mlflow
import pandas as pd
class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        mse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return mse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y= test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        ###Starting mlflow run
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (mse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            #saving metrics as local
            scores = {"mse": mse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("mse", mse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            #model registry
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
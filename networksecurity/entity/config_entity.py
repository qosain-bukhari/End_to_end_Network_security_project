from datetime import datetime
import os
from networksecurity.constant import trainingpipeline

print(trainingpipeline.PIPELINE_NAME)
print(trainingpipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=trainingpipeline.PIPELINE_NAME
        self.artifact_name=trainingpipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.model_dir=os.path.join("final_model")
        self.timestamp: str=timestamp



class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,trainingpipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, trainingpipeline.DATA_INGESTION_FEATURE_STORE_DIR, trainingpipeline.FILE_NAME
            )
        os.makedirs(os.path.dirname(self.feature_store_file_path), exist_ok=True)
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, trainingpipeline.DATA_INGESTION_INGESTED_DIR, trainingpipeline.TRAIN_FILE_NAME
            )
        os.makedirs(os.path.dirname(self.training_file_path), exist_ok=True)
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, trainingpipeline.DATA_INGESTION_INGESTED_DIR, trainingpipeline.TEST_FILE_NAME
            )
        os.makedirs(os.path.dirname(self.testing_file_path), exist_ok=True)

        self.train_test_split_ratio: float = trainingpipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = trainingpipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = trainingpipeline.DATA_INGESTION_DATABASE_NAME
       

class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(
             training_pipeline_config.artifact_dir, trainingpipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(
            self.data_validation_dir, trainingpipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(
            self.data_validation_dir, trainingpipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str = os.path.join(
            self.valid_data_dir, trainingpipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path: str = os.path.join(
            self.valid_data_dir, trainingpipeline.TEST_FILE_NAME)
        self.invalid_train_file_path: str = os.path.join(
            self.invalid_data_dir, trainingpipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path: str = os.path.join(
            self.invalid_data_dir, trainingpipeline.TEST_FILE_NAME)
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            trainingpipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            trainingpipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )

class DataTransformationConfig:
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join( training_pipeline_config.artifact_dir,trainingpipeline.DATA_TRANSFORMATION_DIR_NAME )
        self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir,trainingpipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            trainingpipeline.TRAIN_FILE_NAME.replace("csv", "npy"),)
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  trainingpipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            trainingpipeline.TEST_FILE_NAME.replace("csv", "npy"), )
        self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, trainingpipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            trainingpipeline.PREPROCESSING_OBJECT_FILE_NAME,)
        
    
class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, trainingpipeline.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path: str = os.path.join(
            self.model_trainer_dir, trainingpipeline.MODEL_TRAINER_TRAINED_MODEL_DIR, 
            trainingpipeline.MODEL_FILE_NAME
        )
        self.expected_accuracy: float = trainingpipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold = trainingpipeline.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD
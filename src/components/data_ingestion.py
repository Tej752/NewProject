import os,sys
from src.execption import customexception
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_path:str=os.path.join('artifacts','train.csv')
    test_path:str=os.path.join('artifacts','test.csv')
    raw_path:str=os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initate_data_ingestion(self):
        logging.info('Enter the component')
        try:
            df=pd.read_csv('')
            logging.info('Exported the set')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_path,index=False,header=True)
            logging.info('Train Test Initate')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42) 
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True)
            train_set.to_csv(self.ingestion_config.train_path,index=False,header=True)   
            logging.inof('Split Complete')
            
            return(
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )    
        except Exception as e:
            
            raise CustomException(e,sys)
        
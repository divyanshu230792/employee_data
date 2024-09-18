import pickle
import json
import numpy as np
import pandas as pd
import config as cfg


class Emp_Data():
    def __init__(self):
        pass

    def load_data(self):
        with open (cfg.MODEL_FILENAME,'rb') as f:
            self.model=pickle.load(f)

        with open(cfg.COLUMN_DATA,'r') as f:
            self.col_dta=json.load(f)

        self.col_names=self.model.feature_names_in_
        self.col_counts=self.model.n_features_in_

    def Sal_prediction(self,Gender,Experience,Position):
        self.load_data()
        Gender=self.col_dta['Gender'][Gender]
        Position='Position_'+Position
        Position_index=np.where(self.col_names==Position)[0][0]
        test_array=np.zeros((1,self.col_counts))
        test_array[0,0]=Gender
        test_array[0,1]=Experience
        test_array[0,Position_index]=1
        sal_pred=self.model.predict(test_array)[0]
        print('predicted salaary',sal_pred)
        return sal_pred

def load_dataset():
    df=pd.read_csv(cfg.CSV_FILENAME)
    return df
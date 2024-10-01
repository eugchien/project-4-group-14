import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, sex, age, height, weight, name_of_country, year, season, sport):
    
        # Dataframe
        df = pd.DataFrame()
        df["Sex"] = [sex]
        df["Age"] = [age]
        df["Height"] = [height]
        df["Weight"] = [weight]
        df["NOC"] = [name_of_country]
        df["Year"] = [year]
        df["Season"] = [season]
        df["Sport"] = [sport]
        
        # Load Model
        model = pickle.load(open("Olympic_model.pkl", 'rb'))
        
        # Columns in Order
        df = df.loc[:, ['Sex', 'Age', 'Height', 'Weight', 'NOC', 'Year', 'Season', 'Sport']]
        
        # Predict
        preds = model.predict(df)
        
        # Return Prediction
        return preds[0]
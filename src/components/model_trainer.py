import os, sys
import numpy as np
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.utils import save_object


@dataclass
class ModelTrainerConfig:
    model_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            print("🤖 Training multiple models...")

            models = {
                "LinearRegression": LinearRegression(),
                "DecisionTree": DecisionTreeRegressor(),
                "RandomForest": RandomForestRegressor(),
                "GradientBoosting": GradientBoostingRegressor()
            }

            best_score = -1
            best_model = None
            best_model_name = ""

            for name, model in models.items():
                model.fit(X_train, y_train)
                preds = model.predict(X_test)
                score = r2_score(y_test, preds)

                print(f"{name}: {score}")

                if score > best_score:
                    best_score = score
                    best_model = model
                    best_model_name = name

            print(f"🏆 Best Model: {best_model_name} (Score: {best_score})")

            save_object(self.config.model_path, best_model)

            print("💾 Model saved")

        except Exception as e:
            raise CustomException(e, sys)
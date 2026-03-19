import os
import sys
import pickle
import logging
from sklearn.metrics import r2_score
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info('Exception occurred in load_object function utils')
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for model_name, model in models.items():
            try:
                # Train
                model.fit(X_train, y_train)

                # Predict
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                # Scores
                train_score = r2_score(y_train, y_train_pred)
                test_score = r2_score(y_test, y_test_pred)

                report[model_name] = {
                    "train_score": train_score,
                    "test_score": test_score
                }

            except Exception as model_error:
                logging.warning(f"{model_name} failed: {model_error}")
                report[model_name] = None

        return report

    except Exception as e:
        raise CustomException(e, sys)
"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_best_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=train_best_model, inputs=["X_train", "X_test", "y_train", "y_test"], outputs="model_score", name="train_model")
    ])

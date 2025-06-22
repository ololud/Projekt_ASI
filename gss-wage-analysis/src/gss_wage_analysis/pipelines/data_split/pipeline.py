"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=split_data, inputs="cleaned_data", outputs=["X_train", "X_test", "y_train", "y_test"], name="split_data")
    ])

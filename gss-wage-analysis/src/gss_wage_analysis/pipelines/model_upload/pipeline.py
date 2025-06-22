"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import upload_model_to_azure


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=upload_model_to_azure, inputs="model_score", outputs=None, name="upload_model_to_azure_node")
    ])

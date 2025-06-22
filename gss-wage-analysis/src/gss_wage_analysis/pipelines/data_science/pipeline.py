"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=clean_data, inputs="gss_wages", outputs="cleaned_data", name="clean_data")
    ])

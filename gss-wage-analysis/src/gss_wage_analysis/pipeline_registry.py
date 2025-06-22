"""Project pipelines."""
from __future__ import annotations

from kedro.pipeline import Pipeline
from gss_wage_analysis.pipelines import data_science, data_split, data_modelling, model_upload


def register_pipelines() -> dict[str, Pipeline]:
    return {
        "data_science": data_science.create_pipeline(),
        "data_split": data_split.create_pipeline(),
        "data_modelling": data_modelling.create_pipeline(),
        "model_upload": model_upload.create_pipeline(),
        "__default__": data_science.create_pipeline()
                       + data_split.create_pipeline()
                       + data_modelling.create_pipeline()
                       + model_upload.create_pipeline()
    }

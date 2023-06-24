from __future__ import annotations

import os
import warnings

from model_selector.constants import SAVE_DIR_NAME

from olympus.datasets import Dataset


warnings.simplefilter("ignore")


def get_dataset(dataset_name: str) -> Dataset:
    return Dataset(kind=dataset_name)


def get_search_space(dataset: Dataset) -> dict[str, tuple[float, float]]:
    return {p.name: (p.low, p.high) for p in dataset.param_space.parameters}


def save_dataset(dataset: Dataset, dataset_name: str) -> None:
    dir_name = os.path.join(SAVE_DIR_NAME, dataset_name)
    os.makedirs(dir_name, exist_ok=True)
    dataset.features.to_csv(os.path.join(dir_name, "feats.csv"))
    dataset.targets.to_csv(os.path.join(dir_name, "targets.csv"))

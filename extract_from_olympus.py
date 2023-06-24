from __future__ import annotations

import json
import os
import warnings

from olympus.datasets import Dataset


warnings.simplefilter("ignore")
SAVE_DIR_NAME = "data"


def get_dataset(dataset_name: str) -> Dataset:
    return Dataset(kind=dataset_name)


def get_search_space(dataset: Dataset) -> dict[str, tuple[float, float]]:
    return {p.name: (p.low, p.high) for p in dataset.param_space.parameters}


def save_dataset(dataset: Dataset, dataset_name: str) -> None:
    dir_name = os.path.join(SAVE_DIR_NAME, dataset_name)
    os.makedirs(dir_name, exist_ok=True)
    dataset.features.to_csv(os.path.join(dir_name, "feats.csv"))
    dataset.targets.to_csv(os.path.join(dir_name, "targets.csv"))


if __name__ == "__main__":
    os.makedirs(SAVE_DIR_NAME, exist_ok=True)
    dataset_names = [
        "alkox",
        "benzylation",
        "colors_bob",
        "colors_n9",
        "fullerenes",
        "hplc",
        "photo_pce10",
        "photo_wf3",
        "snar",
        "suzuki",
    ]
    search_spaces: dict[str, dict[str, tuple[float, float]]] = {}
    minimizations: dict[str, bool] = {}
    for dataset_name in dataset_names:
        dataset = get_dataset(dataset_name)
        save_dataset(dataset=dataset, dataset_name=dataset_name)
        search_spaces[dataset_name] = get_search_space(dataset)
        minimizations[dataset_name] = bool(dataset.goal == "maximize")

    with open(os.path.join(SAVE_DIR_NAME, "search_spaces.json"), mode="w") as f:
        json.dump(search_spaces, f, indent=4)

    with open(os.path.join(SAVE_DIR_NAME, "minimizes.json"), mode="w") as f:
        json.dump(minimizations, f, indent=4)

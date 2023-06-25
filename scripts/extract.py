from __future__ import annotations

import json
import os

from model_selector.extract_from_olympus import get_dataset, get_search_space, save_dataset

from olympus_surrogate_bench.constants import DATASET_NAMES, SAVE_DIR_NAME


if __name__ == "__main__":
    os.makedirs(SAVE_DIR_NAME, exist_ok=True)
    search_spaces: dict[str, dict[str, tuple[float, float]]] = {}
    minimizations: dict[str, bool] = {}
    for dataset_name in DATASET_NAMES:
        dataset = get_dataset(dataset_name)
        save_dataset(dataset=dataset, dataset_name=dataset_name)
        search_spaces[dataset_name] = get_search_space(dataset)
        minimizations[dataset_name] = bool(dataset.goal == "maximize")

    with open(os.path.join(SAVE_DIR_NAME, "search_spaces.json"), mode="w") as f:
        json.dump(search_spaces, f, indent=4)

    with open(os.path.join(SAVE_DIR_NAME, "minimizes.json"), mode="w") as f:
        json.dump(minimizations, f, indent=4)

from model_selector.constants import DATASET_NAMES
from model_selector.model_selection import optimize


if __name__ == "__main__":
    for dataset_name in DATASET_NAMES:
        print(f"Start {dataset_name}")
        optimize(dataset_name=dataset_name, n_trials=200)

from __future__ import annotations

import json
import os
import pickle

from model_selector.constants import SAVE_DIR_NAME

import optuna

import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold


SEED = 42


class Evaluator:
    def __init__(self, dataset_name: str, n_folds: int = 5, seed: int = SEED):
        self._feats = pd.read_csv(os.path.join(SAVE_DIR_NAME, dataset_name, "feats.csv"))
        self._targets = pd.read_csv(os.path.join(SAVE_DIR_NAME, dataset_name, "targets.csv"))
        kf = KFold(n_splits=n_folds, shuffle=True, random_state=seed)
        self._fold_indices = [
            (train_indices, val_indices) for train_indices, val_indices in kf.split(self._feats, self._targets)
        ]

    def format_best_trial(self, best_trial: optuna.FrozenTrial) -> dict[str, int | float]:
        return {k: v if k == "max_features" else int(v) for k, v in best_trial.params.items()}

    def full_train(self, best_trial: optuna.FrozenTrial) -> float:
        model_kwargs = dict(n_estimators=100, **self.format_best_trial(best_trial))
        model = RandomForestRegressor(**model_kwargs)
        return model.fit(self._feats, self._targets)

    def __call__(self, trial: optuna.Trial) -> float:
        model_kwargs = dict(
            n_estimators=100,
            max_features=trial.suggest_float(name="max_features", low=0.0, high=1.0),
            max_depth=int(trial.suggest_float(name="max_depth", low=1, high=64, log=True)),
            min_samples_split=int(trial.suggest_float(name="min_samples_split", low=2, high=32, log=True)),
            min_samples_leaf=int(trial.suggest_float(name="min_samples_leaf", low=1, high=16, log=True)),
        )
        score = 0.0  # larger is better! (maximum is 1.0)
        for train_indices, val_indices in self._fold_indices:
            model = RandomForestRegressor(**model_kwargs)
            feats_train, targets_train = self._feats.iloc[train_indices], self._targets.iloc[train_indices]
            model.fit(feats_train, targets_train)
            feats_val, targets_val = self._feats.iloc[val_indices], self._targets.iloc[val_indices]
            score += model.score(feats_val, targets_val)

        return score


def optimize(dataset_name: str, n_trials: int = 200) -> None:
    evaluator = Evaluator(dataset_name=dataset_name)
    sampler = optuna.samplers.TPESampler(seed=SEED)
    study = optuna.create_study(direction="maximize", sampler=sampler)
    study.optimize(evaluator, n_trials=n_trials)

    best_trial = study.best_trial
    with open(os.path.join(SAVE_DIR_NAME, dataset_name, "best_config.json"), "w") as f:
        json.dump(evaluator.format_best_trial(best_trial), f, indent=4)
    with open(os.path.join(SAVE_DIR_NAME, dataset_name, "model.pkl"), "wb") as f:
        pickle.dump(evaluator.full_train(best_trial), f)

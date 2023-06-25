from __future__ import annotations

import unittest

from olympus_surrogate_bench import OlympusSurrogateAPI
from olympus_surrogate_bench.constants import DATASET_NAMES

import pytest


def test_dataset_names():
    for i, name in enumerate(DATASET_NAMES):
        assert name == DATASET_NAMES[i]


def test_init():
    for name in DATASET_NAMES:
        OlympusSurrogateAPI(dataset_name=name)


def test_call():
    for name in DATASET_NAMES:
        api = OlympusSurrogateAPI(dataset_name=name)
        assert isinstance(api(dict(api.config_space.sample_configuration())), float)


def test_validate_config():
    for name in DATASET_NAMES:
        api = OlympusSurrogateAPI(dataset_name=name)
        config = dict(api.config_space.sample_configuration())
        config["dummy"] = 1.0
        with pytest.raises(ValueError, match=r"Keys of eval_config must be identical*"):
            api(config)

        hp_names = list(api._hp_names)
        config = dict(api.config_space.sample_configuration())
        config.pop(hp_names[0])
        with pytest.raises(KeyError, match=r"eval_config must have a key named*"):
            api(config)

        config = dict(api.config_space.sample_configuration())
        hp = api.config_space.get_hyperparameter(hp_names[0])
        config[hp.name] = hp.upper + 1.0
        with pytest.raises(ValueError, match=r".* must be in .*"):
            api(config)

        config = dict(api.config_space.sample_configuration())
        hp = api.config_space.get_hyperparameter(hp_names[0])
        config[hp.name] = hp.lower - 1.0
        with pytest.raises(ValueError, match=r".* must be in .*"):
            api(config)


if __name__ == "__main__":
    unittest.main()

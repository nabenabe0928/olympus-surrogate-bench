from __future__ import annotations

import unittest

from olympus_surrogate_bench import OlympusSurrogateAPI
from olympus_surrogate_bench.constants import DATASET_NAMES


def test_init():
    for name in DATASET_NAMES:
        OlympusSurrogateAPI(dataset_name=name)


def test_call():
    pass


def test_validate_config():
    pass


if __name__ == "__main__":
    unittest.main()

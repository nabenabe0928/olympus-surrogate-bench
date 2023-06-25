import os
import setuptools

import numpy as np

from olympus_surrogate_bench.constants import DATASET_NAMES


DATA_DIR = "data/"
requirements = []
with open("requirements-for-setup.txt", "r") as f:
    for line in f:
        requirements.append(line.strip())

pkg_data = np.ravel(
    [[os.path.join(DATA_DIR, name, f"*.{fmt}") for fmt in ["json", "csv", "pkl"]] for name in DATASET_NAMES]
).tolist()
setuptools.setup(
    name="olympus-surrogate-bench",
    version="0.0.2",
    author="nabenabe0928",
    author_email="shuhei.watanabe.utokyo@gmail.com",
    url="https://github.com/nabenabe0928/olympus-surrogate-bench",
    packages=setuptools.find_packages(),
    package_data={"": ["data/minimizes.json", "data/search_spaces.json"] + pkg_data},
    python_requires=">=3.8",
    platforms=["Linux", "Darwin"],
    install_requires=requirements,
    include_package_data=True,
)

# A Surrogate Benchmark for Olympus

[![Build Status](https://github.com/nabenabe0928/olympus-surrogate-bench/workflows/Functionality%20test/badge.svg?branch=main)](https://github.com/nabenabe0928/olympus-surrogate-bench)
[![codecov](https://codecov.io/gh/nabenabe0928/olympus-surrogate-bench/branch/main/graph/badge.svg?token=SQGBB6W2JV)](https://codecov.io/gh/nabenabe0928/olympus-surrogate-bench)

This repository provides the training script for the surrogate benchmark for [Olympus](https://github.com/aspuru-guzik-group/olympus), an experiment design benchmark dataset, and the benchmark wrappper.

Roughly speaking, Olympus is a hyperparameter optimization benchmark dataset in the chemistry domain.

The surrogate models are built by random forests.
Note that Olympus also provides a surrogate benchmark, but it uses TensorFlow1.X, and hence users cannot use it with Python3.8+.


## Setup

To use the surrogate benchmarks, you can simply install via pip:
```shell
$ pip install olympus-surrogate-bench
```

An easy example is the following:

```python
from olympus_surrogate_bench import OlympusSurrogateAPI


# dataset_id must be chosen from the table below, i.e. 0 -- 9
api = OlympusSurrogateAPI(dataset_id=0)

# Search space
print(api.config_space)

# Random sample
config = dict(api.config_space.sample_configuration())

# Query result
print(api(config))
```

## Datasets

The datasets currently available are the following:
|Dataset ID|Dataset Name|Minimize|
|:--:|--|:--:|
|0|[alkox](https://aspuru-guzik-group.github.io/olympus/classes/datasets/alkox.html#dataset-alkox)|Yes|
|1|[benzylation](https://aspuru-guzik-group.github.io/olympus/classes/datasets/benzylation.html#dataset-benzylation)|No|
|2|[colors_bob](https://aspuru-guzik-group.github.io/olympus/classes/datasets/colors_bob.html)|No|
|3|[colors_n9](https://aspuru-guzik-group.github.io/olympus/classes/datasets/colors_n9.html)|No|
|4|[fullerenes](https://aspuru-guzik-group.github.io/olympus/classes/datasets/fullerenes.html)|Yes|
|5|[hplc](https://aspuru-guzik-group.github.io/olympus/classes/datasets/hplc.html)|Yes|
|6|[photo_pce10](https://aspuru-guzik-group.github.io/olympus/classes/datasets/photo_pce10.html#dataset-photo-pce10)|No|
|7|[photo_wf3](https://aspuru-guzik-group.github.io/olympus/classes/datasets/photo_wf3.html#dataset-photo-wf3)|No|
|8|[snar](https://aspuru-guzik-group.github.io/olympus/classes/datasets/snar.html#dataset-snar)|No|
|9|[suzuki](https://aspuru-guzik-group.github.io/olympus/classes/datasets/suzuki.html#dataset-suzuki)|Yes|

## Training

If you would like to train surrogate models by yourself, you could try out the following:

```shell
$ pip install -r requirements-for-extractor.txt
$ python -m scripts.extract
$ python -m scripts.optimize
```

By running the commands, you get the identical surrogate models.

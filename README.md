# A Surrogate Benchmark for Olympus

[![Build Status](https://github.com/nabenabe0928/olympus-surrogate-bench/workflows/Functionality%20test/badge.svg?branch=main)](https://github.com/nabenabe0928/olympus-surrogate-bench)
[![codecov](https://codecov.io/gh/nabenabe0928/olympus-surrogate-bench/branch/main/graph/badge.svg?token=FQWPWEJSWE)](https://codecov.io/gh/nabenabe0928/olympus-surrogate-bench)

This repository provides the training script for the surrogate benchmark for [Olympus](https://github.com/aspuru-guzik-group/olympus) and the benchmark wrappper.
The surrogate models are built by random forests.
Note that Olympus also provides a surrogate benchmark, but it uses TensorFlow1.X, and hence users cannot use it with Python3.8+.

### NOTE

Before copying the repository, please make sure to change the following parts:
3. The URLs to `Build Status` and `codecov` (we need to copy from the `codecov` website) in `README.md`
4. Setting up the `codecov` of the repository
5. The token of `codecov.yml`

## Local check

In order to check if the codebase passes Github actions, run the following:

```shell
$ pip install black pytest unittest flake8 pre-commit pytest-cov
$ ./check_github_actions_locally.sh
```

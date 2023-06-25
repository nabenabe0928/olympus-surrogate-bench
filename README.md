# A Surrogate Benchmark for Olympus

[![Build Status](https://github.com/nabenabe0928/olympus-surrogate-bench/workflows/Functionality%20test/badge.svg?branch=main)](https://github.com/nabenabe0928/olympus-surrogate-bench)
[![codecov](https://codecov.io/gh/nabenabe0928/olympus-surrogate-bench/branch/main/graph/badge.svg?token=SQGBB6W2JV)](https://codecov.io/gh/nabenabe0928/olympus-surrogate-bench)

This repository provides the training script for the surrogate benchmark for [Olympus](https://github.com/aspuru-guzik-group/olympus) and the benchmark wrappper.
The surrogate models are built by random forests.
Note that Olympus also provides a surrogate benchmark, but it uses TensorFlow1.X, and hence users cannot use it with Python3.8+.

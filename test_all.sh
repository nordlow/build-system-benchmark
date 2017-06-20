#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";
JOB_COUNT=$((${CPU_COUNT} + 1))

./generate_sources.py
./benchmark_scons.sh
./benchmark_bazel.sh

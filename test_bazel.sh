#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";

./generate_sources.py
bazel build -j ${CPU_COUNT} :bench

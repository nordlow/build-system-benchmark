#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";

./generate_sources.py
mkdir -p build
make -s -j ${CPU_COUNT}

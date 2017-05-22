#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";

./generate_sources.py
mkdir build
make -s -j ${CPU_COUNT}

#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";

./generate_sources.py
time scons -s -j ${CPU_COUNT}

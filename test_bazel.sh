#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";
JOB_COUNT=$((${CPU_COUNT} + 1))

./generate_sources.py

# sudo ./increase_inotify_limits.sh    # needed by Bazel's flag `--watchfs`
time bazel --watchfs build -j ${JOB_COUNT} :bench # TODO try out --watchfs when it works

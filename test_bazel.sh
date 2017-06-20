#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";
JOB_COUNT=$((${CPU_COUNT} + 1))

# generate
./generate_sources.py

# sudo ./increase_inotify_limits.sh    # needed by Bazel's flag `--watchfs`

# NOTE disabled: --experimental_action_listener=//:cppcheck_c_cpp
# NOTE disabled: --watchfs
# NOTE disable: --copt="-Wall"

# build
echo
echo "######################"
echo "Benchmarking Bazel ..."
pushd src > /dev/null
time bazel build -j ${JOB_COUNT} //...
popd > /dev/null

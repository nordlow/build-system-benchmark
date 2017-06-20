#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";
JOB_COUNT=$((${CPU_COUNT} + 1))

./generate_sources.py

# SCons
echo "Benchmarking SCons ..."
time scons -s -j ${JOB_COUNT}

# Bazel
echo "Benchmarking Bazel ..."
pushd src
time bazel \
     build \
     -j ${JOB_COUNT} \
     //... # TODO try out --watchfs when it works
popd

#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";
JOB_COUNT=$((${CPU_COUNT} + 1))

echo
echo "######################"
echo "Benchmarking SCons ..."
time scons -s -j ${JOB_COUNT}

#!/bin/bash

CPU_COUNT="$(grep -c processor /proc/cpuinfo)";
JOB_COUNT=$((${CPU_COUNT} + 1))

echo
echo "######################"
echo "Benchmarking Buck ..."

time buck build -j ${JOB_COUNT} //...

#!/bin/bash

SCONS_PROFILE=$(mktemp --suffix=.profile)
SCONS_DOT_OUTPUT=$(mktemp --suffix=.png)

./generate_sources.py
scons -s -Q --profile=${SCONS_PROFILE} && gprof2dot -f pstats ${SCONS_PROFILE} | dot -Tpng -o ${SCONS_DOT_OUTPUT} && xdg-open ${SCONS_DOT_OUTPUT}

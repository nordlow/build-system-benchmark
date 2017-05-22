#!/bin/bash

SCONS_PROFILE=$(mktemp --sufix=.profile)
SCONS_DOT_OUTPUT=$(mktemp --suffix=.png)

scons -s -Q --profile=${SCONS_PROFILE} && gprof2dot -f pstats ${SCONS_PROFILE} | dot -Tpng -o ${SCONS_DOT_OUTPUT} && gnome-open ${SCONS_DOT_OUTPUT}

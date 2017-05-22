#!/bin/bash

scons -s -Q --profile=scons.profile && gprof2dot -f pstats scons.profile | dot -Tpng -o output.png && o output.png

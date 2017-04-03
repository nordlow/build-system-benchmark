#!/usr/bin/env python2

import os
import os.path

SetOption('random', 1);         # randomize build order

env = Environment(LINK="ld.gold") # Initialize the environment

env.Decider('MD5-timestamp')

build_dir = 'build'
home_dir = os.path.expanduser('~')

# setup cache
cache_dir = os.path.join(home_dir, '.cache/scons')
try: os.makedirs(cache_dir)
except: pass                    # ok if exists
env.CacheDir(cache_dir)

env.Library(target=os.path.join(build_dir, 'benchscons'),
            source=env.Glob('src/*.c'))

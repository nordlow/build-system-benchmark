#!/usr/bin/env python3

import os
import shutil


def regenerate_sources(src_path='src',
                       lib_count=2000,
                       file_count=10,
                       header_count=10):

    # generate top Bazel BUILD file
    with open(os.path.join("BUILD"), 'w') as f:
        f.write('''''')

    # generate top Bazel WORKSPACE file
    with open(os.path.join("WORKSPACE"), 'w') as f:
        f.write('''''')

    # generate top Buck file
    with open(os.path.join(".buckconfig"), 'w') as f:
        f.write('''''')

    # empty src tree
    shutil.rmtree(src_path, ignore_errors=True)

    os.makedirs(src_path, exist_ok=True)

    with open(os.path.join("SConstruct"), 'w') as sconstruct_f:
        sconstruct_f.write('''#!/usr/bin/env python2

import os
import os.path
import multiprocessing

num_jobs = min(int(multiprocessing.cpu_count() + 1), 9)
SetOption("num_jobs", num_jobs)

SetOption('random', 1);         # randomize build order

env = Environment(LINK="ld.gold") # Initialize the environment
env.Decider('MD5-timestamp')

build_dir = 'build/scons'
home_dir = os.path.expanduser('~')

# setup cache
cache_dir = os.path.join(home_dir, '.cache', 'scons')
try:
    os.makedirs(cache_dir)
except:
    pass                        # ok if exists
env.CacheDir(cache_dir)
''')

        for lib_index in range(0, lib_count):
            lib_name = 'lib' + '{num:03d}'.format(num=lib_index)

            sub_path = os.path.join(src_path, lib_name)
            os.makedirs(sub_path, exist_ok=True)

            # generate source file
            for i in range(file_count):
                istr = '{num:05d}'.format(num=i)
                test_file_name = 'source'+istr+'.c'
                with open(os.path.join(sub_path, lib_name + '_' + test_file_name), 'w') as f:

                    # include som C-header
                    f.write('''#include <stdio.h>
    #include <stdlib.h>

''')

                    # include local headers
                    for j in range(header_count):
                        jstr = '{num:05d}'.format(num=j)
                        f.write('''#include "utils_''' + jstr + '''.h"\n''')

                        f.write('''
    int function''' + jstr + '''(int x)
    {
        return x+1;
    }
''')

            # generate header file
            for i in range(header_count):
                istr = '{num:05d}'.format(num=i)
                with open(os.path.join(sub_path, 'utils_'+istr+'.h'), 'w') as f:
                    f.write('''#include <stdio.h>
    #include <stdlib.h>

    int utils_''' + istr + '''(int x);
''')

            # generate Bazel BUILD file
            with open(os.path.join(sub_path, "BUILD"), 'w') as f:
                f.write('''cc_library(
    name = "{}",
    srcs = glob(["*.c", "*.h"]),
    linkstatic = 1,
)
'''.format(lib_name))

            # generate Buck BUCK file
            with open(os.path.join(sub_path, "BUCK"), 'w') as f:
                f.write('''cxx_library(
    name = "{}",
    srcs = glob(["*.c", "*.h"]),
)
'''.format(lib_name))

            # generate SCons Library
            sconstruct_f.write('''
env.StaticLibrary(target=os.path.join(build_dir, '{}'),
                  source=env.Glob('{}'))
'''.format(lib_name, os.path.join('src', lib_name, '*.c')))


if (__name__ == '__main__'):
    # regenerate_sources(*sys.argv[1:])
    regenerate_sources()

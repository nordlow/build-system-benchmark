#!/usr/bin/env python3

import os
import shutil


def regenerate_sources(root_path='src',
                       lib_count=2000,
                       file_count=10,
                       header_count=10):

    shutil.rmtree(root_path, ignore_errors=True)

    os.makedirs(root_path, exist_ok=True)

    # generate top Bazel BUILD file
    with open(os.path.join(root_path, "BUILD"), 'w') as f:
        f.write('''''')

    # generate top Bazel WORKSPACE file
    with open(os.path.join(root_path, "WORKSPACE"), 'w') as f:
        f.write('''''')


    for lib_index in range(0, lib_count):
        lib_name = 'lib' + '{num:03d}'.format(num=lib_index)

        sub_path = os.path.join(root_path, lib_name)
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


if (__name__ == '__main__'):
    # regenerate_sources(*sys.argv[1:])
    regenerate_sources()

#!/usr/bin/env python3

import os
import shutil


def regenerate_sources(root_path='src',
                       lib_count=100,
                       file_count=100,
                       header_count=100):

    shutil.rmtree(root_path, ignore_errors=True)

    os.makedirs(root_path, exist_ok=True)

    for lib_index in range(0, lib_count):
        lib_prefix = 'lib' + '{num:03d}'.format(num=lib_index)

        sub_path = os.path.join(root_path, lib_prefix)
        os.makedirs(sub_path, exist_ok=True)

        for i in range(file_count):
            istr = '{num:05d}'.format(num=i)
            test_prefix = 'source'+istr+'.c'
            with open(os.path.join(sub_path, lib_prefix + '_' + test_prefix), 'w') as f:

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

        for i in range(header_count):
            istr = '{num:05d}'.format(num=i)
            with open(os.path.join(sub_path, 'utils_'+istr+'.h'), 'w') as f:
                f.write('''#include <stdio.h>
#include <stdlib.h>

int utils_''' + istr + '''(int x);
''')


if (__name__ == '__main__'):
    # regenerate_sources(*sys.argv[1:])
    regenerate_sources()

#!/usr/bin/env python3

import os


def gen(root_path='src',
        file_count=10000,
        header_count=100):

    os.makedirs(root_path, exist_ok=True)

    for i in range(file_count):
        istr = '{num:05d}'.format(num=i)
        f = open(root_path+'/test_'+istr+'.c', 'w')

        # include som C-header
        f.write('''#include <stdio.h>
#include <stdlib.h>

''')

        # include local headers
        for j in range(header_count):
            jstr = '{num:05d}'.format(num=j)
            f.write('''#include "utils_''' + jstr + '''.h"\n''')

            f.write('''
int f_''' + istr + '''(int x)
{
    return x+1;
}
''')
            f.close()

    for i in range(header_count):
        istr = '{num:05d}'.format(num=i)
        f = open(root_path+'/utils_'+istr+'.h', 'w')
        f.write('''#include <stdio.h>
#include <stdlib.h>

int utils_''' + istr + '''(int x);
''')
        f.close()

if (__name__ == '__main__'):
    # gen(*sys.argv[1:])
    gen()

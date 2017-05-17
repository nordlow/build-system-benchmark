#!/usr/bin/env python3

import os, sys
import unittest

def gen(root_path='src',
        fileCount=2000,
        headerCount=10):

    try: os.makedirs(root_path);
    except: pass                # ok if exists
    
    for i in range(fileCount):
        istr = '{num:05d}'.format(num=i)
        f = open(root_path+'/test_'+istr+'.c', 'w');

        # include som C-header
        f.write('''#include <stdio.h>
#include <stdlib.h>

''');

        # include local headers
        for j in range(headerCount):
            jstr = '{num:05d}'.format(num=j)
            f.write('''#include "utils_''' + jstr + '''.h"\n''');
            
        f.write('''
int f_''' + istr +'''(int x)
{
    return x+1;
}
''');
        f.close();

    for i in range(headerCount):
        istr = '{num:05d}'.format(num=i)
        f = open(root_path+'/utils_'+istr+'.h', 'w');
        f.write('''#include <stdio.h>
#include <stdlib.h>

int utils_''' + istr +'''(int x);
''');
        f.close();

if (__name__ == '__main__'):
    # gen(*sys.argv[1:])
    gen();

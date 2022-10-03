#!/usr/bin/env python
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        
        print(' EXEC -> ' + os.path.basename(__file__)) 

    except Exception as e:
        print( 'Err: ' + str( e ) )

if __name__ == '__main__':
    main()

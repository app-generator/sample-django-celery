#!/usr/bin/env python
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import sys

def main():

    try:
        
        print(' EXEC -> ' + os.path.basename(__file__)) 
        
        # Unix ErrCode
        exit(0)

    except Exception as e:

        print( 'Err: ' + str( e ) )
        exit(1)

if __name__ == '__main__':
    main()

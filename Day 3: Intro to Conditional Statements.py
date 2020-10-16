#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if N%2!=0:
        print("Weird")
    else:
        if N in [2,3,5]:
            print("Not Weird")
        elif N in [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            print("Weird")
        else:
            print("Not Weird")

# Script to generate random numbers for the test

import sys

n = int(sys.argv[1])

print(n)
print('_'.join(str[i*2]) for i in range(n))
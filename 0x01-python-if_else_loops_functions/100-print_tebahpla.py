#!/usr/bin/python3
for i in range(122, 96, -1):
    # where i is odd, print it uppercase
    print('{:c}'.format((65 + (i - 97)) if (i % 2) else i), end="")

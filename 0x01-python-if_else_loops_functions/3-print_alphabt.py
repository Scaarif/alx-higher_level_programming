#!/usr/bin/python3
for i in range(26):
    if (97 + i) == 113 or (97 + i) == 101:
        continue
    else:
        print(f"{(97 + i):c}", end="")

#! python3

import sys

N = int(input())
if N < 1 or N > 1000:
    print("Invalid number of salmons")
    sys.exit()

length = [int(x) for x in input().split()]
for x in length:
    if x < 1 or x > 1000000000:
        print("Invalid input")
        sys.exit()

time = [int(x) for x in input().split()]
for x in length:
    if x < 0 or x > 1000000000:
        print("Invalid input")
        sys.exit()

if len(length) != N or len(time) != N:
    print("Length of input for length or time is not matching with total salmon")
    sys.exit()


print(N)
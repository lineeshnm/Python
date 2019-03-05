#! python3
from pprint import pprint as pp

N = int(input())

# Get the array
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = [map(lambda x, y: x + y, numArray1, numArray2)]

# Write the logic here:



# Print the sumArray
for element in sumArray:
    print(element, end=" ")

print("")
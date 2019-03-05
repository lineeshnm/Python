#! python3
#from pprint import pprint as pp
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

#blank = input()
#if blank != "":
#    print("last line should be blank")
#    sys.exit()

if len(length) != N or len(time) != N:
    print("Length of input for length or time is not matching with total salmon")
    sys.exit()

count_of_salmon = []
#for i in range(0,N):
#    length[i] += 1

#def reduce_time(N):
#    for x in range(0,N):
#        time[x] -= 1

#if N > 1000:
#    print(N)
#    sys.exit()
#for T in range(0,max(time)+max(length)):
for T in range(min(time),max(time)):
    sum_salmon = 0
    for i in range(0,N):
        if (T-time[i] >= 0 and T-time[i]-length[i] < 0):
            sum_salmon += 1

    if sum_salmon > 0:
        count_of_salmon.append(sum_salmon)

        #for T in range(min(time),max(time)):
#    time_sum = sum(1 for i in time if (T-i) == 0)
#    if time_sum != 0:
#        count_of_salmon.append(time_sum)
#    time_zero = [i for i, x in enumerate(time) if x == 0]
#    for i in time_zero:
#        length[i] -= 1
#        if length[i] > 0:
#            time[i] += 1
#    reduce_time(N)

#count_of_salmon = sorted(set(count_of_salmon))
count_of_salmon.sort(reverse=True)
if max(count_of_salmon) == N:
    print(N)
else:
    """Get the optimal catch"""
    temp = []
    for i in range(0,len(count_of_salmon)):
        for j in range(1,len(count_of_salmon)):
            if count_of_salmon[i]+count_of_salmon[j] == N:
                temp.append(count_of_salmon[i]+count_of_salmon[j])
                break
            if count_of_salmon[i]+count_of_salmon[j] <= N:
                temp.append(count_of_salmon[i]+count_of_salmon[j])
    print(max(temp))



from math import sqrt

N= range(1,2000000000)
N= int(input())
M= sqrt(N)

if N % M == 0:
    print(int(M))
else:
    print(0)    
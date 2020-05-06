li=[[int(el) for el in input().split()]for j in range(3)]
m=3
n=3
for o in range(m):
    if o%2==0:
        for p in range(n):
            print(li[p][o],end=" ")
    else:
        for p in range(n-1,-1,-1):
            print(li[p][o],end=" ")
    p  rint()
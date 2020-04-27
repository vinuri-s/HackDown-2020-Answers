# Programming Language : Python
n = int(input())
n -= 1
x = 0
for i in range(n,-1,-1):
    line = list(str(pow(11,i)))
    for y in range(x):
        print(" ",end="")
    for z in line:
        print(z,end=" ")
    x += 1
    print()

# Programming Language : Python
x,y = input().split(' ')
C = int(x)
P = float(y)

ans = P/(P+(1-P)/C)

print('%.2f'%ans)

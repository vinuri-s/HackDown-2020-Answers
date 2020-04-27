# Programming Language : Python
w,h=map(int,input().split())
G = []
for r in range(h):
    G.append(list(map(int,input().strip().split())))
    
for r in range(h):
    prev=w
    for c in range(w-1,-1,-1):
        if G[r][c]==2:
            G[r][c]=0
            G[r][prev-1]=2
            prev=prev-1
        elif G[r][c]==1:
            prev=c

for r in range(h):
    print(" ".join(map(str,G[r])).strip())

# Programming Language : Python
import re
import sys

def getNumbers(str): 
    array = re.findall(r'[0-9]+', str)
    return set(array)

def fib(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fib(n-1) + fib(n-2)
        return arr[n]

arr = [0] * 6001
arr[0] = 1
arr[1] = 1
if __name__ == "__main__":
    sys.setrecursionlimit(100000000)
    x = fib(6000)
    arr1 = set() 
    N = int(input())
    for j in range(N):
        line = input()
        arr1.update(getNumbers(line)) 
    newArr = list(map(int,arr1))
    newArr.sort(reverse=True)
    for i in newArr:
        if i in arr:
            print(i)
            break
    
   

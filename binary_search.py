# Uses python3
import sys

def binary_search(a,left,right,x):
    if left > right:
        return -1
    mid = (left+right)//2
    if a[mid] == x:
        return mid
    else:
        if a[mid]>x:
            return binary_search(a,left,mid-1,x)
        else:
            return binary_search(a,mid+1,right,x)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    l = 0
    r = len(a)-1
    for x in data[n + 2:]:
        print(binary_search(a,l,r,x), end=' ')

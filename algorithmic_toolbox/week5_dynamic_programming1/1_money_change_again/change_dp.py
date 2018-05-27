# Uses python3
import sys

def fill(a):
    a[1:5] = [1,2,1,1]
    for i in range(5,len(a)):
        a[i] = min(a[i-1], a[i-3], a[i-4]) + 1
    

def get_change(m):
    # print (a)
    # exit(0)
    for i in range(5,m + 1):
        pass
    return a[m + 1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    a = [(int)(1e4)] * (int)(1e3 + 5)
    fill(a)
    print(a[m])
    # print(a)
    # for x in range(20):
    #     print()
    # print(get_change(m))

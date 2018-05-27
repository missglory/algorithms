# Uses python3
import sys
def evalt(a, b, op):
    # print(a,b,op)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

cout = sys.stdout.write
width = 15
digits = []
ops = []
mins, maxs = [[0] * width for x in range(width)], [[0] * width for x in range(width)]

def print_arr(arr, width = None):
    if width is None: width = len(arr)
    # for x in arr:
    #     for y in x:
    #         sys.stdout.write(str(y) + '\t')
    for i in range(width):
        for j in range(width):
            sys.stdout.write(str(arr[i][j]) + '\t')
        sys.stdout.write('\n\n\n')

def print_arr(*args): pass

def preinit(width):
    for i in range(width):
        maxs[i][i] =  digits[i]
    for i in range(1, width):
        maxs[i-1][i] = evalt(digits[i-1], digits[i], ops[i-1])
    for i, o in enumerate(maxs):
        mins[i] = o[:]

def minmax(i,j):
    i1, j1, i2, j2, iop = i, i, i + 1, j, i
    minv = (int)(2e9)
    maxv = (int)(-2e9)
    while j1 < j:
        # print(i1, j1, i2, j2, ops[iop])
        e1 = evalt(mins[i1][j1], mins[i2][j2], ops[iop])
        e2 = evalt(mins[i1][j1], maxs[i2][j2], ops[iop])
        e3 = evalt(maxs[i1][j1], mins[i2][j2], ops[iop])
        e4 = evalt(maxs[i1][j1], maxs[i2][j2], ops[iop])
        minv = min(minv, e1, e2, e3, e4)
        maxv = max(maxv, e1, e2, e3, e4)
        j1 += 1
        i2 += 1
        iop += 1
    return minv, maxv



def init(width):
    jj = 2
    for j in range(jj, width):
        i = 0
        while i < width and j < width:
            mins[i][j], maxs[i][j] = minmax(i,j)
            i += 1
            j += 1
        
    
             


def get_maximum_value(dataset):
    #write your code here
    return 0


if __name__ == "__main__":
    unparsed = input()
    for i in range(len(unparsed)):
        if i % 2 == 0:
            digits.append(int(unparsed[i]))
        else:
            ops.append(unparsed[i])
    # print("D", digits)
    # print("ops", ops)
    w = len(digits)
    preinit(w)
    init(len(digits))
    print_arr(mins,w)
    print(maxs[0][w-1])
    print_arr(maxs,w)
    # print(minmax(0,2))

    # print(get_maximum_value())

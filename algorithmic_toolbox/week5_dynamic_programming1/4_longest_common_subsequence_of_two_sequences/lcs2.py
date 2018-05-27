import sys
leng = 12
arr = [[i] + [(int)(900)] * leng for i in range(leng)]
arr[0] = [i for i in range(leng)]

def edit_distance(s, t):
    for i in range(1,len(s) + 1):
        for j in range(1,len(t) + 1):
            if (s[i - 1] == t[j - 1]):
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + 1
    # for x in arr:
    #     for y in x:
    #         sys.stdout.write(str(y) + '\t')
    #     sys.stdout.write("\n")
    return arr[len(s)][len(t)]

def lcs2(s,t):
    i = len(s)
    j = len(t)
    lcs1 = []
    while i > 0 and j > 0:
        # print(i,j,arr[i][j], arr[i-1][j-1])
        if arr[i][j] == arr[i-1][j-1]:
            i -= 1
            j -= 1
            lcs1.append(s[i])
            continue
        if arr[i][j] == arr[i-1][j] + 1:
            i -= 1
            continue
        if arr[i][j] == arr[i][j-1] + 1:
            j -= 1
            continue
        if i > 1 and j > 1: raise Exception(i, j)
    return list(reversed(lcs1))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    s = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    t = data[:m]
    edit_distance(s,t)
    # for x in a:
    #     for y in x:
    #         sys.stdout.write(str(y) + '\t')
    #     sys.stdout.write('\n')
    print(len(lcs2(s,t)))

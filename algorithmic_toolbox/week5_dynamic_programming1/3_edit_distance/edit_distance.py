# Uses python3
import sys

leng = 122

a = [[i] + [(int)(9)] * leng for i in range(leng)]
a[0] = [i for i in range(leng)]




def edit_distance(s, t):
    for i in range(1,len(s) + 1):
        for j in range(1,len(t) + 1):
            if (s[i - 1] == t[j - 1]):
                a[i][j] = a[i-1][j-1]
            else:
                a[i][j] = min(a[i-1][j], a[i][j-1], a[i-1][j-1]) + 1
    # for x in a:
    #     for y in x:
    #         sys.stdout.write(str(y) + '\t')
    #     sys.stdout.write("\n")
    return a[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

# Uses python3
import sys

def optimal_sequence(n):
    s = [(int)(1e9)] * (int)(1e6 + 5)
    s[1:4] = [0,1,1]
    for i in range(4, n + 1):
        if (i % 3 == 0): s[i] = min(s[i], s[i//3])
        if (i % 2 == 0): s[i] = min(s[i], s[i//2])
        s[i] = min(s[i], s[i-1]) + 1
    return s

def backtrace(n,s):
    i = n
    seq = [i]
    while i > 1 and len(seq) < s[n]:
        # print(i, s[i], s[i - 1], s[i//2] if i % 2 == 0 else '-', s[i//3] if i % 3 == 0 else '-')
        # print(i)
        if (i % 2 == 0 and s[i] == s[i//2] + 1):
            i //= 2
            seq.append(i)
            continue
        if (i % 3 == 0 and s[i] == s[i//3] + 1):
            i //= 3
            seq.append(i)
            continue
        if s[i] == s[i-1] + 1:
            i -= 1
            seq.append(i)
    seq.append(1)
    return list(reversed(seq))

# input = sys.stdin.read()
# n = int(input)
n = int(input())
s = optimal_sequence(n)
print(s[n])
seq = backtrace(n,s)
for x in seq:
    sys.stdout.write(str(x) + ' ')

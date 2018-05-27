# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

a.sort()
result = a[n - 1] * a[n - 2]
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

print(result)

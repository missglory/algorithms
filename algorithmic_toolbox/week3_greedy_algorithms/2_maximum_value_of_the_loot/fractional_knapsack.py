# Uses python3
import sys

def get_optimal_value(capacity, inf):
    value = 0.
    # write your code here
    for o in inf:
        if capacity <= 1e-5:
            return value
        if o[2] < capacity - 1e-5:
            capacity -= o[2]
            value += o[1]
        else:
            value += o[1] * capacity / o[2]
            capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    ratio = [v/w for (v,w) in zip(values, weights)]
    inf = [[r,v,w] for (r,v,w) in zip (ratio, values, weights)]
    inf.sort(key = lambda x: x[0], reverse = True)
    # print (inf)
    opt_value = get_optimal_value(capacity, inf)
    print("{:.10f}".format(opt_value))

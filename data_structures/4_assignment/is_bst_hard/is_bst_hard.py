#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

f = False

def in_order(node, tree, ans, mn, mx):
  global f
  lc = not node[1] == -1 and node[0] <= tree[node[1]][0] 
  rc = not node[2] == -1 and node[0] > tree[node[2]][0]
  if node[0] >= mx or node[0] < mn or lc or rc:
    ans = []
    f = True
    return f
  if not node[1] == -1:
    in_order(tree[node[1]], tree, ans, mn, node[0])
  ans.append(node)
  if not node[2] == -1:
    in_order(tree[node[2]], tree, ans, node[0], mx)
  return f

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  ans = []
  if not len(tree): return True
  check = in_order(tree[0], tree, ans, -2**32, 2**32)
  if check:
    return False
  for i in range(1, len(ans)):
    if ans[i-1][0] > ans[i][0]:
      return False
  return True

# sys.stdout.write( '')


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

# if __name__=='__main__':
#   sys.stdin = open(r'C:\Users\Admin\Desktop\crsra\4_assignment\is_bst_hard\test\ts')
#   main()
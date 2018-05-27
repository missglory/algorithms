# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.depth = [0] * self.n
                self.children = [[] for i in range(self.n)]
                self.used = [False] * self.n
                for i in range(self.n):
                        if self.parent[i] == -1: continue
                        self.children[self.parent[i]].append(i)
                self.d = 0

        def compute_height(self, x, d):
                # Replace this code with a faster implementation
                # maxHeight = 0
                # for vertex in range(self.n):
                #         height = 0
                #         i = vertex
                #         while i != -1:
                #                 height += 1
                #                 i = self.parent[i]
                #         maxHeight = max(maxHeight, height);
                # return maxHeight;
                self.d = max(d, self.d)
                for i in self.children[x]:
                        if not self.used[i]:
                                self.used[i] = True
                                self.compute_height(i, d + 1)
                return self.d + 1

                

def main():
  tree = TreeHeight()
  tree.read()
  root = tree.parent.index(-1)
  print(tree.compute_height(root, 0))

threading.Thread(target=main).start()

# if __name__=='__main__':
#         sys.stdin = open(r'C:\Users\Admin\Desktop\crsra\1_assignment\tree_height\tests\01')
#         main()
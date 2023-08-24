import sys
input = sys.stdin.readline

class Trie:
    head = dict()

    def add(self, txts):
        root = self.head
        for i in txts:
            if i in root:
                pass
            else:
                root[i] = dict()
            root = root[i]
        root[0] = True

    def dfs(dep, root):
        if 0 in root:
            return

        curs = sorted(root)
        for cur in curs:
            print("--" * dep,end='')
            print(cur)
            Trie.dfs(dep+1,root[cur])

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        ob = Trie()
        ob.add(input().split()[1:])

    Trie.dfs(0, Trie.head)

import sys
input = sys.stdin.readline

def solve(root, start, end):
    for i in range(start,end):
        if inorder[i] == preorder[root]:
            solve(root + 1,start,i) #left
            solve(root + i + 1 - start, i + 1, end) #right
            print(preorder[root], end= " ")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        preorder = list(map(int,input().split()))
        inorder = list(map(int,input().split()))
        solve(0,0,n)
        print()

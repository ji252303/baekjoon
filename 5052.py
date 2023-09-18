import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    num = []
    for _ in range(n):
        num.append(sys.stdin.readline().rstrip())

    num.sort()

    answer = True
    for i in range(len(num)-1):
        if num[i] == num[i+1][:len(num[i])]:
            answer = False
            break

    if answer:
        print("YES")
    else:
        print("NO")


#트라이를 활용한 풀이

import sys
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.child = [None for _ in range(10)]
        self.check = False #해당 노드를 마지막으로 끝나는 문자열이 있는지


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, phone):
        tmp = self.root
        for i in phone:
            if tmp.child[i] != None:  # 비어있지 않으면
                tmp = tmp.child[i]
            else:
                new = Node(i)
                tmp.child[i] = new
                tmp = new
        tmp.check = True

    def consistency(self, phone):
        tmp = self.root
        for i in range(len(phone)):
            if tmp.check:  # 다른 문자열을 포함하고 있다면
                return False
            tmp = tmp.child[phone[i]]
        return True


for _ in range(int(input())):
    n = int(input())
    phone_list = []
    trie = Trie()

    for _ in range(n):
        phone = list(map(int, input().split()))
        trie.insert(phone)
        phone_list.append(phone)
    result = True

    for p in phone_list:
        result *= trie.consistency(p)

    if result:
        print("YES")
    else:
        print("NO")


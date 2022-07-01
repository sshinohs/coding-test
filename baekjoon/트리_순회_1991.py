import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


# print(tree)

def preorder(tree, now):
    print(now, end='')
    if tree[now][0] != '.':
        preorder(tree, tree[now][0])
    if tree[now][1] != '.':
        preorder(tree, tree[now][1])

def inorder(tree, now):
    if tree[now][0] != '.':
        inorder(tree, tree[now][0])
    print(now, end='')
    if tree[now][1] != '.':
        inorder(tree, tree[now][1])

def postorder(tree, now):
    if tree[now][0] != '.':
        postorder(tree, tree[now][0])
    if tree[now][1] != '.':
        postorder(tree, tree[now][1])
    print(now, end='')

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
print()
import sys
from collections import deque

input = sys.stdin.readline

N, K = int(input().split())

def bfs(st):
    q = deque()
    
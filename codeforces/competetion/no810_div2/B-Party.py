# ## by hsh8086

# import sys
# input = lambda: sys.stdin.readline().rstrip()
 
# inf = float('inf')
 
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = [0] + list(map(int, input().split()))
 
#     li = [[] for _ in range(n + 1)]
#     for _ in range(m):
#         u, v = map(int, input().split())
#         li[u].append(v)
#         li[v].append(u)
    
#     if m % 2 == 0:
#         print(0)
#     else:
#         evens = set()
#         t1 = inf
#         for i in range(1, n + 1):
#             if len(li[i]) % 2 == 1:
#                 t1 = min(t1, a[i])
#             else:
#                 evens.add(i)
 
#         t2 = inf
#         for i in range(1, n + 1):
#             if i not in evens:
#                 continue
#             for v in li[i]:
#                 if v in evens:
#                     t2 = min(t2, a[i] + a[v])
 
#         print(min(t1, t2))


## by swoon

# import sys
 
# R = lambda : sys.stdin.readline()
# MIS = lambda : map(int, R().split())
 
# for _ in range(int(R())):
#     N, M = MIS()
#     L = [0] + list(MIS())
#     cnt = [0]*(N+1)
#     adj = [[] for _ in range(N+1)]
#     for _ in range(M):
#         x, y = MIS()
#         cnt[x] += 1
#         cnt[y] += 1
#         adj[x].append(y)
#         adj[y].append(x)
#     if M%2 == 0:
#         print(0)
#         continue
#     ans = 1323122311221213
#     for i in range(1, N+1):
#         if cnt[i]&1:
#             ans = min(ans, L[i])
#         else:
#             for j in adj[i]:
#                 if cnt[j]%2 == 0:
#                     ans = min(ans, L[i]+L[j])
#     print(ans)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = list(map(int, input().split()))

board = [0] + board


# board_forward = []
# board_backward = []

cumul_forward = [0]
cumul_backward = [0]

for a, b in zip(board[:-1], board[1:]):
    if a - b < 0:
        # board_backward.append(b - a)
        # board_forward.append(0)
        cumul_backward.append(cumul_backward[-1] + b - a)
        cumul_forward.append(cumul_forward[-1])
    else:
        # board_backward.append(0)
        # board_forward.append(a - b)
        cumul_backward.append(cumul_backward[-1])
        cumul_forward.append(cumul_forward[-1] + a - b)

# print(board_forward)
# print(board_backward)

# print('$$')
# print(cumul_forward)
# print(cumul_backward)




# print(board_forward)

for _ in range(m):
    st, ed = map(int, input().split())

    if st < ed:
        print(cumul_forward[ed] - cumul_forward[st])
        # print(sum(board_forward[st:ed]))
    else:
        print(cumul_backward[st] - cumul_backward[ed])
        # print(sum(board_backward[ed:st]))
        # print(board_forward[ed:st])
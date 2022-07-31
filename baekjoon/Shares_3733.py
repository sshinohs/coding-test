import sys
# input = sys.stdin.readline



while True:
    try:
        N, S = map(int, input().split())
    except EOFError:
        break
    else:
        print(S//(N+1))
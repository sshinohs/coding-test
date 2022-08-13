def solution(n, k):
    k_number = decimal_to_k(n, k)
    k_number.append(0)
    print(k_number)
    count = 0
    check = 0
    pool = []
    for i in range(len(k_number)):
        if k_number[i] == 0:
            if len(pool) > 0:
                num = k_direct_decimal(pool, k)
                prime_arr = search_prime(num)
                pool = []
                if is_prime(prime_arr, num):
                    count += 1
        elif k_number[i] != 0:
            pool.append(k_number[i])
    
    return count

def decimal_to_k(n, k):
    arr = []
    while(n//k>0):
        arr.append(n%k)
        n //= k
    arr.append(n)
    return arr[::-1]

def k_direct_decimal(n, k):
    answer = int("".join(map(str,n)))
    return answer

            
def is_prime(prime_arr, num):
    for prime in prime_arr:
        if num == prime:
            return True
    return False

def search_prime(n):
    limit = limit_for_prime(n)
    board = [True for i in range(n+1)]
    board[0] = False
    board[1] = False
    
    for i in range(2, limit):
        if board[i] != False:
            count = 2
            while i * count <= n:
                board[i * count] = False
                count += 1
    
    prime_arr = []
    for i, val in enumerate(board):
        if val == True:
            prime_arr.append(i)
    return prime_arr

    
def limit_for_prime(n):
    count = 1
    while n >= count ** 2:
        count += 1
    return count
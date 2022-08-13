def comparison(a, b, n):
    if ord(a[n])<ord(b[n]):
        return True
    elif ord(a[n])>ord(b[n]):
        return False
    else:
        return comparison2(a, b, 0)

def comparison2(a, b, n):
    if ord(a[n])<ord(b[n]):
        return True
    elif ord(a[n])>ord(b[n]):
        return False
    else:
        if n == len(a) - 1:
            return True
        elif n == len(b) -1:
            return False
        else:
            return comparison2(a, b, n+1)
        
def quick_sort(arr, st, ed, n):
    if st >= ed:
        return
    pivot = st
    left = st + 1
    right = ed
    while left <= right:
        while left <= ed and comparison(arr[left], arr[pivot], n):
            left += 1
        while right >= st+1 and comparison(arr[pivot], arr[right], n):
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, st, right-1, n)
    quick_sort(arr, right+1, ed, n)
    




if __name__=="__main__":

    # strings = ["abce", "abcd", "cdx"]
    # n = 2
    strings = ["sun", "bed", "car"]
    n = 1

    st = 0
    ed = len(strings)-1
    quick_sort(strings, st, ed, n)
    print(strings)
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr1 = list(arr)
    j=k=x=0
    value = []
    for i in range(min(arr), max(arr)):
        if i in arr:
            if i!=max(arr):
                value = value + [i]
    result = max(value)
    print(result)
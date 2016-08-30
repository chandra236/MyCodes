def fun(arr,val):
    n = len(arr)
    i = 0
    j = n - 1
    while i < j:
        d = arr[i] - arr[j]
        d1 = arr[j] - arr[i]
        if val == d:

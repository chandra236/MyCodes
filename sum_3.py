def fun(arr, val):
    #print arr
    arr.sort()
    n = len(arr)
    n1 = n-2
    i = 0
    sum = 0
    while i <= n1:
        j = i + 1
        k = n - 1
        while j <= k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == val:
                print a[i],a[j],a[k]
                j += 1
                k -= 1
            elif sum > val:
                k -= 1
            elif sum < val:
                j += 1
        i += 1
if __name__ == '__main__':
    a = [800,100,100,700,200,900,0]
    fun(a, 1000)

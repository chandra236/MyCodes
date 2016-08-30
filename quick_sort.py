def q_sort(arr, l, r):
    if l < r:
        m = partition(arr, l, r)
        q_sort(arr, l, m-1)
        q_sort(arr, m+1, r)


def partition(arr, l, r):
    pivote = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

if __name__ == '__main__':
    a = [10,3,7,1,0]
    print a
    q_sort(a, 0, len(a)-1)
    print a
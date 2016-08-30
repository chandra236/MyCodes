def height(n):
    if n == 0:
        return 0
    print 1 + height(n-1)

if __name__ == '__main__':
    height(10)
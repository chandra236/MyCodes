def fun(str):
    j = 0
    count = 0
    for i in xrange(len(str)):
        while str[i] == str[i + 1]:
            count += 1
        str[j] = str[i]
        str[j + 1] = count
        j += 2
    print str

if __name__ == '__main__':
    str = raw_input("Enter the string: \n")
    fun(str)
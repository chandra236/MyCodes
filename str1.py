def fun(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 == n1:
        d1 = dict()
        d2 = dict()
        for i in str1:
            if i in d1:
                d1[i] = d1[i] + 1
            else:
                d1[i] = 1

        for j in str2:
            if j in d2:
                d2[j] = d2[j] + 1
            else:
                d2[j] = 1
        for k in d1:
            if k in d2 and d1[k] == d2[k]:
                pass
            else:
                return 'No'
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    print fun('abab','baba')


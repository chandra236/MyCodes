def create_stack():
    return []


def push(s, val):
    s.append(val)


def pop(s):
    return s.pop()


def is_empty(s):
    return s == []


def top(s):
    return s[len(s)-1]


def sort(s1, s2):
    push(s2, s1.pop())
    while not (is_empty(s1)):
        t = pop(s1)
        while not is_empty(s2) and t < top(s2):
            push(s1, pop(s2))
        push(s2, t)

if __name__ == '__main__':
    s1 = create_stack()
    s2 = create_stack()
    push(s1, 10)
    push(s1, 1)
    push(s1, 3)

    sort(s1, s2)

    print s1
    print s2
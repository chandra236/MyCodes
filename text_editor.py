a = ''                                  # Global String initially empty
gl = []                                 # Utility Stack to be used for undo


# Below function will be used for append operation
def append(string, flag):
    global a, gl
    a = a + string
    # Check if append is called by undo or by user.
    # If used by user log the changes in to stack
    if not flag:
        gl.append([string, 'add'])


# Below function will be used for delete operation
def delete(n, flag):
    n = int(n)
    global a, gl
    # Check if delete is called by undo or by user.
    # If used by user log the changes in to stack
    if not flag:
        gl.append([a[len(a) - n:], 'del'])
    a = a[:len(a) - n]


# Below function will be used for print operation
def print_str(n1):
    n = int(n1)
    if len(a) >= n:
        print a[n-1]
    else:
        print 'Given index does not exist in string!'


# Below function takes care of undo operation
def undo():
    if len(gl):
        uo = gl.pop()
        # Get the last change done by user from stack and revert
        if uo[1] == 'add':
            delete(len(uo[0]), 1)
        elif uo[1] == 'del':
            append(uo[0], 1)
    else:
        print 'No undo possible!'
        

if __name__ == '__main__':
    n = int(raw_input())               # Enter number of operations
    for i in xrange(n):
        v = raw_input()    # Enter the operation no. i
        if v.startswith('4'):
            undo()
        else:
            op, val = v[0], v[1:].strip()
            if op == '1':
                append(val, 0)
            elif op == '2':
                delete(val, 0)
            elif op == '3':
                print_str(val)
            else:
                print 'Wrong operation!'

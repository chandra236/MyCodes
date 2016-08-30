
class TextEditor:
    def __init__(self):
        self.a = ''         # Global String initially empty
        self.gl = []        # Utility Stack to be used for undo

    # Below function will be used for append operation
    def append(self, string, flag):
        self.a = self.a + string
        # Check if append is called by undo or by user.
        # If used by user log the changes in to stack
        if not flag:
            self.gl.append([string, 'add'])

    # Below function will be used for delete operation
    def delete(self, n, flag):
        n = int(n)
        # Check if delete is called by undo or by user.
        # If used by user log the changes to global list
        if not flag:
            self.gl.append([self.a[len(self.a) - n:], 'del'])
        self.a = self.a[:len(self.a) - n]                       # Delete the last n no of characters of string

    # Below function will be used for print operation
    def print_str(self, n):
        n = int(n)
        if len(self.a) >= n:
            print self.a[n - 1]
        else:
            print 'Given index does not exist in string!'

    # Below function takes care of undo operation
    def undo(self):
        if len(self.gl):
            uo = self.gl.pop()
            # Get the last change done by user from stack and revert
            if uo[1] == 'add':
                self.delete(len(uo[0]), 1)
            elif uo[1] == 'del':
                self.append(uo[0], 1)
        else:
            print 'No undo possible!'


if __name__ == '__main__':
    t_editor = TextEditor()
    n = int(raw_input())    # Enter number of operations
    for i in xrange(n):     # Loop from 0 to n-1
        v = raw_input()     # Enter the operation no. i
        if v.startswith('4'):
            t_editor.undo()
        else:
            op, val = v[0], v[1:].strip()
            if op == '1':
                t_editor.append(val, 0)
            elif op == '2':
                t_editor.delete(val, 0)
            elif op == '3':
                t_editor.print_str(val)
            else:
                print 'Wrong operation!'

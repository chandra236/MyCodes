class Node:

    def __init__(self):
        self.val = None
        self.next = None

    def set_val(self, val):
        self.val = val

    def set_next(self, node):
        self.next = node


class Llist:

    def __init__(self):
        self.head = None

    def add_node(self,val):
        n = Node()
        n.val = val
        if self.head:
            n.next = self.head
            self.head = n
        else:
            n.next = None
            self.head = n

    def get_len(self):
        count = 0
        s = self.head
        while s:
            count += 1
            s = s.next
        return count

    def print_list(self):
        s = self.head
        s1 = ''
        while s is not None:
            s1 += ',' + str(s.val)
            s = s.next
        print s1[1:]

    def reverse(self):
        curr = self.head
        nex = None
        while curr.next is not None:
            prev = curr.next
            curr.next = nex
            nex = curr
            curr = prev
        curr.next = nex
        self.head = curr

if __name__ == '__main__':
    l = Llist()
    l.add_node(5)
    l.add_node(10)
    l.add_node(13)
    l.add_node(22)
    l.print_list()
    l.reverse()
    l.print_list()


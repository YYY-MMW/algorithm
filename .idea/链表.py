from _ctypes import PyObj_FromPtr

class Node:
    def __init__(self,num):
        self.ele = num
        self.next = None

class link:
    def __init__(self,Node=None):
        self.head = Node

    def is_empty(self):
        return self.head==None

    def length(self):
        tmp = 0
        cur = self.head
        while cur!=None:
            tmp+=1
            cur = cur.next
        return tmp

    def travel(self):
        cur = self.head
        while cur !=None:
            print(cur.ele)
            cur = cur.next

    def find(self,pos):
        assert 0 <= pos < self.length()
        cur = self.head
        step = 0
        while step<=pos:
            cur = cur.next
            step+=1
        return cur.ele

    def add(self,pos,node):
        cur = self.head
        step = 0
        assert (pos>=0 and pos<=self.length())
        if pos != 0:
            while step < pos-1:
                cur = cur.next
                step += 1
            help = cur.next
            cur.next = node
            node.next = help
        else:
            help = self.head
            self.head = node
            node.next = help
    #链表中点
    def mid(self):
        n_1 = self.head
        n_2 = self.head
        while n_2.next!=None and n_2.next.next!=None:
            n_1 = n_1.next
            n_2 = n_2.next.next
        return n_1

'''
a = Node(1)
b = Node(2)
a.next = b
c = Node(3)
link = link(a)
link.travel()
link.add(1,c)
link.travel()
len = link.length()
tmp = link.find(0)
'''


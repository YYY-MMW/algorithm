class Node:
    def __init__(self,ele):
        self.num = ele
        self.next = None

class Link:
    def __init__(self,node = None):
        self.head = node

    def length(self):
        n_1 = self.head
        count = 0
        while n_1!=None:
            count+=1
            n_1 = n_1.next
        return count

    def add(self,pos,node):
        assert pos>=0 and pos<self.length()
        cur = self.head
        if pos ==0 :
            node.next = self.head
            self.head = node
        else:
            for _ in range(pos-1):
                cur = cur.next
        cur.next,node.next = node,cur.next

    def append(self,node):
        cur = self.head
        if cur == None:
            self.head = node
        else:
            while cur.next !=None:
                cur = cur.next
            cur.next = node

    def mid(self):
        n_1 = self.head
        n_2 = self.head
        while n_2.next!=None and n_2.next.next!=None:
            n_1 = n_1.next
            n_2 = n_2.next.next
        return n_1


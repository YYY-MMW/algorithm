from 链表 import *
def easy_link(arr):
    link_arr = Link()
    for i in arr:
        link_arr.append(Node(i))
    return link_arr

def check_Palindrome(link):
    mid = link.mid()
    help = []
    n_1 = link.head
    n_2 = mid.next
    while n_2!=None:
        help.append(n_2)
        n_2 = n_2.next
    while help!=[]:
        if n_1.num != help.pop().num:
            return False
        n_1 = n_1.next
    return True

a = [1,2,3,2,1]
link_a = easy_link(a)
out = check_Palindrome(link_a)
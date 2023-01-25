from 链表 import *
from collections import deque
#根据输入数组生成链表数据结构
def easy_lind(arr):
    Link = link()
    for i in range(len(arr)):
        Link.add(i,Node(arr[i]))
    return Link

#链表回文判断
def check_Palindrome(Link):
    mid = Link.mid()
    n_1 = Link.head
    n_2 = mid.next
    help = []
    while n_2!=None:
        help.append(n_2)
        n_2 = n_2.next
    while help!=[]:
        if n_1.ele != help.pop().ele:
            return False
        n_1 = n_1.next
    return True


a = [1,2,3,2,1,1]
link_a = easy_lind(a)
out = check_Palindrome(link_a)
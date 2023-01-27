#队列
from collections import deque

class TreeNode():#二叉树节点
    def __init__(self,val,lchild=None,rchild=None):
        self.val=val		#二叉树的节点值
        self.lchild=lchild		#左孩子
        self.rchild=rchild		#右孩子

#构建二叉树
node_7 = TreeNode(7)
node_8 = TreeNode(8)
node_6 = TreeNode(6)
node_5 = TreeNode(5)
node_4 = TreeNode(4,node_7,node_8)
node_3 = TreeNode(3,node_6)
node_2 = TreeNode(2,node_4,node_5)
node_1 = TreeNode(1,node_2,node_3)

#递归遍历
def PreOrderRecur(head):
    if head == None:
        return
    #print(head.val) #先序遍历
    PreOrderRecur(head.lchild)
    #print(head.val)  # 中序遍历
    PreOrderRecur(head.rchild)
    # print(head.val)  # 后序遍历

#非递归遍历
class Recur:
    def __init__(self,head=None):
        self.head = head

    def PreOrderunRecur(self):
        print('先序遍历：')
        help = []
        help.append(self.head)
        while help!=[]:
            tmp = help.pop()
            print(tmp.val)
            if tmp.rchild !=None:
                help.append(tmp.rchild)
            if tmp.lchild != None:
                help.append(tmp.lchild)

    def InorderunRecur(self):
        print('中序遍历：')
        help = []
        head = self.head
        while help!=[] or head!=None:
            if head !=None:
                help.append(head)
                head = head.lchild
            else:
                tmp = help.pop()
                print(tmp.val)
                head = tmp.rchild

    def PosOrderunRecur(self):
        print('后序遍历：')
        help = []
        help_2 = []
        help.append(self.head)
        while help!=[]:
            tmp = help.pop()
            help_2.append(tmp)
            if tmp.lchild !=None:
                help.append(tmp.lchild)
            if tmp.rchild != None:
                help.append(tmp.rchild)
        while help_2 !=[]:
            print(help_2.pop().val)

    def isBST(self):
        help = []
        head = self.head
        if head==None:
            return True
        preVal = -1
        while help != [] or head != None:
            if head != None:
                help.append(head)
                head = head.lchild
            else:
                tmp = help.pop()
                if tmp.val<=preVal:
                    return False
                preVal = tmp.val
                head = tmp.rchild


#队列
class BFS:
    def __init__(self,head):
        self.head = head
    def bfs(self):
        print('宽度优先遍历')
        help = deque([])
        help.append(self.head)
        while help != deque([]):
            tmp = help.popleft()
            print(tmp.val)
            if tmp.lchild !=None:
                help.append(tmp.lchild)
            if tmp.rchild !=None:
                help.append(tmp.rchild)
    #是否完全二叉树
    def isFULL(self):
        isEmpty = False
        help = deque([])
        help.append(self.head)
        while help != deque([]):
            tmp = help.popleft()
            if tmp.lchild ==None and tmp.rchild!=None:
                return False
            if tmp.lchild !=None and tmp.rchild==None:
                isEmpty = True
                help.append(tmp.lchild)
            if tmp.lchild !=None or tmp.rchild!=None:
                help.append(tmp.lchild)
                help.append(tmp.rchild)
            if isEmpty and(tmp.lchild !=None or tmp.rchild!=None):
                return False

#宽度优先遍历
B = BFS(node_1)
out = B.isFULL()


from functools import cmp_to_key
import heapq
'''
返回负数的时候，o1排在前面
返回正数的时候，o2排在前面
等于0时，谁排在前面无所谓
'''

#比较器，重载sorted函数
l = [2,5,4,7]
sorted(l,key=cmp_to_key(lambda a,b:a-b))#由大到小，b-a由小到大

#heapq模块使用
heap = []
for i in l:
    heapq.heappush(heap,i)  #连续加入新数据构建小顶堆
heapq.heapify(l)    #一次输入所有构建小顶堆
#利用堆进行排序
for _ in range(len(l)):
    None
    #print(heapq.heappop(l))     #heappop弹出会重新构建堆

#heapq本身不支持自定义比较器，重写数据lt方法实现
class P:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
            if other.a<self.a:
                return True

p_1 = P(2)
p_2 = P(5)
p_3 = P(4)
p_4 = P(7)
l = [p_1,p_2,p_3,p_4]
heapq.heapify(l)    #大顶堆实现
print(l[0].a)



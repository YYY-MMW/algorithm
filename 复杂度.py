import random
#交换两个数 空间复杂度0
def change(a,b):
    b = b+256+5
    a = a^b
    b = a^b
    a = a^b
    return a,b-261

class find_Odd():
    def generate(self,Odd):
        len = random.randint(3,500)//2*2+1  #奇数长度
        ar = [0]*len
        Odd_times = random.randint(1,len+1)//2*2-1
        for i in range(Odd_times):
            ar[i] = Odd
        for i in range(Odd_times,len,2):
            ar[i] = ar[i+1] = random.randint(0,10)
        random.shuffle(ar)
        return ar

    def find_One(self,ar):
        er = 0
        for i in ar:
            er = er^i
        return er

    def find_Two(self,ar):
        er_1 = 0
        er_2 = 0
        for i in ar:
            er_1 = er_1^i
        right_One = er_1&(~er_1+1)  #最右侧位为1
        for i in ar:
            if i&right_One:
                er_2 = er_2^i
        return er_1^er_2,er_2
'''
find = find_Odd()
ar = find.generate(5)
ar.extend(find.generate(6))
a,b = find.find_Two(ar)
'''
class sort():
    def generate(self):
        len = random.randint(1,10)
        ar = [0]*len
        for i in range(len):
            ar[i] = random.randint(0,10)
        random.shuffle(ar)
        return ar

    def insert_sorting(self,arr):
        ar = [i for i in arr]
        for i in range(1,len(ar)):
            for j in range(i-1,-1,-1):
                if ar[j+1]<ar[j]:
                    tmp = ar[j+1]
                    ar[j+1] = ar[j]
                    ar[j] = tmp
                else:break
        return ar

#归并排序
    def merge_sorting(self,arr,L,R):
        #ar = [i for i in arr]
        if L==R:
            return
        mid = L+((R-L)>>1)  #位运算
        self.merge_sorting(arr,L,mid)
        self.merge_sorting(arr,mid+1,R)
        self.merge(arr,L,mid,R)


    def merge(self,arr,L,mid,R):
        help = [0]*(R-L+1)
        p_1,p_2 = L,mid+1
        i = 0
        while(p_1<=mid and p_2<=R ):
            if arr[p_1]<=arr[p_2]:
                help[i] = arr[p_1]
                p_1+=1
                i+=1
            else:
                help[i] = arr[p_2]
                p_2+=1
                i+=1
        while p_1<=mid:
            help[i] = arr[p_1]
            i+=1
            p_1+=1
        while p_2<=R:
            help[i] = arr[p_2]
            p_2+=1
            i+=1
        for i in range(R-L+1):
            arr[i+L] = help[i]



sor = sort()
arr = sor.generate()
arr = [1,3,2,2,1]
ran = sor.merge_sorting(arr,0,len(arr)-1)

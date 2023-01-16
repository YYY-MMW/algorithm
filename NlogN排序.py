import random
#归并排序并求出逆序对
class merge_sorting:
    def __init__(self):
        self.num = 0

    def sorting(self,ar,L,R):
        if L==R:
            return
        mid = L+((R-L)>>1)
        self.sorting(ar,L,mid)
        self.sorting(ar,mid+1,R)
        self.merge(ar,L,mid,R)

    def merge(self,ar,L,mid,R):
        p_1,p_2,i = L,mid+1,0
        help = [0]*(R-L+1)
        while (p_1<=mid and p_2<=R):
            if ar[p_1]>ar[p_2]:
                help[i] = ar[p_1]
                i+=1
                p_1+=1
                self.num+=R-p_2+1
            else:
                help[i] = ar[p_2]
                i += 1
                p_2 += 1
        while p_1<=mid:
            help[i] = ar[p_1]
            p_1+=1
            i+=1
        while p_2<=R:
            help[i] = ar[p_2]
            i+=1
            p_2+=1
        for i in range(R-L+1):
            ar[L+i] = help[i]

#快速排序
class quick_sorting:
    def sorting(self,arr,L,R):
        if L<R:
            p = self.partiton(arr,L,R)
            self.sorting(arr,L,p[0]-1)
            self.sorting(arr,p[0] + 1,R)
    def partiton(self,arr,L,R):
        less = L-1  #小于部分指针
        more = R
        while L<more:
            if arr[L]<arr[R]:
                help = arr[less+1]
                arr[less+1] = arr[L]
                arr[L] = help
                less+=1
                L+=1
            elif arr[L]>arr[R]:
                help = arr[L]
                arr[L] = arr[more-1]
                arr[more-1] = help
                more-=1
            else:
                L+=1
        help = arr[R]
        arr[R] = arr[more]
        arr[more] = help
        return [less+1,more]




arr = [1,3,2,2,1,8,3,9,5,48,6,5]
quick_sort = quick_sorting()
quick_sort.sorting(arr,0,11)

#归并排序
class merge:
    def __init__(self):
        None

    def sorting(self,L, R, arr):
        if L == R:
            return
        mid = L + ((R - L) >> 1)
        self.sorting(L, mid, arr)
        self.sorting(mid+1, R, arr)
        self.merge(L, mid, R, arr)

    def merge(self,L, mid, R, arr):
        p_1, p_2 = L, mid + 1
        i = 0
        help = [0] * (R - L + 1)
        while p_1 <= mid and p_2 <= R:
            if arr[p_1] <= arr[p_2]:
                help[i] = arr[p_1]
                i += 1
                p_1 += 1
            else:
                help[i] = arr[p_2]
                i += 1
                p_2 += 1
        while p_1 <= mid:
            help[i] = arr[p_1]
            p_1 += 1
            i += 1
        while p_2 <= R:
            help[i] = arr[p_2]
            p_2 += 1
            i += 1
        for i in range(R-L+1):
            arr[L+i] = help[i]

#找对大值，递归
def find_Max(arr,L,R):
    if L==R:
        return arr[L]
    mid = L+((R-L)>>1)
    left_max = find_Max(arr,L,mid)
    right_max = find_Max(arr,mid+1,R)
    return max(left_max,right_max)

#快速排序
class quick_sorting:
    def sorting(self,arr,L,R):
        if L<R:
            p = self.partition(arr,L,R)
            self.sorting(arr,L,p[0]-1)
            self.sorting(arr,p[1]+1,R)
    def partition(self,arr,L,R):
        less,more = L-1,R
        while L<more:
            if arr[L]<arr[R]:
                help = arr[L]
                arr[L] = arr[less+1]
                arr[less+1] = help
                less+=1
                L+=1
            elif arr[L]==arr[R]:
                L+=1
            else:
                help = arr[L]
                arr[L] = arr[more-1]
                arr[more-1] = help
                more-=1
        help = arr[R]
        arr[R] = arr[more]
        arr[more] = help
        return [less+1,more]

sor = quick_sorting()
b = [1,5,2,4]
sor.sorting(b,0,3)
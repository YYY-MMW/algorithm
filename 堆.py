#堆排序,时间复杂度NlogN
class heap:
    def heap_insert(self,arr,index):    #arr中index之前为堆结构
        while arr[index]>arr[int((index-1)/2)]:
            help = arr[index]
            arr[index] = arr[int((index-1)/2)]
            arr[int((index-1)/2)] = help
            index = int((index-1)/2)

    def heapify(self,arr,index,heap_size):  #arr堆，index新数据，heap_size堆大小，下一个加入数据索引
        left = index*2+1  #初始值
        while(left<heap_size   ):
            if left+1<heap_size and arr[left]<arr[left+1]:
                largest = index if arr[index]>=arr[left+1] else left+1
            else:
                largest = index if arr[index] >= arr[left ] else left
            if largest == index:
                break
            help = arr[index]
            arr[index] = arr[largest]
            arr[largest] = help
            index = largest
            left = index*2+1

    def heap_sorting(self,arr,heap_size):
        #初始化堆，O(N)
        for i in range(1,heap_size):
            self.heap_insert(arr,i)
        tick = heap_size
        #heapify
        while(tick>1):
            tick-=1
            help = arr[0]
            arr[0] = arr[tick]
            arr[tick] = help
            self.heapify(arr,0,tick)
'''
test = heap()
arr = [1,5,3,8,9,25,64,7]
test.heap_sorting(arr,len(arr))
'''


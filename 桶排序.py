#桶排序
class buket_sort:
    def __init__(self):
        None

    def getDigit(self,num,digit):
        return int((num%(10**digit)-num%(10**(digit-1)))/(10**(digit-1)))

    def radixSort(self,arr,digit):
        help = [0]*len(arr)
        for i in range(1,digit+1):  #进桶次数循环
            count = [0] * 10    #count置零
            #每个桶中个数
            for num in arr:
                count[self.getDigit(num,i)]+=1
            #每个桶小于等于个数
            for j in range(1,10):
                count[j]+=count[j-1]
            #从右往左遍历
            for j in range(len(arr)-1,-1,-1):
                tmp = self.getDigit(arr[j],i)
                help[count[tmp]-1] = arr[j]
                count[tmp]-=1
            for j in range(len(help)):
                arr[j] = help[j]

a = [1,5,7,8,9,5,20,548]
buket = buket_sort()
buket.radixSort(arr=a,digit=3)
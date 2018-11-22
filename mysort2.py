def selectionSort(alist):
    for i in range(len(alist)):
        least=i
        leastValue=alist[i]
        for k in range(i+1, len(alist)):
            if alist[k]<leastValue:
                least=k
                leastValue=alist[k]

        #tmp=alist[i]
        #alist[i]=alist[least]
        #alist[least]=tmp

        alist[i],alist[least]=alist[least],alist[i]

if __name__=="__main__":
    list1=[7,9,5,1,8]
    selectionSort(list1)
    print(list1)

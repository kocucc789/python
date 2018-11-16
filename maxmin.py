def mymax(mylist):
    max_value=mylist[0]
    for i in range(1,len(mylist)):
        if max_value<mylist[i]:
            max_value=mylist[i]
            
    return max_value


def mymin(mylist):
    min_value=mylist[0]
    for i in range(1,len(mylist)):
        if min_value>mylist[i]:
            min_value=mylist[i]
            
    return min_value


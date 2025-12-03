glist= ["togol", "folddyuy","faffst","staffb" ,"hideygud" ,"brag" ,"hilgl"]

def order_list(alist):
    new = []
    temp = []
    if len(alist) == 0:
        return []
    elif len(alist) == 2:
        return []
    else:
        for i in range(len(alist) - 1):
            for j in range(i + 1, len(alist)):
                if len(alist[i]) == len(alist[j]):
                    temp = [alist[i], alist[j]]
                    new.append(temp)
        return new
    
print(order_list(glist))
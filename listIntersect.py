def listIntersect1(lst1, lst2):
    dict2 = listtodict(lst2)
    outlst = []
    for i, x in enumerate(lst1):    # O(n)
        if int(dict2.get(x) or 0) > 0:
            dict2[x] -= 1
            outlst.append(x)
    return outlst

def listtodict(lst):
    outdict = {}
    for x in lst:
        if x in outdict:
            outdict[x] += 1
        else:
            outdict[x] = 1
    
    return outdict

l1 = [3, 2, 12, 4, 5, 5]
l2 = [3, 1, 5, 5, 5]

print(listIntersect1(l1, l2))

assert listIntersect1(l1, l2) == [3, 5, 5]

a = [2, 1, 3, 5, 3, 2]
n = len(a)
myset = dict()
for i in range(0,n):
    if a[i] in myset.keys():
        print (a[i])
        break
    else:
        myset[a[i]] = 1

def linearsearch(a,el):
    for i in range(len(a)):
       if a[i]==el:
        #print(f'{el} is found at index {i}')
        return
    #print('element not found')
    return -1
a=[12,3,14,22,56,75]
print(linearsearch(a,14))
def linearsearch(a,el):
    ar=[]
    for i in range(len(a)):
        if a[i]==el:
            #print(f'{el} is found at index {i}')
            ar.append(i)
     #print('element not found')       
    if len(ar)>0:
        return ar
    return -1
a=[12,3,14,22,56,75,14]
print(linearsearch(a,15))

b=[1,2,3,4,5,6,7,8]
binarysearch(b,6)
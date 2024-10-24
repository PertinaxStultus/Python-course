def listsum(lst):
    for i in range(1,len(lst)):
        lst[i] += lst[i-1]
        
        
list = [1,2,3,4]
listsum(list)
print(list)
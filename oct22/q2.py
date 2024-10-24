
def CubeList(lst):
    return[(i,i**3) for i in lst]

list = [4,3,5]
result = CubeList(list)
print(result)
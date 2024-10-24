numList = []

for num in range(2,10000):
    sum_divition = 0
    for i in range(1,num):
        if num % i ==0:
            sum_divition += i
            
    if sum_divition == num:
        numList.append(num)
        
print("perfect number to 10000 are: ",numList)
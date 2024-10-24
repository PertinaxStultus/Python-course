while True:
    num = int(input("enter a Number: "))

    if (num <= 0):
        break
    
    for i in range(1,11):
        output = i*num
        print(f"{i}*{num}={output}")
        
print()
    
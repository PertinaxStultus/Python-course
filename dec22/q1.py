lst=[]
while(True):
    num = eval(input("Enter number: "))
    if(num < 0):
        print(lst)
        number = eval(input("Enter one more number: "))
        if number in lst:
            lst.remove(number)
        else:
            lst.append(number)
        print(lst)
        break
    else:
        lst.append(num)

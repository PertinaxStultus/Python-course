import random

num_fokes= eval(input("Enter the number of persons: "))
Bdays = [random.randint(1,365) for _ in range(num_fokes)]
    
if len(Bdays) != len(set(Bdays)):
    print("more then two or more persons with the same birthdate")
else:
    print("No one has the same birthdate")
        

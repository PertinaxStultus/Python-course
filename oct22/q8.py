def fun(x):
    i = len(x)
    for t in range(i):
        if x[t]%10 != x[t]//10:
            x[t] = x[t]//10*10+x[t]
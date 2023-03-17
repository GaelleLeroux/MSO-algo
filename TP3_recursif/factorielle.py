def factorielle(n):
    if (n==0):
        return 1
    else :
        return n*factorielle(n-1)
    

u = factorielle(5)
print(u)
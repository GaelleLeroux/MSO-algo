import time


def fibonnacie1(n):
    if n==1 or n==0:
        return 1
    else :
        return(fibonnacie1(n-1)+fibonnacie1(n-2))
    
def fibonnacie2(liste,n):
    liste.append(liste[len(liste)-2]+liste[len(liste)-1])
    if n-2==0:
        return (liste[len(liste)-1])
    else:
        return(fibonnacie2(liste,n-1))
    
def fibonnacie3(F1,F2,n):
    if n-2==0:
        return (F1+F2)
    else:
        return fibonnacie3(F2,F1+F2,n-1)


print("test fibonnaci 1:")
test = [5,10,20,30]
for i in range(len(test)):
    tps1 = time.clock()
    u = fibonnacie1(test[i])
    tps2 = time.clock()
    print(u,tps2-tps1)
    
print("test fibonnaci 2:")
for i in range(len(test)):
    tps1 = time.clock()
    u = fibonnacie2([1,1],test[i])
    tps2 = time.clock()
    print(u,tps2-tps1)
    
print("test fibonnaci 3:")
for i in range(len(test)):
    tps1 = time.clock()
    u = fibonnacie3(1,1,test[i])
    tps2 = time.clock()
    print(u,tps2-tps1)
    

    


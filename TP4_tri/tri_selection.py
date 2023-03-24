

def TriSelection(liste):
    for i in range(len(liste)-1):
        min = i
        for j in range(i+1,len(liste)):
            if liste[j]<liste[i]:
                min = j
        if min!=i:
            liste[i],liste[min]=liste[min],liste[i]
    return liste


test = [17,11,33,25,48,18,6]
print(TriSelection(test))
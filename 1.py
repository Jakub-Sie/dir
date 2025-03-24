# 1. Liczenie wystąpień słów
# Napisz funkcję, która przyjmuje ciąg znaków i zwraca słownik, gdzie kluczami są
# słowa, a wartościami liczba ich wystąpień. Przykład: wejście: "kot pies kot
# mysz pies kot" wyjście: {"kot": 3, "pies": 2, "mysz": 1}

def zliczanie(stirg:str):
    dirt = {}
    L=stirg.split()
    for i in range(len(L)):
       
        if dirt.get(L[i]) in dirt:
            dirt[L[i]]+=1
        else:
            dirt[L[i]] = 0
            dirt[L[i]] += 1

    return(dirt)





print(zliczanie(input("Podaj: ")))

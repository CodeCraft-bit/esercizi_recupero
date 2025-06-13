'''
Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
'''

def esercizio_2(n: list[int | float]) -> dict[str, list[int|float]]:
    listap: list = []
    listan: list = []
    dizionario: dict[str, list[int|float]] = {"positivi": [], "negativi": []}
    for i in n:
        if i >= 0:
            dizionario["positivi"].append(i)
        else:
            dizionario["negativi"].append(i)

    return dizionario

lista: list[int|float] = [1, 2, -4, 5, -7, 42, 78, -94]

risultato: dict[str, list[int|float]] = esercizio_2(lista)
print(risultato)



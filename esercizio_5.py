'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
'''

def moltiplica(lista: list[int], threshold: 5) -> int:
    prod_c: int = 1
    for i in lista:
        if i < threshold:
            prod_c *= i

    return prod_c

lista = [1, 2, 3, 4, 5, 6]
print(moltiplica(lista, 5))

    
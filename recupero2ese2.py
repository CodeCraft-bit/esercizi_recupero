def proDict():
    x: int =  0
    y: int = 0
    prodotto: dict[tuple] = {}
    somma: int = 0
    for i in range(0, 101):
        for z in range (0, 89, 2):
            x = i
            y = z
            prodotto[(x, y)] = x*y
    for w in prodotto.values():
        somma += w
    return somma

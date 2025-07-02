def intero_positivo(x: int):
    s: list[int] = []
    occ: int = 0
    pos: int = 0
    somma: int = 0
    u: bool = False
    while True:
        y = int(input("Inserisci un numero: "))
        if y >= 0 and y.is_integer():
            s.append(y)
            if y == 0:
                break 
        else:
            continue
    for i in range(len(s)):
        if s[i] != x:
            somma += s[i]
        if s[i] == x:
            occ += 1
            if occ == 1 and u == False:
                pos = i
                u = True

    return s, somma, occ, pos

print(intero_positivo(5))

        
    



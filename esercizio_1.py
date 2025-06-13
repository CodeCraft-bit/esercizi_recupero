'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
'''

def converti (x: list[tuple]) -> dict:
    dizionario1: dict = {}
    for element in x:
        key, value = element[0], element[1]
        if key in dizionario1:
            dizionario1[key] += value
        else:
            dizionario1[key] = value
    return dizionario1 

print(converti([(0, "a"), (1, "b"), (2, "c")]))



'''def converti (x: list[tuple]) -> dict:
    dizionario1: dict = {}
    for key, value in x:
        if key in dizionario1:
            dizionario1[key] += value
        else:
            dizionario1[key] = value
    return dizionario1 '''



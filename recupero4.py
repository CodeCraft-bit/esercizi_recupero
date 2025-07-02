import math

def calculateCharges(h: int) -> int:
    tariffa: int = 0
    if h<=3:
        tariffa += 2
    elif h > 3 and h < 17:
        tariffa = 2 + math.ceil(h - 3) * 0.50
    else:
        tariffa = 10
    return tariffa

test: list = [1.5, 4.0, 5.50, 24.0]
result = []
print(f"{'Car':<5}", end="   ") #qui mi creo la prima riga con i vari print e con l'ultimo(print) vado a capo
print(f"{'Hours':<5}", end="   ")
print(f"{'Charge':<5}") 

for n in range(len(test)):
    result.append(calculateCharges(test[n]))
    print(f"{n+1:<5}", end="   ")#mi stampo i valori della macchina a parire da 1
    print(f"{test[n]:<5}", end="   ")#mi stampo le ore
    print(f"{calculateCharges(test[n]):<5}")#richiamando la mia funzione mi stampo le varie tariffe e vado a capo

print(f"{'TOTAL':<5}", end="   ")#con i vari print stampo totale, somma delle ore e delle tariffe 
print(f"{sum(test):<5}", end="   ")
print(f"{sum(result):<5}") 








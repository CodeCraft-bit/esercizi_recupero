'''
 Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''
x: dict = {"mela": 2, "pane": 3, "prosciutto": 25, "carne": 55.50, "tartare": 72.30, "torta": 65}
def esercizio_3(spesa: dict[str, float]) -> dict[str, float]:
    
    y: dict[str, float] = {}
    for key, value in x.items():
        if value < 50:
            y[key] = (value * 1.10, 2)
        else:
            continue
    return y
risultato: dict[str, float] = esercizio_3(x)
print(risultato) 

def ricerca_binaria(x: list, n: int) -> bool:
    if n in x:
        return True
    else:
        return False
x = [1, 2, 3, 4, 5, 6, 7, 8]
print(ricerca_binaria(x, 9))
print(ricerca_binaria(x, 5))
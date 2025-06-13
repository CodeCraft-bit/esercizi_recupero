from string import ascii_lowercase

def caesar_cypher_encrypt(s: str, key: int) -> str:

    risultato: list = []

    for i in s:
        indice = ascii_lowercase.index(i)
        indice_n = indice + key
        risultato.append(ascii_lowercase[indice_n])
    return "".join(risultato)

s = "innamorato"
key = 3
print(caesar_cypher_encrypt(s, key))
print(caesar_cypher_encrypt("lqqdprudwr", -3))

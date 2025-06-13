import string

def count_unique_words(text: str) -> dict[str, int]:
    dizionario: dict[str, int] = {}
    token = text.split()
    for i in token:
        x = i.lower()
        x = x.strip(string.punctuation)
        
        if x != "":
            if x in dizionario:
                dizionario[x] +=1
            else:
                dizionario[x] = 1
    return dizionario

text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
print(output)

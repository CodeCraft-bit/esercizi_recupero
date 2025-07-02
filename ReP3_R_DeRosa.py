from __future__ import annotations
import random

class Creatura:
    def __init__(self, nome: str) -> None:
        self.setNome(nome)
        # self.__nome = nome
        # self._nome = nome
    
    def nome(self) -> str: # Getter, richiama il nome e il suo tipo
        return self.__nome
        
    def setNome(self, nome: str) -> None: #Setter, setta il nome
        if nome.isalpha(): # isinstance(nome_variabile, typo)
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def __str__(self):
        return f"Creatura: {self.__nome}"
    
class Alieno(Creatura):
    def __init__(self, nome ="Robot-") -> None:
        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()
        if nome != "Robot-":
            print("Attenzione! Tutti gli Alieni devono avere il nome Robot- seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            nome = "Robot-"
        self.setNome(str(nome + str(self.matricola())))
    
    def matricola(self) -> int:
        return self.__matricola
    
    def __setMatricola(self) -> None:
        self.__matricola = random.randint(10000, 90000)
    
    def munizioni(self) -> list[int]:
        return self.__munizioni
    
    def __setMunizioni(self) -> None:
        self.__munizioni = list(x**2 for x in range(0, 16))
        
    def __str__(self):
        #nome_str = str("Robot-"+{str(self.matricola())})
        return f"Alieno: {self.nome()}"
    
class Mostro(Creatura):
    def __init__(self, nome, urlo_vittoria: str, gemito_sconfitta: str) -> None:
        super().__init__(nome)
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self.__setAssalto()
        

    def vittoria(self) -> str:
        return self.__vittoria
    
    def __setVittoria(self, urlo_vittoria: str) -> None:
        if isinstance(urlo_vittoria, str):
            self.__vittoria = urlo_vittoria
        else:
            self.__vittoria = "GRAAAHHH"

    def sconfitta(self) -> str:
        return self.__sconfitta
    
    def __setSconfitta(self, gemito_sconfitta: str) -> None:
        if isinstance(gemito_sconfitta, str):
            self.__sconfitta = gemito_sconfitta
        else:
            self.__sconfitta = "Uuurghhh"

    def assalto(self) -> list[int]:
        return self.__assalto
    
    def __setAssalto(self) -> None:
        self.__assalto = []
        for i in range(1, 16):
            x = random.randint(1, 100)
            self.__assalto.append(x)

    def __str__(self) -> str:
        nome_str = self.nome().lower()
        for n in range(1,len(nome_str),2): 
            # funzione range(inizio, fine-1, salti(1 = uno in uno, 2 = uno ogni due))
            nome_str[n] = nome_str[n].upper()
        return f"Mostro: {nome_str}"
       
def pariUguali(a: list[int], b: list[int]) -> list:
    lista_c: list[int] = []
    for x,y in zip(a,b):
        # zip[ (a[0], b[0]), (a[1], b[1])]
        if x % 2 == 0 and y % 2 == 0:
            lista_c.append(1)
        else:
            lista_c.append(0)
    return lista_c

def combattimento(a: Alieno, m: Mostro) -> None:
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Non sono Alieni né Mostri")
    else:
        x = pariUguali(a.munizioni(), m.assalto())
        count = 0
        for i in x:
            if i == 1:
                count += 1

        if count > 4:
            print(f'{m.vittoria()}\n'*3)
            proclamaVincitore(m)
            print(m.nome())
        else:
            print(m.sconfitta())
            proclamaVincitore(a)
            print(a.nome())

def proclamaVincitore(c: Creatura) -> None:
    if isinstance(c, Alieno):
        print(f"Gli Alieni hanno vinto!")
    else: 
        print("I Mostri hanno vinto!")


    


def main():
    pass


if __name__ == '__main__':
    main()
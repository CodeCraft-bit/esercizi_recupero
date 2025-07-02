class Frazione:
   _numeratore: float
   _denominatore: float

   def __init__(self, numeratore: float, denominatore: float) -> None:
      self.set_numeratore(numeratore)
      self.set_denominatore(denominatore)

   def get_numeratore(self) -> float:
      return self.__numeratore
   
   def get_denominatore(self) -> float:
      return self.__denominatore
   
   def set_numeratore(self, numeratore: float) -> None:
      self._numeratore = numeratore 
      while True:
         if numeratore.is_integer():
            continue
         else:
            numeratore = 13

   def set_denominatore(self, denominatore: float) -> None:
      self._denominatore = denominatore
      while True:
         if denominatore.is_integer():
            continue
         else:
            denominatore = 5
   def value(self) -> float:
      return round(self._numeratore/self._denominatore, 3)

   def __str__(self):
      return (f"{self._numeratore/self._denominatore:.3f}")
   
def mcd(x: int, y: int):
   lista1: list[int] = []
   lista2: list[int] = []
   lista3: list[int] = []
   for i in range(1, x):
      if x % i == 0:
         lista1.append(i)
      
   for n in range(1, y):
      if x % i == 0:
         lista2.append(n)
      
   for m in lista2:
      if m in lista1:
         lista3.append[m]
   return max(lista3)

def semplifica(l: list[Frazione]):
   x: list = []
   d = 2
   d1 = 2
   for i in l:
      numeratore = i.numeratore()
      denominatore = i.denominatore()
      while numeratore > 1:
         if numeratore % d == 0:
            numeratore //= d
         else:
            d += 1
      while denominatore > 1:
         if denominatore % d1 == 0:
            denominatore //= d1
         else:
            d1 += 1
      return x.append(numeratore, denominatore)

def fractionCompare(l: list[Frazione], x: list):
   for i in l:
      for z in x: 
         if l.value() == x.value():
            print(f"Valore frazione originale {l}---Valore frazione ridotta{x}")

   

      
      
"""
el cd permite diferernciar entre numeros positivos y numeros negativos
09/18/21
"""


numeros = [0,-1.5,12,32,-5.9,-6.3,-7.5,63,47]

print("numeros negativos de la lista....")
for numero in numeros:
    if numero < 0:
        print(numero)
        
print ("numeros positivos de la lista....")
for numero in numeros:
    if numero > 0:
        print(numero)

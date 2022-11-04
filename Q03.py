# A)
nReal = float(input("Digite um numero real pra saber o cubo dele: "))
cubo = nReal**3
print(f"O cubo de {nReal} é {cubo}m³")
# B)
lista = [0,1,2,3,4,5]
print(lista[2])# acessando o 3 termo na lista

# C)
import math

numero = int(input('''Digite um numero
para saber o seu fatorial: '''))
factor = math.factorial(numero)
cont = numero
print(f"Calculando {numero}!: ",end=" ")

for i in range(numero,0,-1):
  print(f"{i}", end=' ')
  print("x" if i > 1 else "=", end=" "  )
  cont -= 1

print(f"{factor}", end=' ')

#D) 

listasoma = [1,2,3,4,5,6]
cont = 0

soma = listasoma[0] + listasoma[1] +listasoma[2]+listasoma[3] + listasoma[4] + listasoma[5]

print(f"A soma da lista foi {soma}")
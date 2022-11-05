nUsuario = int(input("Digite um numero qualquer para ser somado de 0 até ele: "))
cont = 0
soma = 0
for i in range (0,nUsuario+1,1):
    soma += i
print(f'{soma}')
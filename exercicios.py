"""#Exercicio Soma numeros
lista_soma = []

while True:
    numero = int(input("Digite um numero: "))
    if numero == 0:
        break
    lista_soma.append(numero)
    print(lista_soma)

print(sum(lista_soma))

#Exercicio media numeros
lista_media = []
soma = 0

while True:
    numero = int(input("Digite um número(0 para sair): ",))
    if numero == 0:
        break
    else:
        lista_media.append(numero)
        print(lista_media)

for i in range(len(lista_media)):
    i = lista_media[i]
    soma = soma + i


def media (lista):
    return soma / len(lista)

print(f"A média dos números é de {media(lista_media)}")

#Exercicio maior e menor numero
lista = []
while True:
    numero = int(input("Digite um número(0 para sair): ",))
    if numero == 0:
        break
    else:
        lista.append(numero)
        print(lista)

def maior(lista):
    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
        elif lista[i] > maior:
            maior = lista[i]
    return maior

def menor(lista):
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
    return menor   

print(f"O maior número é {maior(lista)} e o menor número é {menor(lista)}")
"""
#Exercicio negativo
lista = []
while True:
    numero = int(input("Digite um número(0 para sair): ",))
    if numero == 0:
        break
    else:
        lista.append(numero)
        print(lista)

def numeros_negativos(lista):
    negativos = []
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos.append(lista[i])
    return negativos

print(f"Os números negativos são {numeros_negativos(lista)}")

#Exercicio lista invertida
lista = []
while True:
    numero = int(input("Digite um número(0 para sair): ",))
    if numero == 0:
        break
    else:
        lista.append(numero)
        print(lista)

lista_invertida = lista[::-1]

print(f"A lista invertida é {lista_invertida}")
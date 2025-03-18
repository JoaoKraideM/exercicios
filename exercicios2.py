#Ex 1
texto = input("Digite um texto: ")
texto_invertido = texto[::-1]

print(texto_invertido)

#Ex 2
texto = input("Digite um texto: ")
palindromo = texto[::-1] == texto

if palindromo:
    print(f"{texto} É um palíndromo")
else:
    print(f"{texto} Não é um palíndromo")


#Ex 3  
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
    return soma // len(lista)

print(f"A média dos números é de {media(lista_media)}")

#Ex 4

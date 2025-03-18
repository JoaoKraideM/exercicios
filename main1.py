"""
lista_tarefas = []

while True:
    tarefas = input("Digite a tarefa: ")
    if tarefas == "fim":
        break
    lista_tarefas.append(tarefas)
    print(lista_tarefas)

while lista_tarefas:
    tarefa = lista_tarefas.pop(0)
    print(f"Tarefa feita: {tarefa}")
    print(f"Tarefas restantes: {lista_tarefas}")

print("Fim das tarefas!")


while True:
    conta_palavras = 0
    frase = input("Digite uma frase: ")
    if frase == "fim":
        break
    for i in frase:
        if i == " ":
            conta_palavras += 1
    print(f"A frase tem {conta_palavras + 1} palavras.")


lista_pares = []

while True:
    numero = int(input("Digite um número(0 para sair): ",))
    if numero == 0:
        break
    else:
        lista_pares.append(numero)
        print(lista_pares)


soma = 0
for i in range(len(lista_pares)):
    i = lista_pares[i]
    if i % 2 == 0:
        soma = soma + i
    else:
        print(f"O número {i} não vai pra soma")

print(f"A soma dos pares no é de {soma}")"
"""

lista_soma = []

while True:
    numero = int(input("Digite um número(0 para sair): ",))
    if numero == 0:
        break
    else:
        lista_soma.append(numero)
        print(lista_soma)

soma = 0    
for i in range(len(lista_soma)):
    i = lista_soma[i]
    soma = soma + i

print(f"A soma dos números é de {soma}")
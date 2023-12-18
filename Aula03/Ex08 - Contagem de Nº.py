# %%

numeros = []

while True:
    entrada = input("Entre com um número: ")

    if entrada == "":
        break

    numeros.append(int(entrada))

numero_check = int(input("Entre com um número para checar a quantidade: "))

total = 0

for i in numeros: 
    if i == numero_check:
        total += 1

print(f'O número {numero_check} aparece {total} vezes')
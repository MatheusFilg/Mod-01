# %%
 
def fatorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

numero = int(input("Digite o número que deseja saber o fatorial: "))

fatorial_numero = fatorial(numero)

print(f"O fatorial do {numero} é: {fatorial_numero}")

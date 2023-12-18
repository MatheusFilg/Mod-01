# %%
def impar_par(n):
    if (n % 2 == 0):
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número: "))

print(f"O numero {numero} é {impar_par(numero)}")
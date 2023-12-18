# %%

n1 = int(input('Digite um valor: '))
fatorial = 1

for i in range(2, n1+1):
    fatorial = fatorial * i
    print(fatorial)
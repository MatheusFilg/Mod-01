# %%

n1 = int(input('Digite um número e descubra se é primo ou não: '))
ePrimo = 0

for i in range (1, n1 + 1):
    if n1 % i == 0:
        ePrimo += 1
    
if ePrimo == 2:
    print(f'O número {n1} é primo')
else:
    print(f'O número {n1} não é primo')
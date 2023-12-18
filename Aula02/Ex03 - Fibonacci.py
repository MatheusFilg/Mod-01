#%%

n1 = int(input('Digite uma posição que deseja saber da sequência de Fibonacci: '))

fib_0 = 0
fib_1 = 1

i = 1

while i < n1:
    fib_n = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib_n
    i += 1

print(f'A posição {n1} corresponde ao valor {fib_0}')

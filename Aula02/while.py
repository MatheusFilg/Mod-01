# %%

i = 1
while i <= 10:
    print(i)
    i += 1
# %%

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        print('Parando o laço While')
        break
# %%

i = int(input('Digite o valor inicial do contador: '))
j = int(input('Digite o valor final do contador: '))

while i <= j:
    print(i)
    i += 1
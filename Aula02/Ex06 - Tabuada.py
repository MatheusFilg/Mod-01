# %%
n1 = int(input('Digite o número que deseja saber a tabuada: '))

for i in range(1, 11):
    multiplicação = n1 * i
    print(f'{n1} x {i} = {multiplicação}')
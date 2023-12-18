#%%

n1 = int(input('Qual o valor da sua primeira nota? '))
n2 = int(input('Qual o valor da sua segunda nota? '))
n3 = int(input('Qual o valor da sua terceira nota? '))
n4 = int(input('Qual o valor da sua quarta nota? '))

conjunto_notas = [n1, n2, n3, n4]

avg_notas = sum(conjunto_notas) / len(conjunto_notas)
menor_nota = min(conjunto_notas)
maior_nota = max(conjunto_notas)

print(avg_notas)
print(menor_nota)
print(maior_nota)
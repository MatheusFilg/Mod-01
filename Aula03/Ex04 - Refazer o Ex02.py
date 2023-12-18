# %%

notas = []

for i in range(0,4):
    notas.append(float(input(f'Entre com a nota {i+1}: ')))

media = sum(notas) / len(notas)
max = max(notas)
min = min(notas)

print(media)
print(max)
print(min)
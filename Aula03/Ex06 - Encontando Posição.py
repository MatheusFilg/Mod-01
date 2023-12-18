# %%

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

maior_valor = lista.index(max(lista)) +1
menor_valor = lista.index(min(lista)) +1

print(f'O maior valor está na posição: {maior_valor}')
print(f'O menor valor valor está na posição: {menor_valor}')
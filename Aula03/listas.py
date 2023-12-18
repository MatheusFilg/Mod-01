# %%
idades = [34, 37, 22, 29, 18, 15, 32, 44, ['Flavia', 32, 'José']]
#tanto faz o tipo que está na lista,
#permitindo até mesmo listas dentro de listas

idades[-1][0]
idades[-1][-1][:2]

# %%

idades = [34, 37, 22, 29, 18, 15, 32, 44, 27, 63, 58]
avg_idades = sum(idades) / len(idades)
print(f'A média das idades é {avg_idades:.2f} anos')

# %%

idades.sort(reverse=True)
#retorna a propria lista organizada, sem criar cópia 
idades

# %%
novas_idades = [69, 72, 99, 100]
idades.append(novas_idades)
idades.remove(novas_idades)
idades

# %%
idades.extend(novas_idades) #adicionando uma lista
#idades = idades + novas_idades também é uma opção porém faz uma copia da lista
idades.sort()
idades
# %%
a = [1,2,3]
b = a

b.remove(2)
print("b: ", b)
print("a: ", a)

# %%
a = [1,2,3]
b = a.copy()
# ou b = a[:]

b.remove(2)
print("b: ", b)
print("a: ", a)

# %%

# APRENDER SOBRE LIST COMPREHENSION & UNPACK LIST 

# %%

s1 = str(input('Digite uma frase e veja a mágica acontecer: '))

frase_separada = s1.split() #transformando a frase em List
frase_invertida = ""

for palavra in frase_separada:
    frase_invertida += palavra[::-1] + " "

print(frase_invertida)
# %%

s1 = str(input('Digite uma frase e veja a mágica acontecer: '))

frase_invertida = []

for palavra in s1.split():
    frase_invertida.append(palavra[::-1])

print(" ".join(frase_invertida))
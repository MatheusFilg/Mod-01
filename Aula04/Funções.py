# %%

def f(x):
    return x + 2 * (3 + x)

y = f(1)
print(y)
# %%

def soma(a,b):
    """Função que realiza a soma de dois valores não importa o tipo""" #Docstring
    return a + b

print(soma(3,9))


# %%
#Estudar sobre *args e **kwargs
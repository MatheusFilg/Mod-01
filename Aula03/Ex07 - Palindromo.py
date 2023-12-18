# %%

palavra = input("Entre com uma palavra: ")

if palavra.lower() == palavra[::-1].lower():
    print(f"A palavra {palavra} é palindromo")
else:
    print(f"A palavra {palavra} não é palindromo")
# %%

frutas = {
        "maça": 1.50, "pera": 1.25, "Goiaba": 2.15, "Banana": 2.75, 
        "Laranja": 0.65, "Abacaxi": 3.20, "Uva": 1.90, "Limão": 1.25, 
        "Jaca": 5.8
        }

nome = input("Digite o nome de uma fruta que deseja saber o preço: ")

if (nome in frutas):
    print(frutas.get(nome))
else:
    print("Esta fruta não está na nossa lista")
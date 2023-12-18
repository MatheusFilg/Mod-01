# %%
import requests

# %%
arquivo = open("meu_arquivo.txt", "w")

arquivo.write("aspiofdsafsajfiosaji osajiofsajfiosa iopasjfio ajfiosafjioasf")
arquivo.close()
# %%

with open("meu_arquivo.txt", "w") as open_file:
    open_file.write("Eu estive aqui....")
# %%
with open("meu_arquivo.txt", "a") as open_file:
    open_file.write("Eu estive aqui.... mais uma vez vez")
# %%
# %%


url = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(url)
data = response.json()

print(data)
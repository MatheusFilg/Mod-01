# %%

dados = {"nome": "Maatheus", "idade": 32, "nome": "Jeferson", "idade": 25}

dados["nome"] = "Matheus"

dados["idade"]
# %%
dados.keys()
# %%
dados.values()
# %%
dados.items()
# %%

del dados["idade"]
# %%
dados["idade"] = 32
dados["profissão"] = "Estagiário"
dados["Esposa"] = "Julia"
dados
# %%
matheus = {"nome": "Matheus Filgueiras", "idade": 24, "humor": "chato"}

mais_info = {"profissão": "estagiário", "hobby": "jogar poe"}

matheus.update(mais_info)
matheus
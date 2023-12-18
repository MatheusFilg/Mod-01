# %%

# try: 
#     numero = int(input('Escolha um número entre 1 e 15: '))
#     sorte = 8

#     if (numero < sorte):
#         print('Seu número está abaixo, tente novamente')
#     elif (numero > sorte):
#         print('Seu número está acima, tente novamente')
#     elif (numero == sorte):
#         print('Parabéns voce acertou')

# except ValueError as err:
#     print('Tenta um número válido ow bobão')
# %%
import random
sorte = random.randint(1,15)



for i in range(3):
    numero = int(input('Escolha um número entre 1 e 15: '))

    if (numero < sorte):
        print('Seu número está abaixo, tente novamente')
    elif (numero > sorte):
        print('Seu número está acima, tente novamente')
    elif (numero == sorte):
        print('Parabéns voce acertou')
        break

else:
    print(f"Acabaram suas chances, o nº correto era {sorte}") 
    #isso vai ser executado se o for n ter um break



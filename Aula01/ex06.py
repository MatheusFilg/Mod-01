# %%

segundos = int(input('Digite quantos segundos você quer transformar: '))
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60) #resto da divisao de horas
minutos = segundos //60
segundos = segundos % 60


# segundos_restantes = segundos % 60
# minutos = segundos // 60
# minutos_restatens = minutos % 60
# horas = minutos // 60


print(f'{horas:.0f}:{minutos:.0f}:{segundos}')

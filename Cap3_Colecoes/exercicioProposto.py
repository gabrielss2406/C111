# 1.
times = ['Botafogo', 'Barcelona', 'Al Ahli', 'Kashima Reysol', 'Tigres']
# a. 3 primeiros
print(f"3 primeiros colocados: {times[:3]}")
# b. 2 ultimos
print(f"2 ultimos: {times[-2:]}")
# c. lista em ordem alfabetica
times_ordenado = times
times_ordenado.sort()
print(f"Ordenados em ordem alfabetica: {times_ordenado}")
# d. Posicao do Barcelona
print(f"Posicao do Barcelona: {times.index("Barcelona")}\n")

# 2.
conjunto1 = {'Samsung', 'Xiaomi', 'Motorola'}
conjunto2 = {'Apple', 'Motorola'}
print(f'Visitando a primeira loja: {conjunto1}')
print(f'Visitando a segunda loja: {conjunto2}')
print(f'Visitando as duas: {conjunto1 | conjunto2}')
print(f'Modelos em comum: {conjunto1 & conjunto2}\n')

# 3.
dict = {}
dict['nome'] = input('Nome do aluno: ')
dict['media'] = float(input('Media do aluno: '))

if dict['media'] >= 60:
    dict['situacao'] = 'AP'
else:
    dict['situacao'] = 'RP'

print(f'Dados do aluno: {dict}')
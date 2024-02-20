# DICIONARIOS
pessoa = {
    'nome': 'Goku',
    'idade': 32
}
pessoa2 = {
    'nome': 'Volibear',
    'idade': 542
}
# add
pessoa['sexo'] = 'Máquina de batalha'
# update
pessoa['nome'] = 'Ewel'
# delete
del pessoa['idade']
# select
print(pessoa)


# COLECOES ANINHADAS
nomes = [pessoa, pessoa2]
print(nomes[1]['nome'])
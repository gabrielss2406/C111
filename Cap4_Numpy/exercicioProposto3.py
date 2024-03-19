import numpy as np

mtz = np.loadtxt('./Cap4_Numpy/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Get Columns
company_column = mtz[1:, 1]
location_column = mtz[1:, 2]
detail_column = mtz[1:, 4]
cost_column = mtz[1:, 6].astype(float)
status_mission_column = mtz[1:, 7]


# 1. Porcentagem de missoes que deram certo
count_success = np.count_nonzero(status_mission_column == "Success")
sucess_percentage = (count_success / status_mission_column.size) * 100
print(f"Porcentagem de missões que deram certo: {sucess_percentage:.2f} %")


# 2. Média de gastos de uma missão (>0)
cost_mean = np.mean(cost_column[cost_column>0])
print(f"Gasto médio das missões: {cost_mean:.2f}")


# 3. Encontre qujantoas missões foram realizadas pelo EUA (USA)
usa_missions = np.char.find(location_column, "USA")
usa_missions = np.count_nonzero(usa_missions != -1)
print(f"Quantidade de missões realizadas pelo EUA: {usa_missions}")


# 4. Missão mais cara da empresa SpaceX
spacex_missions = cost_column[company_column == "SpaceX"]
max_price = np.argmax(spacex_missions)
detail_spacex_column = detail_column[company_column == "SpaceX"]
print(f"Detalhes da missão mais cara da SpaceX: {detail_spacex_column[max_price]}\n")


# 5. Empresas que ja realizaram missoes e a quantidade de missoes de cada7
companys, cont = np.unique(company_column, return_counts=True)
print("Relação empresa e missões realizadas")
for company, qnt in zip(companys, cont):
    print(f"{company}: {qnt} missões realizadas.")
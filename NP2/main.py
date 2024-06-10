import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./NP2/world_happiness.csv", delimiter=",")

# 1. Crie um Bar Plot que ilustre qual o país mais feliz e o mais infeliz do mundo segundo este dataset;
min_ladder = df["Ladder score"].min()
country_min_ladder = df[df["Ladder score"] == min_ladder]["Country name"].values[0]

max_ladder = df["Ladder score"].max()
country_max_ladder = df[df["Ladder score"] == max_ladder]["Country name"].values[0]

plt.bar([country_min_ladder, country_max_ladder],
        [min_ladder, max_ladder],
        color=["gray", "yellow"])
plt.xlabel("País")
plt.ylabel("Felicidade")
plt.title("País menos feliz X País mais feliz")
plt.show()


# 2. Mostre em um Pie Plot as regiões dos 20 países mais felizes deste dataset;
biggests_ladder = df.nlargest(20, "Ladder score")
regions_biggests_ladder = biggests_ladder.groupby("Regional indicator").sum()

plt.pie(x=regions_biggests_ladder["Ladder score"],
        labels=regions_biggests_ladder.index.values)
plt.title("Distribuição das regiões dos 20 países mais felizes")
plt.legend()
plt.tight_layout()
plt.show()


# 3. Mostre em um Scatter Plot os 5 países mais felizes da América Latina e Caribe. O
# tamanho do marcador de cada país deve ser definido se baseando na respectiva
# renda per capita de cada um deles (faça os devidos ajustes para auxiliar na melhor
# visibilidade dos pontos);
latin_df = df[df["Regional indicator"].str.contains("Latin America and Caribbean")]
biggests_latin_ladder = latin_df.nlargest(5, "Ladder score")

plt.scatter(biggests_latin_ladder["Country name"],
            biggests_latin_ladder["Ladder score"],
            s=biggests_latin_ladder["Log GDP per capita"]*1000,
            linewidths=40,
            color="green")
plt.title("Países mais felizes da América Latina e Caribe e sua renda per capita")
plt.tight_layout()
plt.show()


# 4. Apresente um Bar Plot que compare a "liberdade de se fazer escolhas de vida" do
# Brazil com a média de "liberdade de se fazer escolhas de vida" dos países da
# América Latina e Caribe.
brazil_liberty_choices = df[df["Country name"] == "Brazil"]["Freedom to make life choices"].values[0]
#Obs: I also have latin_df from last question
latin_liberty_choices = latin_df["Freedom to make life choices"].mean()

plt.bar(["Brazil", "Latin America and Caribbean"],
        [brazil_liberty_choices, latin_liberty_choices],
        color="lightblue")
plt.title("Liberdade de escolhas: Brasil X América Latina e Caribe")
plt.xlabel("País ou Região")
plt.ylabel("Grau de felicidade")
plt.show()
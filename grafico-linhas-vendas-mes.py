import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as mtick

df_jan = pd.read_excel('vendas_mes.xlsx', sheet_name='Jan')
df_jan = df_jan.rename(columns={'Unnamed: 0': 'Lojas', 'Vendas': 'Vendas Jan'})

df_fev = pd.read_excel('vendas_mes.xlsx', sheet_name='Fev')
df_fev = df_fev.rename(columns={'Unnamed: 0': 'Lojas', 'Vendas': 'Vendas Fev'})

df_mar = pd.read_excel('vendas_mes.xlsx', sheet_name='Mar')
df_mar = df_mar.rename(columns={'Unnamed: 0': 'Lojas', 'Vendas': 'Vendas Mar'})

df_vendas = pd.concat([df_jan[['Lojas', 'Vendas Jan']], df_fev[['Vendas Fev']], df_mar[['Vendas Mar']]], axis=1)
df_vendas = df_vendas.rename(columns={'Vendas Jan': 'Vendas'})

df_vendas['Total Vendas'] = df_vendas.sum(axis=1)

df_vendas = df_vendas.groupby('Lojas').sum()

display(df_vendas)

graf_linhas = sns.lineplot(data=df_vendas, x="Lojas", y="Total Vendas", color="red", linewidth=2)
fig = plt.gcf()
fig.set_size_inches(10, 6)
graf_linhas.set(title="Vendas 2023", xlabel="Lojas", ylabel="Vendas")
graf_linhas.set(ylim=(0, 2000000))
graf_linhas.tick_params(axis='x', labelrotation=45)
graf_linhas.grid(linestyle="--", alpha=0.7)
graf_linhas.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: '{:,.2f}'.format(x)))

fig = graf_linhas.get_figure()
fig.savefig("grafico_vendas_mes.png")

plt.show()
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
df_vendas['Total de Vendas'] = df_vendas.select_dtypes(include=np.number).sum(axis=1)

df_vendas = df_vendas.groupby('Lojas').sum()

display(df_vendas)

sns.set_theme(style="ticks")

graf_total = sns.barplot(data=df_vendas, x=df_vendas.index, y="Total de Vendas", color="#FF4040")
graf_total.set(title="Total de Vendas", xlabel="Lojas", ylabel="Vendas")

fig = plt.gcf()
fig = plt.gcf()
fig.set_size_inches(10.5, 6.5)
graf_total.set(title="Vendas de Jan/Mar 2023", xlabel="Lojas", ylabel="Vendas")
graf_total.set(ylim=(0, 2000000))
graf_total.tick_params(axis='x', labelrotation=45)
graf_total.grid(linestyle="--", alpha=0.7)
graf_total.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: '{:,.2f}'.format(x)))

fig = graf_total.get_figure()
fig.savefig("grafico_vendas_mes_colunas.png")

plt.show()
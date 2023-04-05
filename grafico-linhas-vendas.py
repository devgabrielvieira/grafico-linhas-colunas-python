import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as mtick

df_vendas=pd.read_excel('vendas.xlsx', "Vendas")
display(df_vendas)

graf_linhas = sns.lineplot(data=df_vendas, x="Lojas", y="Vendas", color="red", linewidth=2)
fig = plt.gcf()
fig.set_size_inches(10, 6)
graf_linhas.set(title="Vendas de Jan/Mar 2023", xlabel="Lojas", ylabel="Vendas")
graf_linhas.set(ylim=(0, 2000000))
graf_linhas.tick_params(axis='x', labelrotation=45)
graf_linhas.grid(linestyle="--", alpha=0.7)
graf_linhas.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: '{:,.2f}'.format(x)))

fig = graf_linhas.get_figure()
fig.savefig("grafico_vendas.png")

plt.show()
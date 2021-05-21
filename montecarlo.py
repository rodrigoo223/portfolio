import random
import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(14,8))

mu = 0.08  # media diaria del pct_change
sigma = 3 # Volatilidad diaria del pct_change

ruedas = 250
simulaciones = 100

capital = [[100] for i in range(simulaciones)]

for j in range(simulaciones):
    for i in range(ruedas):
        v = random.normalvariate(mu,sigma)
        capital[j].append(capital[j][i] * (1+v/100))
    ax.plot(capital[j], lw=1, alpha=0.4, c='gray')

ax.plot([50]*ruedas, 'r--' ,lw=1)
ax.set_yscale('log')
plt.show()


df = pd.DataFrame(capital).round(2)

resumen = {}
resumen['minTemporal'] = df.min().min()
resumen['maxTemporal'] = df.max().max()
resumen['minFinal'] = df.transpose().iloc[-1:].squeeze().min()
resumen['maxFinal'] = df.transpose().iloc[-1:].squeeze().max()
resumen['medio'] = round(df.transpose().iloc[-1:].squeeze().mean(),2)
resumen['errorAbsMedia'] = round(resumen['medio'] * 1/(simulaciones**0.5),2)
print('\n',resumen)

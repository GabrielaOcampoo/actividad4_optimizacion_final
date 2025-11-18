import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tiempos.csv')

medias = df.groupby('script')['time'].mean().reset_index()

# Boxplot
plt.figure(figsize=(8,5))
df.boxplot(column='time', by='script', grid=False)
plt.title('Distribución de tiempos por script')
plt.suptitle('')
plt.ylabel('Tiempo (s)')
plt.xlabel('Script')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('boxplot_tiempos.png')
plt.show()

# Barras
plt.figure(figsize=(6,4))
plt.bar(medias['script'], medias['time'])
plt.title('Tiempos promedio por script')
plt.ylabel('Tiempo (s)')
plt.xlabel('Script')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('comparativa_medias.png')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# ===========================
#   CONFIGURACIÓN GLOBAL
# ===========================
plt.style.use('ggplot')  # Estilo profesional limpio
plt.rcParams['figure.dpi'] = 150   # Alta resolución
plt.rcParams['font.size'] = 10     # Tamaño de letra consistente

# ===========================
#   CARGA DE DATOS
# ===========================
df = pd.read_csv('tiempos.csv')

# Calcular promedios
medias = df.groupby('script')['time'].mean().reset_index()

# ===========================
#   BOX PLOT PROFESIONAL
# ===========================
plt.figure(figsize=(8, 5))

df.boxplot(
    column='time',
    by='script',
    grid=True,
    boxprops=dict(color="black", linewidth=1.2),
    whiskerprops=dict(color="black", linewidth=1.2),
    capprops=dict(color="black", linewidth=1.2),
    medianprops=dict(color="red", linewidth=1.8),
    flierprops=dict(marker='o', markersize=4, markerfacecolor='gray')
)

plt.title('Distribución de tiempos por algoritmo', fontsize=12, fontweight='bold')
plt.suptitle('')  # Quita subtítulo automático
plt.ylabel('Tiempo en segundos', fontsize=11)
plt.xlabel('Algoritmo Evaluado', fontsize=11)
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig('boxplot_tiempos.png', dpi=300)
plt.show()
plt.close()   # <<< 🔥 NECESARIO PARA QUE NO SE DAÑE LA SIGUIENTE GRÁFICA

# ===========================
#   GRÁFICO DE BARRAS PROFESIONAL
# ===========================
plt.figure(figsize=(7, 4))

bars = plt.bar(medias['script'], medias['time'], width=0.6)

colors = ['#4C72B0', '#55A868', '#C44E52']
for bar, color in zip(bars, colors):
    bar.set_color(color)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.001,
        f"{height:.6f}",
        ha='center',
        fontsize=9
    )

plt.title('Tiempo promedio de ejecución por algoritmo', fontsize=12, fontweight='bold')
plt.ylabel('Tiempo promedio (s)', fontsize=11)
plt.xlabel('Algoritmo', fontsize=11)
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig('comparativa_medias.png', dpi=300)
plt.show()
plt.close()   # <<< Opcional pero recomendado

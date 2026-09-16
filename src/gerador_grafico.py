import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('assets', exist_ok=True)

dados = {
    'Quantidade de Nomes': [10, 20, 40, 80, 160],
    'Comparações Observadas': [55, 210, 820, 3240, 12880],
    'Comparações Previstas': [55, 210, 820, 3240, 12880]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(8, 5))

plt.plot(df['Quantidade de Nomes'], df['Comparações Observadas'], 
         marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=6,
         label='Comparações O(n²)')

plt.title('Curva de Crescimento de Comparações - Busca Sequencial', fontsize=14, pad=15)
plt.xlabel('Quantidade de Nomes Inseridos (X)', fontsize=12)
plt.ylabel('Quantidade de Comparações (Y)', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

caminho_arquivo = 'assets/grafico_complexidade.png'
plt.savefig(caminho_arquivo, dpi=300, bbox_inches='tight')

print(f"Gráfico gerado e salvo com sucesso em: '{caminho_arquivo}'")
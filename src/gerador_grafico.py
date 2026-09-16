import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('assets', exist_ok=True)

n_valores = [10, 20, 40, 80, 160]
observadas = []
previstas = []

for n in n_valores:
    caminho_arquivo = f'experimentos/estatisticas_{n}.csv'
    
    try:
        df_estatistica = pd.read_csv(caminho_arquivo)
        comparacoes_reais = df_estatistica['comparacoes'].iloc[0]
        observadas.append(comparacoes_reais)
    except FileNotFoundError:
        print(f"Aviso: Arquivo {caminho_arquivo} não encontrado. Verifique a execução em C.")
        observadas.append(0)

    comparacoes_teoricas = n * (n + 1) // 2
    previstas.append(comparacoes_teoricas)

dados = {
    'Quantidade de Nomes': n_valores,
    'Comparações Observadas': observadas,
    'Comparações Previstas': previstas,
    'Diferença': [obs - prev for obs, prev in zip(observadas, previstas)]
}
df = pd.DataFrame(dados)

print("Tabela formatada para o relatório:\n")
print(df.to_markdown(index=False))

plt.figure(figsize=(8, 5))

plt.plot(df['Quantidade de Nomes'], df['Comparações Observadas'], 
         marker='o', linestyle='-', color='#1f77b4', linewidth=3, markersize=8,
         label='Empírico (Observado)')

plt.plot(df['Quantidade de Nomes'], df['Comparações Previstas'], 
         marker='x', linestyle='--', color='#ff7f0e', linewidth=2, markersize=8,
         label='Teórico (Fórmula)')

plt.title('Validação Empírica vs Teórica - Busca Sequencial O(n²)', fontsize=14, pad=15)
plt.xlabel('Quantidade de Nomes Inseridos (X)', fontsize=12)
plt.ylabel('Quantidade de Comparações (Y)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

caminho_arquivo = 'assets/grafico_complexidade.png'
plt.savefig(caminho_arquivo, dpi=300, bbox_inches='tight')

print(f"\nGráfico dinâmico gerado e salvo com sucesso em: '{caminho_arquivo}'")
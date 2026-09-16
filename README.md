# Análise de Algoritmos - Cadastro de Bolsistas CAPES

O projeto implementa e analisa um algoritmo em C para o processamento e cadastro de bolsistas da CAPES, garantindo que não tenha registros duplicados baseados no campo "Nome". Além disso, realiza a análise da complexidade temporal da busca sequencial ($O(n^2)$) por meio da coleta de dados empíricos e da geração de gráficos.

## Estrutura do projeto

```text
analise-algoritmos-capes/               
├── README.md                    # instruções de compilação e execução
├── src/
│   ├── copiador.c               # código-fonte principal em C
│   └── gerador_grafico.py       # script python para gerar o gráfico de complexidade
├── dados_entrada/
│   └── bolsistas-2025.csv       # arquivo CSV original fornecido
├── experimentos/                # diretório onde os arquivos de saída gerados (cadastros e estatísticas) são salvos
└── assets/                      # diretório onde o gráfico gerado é salvo
```

## Pré-requisitos

Para compilar e executar o projeto, é preciso instalar:

- Compilador C (GCC)
- Python 3.x
- Bibliotecas Python: `pandas` e `matplotlib` (para a geração do gráfico de validação experimental)

```bash
pip install pandas matplotlib
```

## Como compilar o programa em C

O código-fonte principal está na pasta `src/`. Para compilar o programa, abra o terminal na raiz do projeto (`analise-algoritmos-capes/`) e execute o seguinte comando:

```bash
gcc src/copiador.c -o copiador
```

Isso vai gerar o arquivo executável `copiador` (ou `copiador.exe` no Windows) diretamente na pasta raiz.

## Como executar o programa (Testes empíricos)

O programa exige a passagem de três argumentos obrigatórios via linha de comando na seguinte ordem:

1. Caminho do arquivo CSV de origem.
2. Caminho do arquivo CSV de destino (onde os registros válidos serão salvos).
3. Caminho do arquivo CSV de estatísticas (onde o total de nomes inseridos e as comparações realizadas serão registrados).

### Execução do teste geral (Arquivo completo)

Para testar a funcionalidade completa e provar a exclusão do registro redundante, execute:

```bash
./copiador dados_entrada/bolsistas-2025.csv experimentos/cadastro_geral.csv experimentos/estatisticas_geral.csv
```

*(Se estiver utilizando Windows, chame pelo executável `copiador.exe` antes sempre)*

### Execução dos experimentos específicos

Caso o código C esteja com a "trava empírica" ativada (não comentada) para extrair os subconjuntos de teste, repita o processo nomeando os arquivos de acordo com o limite definido:

```bash
# Para 10 nomes:
./copiador dados_entrada/bolsistas-2025.csv experimentos/cadastro_10.csv experimentos/estatisticas_10.csv

# Para 20 nomes:
./copiador dados_entrada/bolsistas-2025.csv experimentos/cadastro_20.csv experimentos/estatisticas_20.csv

# Para 40 nomes:
./copiador dados_entrada/bolsistas-2025.csv experimentos/cadastro_40.csv experimentos/estatisticas_40.csv

# Para 80 nomes:
./copiador dados_entrada/bolsistas-2025.csv experimentos/cadastro_80.csv experimentos/estatisticas_80.csv

# Para 160 nomes:
./copiador dados_entrada/bolsistas-2025.csv experimentos/cadastro_160.csv experimentos/estatisticas_160.csv
```

## Geração do gráfico de Complexidade Temporal

Após executar todos os experimentos propostos (10 a 160 nomes) e coletar os dados, você pode gerar a representação visual da complexidade $O(n^2)$ executando o script auxiliar:

```bash
python src/gerador_grafico.py
```

O gráfico, traçando a curva parabólica ascendente, será processado e salvo automaticamente em alta qualidade na pasta `assets/` com o nome `grafico_complexidade.png`.
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados do banco de dados SQLite
def carregar_dados(db_name, table_name):
    # Conectar ao banco de dados
    conn = sqlite3.connect(db_name)
    
    # Carregar os dados da tabela
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    
    # Fechar a conexão com o banco de dados
    conn.close()
    
    return df

# Função para analisar os dados
def analisar_dados(df):
    # Análise básica, como calcular médias, máximos e mínimos
    estatisticas = df.describe()
    print("Estatísticas Descritivas:")
    print(estatisticas)
    
    # Visualizar a evolução do uso da CPU ao longo do tempo
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['value'], marker='o', linestyle='-', color='b')
    plt.title('Uso de CPU ao Longo do Tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Uso de CPU (%)')
    plt.grid(True)
    plt.show()

    # Criar um gráfico de densidade
    plt.figure(figsize=(8, 4))
    sns.kdeplot(df['value'], shade=True, color='r')
    plt.title('Distribuição do Uso de CPU')
    plt.xlabel('Uso de CPU (%)')
    plt.ylabel('Densidade')
    plt.show()

# Exemplo de uso com os dados armazenados
dados = carregar_dados('monitoramento.db', 'dados_servidor')  # Carregar os dados do SQLite
analisar_dados(dados)  # Analisar e visualizar os dados
import requests
import pandas as pd
from datetime import datetime

# URL da API do Prometheus
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# Função para coletar dados de desempenho
def coletar_dados(metric, start_time, end_time, step):
    # Parâmetros para a consulta na API do Prometheus
    query_params = {
        'query': metric,
        'start': start_time,
        'end': end_time,
        'step': step
    }
    
    # Requisição para a API
    response = requests.get(PROMETHEUS_URL, params=query_params)
    data = response.json()
    
    # Verificar se a resposta contém dados
    if data['status'] == 'success':
        result = data['data']['result']
        if len(result) > 0:
            # Extrair timestamps e valores
            timestamps = [datetime.fromtimestamp(float(ts[0])) for ts in result[0]['values']]
            values = [float(val[1]) for val in result[0]['values']]
            
            # Criar um DataFrame para armazenar os dados
            df = pd.DataFrame({'timestamp': timestamps, 'value': values})
            return df
        else:
            print("Nenhum dado encontrado para a métrica especificada.")
            return pd.DataFrame()
    else:
        print("Erro ao consultar a API:", data)
        return pd.DataFrame()

# Parâmetros para a coleta de dados
metric = 'node_cpu_seconds_total'  # Exemplo de métrica do Prometheus
start_time = '2024-08-01T00:00:00Z'  # Tempo de início
end_time = '2024-08-01T01:00:00Z'    # Tempo de término
step = '30s'  # Intervalo de amostragem

# Coletar os dados
dados = coletar_dados(metric, start_time, end_time, step)
print(dados)

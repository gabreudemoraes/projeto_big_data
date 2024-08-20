from fpdf import FPDF
import matplotlib.pyplot as plt

# Função para criar o relatório em PDF
def gerar_relatorio(estatisticas, titulo, analise_grafico1, analise_grafico2):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Título
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=titulo, ln=True, align="C")

    # Estatísticas descritivas
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Estatísticas Descritivas:", ln=True)
    pdf.set_font("Arial", size=8)
    for index, row in estatisticas.iterrows():
        line = f"{index}: {row.to_dict()}"
        pdf.multi_cell(0, 10, line)
    
    # Inserir gráficos
    pdf.add_page()
    pdf.cell(200, 10, txt="Análise Visual:", ln=True)
    pdf.image(analise_grafico1, x=10, y=40, w=170)
    pdf.add_page()
    pdf.image(analise_grafico2, x=10, y=40, w=170)

    # Salvar o PDF
    pdf.output("relatorio_desempenho.pdf")
    print("Relatório gerado com sucesso!")

# Gerar gráficos e salvá-los como imagens temporárias
dados = carregar_dados('monitoramento.db', 'dados_servidor')
estatisticas = dados.describe()

# Gráfico 1: Uso de CPU ao longo do tempo
plt.figure(figsize=(12, 6))
plt.plot(dados['timestamp'], dados['value'], marker='o', linestyle='-', color='b')
plt.title('Uso de CPU ao Longo do Tempo')
plt.xlabel('Tempo')
plt.ylabel('Uso de CPU (%)')
plt.grid(True)
grafico1 = "grafico_cpu_tempo.png"
plt.savefig(grafico1)

# Gráfico 2: Distribuição do Uso de CPU
plt.figure(figsize=(8, 4))
sns.kdeplot(dados['value'], shade=True, color='r')
plt.title('Distribuição do Uso de CPU')
plt.xlabel('Uso de CPU (%)')
plt.ylabel('Densidade')
grafico2 = "grafico_distribuicao_cpu.png"
plt.savefig(grafico2)

# Gerar o relatório em PDF
gerar_relatorio(estatisticas, "Relatório de Desempenho dos Servidores", grafico1, grafico2)
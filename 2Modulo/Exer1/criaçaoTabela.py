import pandas as pd
import openpyxl as open

# Dados da tabela
dados = {
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

# Criar DataFrame do pandas
df = pd.DataFrame(dados)

# Exportar para Excel
nome_arquivo = 'tabela_excel.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f'Tabela exportada para o arquivo: {nome_arquivo}')

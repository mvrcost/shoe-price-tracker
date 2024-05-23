import pandas as pd
import sqlite3
from datetime import datetime

# Ler o arquivo JSONL
df = pd.read_json('../data/data.jsonl', lines=True)

# Mostrar todas as colunas
pd.options.display.max_columns = None

# Função para limpar e converter preços
def clean_price(price):
    return price.str.replace(',', '.')\
                .str.replace(r'\s+', '', regex=True)\
                .str.replace('.', '')\
                .str.replace('R$', '')\
                .astype(float) / 100

# Limpar e converter preços
df['current_price'] = clean_price(df['current_price'])
df['last_price'] = clean_price(df['last_price'])

# Adicionar colunas adicionais
df['-source'] = 'https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness'
df['_data_coleta'] = datetime.now()


# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('../data/quotes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('centauro_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print(df.head())
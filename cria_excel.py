import pandas as pd

# Criando dados fictícios com erros propositais para o nosso validador encontrar
dados_teste = {
    'Nome_Empresa': ['Empresa Alpha LTDA', 'Beta Servicos', 'Gama Tech', 'Omega Solucoes'],
    'CNPJ': ['12345678000199', '987654321', 'A1B2C3D4E5F6G7', ''], # O segundo está curto, o terceiro tem letras, o quarto está vazio
    'Status': ['Ativo', 'Ativo', 'Inativo', 'Ativo']
}

# Transformando os dados em um DataFrame do Pandas
df = pd.DataFrame(dados_teste)

# Salvando como um arquivo do Excel na sua pasta
df.to_excel('empresas_cadastro.xlsx', index=False)

print("Planilha 'empresas_cadastro.xlsx' criada com sucesso no seu disco!")

# 1. Carrega o arquivo Excel criado no passo anterior
df = pd.read_excel('empresas_cadastro.xlsx')

# Exibe no terminal as colunas da empresa, o CNPJ original e o diagnóstico que o robô deu
print("\n--- RESULTADO DA AUDITORIA ---")
print(df[['Nome_Empresa', 'CNPJ', 'Status']])
import pandas as pd

print("Iniciando a validação da planilha...")

# 1. Carrega o arquivo Excel criado no passo anterior
df = pd.read_excel('empresas_cadastro.xlsx')

# Função que aplica as regras de negócio em cada linha do CNPJ
def checar_cnpj(cnpj):
    # Transforma em string e remove espaços vazios nas pontas
    cnpj_str = str(cnpj).strip()
    
    # Regra 1: Verificar se está vazio ou se virou 'nan' (Not a Number do Pandas)
    if cnpj_str == '' or cnpj_str.lower() == 'nan':
        return 'Erro: CNPJ Vazio'
        
    # Regra 2: Verificar se contém letras ou símbolos
    if not cnpj_str.isdigit():
        return 'Erro: Contém Letras'
        
    # Regra 3: Verificar a quantidade correta de dígitos do CNPJ (14 números)
    if len(cnpj_str) != 14:
        return 'Erro: Tamanho Incorreto'
        
    # Se passou por todos os testes, o dado está limpo
    return 'OK: Válido'

# 2. Aplica a função linha por linha na coluna 'CNPJ' e salva o resultado em uma nova coluna
df['Validacao_CNPJ'] = df['CNPJ'].apply(checar_cnpj)

# 3. Salva a nova planilha gerando o relatório final de auditoria
df.to_excel('relatorio_validado.xlsx', index=False)

print("Processo concluído! O arquivo 'relatorio_validado.xlsx' foi gerado.")

# Exibe no terminal as colunas da empresa, o CNPJ original e o diagnóstico que o robô deu
print("\n--- RESULTADO DA AUDITORIA ---")
print(df[['Nome_Empresa', 'CNPJ', 'Validacao_CNPJ']])


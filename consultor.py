'''import requests

print("Consultando dados cadastrais via GET na API Minha Receita...")

# CNPJ público de teste (apenas números, bem limpo)
cnpj_alvo = "06990590000123"

# Rota oficial baseada na documentação (GET /cnpj)
url_oficial = f"https://minhareceita.org/{cnpj_alvo.strip()}"

try:
    # Fazemos a requisição utilizando o método GET, conforme exige o servidor
    resposta = requests.get(url_oficial, timeout=15)
    
    # Se o servidor responder com sucesso
    if resposta.status_code == 200:
        dados = resposta.json()
        print("\n=== DADOS CONSULTADOS COM SUCESSO ===")
        print(f"Razão Social: {dados.get('razao_social')}")
        print(f"Nome Fantasia: {dados.get('nome_fantasia') or 'Não informado'}")
        print(f"Situação Cadastral: {dados.get('descricao_situacao_cadastral')}")
    else:
        print(f"\nO servidor recusou a requisição. Código HTTP: {resposta.status_code}")

except Exception as erro:
    print(f"\nErro de processamento: {erro}")
'''

import requests
import time
from urllib.parse import urljoin

print("Iniciando o Consultador Automático em Lote (Versão Blindada)...")

lista_cnpjs = [
    "06990590000123",  # Google Brasil
    "17213813000125",  # Mercado Livre
    "33592510000154"   # Vale S.A.
]

# Definimos a URL base terminando com barra explicitamente
url_base = "https://minhareceita.org"

# Força o cabeçalho para evitar bloqueios de segurança
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

relatorio_final = []

for cnpj in lista_cnpjs:
    cnpj_limpo = str(cnpj).strip()
    print(f"Consultando o CNPJ: {cnpj_limpo}...")
    
    # O urljoin garante por lei que a URL base e o CNPJ se unam com uma barra entre eles
    url_correta = urljoin(url_base, cnpj_limpo)
    
    try:
        resposta = requests.get(url_correta, headers=headers, timeout=15)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            empresa_da_vez = {
                "CNPJ": cnpj_limpo,
                "Razao_Social": dados.get("razao_social"),
                "Situacao": dados.get("descricao_situacao_cadastral")
            }
            relatorio_final.append(empresa_da_vez)
            print(f"-> Sucesso: {dados.get('razao_social')}")
        else:
            print(f"-> Erro ao consultar este CNPJ. Código: {resposta.status_code}")
            
    except Exception as e:
        print(f"-> Falha de conexão neste CNPJ: {e}")
    
    time.sleep(2.0)

print("\n--- RELATÓRIO DE CONSULTA EM LOTE CONCLUÍDO ---")
print("CNPJ | RAZÃO SOCIAL | SITUAÇÃO")
for emp in relatorio_final:
    print(f"{emp['CNPJ']} | {emp['Razao_Social']} | {emp['Situacao']}")

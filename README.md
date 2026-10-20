# Validador Automatizado de Planilhas de Cadastro

Este é um script em Python focado em rotinas de Backoffice e Auditoria Administrativa. Ele automatiza a verificação de integridade de dados cadastrais (CNPJ) vindos de planilhas do Excel, reduzindo o tempo de análise manual e prevenindo erros operacionais.

## 🛠️ Tecnologias Utilizadas
- Python
- Pandas (Manipulação de dados estruturados)
- Openpyxl (Integração com arquivos Excel .xlsx)

## 📌 Como Funciona
O robô lê a planilha de entrada e aplica regras de negócio automatizadas para classificar cada linha:
- Identifica campos vazios ou nulos.
- Detecta caracteres inválidos (letras ou símbolos no documento).
- Valida a quantidade correta de dígitos (14 caracteres obrigatórios para CNPJ).
- Gera um novo relatório em Excel contendo o status de auditoria de cada registro.

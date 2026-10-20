### Portfólio de Automações e Auditoria de Dados (Backoffice & Tecnologia)

Este repositório reúne scripts em Python desenvolvidos para otimizar rotinas operacionais, auditoria de cadastros e integração com serviços web (APIs). O objetivo é demonstrar a aplicação prática de conceitos lógicos e tratamento de dados no dia a dia administrativo e de suporte técnico. 

### 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python** (Lógica central e estruturação de scripts)
* **Pandas** (Manipulação e higienização de dados estruturados)
* **Openpyxl** (Suporte para leitura e escrita de arquivos Excel .xlsx)
* **Requests** (Comunicação HTTP e consumo de APIs REST)
* **Urllib** (Tratamento seguro e blindagem de URLs)

### 🤖 Projetos Inclusos

### 1. Validador Automatizado de Planilhas (validador.py)

Automação focada em conformidade (compliance) e prevenção a fraudes cadastrais. O robô lê arquivos do Excel contendo dados de empresas e audita a coluna de CNPJ com base em regras de negócio rígidas. 

* **Como funciona:** 

  * Detecta e aponta campos nulos ou vazios.
  * Identifica caracteres inválidos (letras ou símbolos misturados).
  * Valida a quantidade exata de dígitos obrigatórios (14 caracteres).
  * Gera um relatório final em Excel (relatorio_validated.xlsx) com o diagnóstico de cada linha.

### 2. Consultador de Dados Cadastrais em Lote via API (consultor.py)

Script focado em enriquecimento de dados e checagem de regularidade cadastral de clientes corporativos sem a necessidade de digitação manual em portais públicos. 

* **Como funciona:** 

  * Consome dados em lote de forma sequencial a partir de uma lista de CNPJs.
  * Realiza requisições seguras via método GET utilizando a API aberta do projeto *Minha Receita*.
  * Utiliza tratamento com urljoin e gerenciamento de cabeçalhos (User-Agent) para garantir estabilidade de conexão de rede.
  * Possui tratamento nativo de exceções e erros HTTP (como o código 400), garantindo que dados mal digitados sejam reportados no terminal sem interromper o fluxo operacional dos demais registros.

### ⚙️ Como Executar os Scripts locais

1. Certifique-se de estar com o ambiente virtual ativo no terminal: 

bash

venv\Scripts\activate

Use o código com cuidado.
2. Para rodar o validador de planilhas: 

bash

python validador.py

Use o código com cuidado.
3. Para rodar o consultador de APIs em lote: 

bash

python consultor.py

Use o código com cuidado.
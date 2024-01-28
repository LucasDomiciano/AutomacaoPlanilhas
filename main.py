import openpyxl
import requests

# Função para ler dados de uma planilha do Excel
def ler_dados_da_planilha(nome_arquivo, planilha_nome):
    workbook = openpyxl.load_workbook(nome_arquivo)
    planilha = workbook[planilha_nome]

    dados = []
    for row in planilha.iter_rows(min_row=2, values_only=True):
        dados.append({
            'nome': row[0],
            'email': row[1],
            'idade': row[2]
        })

    return dados

# Função para preencher um formulário web usando requests
def preencher_formulario(dados):
    url = "https://www.exemplo.com/formulario"
    
    for pessoa in dados:
        payload = {
            'nome': pessoa['nome'],
            'email': pessoa['email'],
            'idade': pessoa['idade']
            # Adicione outros campos conforme necessário
        }

        # Envia a solicitação POST para preencher o formulário
        response = requests.post(url, data=payload)

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            print(f"Formulário preenchido com sucesso para {pessoa['nome']}")
        else:
            print(f"Falha ao preencher o formulário para {pessoa['nome']}. Código de status: {response.status_code}")

# Nome do arquivo Excel e nome da planilha
nome_arquivo_excel = 'dados.xlsx'
nome_planilha = 'dados_usuarios'

# Lê dados da planilha
dados_para_preencher = ler_dados_da_planilha(nome_arquivo_excel, nome_planilha)

# Preenche o formulário web
preencher_formulario(dados_para_preencher)

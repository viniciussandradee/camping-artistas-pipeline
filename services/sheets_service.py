import gspread
from config import settings
from utils.cleaners import limpar_dados
from utils.formatters import para_lista_de_listas

def executar_pipeline():

    cliente = gspread.service_account(filename=settings.campingartistas)

    planilha = cliente.open_by_key(settings.SHEET_ID)

    aba_entrada = planilha.sheet1

    dados = aba_entrada.get_all_records()
    print("TOTAL LIDO: ", len(dados))

    if dados:
        print("Primeiro Item: ")
        print(dados[0])

    dados_ok, dados_ruins, dados_duplicados = limpar_dados(dados)
    print("Validos: ", len(dados_ok))
    print("Invalidos: ", len(dados_ruins))
    print("Duplicados: ", len(dados_duplicados))

    aba_ok = planilha.worksheet("dados_ok")
    aba_ruins = planilha.worksheet("dados_ruins")
    aba_duplicados = planilha.worksheet("dados_duplicados")

    aba_ok.clear()
    aba_ruins.clear()
    aba_duplicados.clear()

    cabecalho = [
        "nome",
        "cpf",
        "telefone",
        "area",
        "status",
        "detalhe"
    ]

    aba_ok.append_row(cabecalho)
    aba_ruins.append_row(cabecalho)
    aba_duplicados.append_row(cabecalho)

    if dados_ok:
        aba_ok.append_rows(para_lista_de_listas(dados_ok))

    if dados_ruins:
        aba_ruins.append_rows(para_lista_de_listas(dados_ruins))

    if dados_duplicados:
        aba_duplicados.append_rows(para_lista_de_listas(dados_duplicados))




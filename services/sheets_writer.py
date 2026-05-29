from services.sheets_reader import conectar_planilha
from utils.formatters import para_lista_de_listas

def escrever_resultados(dados_ok, dados_ruins, dados_duplicados):

    planilha = conectar_planilha()

    aba_ok = planilha.worksheet("dados_ok")
    aba_ruins = planilha.worksheet("dados_ruins")
    aba_duplicados = planilha.worksheet("dados_duplicados")

    # limpa conteúdo antigo
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

    # recria cabeçalho
    aba_ok.append_row(cabecalho)
    aba_ruins.append_row(cabecalho)
    aba_duplicados.append_row(cabecalho)

    # escreve estado completo
    if dados_ok:
        aba_ok.append_rows(
            para_lista_de_listas(dados_ok)
        )

    if dados_ruins:
        aba_ruins.append_rows(
            para_lista_de_listas(dados_ruins)
        )

    if dados_duplicados:
        aba_duplicados.append_rows(
            para_lista_de_listas(dados_duplicados)
        )
import gspread
from config import settings

def conectar_planilha():

    cliente = gspread.service_account(
        filename=settings.campingartistas
    )

    planilha = cliente.open_by_key(
        settings.SHEET_ID
    )

    return planilha

def ler_dados():
    planilha = conectar_planilha()
    aba_entrada = planilha.sheet1
    dados = aba_entrada.get_all_records()

    return dados

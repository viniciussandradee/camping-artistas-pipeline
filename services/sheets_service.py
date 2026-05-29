from services.sheets_reader import ler_dados
from services.sheets_writer import escrever_resultados
from utils.cleaners import limpar_dados
from utils.logger import log
from utils.storage import (
    carregar_processados,
    salvar_processados
)
from utils.dataframe import criar_dataframe
from utils.charts import grafico_por_area
from utils.report import gerar_relatorio
from utils.csv_exporter import exportar_snapshot_csv
from utils.storage import ler_snapshot, salvar_snapshot, atualizar_snapshot
from utils.viewer import mostrar_estado

def executar_pipeline():

    log("INFO", "Lendo dados da planilha")

    dados = ler_dados()
    processados = carregar_processados()
    dados_novos = []

    for item in dados:
        cpf = str(item.get("CPF / RG / PASSAPORTE", "")).strip()

        area = str(item.get("ÁREA DO PROJETO", "")).strip()

        chave = f"{cpf}-{area}"

        if chave not in processados:
            dados_novos.append(item)
            processados.add(chave)

    log("INFO",f"{len(dados_novos)} novos registros encontrados")

    snapshot = ler_snapshot()
    snapshot = atualizar_snapshot(snapshot, dados_novos)
    salvar_snapshot(snapshot)
    dados_ok, dados_ruins, dados_duplicados = (limpar_dados(snapshot))

    snapshot_atual = ler_snapshot()
    exportar_snapshot_csv("exports/snapshot_completo.csv", snapshot_atual)

    gerar_relatorio(
        total=len(dados_novos),
        validos=len(dados_ok),
        invalidos=len(dados_ruins),
        duplicados=len(dados_duplicados)
    )

    escrever_resultados(dados_ok, dados_ruins, dados_duplicados)

    df_ok = criar_dataframe(dados_ok)

    if not df_ok.empty:

        grafico_por_area(df_ok)

    salvar_processados(processados)

    log(
        "SUCESSO",
        "Pipeline executado com sucesso"
    )
    mostrar_estado()
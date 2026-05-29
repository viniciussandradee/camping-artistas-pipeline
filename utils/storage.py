import json
import os

CAMINHO_PROCESSADOS = "data/processados.json"
CAMINHO_SNAPSHOT = "data/snapshot.json"

def ler_json(caminho):
    if not os.path.exists(caminho):
        return []

    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_processados():
    dados = ler_json(CAMINHO_PROCESSADOS)
    return set(dados)

def salvar_processados(processados):

    with open(CAMINHO_PROCESSADOS, "w", encoding="utf-8") as f:
        json.dump(
            list(processados),
            f,
            indent=4,
            ensure_ascii=False
        )

def ler_snapshot():
    if not os.path.exists(CAMINHO_SNAPSHOT):
        return []

    with open(CAMINHO_SNAPSHOT, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_snapshot(snapshot):
    with open(CAMINHO_SNAPSHOT, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=4)

def atualizar_snapshot(snapshot, novos_registros):
    """
    Atualiza snapshot como estado oficial do sistema.
    Sem duplicação cega
    """

    for novo in novos_registros:
        cpf = str(novo.get("CPF / RG / PASSAPORTE", "")).strip()
        area = str(novo.get("ÁREA DO PROJETO", "")).strip()

        chave = f"{cpf}-{area}"

        atualizado = False

        for item in snapshot:
            cpf_item = str(item.get("CPF / RG / PASSAPORTE", "")).strip()
            area_item = str(item.get("ÁREA DO PROJETO", "")).strip()

            if f"{cpf_item}-{area_item}" == chave:
                item.update(novo)
                atualizado = True
                break

        if not atualizado:
            snapshot.append(novo)

    return snapshot

def obter_estado_atual():
    return ler_snapshot()
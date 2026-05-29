from utils.storage import ler_snapshot

def mostrar_estado():
    dados = ler_snapshot()

    if not dados:
        print("Nenhum dado encontrado")
        return

    print("\n===ESTADO ATUAL DO SISTEMA===\n")

    for item in dados:
        print(
            f"{item.get('nome', '')} | ",
            f"{item.get('cpf', '')} | ",
            f"{item.get('area', '')} | ",
            f"{item.get('status', '')}"
        )
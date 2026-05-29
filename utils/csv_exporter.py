import csv

def exportar_csv(nome_arquivo, dados):

    if not dados:
        return

    with open(nome_arquivo, mode = "w", newline = "", encoding = "utf-8") as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            "nome",
            "cpf",
            "telefone",
            "area",
            "status",
            "detalhe"
        ])

        for item in dados:
            writer.writerow([
                item.get("nome", ""),
                item.get("cpf", ""),
                item.get("telefone", ""),
                item.get("area", ""),
                item.get("status", ""),
                item.get("detalhe", "")
            ])

def exportar_snapshot_csv(nome_arquivo, snapshot):
    if not snapshot:
        return

    campos = sorted(set().union(*[item.keys() for item in snapshot]))

    with open(nome_arquivo, "w", newline = "", encoding = "utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames = campos)

        writer.writeheader()

        for item in snapshot:
            writer.writerow(item)

def para_lista_de_listas(dados):
    resultado = []

    for item in dados:
        resultado.append([
            item.get("nome", ""),
            item.get("cpf", ""),
            item.get("telefone", ""),
            item.get("area", ""),
            item.get("status", ""),
            item.get("detalhe", "")
        ])

    return resultado
import re

col_nome = "NOME COMPLETO"
col_cpf = "CPF / RG / PASSAPORTE"
col_telefone = "TELEFONE DE CONTATO (CÓD. PAÍS + DDD + TELEFONE)"
col_area = "ÁREA DO PROJETO"

def get_valor(item, chave):
    return item.get(chave, "")

def limpar_texto(valor):
    if not valor:
        return ""

    valor = str(valor)
    valor = valor.strip()
    valor = re.sub(r"\s+", " ", valor)
    valor = valor.title()
    
    return valor

def limpar_doc(valor):
    if not valor:
        return ""

    valor = str(valor)
    valor = re.sub(r"\D", "", valor)

    return valor

def limpar_telefone(valor):
    if not valor:
        return ""

    valor = str(valor)
    valor = re.sub(r"\D", "", valor)

    return valor

def validar_cpf(cpf):
    cpf = limpar_doc(cpf)

    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    #dv1
    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    dv1 = (soma * 10 ) % 11
    if dv1 == 10:
        dv1 = 0

    if dv1 != int(cpf[9]):
        return False

    #dv2
    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    dv2 = (soma * 10) % 11

    if dv2 == 10:
        dv2 = 0

    if dv2 != int(cpf[10]):
        return False

    return True

def validar_telefone(telefone):
    telefone = limpar_telefone(telefone)

    if len(telefone) < 10:
        return False

    return True

def validar_item(item, vistos):
    nome = limpar_texto(get_valor(item, col_nome))
    cpf = limpar_doc(get_valor(item, col_cpf))
    telefone = limpar_telefone(get_valor(item, col_telefone))
    area = limpar_texto(get_valor(item, col_area))

    erros = []

    if not validar_cpf(cpf):
        erros.append("CPF inválido. Favor verificar")

    if not validar_telefone(telefone):
        erros.append("Telefone Incorreto. Favor Verificar")

    chave = f"{cpf}-{area}"

    item_limpo = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "area": area,
    }

    if chave in vistos:
        item_limpo["status"] = "duplicado"
        item_limpo["detalhe"] = f"CPF repetido na área {area}"

        return item_limpo, "duplicado"

    vistos.add(chave)

    if erros:

        item_limpo["status"] = "invalido"
        item_limpo["detalhe"] = " | ".join(erros)

        return item_limpo, "invalido"

    item_limpo["status"] = "valido"
    return item_limpo, "valido"

def limpar_dados(dados):
    validos = []
    invalidos = []
    duplicados = []

    vistos = set()

    for item in dados:
        resultado, categoria = validar_item(item, vistos)

        if categoria == "valido":
            validos.append(resultado)

        elif categoria == "invalido":
            invalidos.append(resultado)

        elif categoria == "duplicado":
            duplicados.append(resultado)

    return validos, invalidos, duplicados





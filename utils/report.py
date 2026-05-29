def gerar_relatorio(
        total,
        validos,
        invalidos,
        duplicados
):
    relatorio = f"""
===========================
RELATORIO DE EXECUÇÃO
===========================
    
Total de Registros: {total}
Validados: {validos}
Invalidados: {invalidos}
Duplicados: {duplicados}
===========================
"""
    return relatorio

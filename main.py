def diagnosticar_fila(nome, docs, erro):
    if docs > 10 or erro:
        return "CRITICA"
    elif docs > 5:
        return "ALERTA"
    return "NORMAL"

def gerar_relatorio(filas):
    saida = []
    for f in filas:
        status = diagnosticar_fila(f["nome"], f["docs"], f["erro"])
        linha = f"{f['nome'].upper()} | {status} | {f['docs']} docs"
        if f["erro"]:
            linha += " | ERRO"
        saida.append(linha)
    return saida

filas_exemplo = [
    {"nome": "imp_rh", "docs": 15, "erro": True},
    {"nome": "imp_financeiro", "docs": 8, "erro": False},
    {"nome": "imp_geral", "docs": 3, "erro": False}
]

relatorio = gerar_relatorio(filas_exemplo)
for r in relatorio:
    print(r)
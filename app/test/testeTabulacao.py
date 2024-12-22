from prettytable import PrettyTable


def exibir_tabela(headers, dados):
    dados_limitados = []

    for linha in dados:
        linha_limitada = []
        for valor in linha:
            str_valor = str(valor)
            # Limita cada valor a 30 caracteres, adicionando '...' se necessário
            if len(str_valor) > 10:
                str_valor = str_valor[:27] + '...'
            linha_limitada.append(str_valor)
        dados_limitados.append(linha_limitada)

    tabela = PrettyTable(headers)

    for linha in dados:
        tabela.add_row(linha)
    print(tabela)


# Exemplo de cabeçalhos e dados
headers = ["Iteração", "xB", "xA",
           "raiz aproximada", "imagem da função", "erro"]
dados = [
    [1, 0.123456789012345678901234567890,
        0.98765432109876543210987654321, 2.0, 5.5, 0.001],
    [2, 0.456789012345678901234567890,
        1.23456789012345678901234567890, 2.1, 5.8, 0.002],
    [3, 0.78901234567890123456789012345,
        1.67890123456789012345678901234, 2.15, 6.0, 0.0015],
]

# Chama a função para exibir a tabela
exibir_tabela(headers, dados)

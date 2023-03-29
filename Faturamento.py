import pandas as pd


def menor_valor(valores):
    return valor_filtrado["valor"].min()


def maior_valor(valores):
    return valor_filtrado["valor"].max()


def media_mensal(valores):
    soma_valores = valor_filtrado["valor"].sum()
    media_dia = len(valor_filtrado["dia"] != 0)
    media_mensal = soma_valores / media_dia
    dados_media = valor_filtrado[valor_filtrado["valor"] > media_mensal]
    return len(dados_media["dia"])


try:
    caminho_arquivo = input("Digite o caminho: ")
    dados = pd.read_json(caminho_arquivo)
    valor_filtrado = dados[dados["valor"] != 0]
    menor_faturamento = menor_valor(valor_filtrado)
    maior_faturamento = maior_valor(valor_filtrado)
    dias_superior_media = media_mensal(valor_filtrado)

    print(f"O menor valor de faturamento do mês (excluindo os dias com 0) é de {menor_faturamento:.2f}")
    print(f"O maior valor de faturamento do mês (excluindo os dias com 0) é de {maior_faturamento:.2f}")
    print(f"A quantidade de dias em que o faturamento foi superior a média foram de {dias_superior_media}")
except ValueError:
    print("Caminho inválido por favor tente novamente")

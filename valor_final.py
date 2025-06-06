def calcular_lucro(preco_fabrica, percentual_lucro):
    return preco_fabrica * (percentual_lucro / 100)

def calcular_impostos(preco_fabrica, percentual_impostos):
    return preco_fabrica * (percentual_impostos / 100)

def calcular_preco_final(preco_fabrica, impostos, lucro):
    return preco_fabrica + impostos + lucro

def main():
    try:
        preco_fabrica = int(input("Informe o preço de fábrica: "))
        percentual_impostos = float(input("Informe a porcentagem de lucro do distribuidor (%): "))
        percentual_lucro = float(input("Informe a porcentagem de impostos (%): "))

        lucro = calcular_lucro(preco_fabrica, percentual_lucro)
        impostos = calcular_impostos(preco_fabrica, percentual_impostos)
        preco_final = calcular_preco_final(preco_fabrica, lucro, impostos)

    except:
        print("Erro. Insira um valor válido para as ações.")

    print("\n----DETALHAMENTO ----")
    print(f"Lucro do distribuidor: R${lucro:.2f}")
    print(f"Impostos: {impostos:.2f}")
    print(f"Valor final: R${preco_final:.2f}")

main()
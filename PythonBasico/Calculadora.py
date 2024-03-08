continuar = "n"

while continuar != "s":
    primeiro_numero = int(input("Qual o primeiro numero?"))
    segundo_numero = int(input("Qual o segundo numero?"))

    print("1 - adição")
    print("2 - subtação")
    print("3 - multiplicação")
    print("4 - divisão")

    operacao = int(input("Qual operacao você deseja?"))

    if operacao == 1:
        resposta = primeiro_numero + segundo_numero
    elif operacao == 2:
        resposta = primeiro_numero - segundo_numero
    elif operacao == 3:
        resposta = primeiro_numero * segundo_numero
    elif operacao == 2:
        resposta = primeiro_numero / segundo_numero

    print("A resposta é ", resposta)
    continuar = input("Deseja parar?")
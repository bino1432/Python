continua = True
while continua:
 n = int(input("Digite um número: "))
 for i in range(1, 11):
    print(n, "x", i, "=", n*i)
 resposta=input("Deseja continuar (s/n)?")
 if resposta=="n":
    continua=False
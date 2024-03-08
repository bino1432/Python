numero = int(input("Digite um numero: "))
if numero >= 100:
  print("O numero deve ser menor que 100")
else:
  dezena = numero // 10
  unidade = numero % 10;
soma = dezena + unidade
print("A soma é: ", soma)
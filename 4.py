def imprimir_digitos(numero):
  try:
    numero = int(numero)
  except ValueError:
    print("Número inválido. Digite um número inteiro.")
    return

  for digito in str(numero):
    print(digito, end="   ")

numero = input("Digite um número: ")
imprimir_digitos(numero)

def calcular_quadrado(numero):
  if not isinstance(numero, int) or numero < 0:
    raise ValueError("O número deve ser um inteiro não negativo.")

  quadrado = 0
  for i in range(1, numero + 1):
    quadrado += 2 * i - 1

  return quadrado

numero = int(input("Digite um número: "))

try:
  quadrado = calcular_quadrado(numero)
except ValueError as e:
  print(f"Erro: {e}")
else:
  print(f"O quadrado de {numero} é {quadrado}")

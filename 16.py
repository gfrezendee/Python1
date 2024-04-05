def calcular_fibonacci(numero):
  if not isinstance(numero, int) or numero < 3:
    raise ValueError("O número deve ser um inteiro maior ou igual a 3.")

  a, b = 0, 1
  for i in range(numero - 1):
    a, b = b, a + b

  return b

numero = int(input("Digite o número do termo: "))

try:
  termo_fibonacci = calcular_fibonacci(numero)
except ValueError as e:
  print(f"Erro: {e}")
else:
  print(f"O {numero}º termo da série de Fibonacci é {termo_fibonacci}")

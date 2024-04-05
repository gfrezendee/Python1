def fatorial(numero):
  if numero < 0:
    raise ValueError("O número deve ser não negativo.")
  elif numero == 0:
    return 1
  else:
    resultado = 1
    for i in range(1, numero + 1):
      resultado *= i
    return resultado

numero = int(input("Digite um número não negativo: "))

try:
  fatorial_numero = fatorial(numero)
except ValueError as e:
  print(f"Erro: {e}")
else:
  print(f"O fatorial de {numero} é {fatorial_numero}")

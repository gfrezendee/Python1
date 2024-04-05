def eh_primo(numero):
  if numero < 2: return False
  for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0: return False
  return True

n = int(input("Digite quantos números primos você deseja ver: "))
primos = []
numero = 2
while len(primos) < n:
  if eh_primo(numero):
    primos.append(numero)
  numero += 1

print(f"Os {n} primeiros números primos são: {primos}")

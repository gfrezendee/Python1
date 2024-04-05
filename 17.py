numero_conta = int(input("Digite o número da conta (sem o dígito verificador): "))

soma = 0
for i, digito in enumerate(str(numero_conta)[::-1]):
  soma += int(digito) * (2 ** i)

resto = soma % 10
digito_verificador = 0 if resto == 0 else 10 - resto

numero_conta_completo = f"{str(numero_conta).zfill(6)}-{digito_verificador}"

print(f"O número da conta completo é: {numero_conta_completo}")

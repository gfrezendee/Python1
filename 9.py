num = int(input("Insira um número: "))
op = input("Insira o operador: ")

match op:
    case '+':
        for i in range(0,11):
               print(num+i)
    case '-':
        for i in range(0,11):
               print(num-i)
    case '*':
        for i in range(0,11):
               print(num*i)
    case '/':
        for i in range(1,11):
               print(str(f"{(num/i):.2f}"))
    case _:
        print('Operador inválido')

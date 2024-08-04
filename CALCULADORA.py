num1 = float(input('Digite o Primeiro número: '))
sinal = str(input('Digite a operação: '))
num2 = float(input('Digite o Segundo número: '))
if sinal == '+':
    print(f'É igual = {num1+num2}')
elif sinal == '-':
    print(f'É igual {num1 - num2}')
elif sinal == '*':
    print(f'É igual, {num1 * num2}')
elif sinal == '/':
    print(f'É igual. {num1 / num2}')
else:
    print('Operação invalida, TENTE NOVAMENTE!')

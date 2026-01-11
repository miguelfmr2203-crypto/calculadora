print("qula calculo voce quer fazer")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação (+, -, *, /): ")

if operador == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif operador == '-':
    resultado = num1 - num2
    print(f"resultado: {num1} - {num2} = {resultado}")
  
elif operador == '*':
    resultado = num1 * num2
    print(f"resultado: {num1} * {num2} = {resultado}")

elif operador == '/':
    if num2 != 0:
        resutado = num1 / num2
        print(f"resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")


else:
    # Caso o usuário digite algo que não seja um dos 4 sinais
    print("Operador inválido!")   
    
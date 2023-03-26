
def calculadora(opt, num1, num2):
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    elif opt == "/":
        return num1 / num2
    else:
        return print("opcao invalida")




number1 = int (input("Digite 1 numeros "))
number2 = int (input("Digite outro numeros "))


operacao = input("Descreva a operacao desejada ")

print (calculadora(operacao, number1, number2))
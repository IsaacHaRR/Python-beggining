
def e_par(num):
    num2 = num % 2
    if num2 == 0:
        return True
    else:
        return False

number = int(input("Digite um numero: "))

if e_par(number):
    print("e par")
else:
    print("e impar")

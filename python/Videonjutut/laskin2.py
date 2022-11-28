num1 = float(input("Syötä ensimmäinen numero: "))
op = input("Syötä laskutapa: ")
num2 = float(input("Syötä toinen numero: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("Väärä laskutapa")
#I am going to make a calculator in python.

a = int(input("Wat wil je berekenen? Wat is het eerste cijfer?"))
optie = input("Kies uit: /, *, + -")
b = int(input("Wat wil je berekenen? Wat is het tweede cijfer?"))

def rekenmachineBerekening(optie, a, b):
    match optie:
        case "/":
            return a / b
        case "*":
            return a * b
        case "+":
            return a + b
        case "-":
            return a - b
        
resultaat = rekenmachineBerekening(optie, a, b)


print(f"Het resultaat is {resultaat}")
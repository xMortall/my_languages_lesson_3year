#calculadora

def decorador(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"O resultado da operação é: {result}")
        return result
    return wrapper

@decorador
def somar(a, b):
    return a + b

@decorador
def subtrair(a, b):
    return a - b

def input_numbers():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b
    

def escolher_operacao():
    operacao = input("Escolha a operação (somar/subtrair): ")
    if operacao == "somar":
        a, b = input_numbers()
        return somar(a, b)
    elif operacao == "subtrair":
        a, b = input_numbers()
        return subtrair(a, b)
    else:
        print("Operação inválida.")
        return None
    
    
escolher_operacao()
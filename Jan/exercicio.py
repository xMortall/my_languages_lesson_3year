# Cruar yn deciradir qye verufuqye i oruneuri argynebti da função.
# Se o primeiro argumento for o nome "admin", a função deve correr
# normalmente. Se for qualquer outro nome, o decorador deve impedir
# a execução e mostrar uma mensagem de erro: "Acesso Negado!".

def verificar_admin(func):
    def wrapper(*args, **kwargs):
        if args and args[0] == "admin":
            print(func.__name__)
            return func(*args, **kwargs)
        else:
            print("Acesso Negado!")
        return wrapper(*args, **kwargs)
    return wrapper

@verificar_admin
def acessar_sistema(utilizador):
    print(f"Acesso concedido ao usuário: {utilizador}")

acessar_sistema("admin")
acessar_sistema("usuario")
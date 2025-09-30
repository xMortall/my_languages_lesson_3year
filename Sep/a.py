"""
Faz uma função que receba um set e dentro da função um a um, os elementos do set são transferidos
para outro set de 1 em 1 até que o primeiro set fique vazio.

Exemplo:
set1 = {1, 2, 3, 4, 5}
set2 =  {}

set1 = {}
set2 = {1, 2, 3, 4, 5}
"""

def transfer_set_elements(_set1, _set2):
    for i in range(len(_set1)):
        print("set 1 :", *_set1)
        print("set 2 :", *_set2)
        print("-"*20)
        _set2.add(_set1.pop())

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = set()
    transfer_set_elements(set1, set2)

if __name__ == "__main__":
    main()
"""
Jogo do bingo com 100 bolas e elas rendomizão no terminal e marca as bolas que já sairam automaticomente, e que tenha visualizaão da tabela com cores.
"""
import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")

def print_bingo_board(called_numbers, last_number):
    clear_screen()
    print("Bingo Board:")
    for i in range(1, 101):
        if i in called_numbers:
            print(f"\033[92m{i:3}\033[0m", end=' ')
        else:
            print(f"{i:3}", end=' ')
        if i % 10 == 0:
            print()
    print(f"\nNúmero sorteado agora: \033[93m{last_number}\033[0m")
    print("\nNúmeros já sorteados:", sorted(called_numbers))
    time.sleep(1)

def main():
    numbers = list(range(1, 101))
    random.shuffle(numbers)
    called_numbers = set()

    clear_screen()

    for number in numbers:
        called_numbers.add(number)
        print_bingo_board(called_numbers, number)
        time.sleep(0.5)
    clear_screen()

if __name__ == "__main__":
    main()

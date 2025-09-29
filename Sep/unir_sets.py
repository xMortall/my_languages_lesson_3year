"""
Programa com uma função que aceita como parâmetro 2 sets e devolve a sua união
"""

def uniao_set(set1:set, set2:set) -> set:
    return set1.union(set2)

def main():
    set_a = {1, 2, 3, 4}
    set_b = {5, 6, 7, 8}
    print(f"A união dos sets é: {uniao_set(set_a, set_b)}")

if __name__ == "__main__":
    main()
class Pessoa:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def _morada(self):
        _morada = ""
        return _morada

    def __numero_(self):
        __numero_ = ""
        return __numero_


class Alunos(Pessoa):
    curso = ""
    def __init__(self, Nome, Idade, curso):
        super().__init__(Nome, Idade)
        self.curso = curso


def main():
    aluno1 = Alunos("Jan", 21, "Engenharia de Software")

    print(aluno1.Nome)
    print(aluno1.Idade)
    print(aluno1.curso)

if __name__ == "__main__":
    main()
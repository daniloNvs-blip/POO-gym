class Aluno:
    """Aluno da academia: integra um Personal e um Treino."""

    def __init__(self, matricula, nome, cpf, telefone, personal, treino):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.personal = personal
        self.treino = treino

    def exibir_dados(self):
        print(f"Aluno: {self.nome} | Matrícula: {self.matricula}")
        print(f"CPF: {self.cpf} | Telefone: {self.telefone}")

    def exibir_ficha(self):
        print("=== FICHA DO ALUNO ===")
        self.exibir_dados()
        print("--- Personal ---")
        self.personal.exibir_dados()
        print("--- Treino ---")
        self.treino.exibir_treino()

class Personal:
    """Personal trainer responsável por orientar o aluno."""

    def __init__(self, cref, nome, especialidade):
        self.cref = cref
        self.nome = nome
        self.especialidade = especialidade

    def exibir_dados(self):
        print(f"Personal: {self.nome}")
        print(f"CREF: {self.cref}")
        print(f"Especialidade: {self.especialidade}")

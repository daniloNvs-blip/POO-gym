class Treino:
    """Treino composto por uma lista de objetos Exercicio."""

    def __init__(self, codigo, nome, objetivo):
        self.codigo = codigo
        self.nome = nome
        self.objetivo = objetivo
        self.exercicios = []

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    def calcular_volume_total(self):
        total = 0
        for exercicio in self.exercicios:
            total += exercicio.calcular_volume()
        return total

    def exibir_treino(self):
        print(f"Treino {self.codigo}: {self.nome} (objetivo: {self.objetivo})")
        for exercicio in self.exercicios:
            print("  -", end=" ")
            exercicio.exibir_exercicio()
        print(f"Volume total: {self.calcular_volume_total()} kg")

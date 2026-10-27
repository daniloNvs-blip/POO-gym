class Exercicio:
    """Exercício físico com séries, repetições e carga."""

    def __init__(self, codigo, nome, grupo_muscular, series, repeticoes, carga):
        self.codigo = codigo
        self.nome = nome
        self.grupo_muscular = grupo_muscular
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga

    def calcular_volume(self):
        # volume = séries x repetições x carga (kg)
        return self.series * self.repeticoes * self.carga

    def exibir_exercicio(self):
        print(f"{self.nome} ({self.grupo_muscular}) - "
              f"{self.series}x{self.repeticoes} com {self.carga} kg "
              f"| volume: {self.calcular_volume()} kg")

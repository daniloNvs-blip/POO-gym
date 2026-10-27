from cppersonal import Personal
from cs01exercicio import Exercicio
from cs02treino import Treino
from cs03aluno import Aluno

# 1. Personal
personal = Personal("012345-G/GO", "Carla Mendes", "Hipertrofia")

# 2. Exercícios
supino = Exercicio(1, "Supino reto", "Peito", 4, 10, 40)
crucifixo = Exercicio(2, "Crucifixo", "Peito", 3, 12, 14)
triceps = Exercicio(3, "Tríceps corda", "Tríceps", 3, 15, 25)

# 3. Treino (composição de exercícios)
treino = Treino("A", "Peito e Tríceps", "Hipertrofia")
treino.adicionar_exercicio(supino)
treino.adicionar_exercicio(crucifixo)
treino.adicionar_exercicio(triceps)

# 4. Aluno (associa Personal e Treino)
aluno = Aluno(1001, "João da Silva", "111.222.333-44",
              "(61) 99999-9999", personal, treino)

# 5. Exibir a ficha completa
aluno.exibir_ficha()

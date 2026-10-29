import streamlit as st

from escola import Escola
from aluno import Aluno
from professor import Professor
from disciplina import Disciplina
from turma import Turma


# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Sistema Escolar",
    page_icon="🏫",
    layout="wide"
)


# ==========================================
# CRIANDO OS OBJETOS
# ==========================================

escola = Escola(
    "Escola Municipal Brasil",
    "Rua Principal, 100",
    "(11) 99999-9999"
)


aluno1 = Aluno(
    1,
    "João Silva",
    "10/05/2008"
)

aluno2 = Aluno(
    2,
    "Maria Souza",
    "20/08/2008"
)


professor1 = Professor(
    1,
    "Carlos Oliveira",
    "carlos@escola.com"
)


matematica = Disciplina(
    1,
    "Matemática",
    80
)

portugues = Disciplina(
    2,
    "Português",
    80
)


turma1 = Turma(
    101,
    "1º Ano A",
    2026
)


# ==========================================
# CADASTROS
# ==========================================

escola.cadastrar_aluno(aluno1)
escola.cadastrar_aluno(aluno2)

escola.cadastrar_professor(professor1)

escola.criar_turma(turma1)


# ==========================================
# MATRÍCULAS
# ==========================================

aluno1.matricular(turma1)
aluno2.matricular(turma1)


# ==========================================
# DISCIPLINAS
# ==========================================

turma1.adicionar_disciplina(matematica)
turma1.adicionar_disciplina(portugues)


# ==========================================
# PROFESSOR
# ==========================================

professor1.lecionar(matematica)
professor1.lecionar(portugues)


# ==========================================
# NOTAS
# ==========================================

professor1.lancar_nota(
    aluno1,
    matematica,
    8.5
)

professor1.lancar_nota(
    aluno1,
    portugues,
    9.0
)


# ==========================================
# INTERFACE
# ==========================================

st.title("🏫 Sistema Escolar")

st.write(
    "Sistema de gerenciamento de alunos, "
    "professores, disciplinas e turmas."
)


# ==========================================
# INFORMAÇÕES DA ESCOLA
# ==========================================

st.header("🏫 Informações da Escola")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Escola", escola.nome)

with col2:
    st.write("📍 **Endereço**")
    st.write(escola.endereco)

with col3:
    st.write("📞 **Telefone**")
    st.write(escola.telefone)


st.divider()


# ==========================================
# ALUNOS
# ==========================================

st.header("👨‍🎓 Alunos")


for aluno in escola.alunos:

    with st.container(border=True):

        st.subheader(aluno.nome)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"**ID:** {aluno.id}")

        with col2:
            st.write(
                f"**Nascimento:** "
                f"{aluno.data_nascimento}"
            )

        with col3:

            if aluno.turma:
                st.write(
                    f"**Turma:** "
                    f"{aluno.turma.nome}"
                )


        if aluno.notas:

            st.write("### 📊 Notas")

            for disciplina, nota in aluno.notas.items():

                st.write(
                    f"**{disciplina}:** {nota:.1f}"
                )


st.divider()


# ==========================================
# PROFESSORES
# ==========================================

st.header("👨‍🏫 Professores")


for professor in escola.professores:

    with st.container(border=True):

        st.subheader(professor.nome)

        st.write(
            f"**ID:** {professor.id}"
        )

        st.write(
            f"**E-mail:** {professor.email}"
        )

        st.write("### 📚 Disciplinas")

        for disciplina in professor.disciplinas:

            st.write(
                f"- {disciplina.nome}"
            )


st.divider()


# ==========================================
# TURMAS
# ==========================================

st.header("📚 Turmas")


for turma in escola.turmas:

    with st.container(border=True):

        st.subheader(turma.nome)

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Código:** {turma.codigo}"
            )

        with col2:

            st.write(
                f"**Ano:** {turma.ano}"
            )


        st.write("### 👨‍🎓 Alunos")

        for aluno in turma.alunos:

            st.write(
                f"- {aluno.nome}"
            )


        st.write("### 📚 Disciplinas")

        for disciplina in turma.disciplinas:

            st.write(
                f"- {disciplina.nome} "
                f"({disciplina.carga_horaria} horas)"
            )


# ==========================================
# RODAPÉ
# ==========================================

st.divider()

st.caption(
    "Sistema Escolar - Desenvolvido em Python + Streamlit"
)
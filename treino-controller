from database import conectar

def criar_treino(id_aluno, id_instrutor, objetivo):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO treinos (id_aluno, id_instrutor, objetivo) VALUES (%s, %s, %s) RETURNING id_treino",
            (id_aluno, id_instrutor, objetivo)
        )
        id_treino_novo = cur.fetchone()[0]
        conn.commit()
        print(f"Ficha de treino ID {id_treino_novo} criada com sucesso!")
        return id_treino_novo
    except Exception as e:
        print(f"Erro ao criar treino: {e}")
        return None
    finally:
        if conn:
            cur.close()
            conn.close()

def adicionar_exercicio_ao_treino(id_treino, id_exercicio, series, repeticoes, carga_kg, observacao):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO treino_exercicios (id_treino, id_exercicio, series, repeticoes, carga_kg, observacao)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (id_treino, id_exercicio, series, repeticoes, carga_kg, observacao)
        )
        conn.commit()
        print("Exercício adicionado ao treino com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar exercício ao treino: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def listar_treinos_de_aluno(id_aluno):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            SELECT t.id_treino, t.objetivo, t.data_criacao, i.nome_completo AS nome_instrutor
            FROM treinos t
            JOIN instrutores i ON t.id_instrutor = i.id_instrutor
            WHERE t.id_aluno = %s
            ORDER BY t.data_criacao DESC
        """, (id_aluno,))
        treinos = cur.fetchall()
        
        if not treinos:
            print(f"Nenhum treino encontrado para o aluno com ID {id_aluno}.")
            return False

        print(f"\n--- Treinos do Aluno ID {id_aluno} ---")
        for treino in treinos:
            print(f"ID Treino: {treino[0]}, Objetivo: {treino[1]}, Data: {treino[2]}, Instrutor: {treino[3]}")
        return True
    except Exception as e:
        print(f"Erro ao listar treinos: {e}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def ver_detalhes_do_treino(id_treino):
    try:
        conn = conectar()
        cur = conn.cursor()
        
        # 1. Buscar informações do cabeçalho do treino
        cur.execute("""
            SELECT t.id_treino, t.objetivo, t.data_criacao, a.nome_completo, i.nome_completo
            FROM treinos t
            JOIN alunos a ON t.id_aluno = a.id_aluno
            JOIN instrutores i ON t.id_instrutor = i.id_instrutor
            WHERE t.id_treino = %s
        """, (id_treino,))
        treino_info = cur.fetchone()

        if not treino_info:
            print(f"Nenhum treino encontrado com o ID {id_treino}.")
            return

        # 2. Buscar os exercícios do treino
        cur.execute("""
            SELECT e.nome_exercicio, te.series, te.repeticoes, te.carga_kg, te.observacao
            FROM treino_exercicios te
            JOIN exercicios e ON te.id_exercicio = e.id_exercicio
            WHERE te.id_treino = %s
            ORDER BY e.nome_exercicio
        """, (id_treino,))
        exercicios = cur.fetchall()

        # 3. Exibir tudo
        print("\n Detalhes da Ficha de Treino")
        print(f"ID do Treino: {treino_info[0]}")
        print(f"Aluno: {treino_info[3]}")
        print(f"Instrutor: {treino_info[4]}")
        print(f"Objetivo: {treino_info[1]}")
        print(f"Data de Criação: {treino_info[2]}")
        print("\n--- Exercícios ---")
        if not exercicios:
            print("Nenhum exercício cadastrado para esta ficha.")
        else:
            for ex in exercicios:
                print(f"  - Nome: {ex[0]}")
                print(f"    Séries: {ex[1]}, Repetições: {ex[2]}, Carga: {ex[3]}kg")
                if ex[4]:
                    print(f"    Obs: {ex[4]}")
    except Exception as e:
        print(f"Erro ao ver detalhes do treino: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def remover_treino(id_treino):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM treinos WHERE id_treino = %s", (id_treino,))
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum treino encontrado com o ID {id_treino}.")
        else:
            print("Ficha de treino removida com sucesso!")
    except Exception as e:
        print(f"Erro ao remover treino: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

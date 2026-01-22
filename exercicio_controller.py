from database import conectar

def inserir_exercicio(nome, grupo_muscular, instrucoes):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO exercicios (nome_exercicio, grupo_muscular, instrucoes_execucao) VALUES (%s, %s, %s)",
            (nome, grupo_muscular, instrucoes)
        )
        conn.commit()
        print("Exercício inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir exercício: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def listar_exercicios():
    try:
        conn = conectar()
        cur = conn.cursor()
        # Ordena por grupo muscular e depois por nome para melhor organização
        cur.execute("SELECT id_exercicio, nome_exercicio, grupo_muscular FROM exercicios ORDER BY grupo_muscular, nome_exercicio")
        exercicios = cur.fetchall()
        if not exercicios:
            print("Nenhum exercício encontrado.")
            return

        print("\n--- Catálogo de Exercícios ---")
        for exercicio in exercicios:
            print(f"ID: {exercicio[0]}, Nome: {exercicio[1]}, Grupo Muscular: {exercicio[2]}")
        print("------------------------------\n")
    except Exception as e:
        print(f"Erro ao listar exercícios: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def atualizar_exercicio(id_exercicio, nome, grupo_muscular, instrucoes):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE exercicios 
            SET nome_exercicio = %s, grupo_muscular = %s, instrucoes_execucao = %s
            WHERE id_exercicio = %s
            """,
            (nome, grupo_muscular, instrucoes, id_exercicio)
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum exercício encontrado com o ID {id_exercicio}.")
        else:
            print("Exercício atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar exercício: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def remover_exercicio(id_exercicio):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM exercicios WHERE id_exercicio = %s", (id_exercicio,))
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum exercício encontrado com o ID {id_exercicio}.")
        else:
            print("Exercício removido com sucesso!")
    except Exception as e:
        print(f"Erro ao remover exercício: {e}")
        print("Verifique se o exercício não está associado a nenhuma ficha de treino.")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_exercicio_por_id(id_exercicio):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM exercicios WHERE id_exercicio = %s", (id_exercicio,))
        exercicio = cur.fetchone()

        if exercicio:
            print("\n--- Exercício Encontrado ---")
            print(f"ID: {exercicio[0]}")
            print(f"Nome: {exercicio[1]}")
            print(f"Grupo Muscular: {exercicio[2]}")
            print(f"Instruções: {exercicio[3]}")
            print("----------------------------\n")
        else:
            print(f"Nenhum exercício encontrado com o ID {id_exercicio}.")
    except Exception as e:
        print(f"Erro ao buscar exercício: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_exercicio_por_nome(nome):
    try:
        conn = conectar()
        cur = conn.cursor()
        # Usamos ILIKE para busca case-insensitive e % para busca parcial
        termo_busca = f"%{nome}%"
        cur.execute("SELECT id_exercicio, nome_exercicio, grupo_muscular FROM exercicios WHERE nome_exercicio ILIKE %s", (termo_busca,))
        exercicios = cur.fetchall()

        if exercicios:
            print("\n--- Exercícios Encontrados ---")
            for exercicio in exercicios:
                print(f"ID: {exercicio[0]}, Nome: {exercicio[1]}, Grupo Muscular: {exercicio[2]}")
            print("------------------------------\n")
        else:
            print(f"Nenhum exercício encontrado com o nome '{nome}'.")
    except Exception as e:
        print(f"Erro ao buscar exercício: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

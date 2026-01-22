from database import conectar

def inserir_plano(nome_plano, valor_mensal, descricao):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO planos (nome_plano, valor_mensal, descricao) VALUES (%s, %s, %s)",
            (nome_plano, valor_mensal, descricao)
        )
        conn.commit()
        print("Plano inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir plano: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def listar_planos():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id_plano, nome_plano, valor_mensal, descricao FROM planos ORDER BY id_plano")
        planos = cur.fetchall()
        if not planos:
            print("Nenhum plano encontrado.")
            return

        print("\n Lista de Planos")
        for plano in planos:
            print(f"ID: {plano[0]}, Nome: {plano[1]}, Valor: R${plano[2]:.2f}, Descrição: {plano[3]}")
        print("-----------------------\n")
    except Exception as e:
        print(f"Erro ao listar planos: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def atualizar_plano(id_plano, nome_plano, valor_mensal, descricao):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE planos 
            SET nome_plano = %s, valor_mensal = %s, descricao = %s 
            WHERE id_plano = %s
            """,
            (nome_plano, valor_mensal, descricao, id_plano)
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum plano encontrado com o ID {id_plano}.")
        else:
            print("Plano atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar plano: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def remover_plano(id_plano):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM planos WHERE id_plano = %s", (id_plano,))
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum plano encontrado com o ID {id_plano}.")
        else:
            print("Plano removido com sucesso!")
    except Exception as e:
        # Informa sobre restrições de chave estrangeira
        print(f"Erro ao remover plano: {e}")
        print("Verifique se não há alunos associados a este plano antes de removê-lo.")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_plano_por_id(id_plano):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id_plano, nome_plano, valor_mensal, descricao FROM planos WHERE id_plano = %s", (id_plano,))
        plano = cur.fetchone()

        if plano:
            print("\n--- Plano Encontrado ---")
            print(f"ID: {plano[0]}, Nome: {plano[1]}, Valor: R${plano[2]:.2f}, Descrição: {plano[3]}")
            print("------------------------\n")
        else:
            print(f"Nenhum plano encontrado com o ID {id_plano}.")
    except Exception as e:
        print(f"Erro ao buscar plano: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

from database import conectar

def inserir_instrutor(nome_completo, cpf, especialidade):
    try:
        conn = conectar()
        cur = conn.cursor()
        cpf_numerico = ''.join(filter(str.isdigit, cpf))
        if len(cpf_numerico) != 11:
            print("Erro: CPF inválido. Deve conter 11 dígitos.")
            return
            
        cur.execute(
            "INSERT INTO instrutores (nome_completo, cpf, especialidade) VALUES (%s, %s, %s)",
            (nome_completo, cpf_numerico, especialidade)
        )
        conn.commit()
        print("Instrutor inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir instrutor: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def listar_instrutores():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id_instrutor, nome_completo, cpf, especialidade FROM instrutores ORDER BY id_instrutor")
        instrutores = cur.fetchall()
        if not instrutores:
            print("Nenhum instrutor encontrado.")
            return

        print("\n--- Lista de Instrutores ---")
        for instrutor in instrutores:
            print(f"ID: {instrutor[0]}, Nome: {instrutor[1]}, CPF: {instrutor[2]}, Especialidade: {instrutor[3]}")
        print("----------------------------\n")
    except Exception as e:
        print(f"Erro ao listar instrutores: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def atualizar_instrutor(id_instrutor, nome_completo, especialidade):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE instrutores 
            SET nome_completo = %s, especialidade = %s 
            WHERE id_instrutor = %s
            """,
            (nome_completo, especialidade, id_instrutor)
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum instrutor encontrado com o ID {id_instrutor}.")
        else:
            print("Instrutor atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar instrutor: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def remover_instrutor(id_instrutor):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM instrutores WHERE id_instrutor = %s", (id_instrutor,))
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum instrutor encontrado com o ID {id_instrutor}.")
        else:
            print("Instrutor removido com sucesso!")
    except Exception as e:
        print(f"Erro ao remover instrutor: {e}")
        print("Verifique se o instrutor não está associado a treinos ou avaliações físicas.")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_instrutor_por_id(id_instrutor):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id_instrutor, nome_completo, cpf, especialidade FROM instrutores WHERE id_instrutor = %s", (id_instrutor,))
        instrutor = cur.fetchone()

        if instrutor:
            print("\n--- Instrutor Encontrado ---")
            print(f"ID: {instrutor[0]}, Nome: {instrutor[1]}, CPF: {instrutor[2]}, Especialidade: {instrutor[3]}")
            print("----------------------------\n")
        else:
            print(f"Nenhum instrutor encontrado com o ID {id_instrutor}.")
    except Exception as e:
        print(f"Erro ao buscar instrutor: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_instrutor_por_cpf(cpf):
    try:
        conn = conectar()
        cur = conn.cursor()
        cpf_numerico = ''.join(filter(str.isdigit, cpf))
        cur.execute("SELECT id_instrutor, nome_completo, cpf, especialidade FROM instrutores WHERE cpf = %s", (cpf_numerico,))
        instrutor = cur.fetchone()

        if instrutor:
            print("\n--- Instrutor Encontrado ---")
            print(f"ID: {instrutor[0]}, Nome: {instrutor[1]}, CPF: {instrutor[2]}, Especialidade: {instrutor[3]}")
            print("----------------------------\n")
        else:
            print(f"Nenhum instrutor encontrado com o CPF {cpf}.")
    except Exception as e:
        print(f"Erro ao buscar instrutor: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

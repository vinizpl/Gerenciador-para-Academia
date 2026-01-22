from database import conectar
from datetime import datetime

def inserir_aluno(nome, data_nascimento, email, telefone, id_plano):
    try:
        # Validação do formato da data
        datetime.strptime(data_nascimento, '%Y-%m-%d')
        
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO alunos (nome_completo, data_nascimento, email, telefone, id_plano) 
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nome, data_nascimento, email, telefone, id_plano)
        )
        conn.commit()
        print("Aluno inserido com sucesso!")
    except ValueError:
        print("Erro: Formato de data inválido. Use AAAA-MM-DD.")
    except Exception as e:
        print(f"Erro ao inserir aluno: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def listar_alunos():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            SELECT a.id_aluno, a.nome_completo, a.email, p.nome_plano 
            FROM alunos a
            JOIN planos p ON a.id_plano = p.id_plano
            ORDER BY a.nome_completo
        """)
        alunos = cur.fetchall()
        if not alunos:
            print("Nenhum aluno encontrado.")
            return

        print("\n--- Lista de Alunos ---")
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Plano: {aluno[3]}")
        print("-----------------------\n")
    except Exception as e:
        print(f"Erro ao listar alunos: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def atualizar_aluno(id_aluno, nome, data_nascimento, email, telefone, id_plano):
    try:
        # Validação do formato da data
        datetime.strptime(data_nascimento, '%Y-%m-%d')

        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE alunos 
            SET nome_completo = %s, data_nascimento = %s, email = %s, telefone = %s, id_plano = %s
            WHERE id_aluno = %s
            """,
            (nome, data_nascimento, email, telefone, id_plano, id_aluno)
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum aluno encontrado com o ID {id_aluno}.")
        else:
            print("Aluno atualizado com sucesso!")
    except ValueError:
        print("Erro: Formato de data inválido. Use AAAA-MM-DD.")
    except Exception as e:
        print(f"Erro ao atualizar aluno: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def remover_aluno(id_aluno):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhum aluno encontrado com o ID {id_aluno}.")
        else:
            print("Aluno removido com sucesso!")
    except Exception as e:
        print(f"Erro ao remover aluno: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_aluno_por_id(id_aluno):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            SELECT a.id_aluno, a.nome_completo, a.data_nascimento, a.email, a.telefone, a.data_matricula, p.nome_plano 
            FROM alunos a
            JOIN planos p ON a.id_plano = p.id_plano
            WHERE a.id_aluno = %s
        """, (id_aluno,))
        aluno = cur.fetchone()

        if aluno:
            print("\n--- Aluno Encontrado ---")
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Data de Nascimento: {aluno[2]}")
            print(f"Email: {aluno[3]}")
            print(f"Telefone: {aluno[4]}")
            print(f"Data de Matrícula: {aluno[5]}")
            print(f"Plano: {aluno[6]}")
            print("------------------------\n")
        else:
            print(f"Nenhum aluno encontrado com o ID {id_aluno}.")
    except Exception as e:
        print(f"Erro ao buscar aluno: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_aluno_por_email(email):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            SELECT a.id_aluno, a.nome_completo, a.email, p.nome_plano 
            FROM alunos a
            JOIN planos p ON a.id_plano = p.id_plano
            WHERE a.email = %s
        """, (email,))
        aluno = cur.fetchone()

        if aluno:
            print("\n--- Aluno Encontrado ---")
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Plano: {aluno[3]}")
            print("------------------------\n")
        else:
            print(f"Nenhum aluno encontrado com o email '{email}'.")
    except Exception as e:
        print(f"Erro ao buscar aluno: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

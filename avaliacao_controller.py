from database import conectar
from datetime import datetime

def inserir_avaliacao(id_aluno, id_instrutor, data, peso, altura, p_gordura, obs):
    try:
        datetime.strptime(data, '%Y-%m-%d')

        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO avaliacoes_fisicas 
            (id_aluno, id_instrutor, data_avaliacao, peso_kg, altura_cm, percentual_gordura, observacoes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (id_aluno, id_instrutor, data, peso, altura, p_gordura, obs)
        )
        conn.commit()
        print("Avaliação física inserida com sucesso!")
    except ValueError:
        print("Erro: Formato de data inválido. Use AAAA-MM-DD.")
    except Exception as e:
        print(f"Erro ao inserir avaliação: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def listar_avaliacoes_de_aluno(id_aluno):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            SELECT av.id_avaliacao, av.data_avaliacao, av.peso_kg, av.altura_cm, av.percentual_gordura, i.nome_completo
            FROM avaliacoes_fisicas av
            JOIN instrutores i ON av.id_instrutor = i.id_instrutor
            WHERE av.id_aluno = %s
            ORDER BY av.data_avaliacao DESC
        """, (id_aluno,))
        avaliacoes = cur.fetchall()

        if not avaliacoes:
            print(f"Nenhuma avaliação encontrada para o aluno com ID {id_aluno}.")
            return False

        print(f"\n--- Histórico de Avaliações do Aluno ID {id_aluno} ---")
        for av in avaliacoes:
            print(f"ID Avaliação: {av[0]}, Data: {av[1]}, Peso: {av[2]}kg, Altura: {av[3]}cm, % Gordura: {av[4]}, Instrutor: {av[5]}")
        print("--------------------------------------------------\n")
        return True
    except Exception as e:
        print(f"Erro ao listar avaliações: {e}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def remover_avaliacao(id_avaliacao):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM avaliacoes_fisicas WHERE id_avaliacao = %s", (id_avaliacao,))
        conn.commit()
        if cur.rowcount == 0:
            print(f"Nenhuma avaliação encontrada com o ID {id_avaliacao}.")
        else:
            print("Avaliação física removida com sucesso!")
    except Exception as e:
        print(f"Erro ao remover avaliação: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

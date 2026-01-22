from database import conectar
from treino_controller import ver_detalhes_do_treino # Reutilizaremos esta função!

def relatorio_treinos_por_instrutor():
    sql = """
        SELECT 
            i.nome_completo,
            COUNT(t.id_treino) AS quantidade_de_treinos
        FROM instrutores i
        LEFT JOIN treinos t ON i.id_instrutor = t.id_instrutor
        GROUP BY i.id_instrutor, i.nome_completo
        ORDER BY quantidade_de_treinos DESC;
    """
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(sql)
        resultados = cur.fetchall()
        print("\n Relatório: Treinos Criados por Instrutor")
        for res in resultados:
            print(f"Instrutor: {res[0]}, Treinos Criados: {res[1]}")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()


def relatorio_exercicios_populares():
    sql = """
        SELECT
            e.nome_exercicio,
            COUNT(te.id_treino) AS popularidade
        FROM exercicios e
        JOIN treino_exercicios te ON e.id_exercicio = te.id_exercicio
        GROUP BY e.id_exercicio, e.nome_exercicio
        HAVING COUNT(te.id_treino) >= 2
        ORDER BY popularidade DESC;
    """
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(sql)
        resultados = cur.fetchall()
        print("\n Relatório: Exercícios Mais Populares (em >= 2 treinos)")
        for res in resultados:
            print(f"Exercício: {res[0]}, Usado em: {res[1]} treinos")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def relatorio_alunos_desatualizados():
    sql = """
        SELECT 
            a.nome_completo,
            a.email,
            MAX(av.data_avaliacao) AS ultima_avaliacao
        FROM alunos a
        LEFT JOIN avaliacoes_fisicas av ON a.id_aluno = av.id_aluno
        GROUP BY a.id_aluno, a.nome_completo, a.email
        HAVING MAX(av.data_avaliacao) < (CURRENT_DATE - INTERVAL '6 months') OR MAX(av.data_avaliacao) IS NULL
        ORDER BY ultima_avaliacao ASC NULLS FIRST;
    """
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(sql)
        resultados = cur.fetchall()
        print("\n Relatório: Alunos com Avaliação Desatualizada (> 6 meses)")
        for res in resultados:
            ultima_data = res[2] if res[2] else "Nunca avaliado"
            print(f"Aluno: {res[0]}, Email: {res[1]}, Última Avaliação: {ultima_data}")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def relatorio_media_idade_por_plano():
    sql = """
        SELECT 
            p.nome_plano,
            TRUNC(AVG(EXTRACT(YEAR FROM AGE(a.data_nascimento)))) AS media_idade_anos
        FROM planos p
        JOIN alunos a ON p.id_plano = a.id_plano
        GROUP BY p.nome_plano
        ORDER BY p.nome_plano;
    """
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(sql)
        resultados = cur.fetchall()
        print("\n Relatório: Média de Idade por Plano")
        for res in resultados:
            print(f"Plano: {res[0]}, Média de Idade: {res[1]} anos")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def consulta_ultimo_treino_aluno(id_aluno):
    sql_ultimo_id = "SELECT id_treino FROM treinos WHERE id_aluno = %s ORDER BY data_criacao DESC LIMIT 1;"
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(sql_ultimo_id, (id_aluno,))
        resultado = cur.fetchone()
        
        if not resultado:
            print(f"Nenhum treino encontrado para o aluno com ID {id_aluno}.")
            return
        
        id_ultimo_treino = resultado[0]
        print(f"Consulta do último treino (ID: {id_ultimo_treino}) do aluno {id_aluno}:")
        # Reutiliza a função já pronta para mostrar os detalhes
        ver_detalhes_do_treino(id_ultimo_treino)
        
    except Exception as e:
        print(f"Erro ao consultar último treino: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

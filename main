import plano_controller as pc
import instrutor_controller as ic
import exercicio_controller as ec
import aluno_controller as ac
import treino_controller as tc
import avaliacao_controller as avc
import reports_controller as rp

def menu_planos():
    while True:
        print("\n Gerenciamento de Planos")
        print("1. Adicionar Novo Plano")
        print("2. Listar Todos os Planos")
        print("3. Atualizar Plano Existente")
        print("4. Remover Plano")
        print("5. Buscar Plano por ID")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do plano: ")
            valor = float(input("Valor mensal: "))
            descricao = input("Descrição: ")
            pc.inserir_plano(nome, valor, descricao)
        elif opcao == '2':
            pc.listar_planos()
        elif opcao == '3':
            id_plano = int(input("ID do plano a ser atualizado: "))
            nome = input("Novo nome do plano: ")
            valor = float(input("Novo valor mensal: "))
            descricao = input("Nova descrição: ")
            pc.atualizar_plano(id_plano, nome, valor, descricao)
        elif opcao == '4':
            id_plano = int(input("ID do plano a ser removido: "))
            pc.remover_plano(id_plano)
        elif opcao == '5':
            id_plano = int(input("ID do plano a ser buscado: "))
            pc.buscar_plano_por_id(id_plano)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_instrutores():
    while True:
        print("\n Gerenciamento de Instrutores")
        print("1. Adicionar Novo Instrutor")
        print("2. Listar Todos os Instrutores")
        print("3. Atualizar Instrutor Existente")
        print("4. Remover Instrutor")
        print("5. Buscar Instrutor por ID")
        print("6. Buscar Instrutor por CPF")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome completo do instrutor: ")
            cpf = input("CPF do instrutor: ")
            especialidade = input("Especialidade: ")
            ic.inserir_instrutor(nome, cpf, especialidade)
        elif opcao == '2':
            ic.listar_instrutores()
        elif opcao == '3':
            id_instrutor = int(input("ID do instrutor a ser atualizado: "))
            nome = input("Novo nome completo: ")
            especialidade = input("Nova especialidade: ")
            ic.atualizar_instrutor(id_instrutor, nome, especialidade)
        elif opcao == '4':
            id_instrutor = int(input("ID do instrutor a ser removido: "))
            ic.remover_instrutor(id_instrutor)
        elif opcao == '5':
            id_instrutor = int(input("ID do instrutor a ser buscado: "))
            ic.buscar_instrutor_por_id(id_instrutor)
        elif opcao == '6':
            cpf = input("CPF do instrutor a ser buscado: ")
            ic.buscar_instrutor_por_cpf(cpf)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_exercicios():
    while True:
        print("\nGerenciamento de Exercícios")
        print("1. Adicionar Novo Exercício")
        print("2. Listar Todos os Exercícios")
        print("3. Atualizar Exercício Existente")
        print("4. Remover Exercício")
        print("5. Buscar Exercício por ID")
        print("6. Buscar Exercício por Nome")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do exercício: ")
            grupo = input("Grupo muscular: ")
            instrucoes = input("Instruções de execução: ")
            ec.inserir_exercicio(nome, grupo, instrucoes)
        elif opcao == '2':
            ec.listar_exercicios()
        elif opcao == '3':
            id_ex = int(input("ID do exercício a ser atualizado: "))
            nome = input("Novo nome do exercício: ")
            grupo = input("Novo grupo muscular: ")
            instrucoes = input("Novas instruções: ")
            ec.atualizar_exercicio(id_ex, nome, grupo, instrucoes)
        elif opcao == '4':
            id_ex = int(input("ID do exercício a ser removido: "))
            ec.remover_exercicio(id_ex)
        elif opcao == '5':
            id_ex = int(input("ID do exercício a ser buscado: "))
            ec.buscar_exercicio_por_id(id_ex)
        elif opcao == '6':
            nome = input("Nome do exercício a ser buscado: ")
            ec.buscar_exercicio_por_nome(nome)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_alunos():
    while True:
        print("\n Gerenciamento de Alunos ")
        print("1. Adicionar Novo Aluno")
        print("2. Listar Todos os Alunos")
        print("3. Atualizar Aluno Existente")
        print("4. Remover Aluno")
        print("5. Buscar Aluno por ID")
        print("6. Buscar Aluno por Email")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome completo do aluno: ")
            data_nasc = input("Data de nascimento (AAAA-MM-DD): ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            print("Planos disponíveis:")
            pc.listar_planos()
            id_plano = int(input("ID do plano escolhido: "))
            ac.inserir_aluno(nome, data_nasc, email, telefone, id_plano)
        elif opcao == '2':
            ac.listar_alunos()
        elif opcao == '3':
            id_aluno = int(input("ID do aluno a ser atualizado: "))
            nome = input("Novo nome completo: ")
            data_nasc = input("Nova data de nascimento (AAAA-MM-DD): ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            print("Planos disponíveis:")
            pc.listar_planos()
            id_plano = int(input("Novo ID do plano: "))
            ac.atualizar_aluno(id_aluno, nome, data_nasc, email, telefone, id_plano)
        elif opcao == '4':
            id_aluno = int(input("ID do aluno a ser removido: "))
            ac.remover_aluno(id_aluno)
        elif opcao == '5':
            id_aluno = int(input("ID do aluno a ser buscado: "))
            ac.buscar_aluno_por_id(id_aluno)
        elif opcao == '6':
            email = input("Email do aluno a ser buscado: ")
            ac.buscar_aluno_por_email(email)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_treinos():
    while True:
        print("\n Gerenciamento de Treinos")
        print("1. Criar Nova Ficha de Treino")
        print("2. Adicionar Exercício a um Treino")
        print("3. Ver Detalhes de um Treino")
        print("4. Listar Treinos de um Aluno")
        print("5. Remover Ficha de Treino")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ac.listar_alunos()
            id_aluno = int(input("ID do aluno para o treino: "))
            ic.listar_instrutores()
            id_instrutor = int(input("ID do instrutor responsável: "))
            objetivo = input("Objetivo do treino (ex: Hipertrofia): ")
            tc.criar_treino(id_aluno, id_instrutor, objetivo)
        elif opcao == '2':
            id_treino = int(input("ID da ficha de treino para adicionar o exercício: "))
            ec.listar_exercicios()
            id_exercicio = int(input("ID do exercício a ser adicionado: "))
            series = int(input("Número de séries: "))
            repeticoes = input("Repetições (ex: 10-12): ")
            carga = float(input("Carga (kg): "))
            obs = input("Observações (opcional): ")
            tc.adicionar_exercicio_ao_treino(id_treino, id_exercicio, series, repeticoes, carga, obs)
        elif opcao == '3':
            id_treino = int(input("ID do treino para ver os detalhes: "))
            tc.ver_detalhes_do_treino(id_treino)
        elif opcao == '4':
            id_aluno = int(input("ID do aluno para listar os treinos: "))
            tc.listar_treinos_de_aluno(id_aluno)
        elif opcao == '5':
            id_treino = int(input("ID da ficha de treino a ser removida: "))
            tc.remover_treino(id_treino)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_avaliacoes():
    while True:
        print("\n Gerenciamento de Avaliações Físicas")
        print("1. Registrar Nova Avaliação")
        print("2. Listar Histórico de Avaliações de um Aluno")
        print("3. Remover uma Avaliação")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ac.listar_alunos()
            id_aluno = int(input("ID do aluno para a avaliação: "))
            ic.listar_instrutores()
            id_instrutor = int(input("ID do instrutor que realizou a avaliação: "))
            data = input("Data da avaliação (AAAA-MM-DD): ")
            peso = float(input("Peso (kg): "))
            altura = int(input("Altura (cm): "))
            p_gordura = float(input("Percentual de gordura (%): "))
            obs = input("Observações (opcional): ")
            avc.inserir_avaliacao(id_aluno, id_instrutor, data, peso, altura, p_gordura, obs)
        elif opcao == '2':
            id_aluno = int(input("ID do aluno para ver o histórico: "))
            avc.listar_avaliacoes_de_aluno(id_aluno)
        elif opcao == '3':
            id_avaliacao = int(input("ID da avaliação a ser removida: "))
            avc.remover_avaliacao(id_avaliacao)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_relatorios():
    while True:
        print("\n Relatórios e Consultas Avançadas")
        print("1. Quantidade de treinos por instrutor")
        print("2. Exercícios mais populares")
        print("3. Alunos com avaliações desatualizadas")
        print("4. Média de idade por plano")
        print("5. Consultar último treino de um aluno")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            rp.relatorio_treinos_por_instrutor()
        elif opcao == '2':
            rp.relatorio_exercicios_populares()
        elif opcao == '3':
            rp.relatorio_alunos_desatualizados()
        elif opcao == '4':
            rp.relatorio_media_idade_por_plano()
        elif opcao == '5':
            ac.listar_alunos()
            id_aluno = int(input("Digite o ID do aluno para consultar: "))
            rp.consulta_ultimo_treino_aluno(id_aluno)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_principal():
    while True:
        print("Sistema de Gerenciamento da Academia")
        print("1. Gerenciar Planos")
        print("2. Gerenciar Instrutores")
        print("3. Gerenciar Exercícios")
        print("4. Gerenciar Alunos")
        print("5. Gerenciar Treinos")
        print("6. Gerenciar Avaliações Físicas")
        print("7. Relatórios e Consultas Avançadas")
        print("0. Sair do Sistema")

        opcao = input("Escolha uma área para gerenciar: ")

        if opcao == '1':
            menu_planos()
        elif opcao == '2':
            menu_instrutores()
        elif opcao == '3':
            menu_exercicios()
        elif opcao == '4':
            menu_alunos()
        elif opcao == '5':
            menu_treinos()
        elif opcao == '6':
            menu_avaliacoes()
        elif opcao == '7':
            menu_relatorios()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

"""Naruto Uzumaki - Tô certo!"""

if __name__ == "__main__":
    menu_principal()

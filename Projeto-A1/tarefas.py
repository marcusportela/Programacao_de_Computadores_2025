# tarefas.py

# Estrutura de dados para armazenar as tarefas
# Cada tarefa será um dicionário com 'descricao', 'concluida' e 'prioridade'
# Usaremos uma lista (vetor) para armazenar esses dicionários
tarefas = []

def adicionar_tarefa(descricao, prioridade="média"):
    """Adiciona uma nova tarefa à lista de tarefas."""
    if not isinstance(descricao, str) or not descricao.strip():
        print("Erro: A descrição da tarefa não pode ser vazia.")
        return False
    if prioridade.lower() not in ["baixa", "média", "alta"]:
        print("Erro: Prioridade inválida. Use 'baixa', 'média' ou 'alta'.")
        return False
    tarefa = {
        "descricao": descricao.strip(),
        "concluida": False,
        "prioridade": prioridade.lower()
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com prioridade '{prioridade}'.")
    return True

def visualizar_tarefas():
    """Exibe todas as tarefas cadastradas."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    # Opcional: Ordenar tarefas por prioridade para melhor visualização
    # Usando uma matriz para mapear prioridades para ordenação
    prioridades_map = {"alta": 1, "média": 2, "baixa": 3}
    tarefas_ordenadas = sorted(tarefas, key=lambda t: prioridades_map.get(t['prioridade'], 99))

    print("\n--- SUAS TAREFAS ---")
    # Itera sobre o vetor de tarefas
    for i, tarefa in enumerate(tarefas_ordenadas):
        status = "✔️ Concluída" if tarefa["concluida"] else "⏳ Pendente"
        # Usando f-strings para formatação
        print(f"{i + 1}. [{status}] (Prioridade: {tarefa['prioridade'].capitalize()}) - {tarefa['descricao']}")
    print("-------------------\n")

def marcar_tarefa_concluida(indice):
    """Marca uma tarefa como concluída, dado seu índice."""
    if not isinstance(indice, int) or indice <= 0:
        print("Erro: O índice da tarefa deve ser um número inteiro positivo.")
        return False
    if 0 < indice <= len(tarefas):
        # Ajusta o índice para a lista baseada em 0
        tarefas[indice - 1]["concluida"] = True
        print(f"Tarefa '{tarefas[indice - 1]['descricao']}' marcada como concluída.")
        return True
    else:
        print("Erro: Índice de tarefa inválido.")
        return False

def remover_tarefa(indice):
    """Remove uma tarefa da lista, dado seu índice."""
    if not isinstance(indice, int) or indice <= 0:
        print("Erro: O índice da tarefa deve ser um número inteiro positivo.")
        return False
    if 0 < indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida.")
        return True
    else:
        print("Erro: Índice de tarefa inválido.")
        return False

def menu():
    """Exibe o menu de opções e processa a escolha do usuário."""
    while True: # Laço de repetição principal do menu
        print("--- GERENCIADOR DE TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")
        print("-----------------------------")

        escolha = input("Escolha uma opção: ")

        # Estruturas condicionais (if/elif/else) para as opções
        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade (baixa, média, alta - padrão: média): ").strip() or "média"
            adicionar_tarefa(descricao, prioridade)
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            try:
                indice = int(input("Digite o número da tarefa a ser marcada como concluída: "))
                marcar_tarefa_concluida(indice)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif escolha == '4':
            try:
                indice = int(input("Digite o número da tarefa a ser removida: "))
                remover_tarefa(indice)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif escolha == '5':
            print("Saindo do Gerenciador de Tarefas. Até mais!")
            break # Encerra o laço de repetição
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()
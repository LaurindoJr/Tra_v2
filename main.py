"""
Script principal para executar e comparar os algoritmos de otimização
para o Problema do Caixeiro Viajante (TSP).

Este script serve como ponto de entrada para a primeira parte do projeto.
Ele carrega a definição do problema TSP a partir de um arquivo, executa
diferentes algoritmos (Hill Climbing, Algoritmo Genético, Colônia de Formigas),
coleta resultados (distância da rota, tempo de execução), gera visualizações
(grafo base, rotas aleatórias, rotas solução, gráficos comparativos) e 
apresenta um resumo final no terminal.
"""
import argparse # Para lidar com argumentos de linha de comando (embora não usado ativamente aqui)
from util import TSPProblem # Classe que encapsula a definição do problema TSP (cidades, distâncias)
# Funções de visualização específicas para o TSP
from util.TSP.visualization import plot_solution, plot_convergence, plot_comparison # Classes que implementam os algoritmos TSP
from algoritimos import GeneticAlgorithm, AntColony, HillClimbing
import time # Para medir o tempo de execução dos algoritmos
import os # Para operações de sistema de arquivos (criar diretórios de plots

def run_algorithm(problem, algorithm_class, **kwargs): #Executa um único algoritmo TSP e retorna um dicionário com os resultados.
    start_time = time.time()  # Marca o tempo de início
    solver = algorithm_class(problem, **kwargs) # Cria uma instância do algoritmo, passando o problema e outros parâmetros
    solution = solver.solve() # Chama o método principal do algoritmo para encontrar a solução
    exec_time = time.time() - start_time  # Marca o tempo de fim e calcula a duração
    distance = problem.path_distance(solution) # Calcula a distância total da rota encontrada usando um método do problema

# Retorna os resultados organizados em um dicionário
    return {
        'solution': solution, # A lista ordenada de cidades na rota
        'distance': distance, # O custo total (distância) da rota
        'time': exec_time, # O tempo que o algoritmo levou para executar
        'convergence': getattr(solver, 'convergence_data', None) # Dados para gráfico de convergência, se o algoritmo fornecer
    }


def main():
    """
    Função principal que orquestra a execução da Parte 1 (TSP).
    
    - Carrega o problema.
    - Gera visualizações iniciais (grafo base, rotas aleatórias).
    - Define e executa cada algoritmo configurado.
    - Coleta e imprime resultados individuais.
    - Gera visualizações das soluções e gráficos comparativos.
    - Imprime um resumo final comparando os algoritmos.
    """

    parser = argparse.ArgumentParser(description="TSP Solver for Non-Complete Graphs") # Configura o parser de argumentos (poderia ser usado para passar o nome do arquivo de distâncias, etc.)
    args = parser.parse_args() # Lê os argumentos (nenhum definido aqui, então não faz nada)

    # Load problem
    # Tenta carregar a definição do problema do arquivo especificado
    try:
        problem = TSPProblem('distancias.txt') # Cria a instância do problema
    except Exception as e:  # Informa o usuário se houver erro ao carregar o arquivo
        print(f"Error loading problem: {str(e)}")
        return # Encerra a execução se o problema não puder ser carregado

  # Imprime informações básicas sobre o problema carregado
    print(f"\nSolving TSP with {len(problem.cities)} cities starting at {problem.start_city}")
    print(f"Cities: {', '.join(problem.cities)}")

    # Define os algoritmos que serão executados e seus respectivos parâmetros.
    # Cada entrada no dicionário contém a classe do algoritmo e um dicionário de parâmetros.

    # Algorithm configurations
    algorithms = {
        'Hill Climbing': (HillClimbing, {'max_iterations': 1000}), # Busca local simples
        'Genetic Algorithm': (GeneticAlgorithm, {'population_size': 50, 'generations': 100}), # Baseado em evolução
        'Ant Colony': (AntColony, {'num_ants': 10, 'iterations': 50}) # Baseado em feromonios
    }

    # Gera visualizações iniciais# Dicionários para armazenar os resultados e dados de convergência de cada algoritmo
    results = {}
    convergence_data = {}

    # Itera sobre cada algoritmo definido na configuração
    for name, (algo_class, params) in algorithms.items():
        print(f"\nRunning {name}...")
        try:
            # Chama a função auxiliar para executar o algoritmo e coletar resultados
            result = run_algorithm(problem, algo_class, **params)
            results[name] = result # Armazena os resultados

            # Verifica se o algoritmo retornou dados de convergência
            if result['convergence']:
                convergence_data[name] = result['convergence']
            # Gera visualizações para a solução encontrada
            print(f"Solution: {' -> '.join(result['solution'])} -> {result['solution'][0]}")
            print(f"Distance: {result['distance']:.2f}")
            print(f"Time: {result['time']:.2f}s")

            # Gera e salva um gráfico visualizando a rota encontrada por este algoritmo
            plot_solution(problem, result['solution'], f"{name} Solution", True)
        except Exception as e: # Captura e informa erros durante a execução de um algoritmo específico
            print(f"Error running {name}: {str(e)}")
            continue # Continua para o próximo algoritmo

    if convergence_data: # Verifica se há dados de convergência para plotar
        plot_convergence(convergence_data, "Algorithm Convergence", save=True)
    plot_comparison(results, save=True)

    print("\nAlgorithm Comparison:")
    # Imprime um resumo dos resultados de cada algoritmo                            
    print("{:<20} {:<15} {:<15}".format("Algorithm", "Distance", "Time (s)"))
    for name, result in results.items():
        print("{:<20} {:<15.2f} {:<15.2f}".format(name, result['distance'], result['time']))

# Ponto de entrada padrão para execução do script Python
if __name__ == "__main__":
    main() # Chama a função principal
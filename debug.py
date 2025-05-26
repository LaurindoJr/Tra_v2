from util.TSP.tsp_problem import TSPProblem
from algoritimos.TSP.genetic_algorithm import GeneticAlgorithm

def debug():
    problem = TSPProblem("distancias.txt")
    print("\nCidades:", problem.cities)
    print("Cidade inicial:", problem.start_city)

    # Verifica conexões
    print("\nConexões faltantes:")
    for i, city1 in enumerate(problem.cities):
        for city2 in problem.cities[i + 1:]:
            if problem.get_distance(city1, city2) == float('inf'):
                print(f"{city1} <-> {city2}: desconectado")

    # Testa o algoritmo
    try:
        ga = GeneticAlgorithm(problem, population_size=10, generations=5)
        solution = ga.solve()
        print("\nSolução encontrada:", solution)
        print("Distância:", problem.path_distance(solution))
    except Exception as e:
        print("\nErro durante execução:", str(e))


if __name__ == "__main__":
    debug()
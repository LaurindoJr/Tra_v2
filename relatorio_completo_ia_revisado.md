# Relatório Completo Revisado do Projeto 01: Otimização com Metaheurísticas

## Introdução Geral

Este documento apresenta um relatório consolidado, detalhado e revisado referente ao Projeto 01 da disciplina de Inteligência Artificial. O projeto abrange a aplicação e comparação de diferentes algoritmos de otimização metaheurística em dois problemas clássicos e distintos: o Problema do Caixeiro Viajante (TSP) em um grafo específico e a Otimização Contínua da função multidimensional de Schwefel. O objetivo principal é avaliar a eficácia, eficiência e características de convergência de algoritmos como Algoritmo Genético (GA), Otimização por Colônia de Formigas (ACO) e Hill Climbing (HC) em cenários de otimização combinatória e contínua, respectivamente.

O relatório está estruturado em duas partes principais, cada uma dedicada a um dos problemas abordados. Para cada problema, descrevemos a metodologia empregada, as implementações dos algoritmos, os resultados obtidos através de execuções e as análises comparativas baseadas em métricas de desempenho como qualidade da solução (distância no TSP, fitness na função Schwefel), precisão (para a função Schwefel) e tempo de execução. As análises são suportadas por visualizações gráficas que ilustram o problema base, exemplos de soluções, a própria função objetivo (no caso da Schwefel) e a evolução do processo de otimização, com saídas de terminal contextualizadas para maior clareza.

---

## Parte 1: Problema do Caixeiro Viajante (TSP)

### 1.1. Descrição do Problema e Grafo Base

O Problema do Caixeiro Viajante (TSP) é um problema de otimização combinatória NP-difícil. O objetivo é encontrar o caminho mais curto possível que visite um conjunto de cidades exatamente uma vez e retorne à cidade de origem. Neste projeto, o problema foi definido sobre um grafo específico com 18 cidades, cujas conexões e distâncias foram fornecidas no arquivo `distancias.txt`. A cidade de partida foi definida como a cidade "1".

Para melhor compreensão do espaço de busca, o gráfico abaixo ilustra o grafo base do problema, mostrando todas as 18 cidades e as conexões diretas possíveis entre elas, juntamente com suas respectivas distâncias. Note que este não é um grafo completo; nem todas as cidades estão diretamente conectadas.

**Grafo Base do Problema TSP:**

![Grafo Base TSP](codigo_fonte/plots/TSP_Base_Graph_20250523_103904.png)

*Este gráfico mostra a estrutura de conectividade e as distâncias entre as cidades, representando o desafio que os algoritmos precisam superar para encontrar a rota ótima.*

### 1.2. Metodologia e Implementação

Foram implementados três algoritmos metaheurísticos em Python para resolver a instância do TSP fornecida:

1.  **Hill Climbing (HC) com Permutação:** Inicia com uma rota aleatória válida e iterativamente tenta melhorar a solução realizando pequenas modificações (permutações). Aceita apenas movimentos que diminuem a distância total.
2.  **Algoritmo Genético (GA):** Abordagem populacional que simula a evolução natural com seleção, crossover e mutação de rotas. Configuração: população de 50, 100 gerações.
3.  **Otimização por Colônia de Formigas (ACO):** Inspirado no comportamento de formigas, usa feromônios artificiais para guiar a construção de rotas. Configuração: 10 formigas, 50 iterações.

O código principal (`main.py`) carrega o problema, gera visualizações, executa os algoritmos e compara os resultados. Saídas de terminal são prefixadas com `[TSP]`.

### 1.3. Exemplos de Rotas Aleatórias Válidas

Visualizar rotas aleatórias válidas ajuda a entender a complexidade. Elas cumprem as regras, mas geralmente são muito longas:

**Exemplo de Rota Aleatória Válida 1:**

![Rota Aleatória 1](codigo_fonte/plots/TSP_Random_Valid_Route_#1_20250523_103905.png)

**Exemplo de Rota Aleatória Válida 2:**

![Rota Aleatória 2](codigo_fonte/plots/TSP_Random_Valid_Route_#2_20250523_103907.png)

*Estas rotas ilustram a necessidade de algoritmos inteligentes para encontrar caminhos curtos.*

### 1.4. Resultados da Execução dos Algoritmos TSP

Resultados da última execução (prefixo `[TSP]` omitido):

```
--- Executando Algoritmos TSP ---
Executando Hill Climbing...
Solução: 1 -> ... -> 1
Distância: 429.00, Tempo: 0.10s
Executando Genetic Algorithm...
Solução: 1 -> ... -> 1
Distância: 398.00, Tempo: 2.14s
Executando Ant Colony...
Solução: 1 -> ... -> 1
Distância: 410.00, Tempo: 0.06s
--- Comparação Final dos Algoritmos TSP ---
Algorithm            Distance        Time (s)       
--------------------------------------------------
Genetic Algorithm    398.00          2.14           
Ant Colony           410.00          0.06           
Hill Climbing        429.00          0.10           
--------------------------------------------------
```

### 1.5. Visualizações das Soluções e Comparações TSP

**Soluções Finais Encontradas:**

*   **Hill Climbing:**
    ![Solução Hill Climbing TSP](codigo_fonte/plots/Hill_Climbing_Solution_20250523_103908.png)
*   **Algoritmo Genético:**
    ![Solução Algoritmo Genético TSP](codigo_fonte/plots/Genetic_Algorithm_Solution_20250523_103912.png)
*   **Colônia de Formigas:**
    ![Solução Colônia de Formigas TSP](codigo_fonte/plots/Ant_Colony_Solution_20250523_103913.png)

**Gráficos Comparativos:**

*   **Convergência:**
    ![Convergência TSP](codigo_fonte/output_plots/convergence_20250523_103914.png)
*   **Comparação Final:**
    ![Comparação TSP](codigo_fonte/output_plots/comparison_20250523_103914.png)

### 1.6. Análise dos Resultados do TSP

*   **Qualidade:** GA encontrou a melhor solução (398.00) na última execução, mas resultados podem variar. ACO foi consistentemente bom.
*   **Tempo:** ACO e HC foram muito rápidos; GA foi significativamente mais lento.
*   **Conclusão:** Há um trade-off entre qualidade (GA pode ser melhor, mas é lento) e velocidade (ACO/HC são rápidos, mas podem não achar o ótimo absoluto). A escolha depende da prioridade.

---

## Parte 2: Otimização Contínua da Função Schwefel

### 2.1. Descrição do Problema e Visualização da Função

A segunda parte foca na otimização da função Schwefel em 5 dimensões (`n=5`), com variáveis `xi` em `[-500, 500]`. A função é:

`f(x) = 418.9829 * n - Σ(xi * sin(sqrt(|xi|)))`

O objetivo é encontrar o valor mínimo desta função. Ela é conhecida por ser difícil de otimizar, pois possui muitos "vales" (mínimos locais) onde um algoritmo pode ficar "preso", achando que encontrou a melhor solução, quando na verdade existe um vale ainda mais profundo (o mínimo global) em outro lugar.

Para entender melhor o desafio, vamos visualizar a função Schwefel em 2 dimensões (usando apenas `x1` e `x2`). Embora nosso problema real tenha 5 dimensões (impossível de visualizar diretamente), a versão 2D mostra a mesma característica de múltiplos mínimos locais.

**Visualização 2D (Mapa de Contorno):**

![Função Schwefel 2D](codigo_fonte/schwefel_optimization/schwefel_plots/schwefel_function_2d_20250523_104510.png)

*Pense neste gráfico como um mapa topográfico. As cores representam a "altitude" (o valor da função Schwefel). Cores mais escuras (azul/roxo) indicam "vales" mais profundos (valores menores da função, que são melhores soluções). Cores mais claras (amarelo) indicam "picos" (valores maiores). Observe que existem muitos vales espalhados. O ponto vermelho marca a localização aproximada do vale mais profundo de todos (o mínimo global). O desafio para os algoritmos é navegar por este mapa e encontrar o ponto vermelho, sem ficar preso em um dos outros vales menos profundos.*

**Visualização 3D (Superfície):**

![Função Schwefel 3D](codigo_fonte/schwefel_optimization/schwefel_plots/schwefel_function_3d_20250523_104510.png)

*Este gráfico mostra a mesma função como uma paisagem tridimensional. A altura da superfície em cada ponto representa o valor da função. Novamente, vemos uma paisagem muito "acidentada", cheia de vales e picos. O ponto vermelho flutuando marca a localização e a "profundidade" do mínimo global. Os algoritmos de otimização tentam "descer" por esta paisagem para encontrar o ponto mais baixo possível (o ponto vermelho), mas podem facilmente ficar presos em um dos muitos outros vales que não são o mais profundo.*

### 2.2. Metodologia e Implementação

Três algoritmos foram adaptados para este problema contínuo:

1.  **Algoritmo Genético (GA):** Adaptado para variáveis contínuas. Configuração: população 100, 300 gerações.
2.  **Otimização por Colônia de Formigas para Contínuo (ACO_R):** Variante do ACO para espaços contínuos. Configuração: 50 formigas, 200 iterações.
3.  **Hill Climbing com Reinício Aleatório (HC):** Busca local com 100 reinícios.

Comparamos o melhor valor da função (fitness), a precisão (distância ao mínimo global conhecido em 5D) e o tempo.

### 2.3. Resultados da Otimização da Função Schwefel

Resultados da execução anterior:

```
--- Comparação Final dos Algoritmos (Função Schwefel) ---
Algoritmo                 Melhor Fitness       Precisão (Dist. Mín) Tempo (s)      
--------------------------------------------------------------------------------
Ant Colony (ACO_R)        118.4384             723.4936             1.02           
Hill Climbing (Restarts)  339.1806             757.0288             0.38           
Genetic Algorithm         473.7571             1446.9508            1.24           
--------------------------------------------------------------------------------
```

### 2.4. Visualizações da Otimização da Função Schwefel (Desempenho dos Algoritmos)

**Gráfico de Convergência:**

![Gráfico de Convergência Schwefel](codigo_fonte/schwefel_optimization/schwefel_plots/schwefel_convergence.png)

*Mostra como o melhor valor encontrado por cada algoritmo diminui ao longo do tempo/iterações.*

**Gráfico de Comparação:**

![Gráfico de Comparação Schwefel](codigo_fonte/schwefel_optimization/schwefel_plots/schwefel_comparison.png)

*Compara o valor final, a precisão e o tempo dos algoritmos.*

### 2.5. Análise dos Resultados da Função Schwefel

*   **Fitness e Precisão:** ACO_R obteve o melhor resultado (menor fitness, menor distância ao mínimo global), mostrando-se mais capaz de navegar pela paisagem complexa da função Schwefel.
*   **Convergência:** ACO_R e HC mostraram melhorias significativas. O GA convergiu mais lentamente para uma solução inferior.
*   **Tempo:** HC foi o mais rápido, mas menos preciso que ACO_R. GA foi o mais lento.

**Conclusão da Parte 2:** Visualizar a função Schwefel ajuda a entender por que ela é desafiadora. O ACO_R foi o mais eficaz em encontrar boas soluções nesta paisagem complexa, embora não seja o mais rápido. O HC com reinícios é rápido, mas menos preciso. O GA teve mais dificuldades.

---

## Conclusão Geral do Projeto (Revisada e Enriquecida)

Este projeto comparou metaheurísticas em otimização combinatória (TSP) e contínua (Função Schwefel), com visualizações aprimoradas para maior clareza.

No TSP, os gráficos do grafo base e rotas aleatórias contextualizam o problema. Os resultados mostram que GA pode achar ótimas soluções, mas é lento. ACO oferece um bom equilíbrio entre qualidade e velocidade. HC é rápido, mas pode ficar preso em soluções inferiores.

Na otimização da função Schwefel, os gráficos 2D e 3D ilustram a dificuldade causada pelos múltiplos mínimos locais. O ACO_R se destacou na qualidade da solução, enquanto HC foi mais rápido, e GA teve desempenho inferior com os parâmetros usados.

A análise reforça que não há metaheurística universalmente superior. A escolha depende do problema, dos parâmetros e das prioridades (qualidade vs. tempo). As visualizações adicionadas, tanto do problema quanto da função objetivo, juntamente com as saídas de terminal contextualizadas, melhoram significativamente a compreensão dos desafios e dos resultados obtidos.


import numpy as np
from queue import PriorityQueue
import time
import os


class Graph():
    def __init__(self, tam):
        self.dist = np.zeros(shape=(tam))
        for i in range(tam):
            self.dist[i] = int(1e18)
        self.graph = list()
        for _ in range(tam):
            self.graph.append(list())
    
    def add_edge(self, u, v, d):
        self.graph[u].append((v, d))
        self.graph[v].append((u, d))
    
    def Dijkstra(self, initial):
        q = PriorityQueue()
        q.put((0, initial))
        self.dist[initial] = 0
        
        while not q.empty():
            d, u = q.get()
            
            print(f"Analisando vertice {u} que tem uma distância {d} de {initial}")
            time.sleep(3)
            
            if d > self.dist[u]:
                continue
            
            for to, di in self.graph[u]:
                print(f"Checando se a distancia de {u} até {to} mais a distancia de {initial} até {u} é menor que a distância de {initial} até {to} ja encontrada")
                time.sleep(3)
                
                if d + di < self.dist[to]:
                    print(f"Sim a distancia é menor sendo {di + d} a distância passando por {u} e {self.dist[to]} a distancia direto")
                    time.sleep(3)
                    self.dist[to] = d + di
                    q.put((d+di, to))
            
            self.print_dist()
            time.sleep(5)
            os.system('cls')
            
    def print_dist(self):
        for i in range(len(self.dist)):
            print(f"A distância até {i} é {'inf' if self.dist[i] == int(1e18) else str(self.dist[i])}")



n = int(input("Digite o tamanho do grafo "))
m = int(input("Digite o numero de arestas"))
g = Graph(n)
print(f"Digite {m} as arestas no seguinte formato: <vertice1 vertice2 distancia> e no final aperte enter para inserir a próxima")
for _ in range(m):
    u, v, d = map(int, input().split())
    g.add_edge(u, v, d)
print(f"Agora iremos mostrar como acontece passo a passo o dijkstra, apenas escolha o ponto inicial de 0 a {n-1}")
initial = int(input())

g.Dijkstra(initial)

print("Resultado final:")
g.print_dist()
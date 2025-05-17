from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Используем defaultdict для хранения списка смежности
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Добавляет ребро между вершинами u и v в неориентированном графе.
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        """
        Обход графа в глубину (DFS) с использованием стека.
        Сложность: O(|E| + |V|), где |E| — количество рёбер, |V| — количество вершин.
        """
        visited = set()  # Множество для хранения посещённых вершин
        stack = [start]  # Стек для обхода

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")  # Обрабатываем вершину
                visited.add(vertex)
                # Добавляем всех непосещённых соседей в стек
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start):
        """
        Обход графа в ширину (BFS) с использованием очереди.
        Сложность: O(|E| + |V|), где |E| — количество рёбер, |V| — количество вершин.
        """
        visited = set()  # Множество для хранения посещённых вершин
        queue = deque([start])  # Очередь для обхода
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")  # Обрабатываем вершину
            # Добавляем всех непосещённых соседей в очередь
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Пример использования
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("DFS (обход в глубину):")
    g.dfs(0)  # Ожидаемый вывод: 0 2 3 4 1

    print("\nBFS (обход в ширину):")
    g.bfs(0)  # Ожидаемый вывод: 0 1 2 3 4
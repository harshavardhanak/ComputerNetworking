class Network:
    def __init__(self, n):
        self.matrix = []
        self.n = n

    def addlink(self, u, v, w):
        self.matrix.append((u, v, w))

    def printtable(self, dist, src):
        print("Vector Table of {}".format(chr(ord('A')+src)))
        print("{0}\t{1}".format("Dest", "cost"))
        for i in range(self.n):
            print("{0}\t{1}".format(chr(ord('A')+i), dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def algor(self, src):

        # Step 1: Initialize distances from src to all other vertices

        dist = [99] * self.n
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.n - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.matrix:
                if dist[u] != 99 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        # print all distance
        self.printtable(dist, src)


def main():
    matrix = []
    print("Enter No. of Nodes : ")
    n = int(input())
    print("Enter the Adjacency Matrix :")
    for i in range(n):
        m = list(map(int, input().split(" ")))
        matrix.append(m)
    g = Network(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                g.addlink(i, j, 1)

    for _ in range(n):
        g.algor(_)
main()
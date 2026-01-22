import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # start queue
        Q = deque([[start]])
        # create visited set (only has start node)
        visited = set([start])
        # define traversal order list (ordered list of how nodes are visited)
        traversal_order = [start]

        # check edge case:
        if start == end:
            return [start]
        
        # loop through all the nodes
        while Q:
            # extract first edge (v), set current path, and node
            current_path = Q.popleft()
            N = current_path[-1]

            # traverse through each neighbor of the current node
            for neighbor in self.graph.neighbors(N):
                # check if neighbor visited
                # if not visited, add to visited set and traversal order
                # also add it to current path (the shortest path candidate)
                # if target node (end) found, return shortest path candidate
                # ^ this is bc when BFS first visits a node, it has the shortest path to it by default
                if neighbor not in visited:
                    visited.add(neighbor)
                    traversal_order.append(neighbor)
                    shortest_path_candidate = list(current_path)
                    shortest_path_candidate.append(neighbor)

                    if end and neighbor == end:
                        return shortest_path_candidate
                    Q.append(shortest_path_candidate)

        # If there is no end node
        if end is None:
            return traversal_order
        # return none if path is not found
        return None

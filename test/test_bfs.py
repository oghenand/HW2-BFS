# write tests for bfs
import pytest
from search.graph import Graph
import networkx as nx
from collections import deque
import random

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    filename = 'data/tiny_network.adjlist'
    graphObj = Graph(filename)
    start_node = random.choice(list(graphObj.graph.nodes()))
    traversal_order = graphObj.bfs(start=start_node)
    bfs_tree = nx.bfs_tree(graphObj.graph, source=start_node)
    bfs_traversal_order = list(bfs_tree.nodes())

    assert traversal_order == bfs_traversal_order, "Traversal order incorrect!"

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    filename = 'data/citation_network.adjlist'
    graphObj = Graph(filename)
    start_node = random.choice(list(graphObj.graph.nodes()))

    bfs_tree = nx.bfs_tree(graphObj.graph, source=start_node)
    bfs_traversal_order = list(bfs_tree.nodes())
    
    # test case 1: if no end input, return BFS traversal
    assert graphObj.bfs(start=start_node) == bfs_traversal_order

    # test case 2: if end node and path does not exist, return None
    end_node_test_case_2 = ''
    assert graphObj.bfs(start=start_node, end=end_node_test_case_2) == None, "BFS must return none for path that does not exist!"
    
    # test case 3: if end node and path does exist, return path
    end_node_test_case_3 = random.choice(list(graphObj.graph.nodes()))
    true_path = nx.shortest_path(graphObj.graph, source=start_node, target=end_node_test_case_3)
    assert graphObj.bfs(start=start_node, end=end_node_test_case_3) == true_path, "BFS returns wrong path!"


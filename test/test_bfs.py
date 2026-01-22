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
    assert graphObj.bfs(start=start_node) == bfs_traversal_order, "BFS returns incorrect traversal order with no end input"

    # test case 2: if end node and path does not exist, return None
    end_node_test_case_2 = ''
    with pytest.raises(ValueError):
        graphObj.bfs(start=start_node, end=end_node_test_case_2)
    
    # test case 3: if end node and path does exist, return path
    # find reachable nodes from start node and pick one
    reachable_nodes = list(nx.descendants(graphObj.graph, source=start_node)) + [start_node]
    end_node_test_case_3 = random.choice(reachable_nodes)

    # find true path with nx
    true_path = nx.shortest_path(graphObj.graph, source=start_node, target=end_node_test_case_3)
    # find shortest path with bfs
    bfs_path = graphObj.bfs(start=start_node, end=end_node_test_case_3)

    # compare and assert
    # first check if start and end nodes the same
    assert start_node == bfs_path[0], "BFS has wrong start node!"
    assert end_node_test_case_3 == bfs_path[-1], "BFS has wrong end node!"

    # check if path lens the same (multiple shortest paths can exist!)
    assert len(true_path) == len(bfs_path)
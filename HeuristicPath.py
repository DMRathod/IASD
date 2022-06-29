import sys
import numpy as np

def compute_shortest_heuristic_path_with_intent(connecting_point_graph, p_source, p_destination, intent):
    init_graph = {}
    nodes_with_intent = []
    print("Points with intent : ", end=" ")
    for key, values in connecting_point_graph.items():
        init_graph[key.name] = {}
        if key.intent_id == intent:
            dis_destination = np.sqrt((key.x_coordinate - p_destination.x_coordinate) ** 2 + (key.y_coordinate - p_destination.y_coordinate) ** 2)
            source_destination = np.sqrt((p_source.x_coordinate - p_destination.x_coordinate) ** 2 + (p_source.y_coordinate - p_destination.y_coordinate) ** 2)
            if dis_destination <= (0.75) * source_destination:
                print(key.name, end=" ")
                # print(dis_destination, source_destination)
                nodes_with_intent.append(key)
        for i in values:
            if i[1] != 0:
                init_graph[key.name][i[0].name] = i[1]
    print()

    if nodes_with_intent != []:
        # this small code will find the closest node with intent
        lower_distance = float('inf')
        intent_point = None
        for each in nodes_with_intent:
            d_to_destination = np.sqrt((each.x_coordinate - p_destination.x_coordinate) ** 2 + (each.y_coordinate - p_destination.y_coordinate) ** 2)
            d_to_source = np.sqrt((each.x_coordinate - p_source.x_coordinate) ** 2 + (each.y_coordinate - p_source.y_coordinate) ** 2)
            d = min(d_to_source, d_to_destination)
            if lower_distance > d:
                lower_distance = d
                intent_point = each

        if intent_point == None:
            sys.exit()
        # print(init_graph)
        graph = Graph(init_graph.keys(), init_graph)
        # print("Nodes :", graph)
        # for key, value in graph.items():
        # print(key, value)
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=p_source.name)
        path, heuristic_cost1 = print_result(previous_nodes, shortest_path, start_node=p_source.name, target_node=intent_point.name)
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=intent_point.name)
        temp_rslt, heuristic_cost2 = print_result(previous_nodes, shortest_path, start_node=intent_point.name, target_node=p_destination.name, flag=False)
        path = path + (" -> "+temp_rslt if temp_rslt else temp_rslt)
        heuristic_cost1 += heuristic_cost2
        print("Path : ", path)
        print("Heuristic_cost : ", heuristic_cost1)
    else:
        print("Intent aware path does not exist within the range hence context-aware path is as below :")
        graph = Graph(init_graph.keys(), init_graph)
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=p_source.name)
        path, heuristic_cost1 = print_result(previous_nodes, shortest_path, start_node=p_source.name, target_node=p_destination.name)
        print("Path : ", path)
        print("Heuristic_cost : ", heuristic_cost1)

    #
    # for k, v in connecting_point_graph.items():
    #     print(k.name, "=>", end='')
    #     print("V", v)
    #     for e in v:
    #         print(e[1], end=' ')
    #     print()




def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node==None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node, flag=True):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    # print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    if flag:
        return " -> ".join(reversed(path[:])), shortest_path[target_node]
    else:
        return " -> ".join(reversed(path[:-1])), shortest_path[target_node]


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


# print(connecting_graph)
# graph = Graph(nodes, init_graph)

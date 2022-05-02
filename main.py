import Node
import networkx as nx
import Fog as fg
import ClusterHead
import CreateConnectedClusterHeads as CG
import CreateConnectingPoints as CP
import ClusterHead as CH
import matplotlib.pyplot as plt
import CreateLattice as Cl

if __name__ == '__main__':

    graph = CG.cluster_head_list()


    point_graph = CP.CreateConnectingPoint()
    connecting_point_graph = point_graph.connecting_point_adjacency_list
    print(connecting_point_graph)



    for item in connecting_point_graph.items():
        print(item[0].name, end="")
        for it in item[1]:
            print(it[0].name, end='')



    # print(graph)
    visited = {}
    for key in graph.keys():
        visited[key] = False

    source_coordinates = (20, 50)
    destination_coordinates = (110, 8)




    # Config1 =  CG.Create_clusters()
    # result = Config1.assign_connecting_points()
    # print(result)
    # for r in result:
    #     print(r.name, end='')






    # print(graph)
    # print(graph.keys())
    # visited = [False] * (len(graph)+1)
    # print(visited)


    # this will give us the list of cluster with which we need to communicate
    clusterslist = CH.get_list_of_clusters(graph, source_coordinates, destination_coordinates)

    # creating physical location points for generating the graph
    # points = CP.CreateConnectingPoint.get_connecting_points()









    # print(clusterslist)
    if clusterslist:
        for i in clusterslist:
            print(f'({i.x_coordinate}, {i.y_coordinate})', end=" ")

    n1 = Node.Node('N' + str(1), ['s1', 's2', 's3'], ['d1', 'd2'])
    n2 = Node.Node(2, ['s1', 's2'], ['d1', 'd3', 'd4'])
    n3 = Node.Node(3, ['s3'], ['d1', 'd2'])
    # n0 = Node.Node(0, ['s4'], ['d3', 'd4'])

    dict1 = n1.delta()
    # print(n1.ID)
    # Cl.activate_points(dict1)
    # print("dict : ", len(dict1), dict1)
    # n5 = Node.Node(5, ['s1', 's2', 's3', 's4', 's5', 's6'], ['d1', 'd2', 'd3', 'd4', 'd5'])
    # n4 = Node.Node(4, ['s1', 's2', 's3', 's4', 's5'], ['d1', 'd2', 'd3'])

    # n6 = Node.Node(6, ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8'], ['d8', 'd9', 'd10'])
    # n7 = Node.Node(7, ['s1', 's2', 's3', 's4'], ['d8', 'd9'])
    # n8 = Node.Node(8, ['s1', 's2'], ['d10'])

    # print(n5)
    # help(n5)
    # dir(n5)
    # print(n1.set_of_services)
    f1 = fg.Fog(101)
    # f2 = fg.Fog(102, 'fog2')

    network = nx.Graph()
    network.add_node(n1)
    network.add_node(n2)
    network.add_node(n3)
    # network.add_node(n4)
    # network.add_node(n5)
    # network.add_node(n6)
    # network.add_node(n7)
    # network.add_node(n8)
    # network.add_node(f1)
    # network.add_node(f2)
    #
    nodes = [n1, n2, n3]
    for i in nodes:
        network.add_edge(f1, i)

    # network.add_edge(f1, n1)
    # network.add_edge(f1, n2)
    # network.add_edge(f1, n3)
    # network.add_edge(f1, n4)
    # network.add_edge(f1, n5)

    # network.add_edge(f2, n6)
    # network.add_edge(f2, n7)
    # network.add_edge(f2, n8)
    #
    # network.add_edge(f2, f1)

    f1_list = network.neighbors(f1)
    # f2_list = network.neighbors(f2)

    Datacontexts = set()
    Serviceset = []
    for each in f1_list:
        if hasattr(each, 'ID'):
            # print(each.ID, each.set_of_services, each.set_of_dataContexts)
            Datacontexts.update(set(each.set_of_dataContexts))
            Serviceset.append(each.set_of_services)
    f1.Dc = Datacontexts.copy()
    f1.Sc_union = Serviceset.copy()
    Datacontexts.clear()
    Serviceset.clear()
    # for each in f2_list:
    #     if hasattr(each, 'ID'):
    #         print(each.ID, each.set_of_services, each.set_of_dataContexts)
    #         Datacontexts.update(set(each.set_of_dataContexts))
    #         Serviceset.append(each.set_of_services)
    #
    # f2.Dc = Datacontexts.copy()
    # f2.Sc_union = Serviceset.copy()

    # print("Data Contexts of Cluster 1", f1.Dc)
    # print("Union of Services of the Cluster 1", f1.Sc_union)

    # print("Data Contexts of Cluster 2", f2.Dc)
    # print("Union of Services of the Cluster 2", f2.Sc_union)

    # string = ['a', 'b', 'c', 'd']
    # print(f1.Dc)
    Cl.CreateLattice(f1.Dc, dict1)
    # Cl.CreateLattice(f2.Dc)

    # Cl.Creation_L(f1.Dc)

    # nx.draw(network, with_labels=True)
    # plt.savefig("f1.png")

    # print(network.number_of_nodes())

import time
import Initialize

if __name__ == '__main__':
    source_coordinates = (11, 59)
    destination_coordinates = (39, 41)

    # Config1 = CG.Create_clusters()
    # point_graph = CP.CreateConnectingPoint()
    # graph = CG.Create_clusters.get_graph_of_cluster_heads()


    # $$ print connecting points $$
    # connecting_point_graph = point_graph.connecting_point_adjacency_list
    # print("Physical Connecting point")
    # for k, v in connecting_point_graph.items():
    #     print(k.name, "=>", end='')
    #     for e in v:
    #         print(e[0].name, end='')
    #     print()

    # assignment of nodes
    # number_of_nodes = 20
    # list_of_all_nodes = An.assign_nodes_to_cluster(number_of_nodes)

    # print(list_of_all_nodes[1])
    # for i in list_of_all_nodes: print(i)
    # list_of_all_nodes[0].service_request(source_coordinates, destination_coordinates)
    # list_of_all_nodes[0].set_of_dataContexts = [[{'d3'}, {'d2'}]]
    # list_of_all_nodes[0].set_of_dataContexts = [[{'d2'}, {'d2', 'd3'}, {'d2', 'd3', 'd1'}]]
    # list_of_all_nodes[0].service_request(source_coordinates, destination_coordinates)

    # list_of_all_nodes[0].set_of_dataContexts = [[{'d2'}, {'d3', 'd2'}]]






    # for item in connecting_point_graph.items():
    #     print(item[0].name, end="")
    #     for it in item[1]:
    #         print(it[0].name, end='')



    # print(graph)
    # visited = {}
    # for key in graph.keys():
    #     visited[key] = False
    #
    # source_coordinates = (20, 50)
    # destination_coordinates = (110, 8)




    # Config1 =  CG.Create_clusters()

    # Assign Connecting point to the clusters and return list of connecting point
    # result = Config1.assign_connecting_points1()
    # print(result)
    # for r in result:
    #     print("Name of connecting point", r.name)

    # $$ Initilize the structure $$
    list_of_all_nodes, cluster_graph, point_graph = Initialize.Init_structure()
    # print("list of nodes:", list_of_all_nodes)
    # print("cluster graph :", cluster_graph)
    # print("point graph:", point_graph)
    # g =nx.from_dict_of_lists(point_graph)
    # print(g.edges())

    # print(point_graph)
    # $$ service request from node to cluster head $$
    # list_of_all_nodes[0].service_request(source_coordinates, destination_coordinates)

    # request with source, destination and intent where we have consider
    # intent = 1 for fuel station,
    # intent = 2 for restaurant
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%--Simulation Initiated--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    print('''GIVE INPUT FROM FOLLOWING SET \n \t \t \t \t { (11, 59, 'a'), (12, 45, 'b'), (39, 41, 'c',), (50, 58, 'd',), 
                (70, 60, 'e', 1), (69, 39, 'f',), (55, 31, 'g', 1), (43, 20, 'h', 1)
                (25, 18, 'i', 2), (45, 5, 'j'), (71, 20, 'k', ), (88, 30, 'l', )
                (90, 10, 'm',), (84, 40, 'n', 3), (102, 20, 'o'), (114, 5, 'p')
                (95, 0, 'q'), (102, 32, 'r', 2), (27, 2, 's', 1), (5, 20, 't')} ''')

    start_time = time.time()
    print("Source : A = ", source_coordinates,"Destination : C = ", destination_coordinates)
    list_of_all_nodes[0].service_request(cluster_graph, source_coordinates, destination_coordinates, intent=2)
    total_time = (time.time() - start_time)
    print("--- %s milli-seconds taken to execute ---" % (total_time))
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%--Simulation Completed--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%--Second Simulation--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    start_time = time.time()
    print("Source : A = ", source_coordinates, "Destination : C = ", destination_coordinates)
    list_of_all_nodes[0].service_request(cluster_graph, source_coordinates, destination_coordinates, intent=1)
    total_time = (time.time() - start_time)
    print("--- %s milli-seconds taken to execute ---" % (total_time))
    print()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%--Simulation Completed--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


    # print(graph)
    # print(graph.keys())
    # visited = [False] * (len(graph)+1)
    # print(visited)
    # list1 = Config1.get_graph_of_cluster_heads()
    # print(list1)

    # this will give us the list of cluster with which we need to communicate
    # clusterslist = CH.get_list_of_clusters(graph, source_coordinates, destination_coordinates)

    # creating physical location points for generating the graph
    # points = CP.CreateConnectingPoint.get_connecting_points()









    # print(clusterslist)
    # if clusterslist:
    #     for i in clusterslist:
    #         print(f'({i.x_coordinate}, {i.y_coordinate})', end=" ")
    #
    # n1 = Node.Node('N' + str(1), ['s1', 's2', 's3'], ['d1', 'd2'])
    # n2 = Node.Node(2, ['s1', 's2'], ['d1', 'd3', 'd4'])
    # n3 = Node.Node(3, ['s3'], ['d1', 'd2'])
    # n0 = Node.Node(0, ['s4'], ['d3', 'd4'])

    # dict1 = n1.delta()
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
    # f1 = fg.Fog(101)
    # f2 = fg.Fog(102, 'fog2')

    # network = nx.Graph()
    # network.add_node(n1)
    # network.add_node(n2)
    # network.add_node(n3)
    # network.add_node(n4)
    # network.add_node(n5)
    # network.add_node(n6)
    # network.add_node(n7)
    # network.add_node(n8)
    # network.add_node(f1)
    # network.add_node(f2)
    #
    # nodes = [n1, n2, n3]
    # for i in nodes:
    #     network.add_edge(f1, i)

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

    # f1_list = network.neighbors(f1)
    # # f2_list = network.neighbors(f2)
    #
    # Datacontexts = set()
    # Serviceset = []
    # for each in f1_list:
    #     if hasattr(each, 'ID'):
    #         # print(each.ID, each.set_of_services, each.set_of_dataContexts)
    #         Datacontexts.update(set(each.set_of_dataContexts))
    #         Serviceset.append(each.set_of_services)
    # f1.Dc = Datacontexts.copy()
    # f1.Sc_union = Serviceset.copy()
    # Datacontexts.clear()
    # Serviceset.clear()
    # # for each in f2_list:
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
    # Cl.CreateLattice(f1.Dc, dict1)
    # Cl.CreateLattice(f2.Dc)

    # Cl.Creation_L(f1.Dc)

    # nx.draw(network, with_labels=True)
    # plt.savefig("f1.png")

    # print(network.number_of_nodes())

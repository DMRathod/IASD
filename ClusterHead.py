import time
from collections import defaultdict
import pickle
import random
import sys
import Response_module as ResM
# import CreateConnectedClusterHeads as CG
import numpy as np

# import shortest_path
import HeuristicPath as sp
import CreateConnectingPoints as CP
import createlatticeee as cgl


point_graph = CP.CreateConnectingPoint()
connecting_point_graph = point_graph.connecting_point_adjacency_list
list_of_connecting_points = point_graph.get_connecting_points()

# Config_of_cluster_heads = CG.Create_clusters()
# cluster_graph = Config_of_cluster_heads.get_graph_of_cluster_heads()
# #

def Euclidean_dist(p1, p2):
    return np.sqrt((p2.x_coordinate - p1.x_coordinate) ** 2 + (p2.y_coordinate - p1.y_coordinate) ** 2)


def average_weights(values):
    return sum(values)/len(values)


#
# def check_in_CGL(datacontext, cluster_head):
#     # CGL_dict = cgl.CGL([set(i) for i in datacontext])
#     for each in datacontext:
#         if each in cluster_head.CGL.keys():
#             return False
#     return True
#
#
# def store_in_file(CGL_dict, name):
#     db = CGL_dict
#     dbfile = open(name, 'wb')
#     pickle.dump(db, dbfile)
#     dbfile.close()
#
#
# def load_from_file(name):
#     dbfile = open(name, 'rb')
#     db = pickle.load(dbfile)
#     for keys in db:
#         print(keys, "=>", db[keys])
#     dbfile.close()
#     return db
#
#
# def init_CGL(db, name):
#     dbfile = open(name, 'wb')
#     pickle.dump(db, dbfile)
#     dbfile.close()
#     return load_from_file(name)
#
#
# def update_CGL(test_cases, name):
#     first = False
#     for req in test_cases:
#         length_to_node = defaultdict(set)
#         length_to_node[0] = {frozenset()}
#         if first:
#             nodes_to_children = defaultdict(set)
#         else:
#             nodes_to_children = load_from_file(name)
#         nodes_to_children[frozenset()] = set()
#         for node in req:
#             node_len = len(node)
#             length_to_node[node_len].add(frozenset(node))
#             connected_to_atleast_one = False
#             for i in range(node_len-1, -1, -1):
#                 old_nodes = length_to_node[i]
#                 for old_node in old_nodes:
#                     if old_node.issubset(node):
#                         nodes_to_children[frozenset(node)].add(frozenset(old_node))
#                         connected_to_atleast_one = True
#                 if connected_to_atleast_one:
#                     break
#         # print(nodes_to_children)
#         for key, val in nodes_to_children.items():
#             print(f'{list(key)} :::: {[" ".join(i) for i in val]}')
#
#     store_in_file(nodes_to_children, name)
#     return load_from_file(name)
#


def assign_weights_to_edges(weights_of_connecting_point, fresh=True):
    def return_object_by_name(name):
        for p in connecting_point_graph.keys():
            if p.name == name:
                return p

    print("weights of edges of connecting points")

    weights_of_connecting_point1 = defaultdict()

    # converting all object to its origional id's
    for k, v in weights_of_connecting_point.items():
        key = return_object_by_name(k.name)
        weights_of_connecting_point1[key] = v


    # for k, v in connecting_point_graph.items():
    #     print(k.name, "=>", end='')
    #     for e in v:
    #         print(e[0].name, end='')
    #     print()
    if not fresh:
        for each in weights_of_connecting_point1.keys():
            # print(each.name, end=" ")
            for p in connecting_point_graph[each]:
                if p[0] in weights_of_connecting_point1.keys():
                    if p[1] != 0:
                        temp = average_weights([weights_of_connecting_point1[each], weights_of_connecting_point1[p[0]]])
                        p[1] = average_weights([p[1], temp])
                    else:
                        p[1] = average_weights([weights_of_connecting_point1[each], weights_of_connecting_point1[p[0]]])
        # sys.exit("I am here")
    else:
        for each in weights_of_connecting_point.keys():
            # print(each.name, end=" ")
            for p in connecting_point_graph[each]:
                if p[0] in weights_of_connecting_point.keys():
                    if p[1] != 0:
                        temp = average_weights([weights_of_connecting_point[each], weights_of_connecting_point[p[0]]])
                        p[1] = average_weights([p[1], temp])
                    else:
                        p[1] = average_weights([weights_of_connecting_point[each], weights_of_connecting_point[p[0]]])
    #     # print()
            # print(p[0].name, p[1])
    for k, v in connecting_point_graph.items():
        print(k.name, "=>", end='')
        for e in v:
            print(e[1], end=' ')
        print()


def get_list_of_clusters(graph, source, destination):
    time.sleep(2)
    s_exist = False
    d_exist = False

    for each in graph.keys():
        if each.x_coordinate == source[0] and each.y_coordinate == source[1]:
            source1 = each
            s_exist = True
        if each.x_coordinate == destination[0] and each.y_coordinate == destination[1]:
            destination1 = each
            d_exist = True

    if s_exist == False or d_exist == False:
        print("Source or destination Does not exist")
        return

    limitation_factor = 1
    list_of_cluster_heads = []
    # Variation of BFS
    # visited = [False] * (len(graph)+1)
    visited = {}
    for key in graph.keys():
        visited[key] = False
    # print(visited)
    queue = [source1]
    visited[source1] = True
    # j = 0
    # print(graph[source1])
    while queue:
        temp = queue.pop(0)
        # print(temp, i)
        # j += 1
        if Euclidean_dist(temp, source1) <= Euclidean_dist(destination1, source1) and Euclidean_dist(temp, destination1) <= limitation_factor * (Euclidean_dist(source1, destination1)):
            list_of_cluster_heads.append(temp)
            # print(graph[temp])
            for i in graph[temp]:
                # print(i[0])
                if not visited[i[0]]:
                    queue.append(i[0])
                    visited[i[0]] = True
    return list_of_cluster_heads

#
#




class ClusterHead:

    def __init__(self, x_coordinate, y_coordinate, name):
        self.list_of_nodes = []
        self.list_of_connectingPoints = []
        # self.list_of_values_of_connectingPoints = []
        self.weights_of_connecting_points_dict = defaultdict()
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        l, self.CGL = self.initiate_CGL()
        self.datacontext_dict = defaultdict()
        self.initiate_weight_dict()

    # return after checking if any other valid connecting point or not
    # def include_connecting_points(self, points, bound):
    #     # distance_dict = {}
    #     for each in points:
    #         d = np.sqrt((each.x_coordinate - self.x_coordinate) ** 2 + (each.y_coordinate - self.y_coordinate) ** 2)
    #         print("cluster head", each.name, d)
    #         if d <= bound:
    #             self.list_of_connectingPoint.append(each)
    #     return self.list_of_connectingPoint

    # return the existing list of the connecting points
    def print_connecting_points(self):
        return self.list_of_connectingPoint

    def get_list_of_nodes(self):
        return self.list_of_nodes

    def requirement_to_datacontext(self, service_type):
        # we can assign some predefined datacontext to the services so that it can be used for constructing the CGL that will be accumulated from the individual nodes
        possible_contexts = [[{'d1'}]]
        # possible_contexts = [[{'d1'}], [{'d2'}], [{'d1', 'd2'}], [{'d1', 'd2', 'd3'}], [{'d2'}], [{'d3'}]]
        if service_type == 1:
            d = random.choice(possible_contexts)
            # print("choice is :", d)
            return [d]
    # validates the service request for existance of location and service type and it will return the corresponding cluster heads coordinates
    @classmethod
    def validate_service_request(cls, service_type, source, destination):
        source_flag = False
        destination_flag = False
        temp_source = None
        temp_destination = None
        point_source = None
        point_destination = None
        for each in list_of_connecting_points:
            if source[0] == each.x_coordinate and source[1] == each.y_coordinate:
                temp_source = (each.parent_cluster.x_coordinate, each.parent_cluster.y_coordinate)
                point_source = each
                print("Source Found")
                source_flag = True
            if destination[0] == each.x_coordinate and destination[1] == each.y_coordinate:
                temp_destination = (each.parent_cluster.x_coordinate, each.parent_cluster.y_coordinate)
                destination_flag = True
                point_destination = each
            # print(each.name, " x: ", each.x_coordinate, " y: ", each.y_coordinate)
        if not source_flag or not destination_flag or service_type != 1:
            sys.exit("Source or Destination point Does not exist or service type does not matched")
        return temp_source, temp_destination, point_source, point_destination






    def compute_connecting_point_weight_from_datacontext(self, datacontext):
        # $$ randomly assigning the weights to the nodes, we can think some statistical method for assigning weights
        weights = [2, 3, 4]

        for each in self.list_of_connectingPoints:
            self.weights_of_connecting_points_dict[each] = random.choice(weights)
        # for i in range(len(self.list_of_connectingPoints)):
        #     self.weights_of_connecting_points.append(random.choice(weights))
        # print(self.weights_of_connecting_points)

    def internal_service_response(self, service_type):
        datacontext = self.requirement_to_datacontext(service_type)
        # datacontext = [[{'d2'}, {'d3'}]]
        context_used_before = self.check_in_CGL(datacontext)
        print("data context = ", datacontext, "For Cluster ", self.name)
        if not context_used_before:
            self.CGL = self.update_CGL(datacontext,  load_old=True)
            self.compute_connecting_point_weight_from_datacontext(datacontext)

            self.datacontext_dict[frozenset(datacontext[0][0])] = self.weights_of_connecting_points_dict
            self.store_weight_dict(self.datacontext_dict)
            assign_weights_to_edges(self.weights_of_connecting_points_dict, fresh=True)
        else:
            print('Loading connecting point weights from file...(datacontext is used before)')
            weight_dictn = self.load_weight_dict()
            print(self.weights_of_connecting_points_dict)
            self.weights_of_connecting_points_dict = weight_dictn[frozenset(datacontext[0][0])] # when will you get back this object address will be changed so be careful when you are using it.
            print(self.weights_of_connecting_points_dict) # check different address of the each object.
            # for key, value in self.weights_of_connecting_points_dict.items():
            #     print(key.name, "=>", value )
            assign_weights_to_edges(self.weights_of_connecting_points_dict, fresh=False)

        #

        # datacontext = [[{'d2', 'd3'}]]
        # context_used_before = self.check_in_CGL(datacontext)
        # print("data context = ", datacontext)
        # if not context_used_before:
            # self.CGL = self.update_CGL(datacontext,  load_old=True)

        print("Updated CGL", context_used_before, self.CGL)
        # print("list of connecting point", self.weights_of_connecting_points_dict)
        # ResM.assign_weights_to_edges(self.weights_of_connecting_points_dict)
        # RM.get_list_of_clusters(service_type, source, destination)

    def service_response(self, service_type, cluster_graph, p_source, p_destination, intent):
        time.sleep(0.05)
        c_source, c_destination, p_source, p_destination = ClusterHead.validate_service_request(service_type, p_source, p_destination)
        # print("idhar ", c_source, c_destination, p_source, p_destination)
        # sys.exit("Here i am")
        # datacontext_dict = defaultdict()
        # datacontext = self.requirement_to_datacontext(service_type)
        # # datacontext = [[{'d2'}, {'d3'}]]
        # context_used_before = self.check_in_CGL(datacontext)
        # print("data context = ", datacontext, "For Cluster ", self.name)
        #
        # if not context_used_before:
        #     self.CGL = self.update_CGL(datacontext,  load_old=True)
        #     self.compute_connecting_point_weight_from_datacontext(datacontext)
        #     # print("data", frozenset(datacontext[0][0]))
        #     # self.datacontext_dict[datacontext[0]] = self.weights_of_connecting_points_dict
        #
        #     # store the connecting point weights into the file for nearer future use
        #     self.datacontext_dict[frozenset(datacontext[0][0])] = self.weights_of_connecting_points_dict
        #     self.store_weight_dict(self.datacontext_dict)
        # else:
        #     print('Loading connecting point weights from file...(datacontext is used before)')
        #     weight_dictn = self.load_weight_dict()
        #     self.weights_of_connecting_points_dict = weight_dictn[frozenset(datacontext[0][0])]
        #
        # # datacontext = [[{'d2', 'd3'}]]
        # # context_used_before = self.check_in_CGL(datacontext)
        # # print("data context = ", datacontext)
        # # if not context_used_before:
        #     # self.CGL = self.update_CGL(datacontext,  load_old=True)
        #
        # print("Updated CGL", context_used_before, self.CGL)
        # print("list of connecting point", self.weights_of_connecting_points_dict)
        # assign_weights_to_edges(self.weights_of_connecting_points_dict)
        list_of_involved_clusters = get_list_of_clusters(cluster_graph, c_source, c_destination)
        for each in list_of_involved_clusters:
            each.internal_service_response(service_type)
        # communicate_with_other_clusters(service_type, source, destination)

        # ResM.assign_weights_to_edges(self.weights_of_connecting_points_dict)
        # ResM.communicate_with_other_clusters(service_type, source, destination)
        # path = self.compute_shortest_path_heuristic()
        # return
        sp.compute_shortest_heuristic_path_with_intent(connecting_point_graph, p_source, p_destination, intent)
        time.sleep(0.03)




    # def compute_shortest_path_heuristic(self, ):
    #
    #     return path

    def check_in_CGL(self, datacontext):
        print("data Conetxt new one:", datacontext)
        CGL_keys = self.CGL.keys()
        print("CGL in CHECK", self.CGL)
        if frozenset(datacontext[0][0]) in CGL_keys:
            return True
        return False


        # use when you have series of data context

        # for each in datacontext[0]:
        #     if frozenset(each) in CGL_keys:
        #         datacontext[0].remove(each)
        # print("updated datacontext req", datacontext)
        # return False

    def initiate_CGL(self):
        len_to_node = defaultdict(set)
        len_to_node[0] = {frozenset()}
        db = (len_to_node, defaultdict(set))
        dbfile = open(self.name, 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()
        return self.load_from_file()

    def initiate_weight_dict(self):
        weight_dict = defaultdict()
        db = weight_dict
        dbfile = open(self.name+"wdict", 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()


    def load_from_file(self):
        dbfile = open(self.name, 'rb')
        db = pickle.load(dbfile)
        # for keys in db:
        #     print(keys, "=>", db[keys])
        dbfile.close()
        return db[0], db[1]

    def load_weight_dict(self):
        dbfile = open(self.name+"wdict", 'rb')
        db = pickle.load(dbfile)
        dbfile.close()
        return db

    def store_in_file(self, len_to_nodes, CGL_dict):
        db = (len_to_nodes, CGL_dict)
        dbfile = open(self.name, 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()

    def store_weight_dict(self, weight_dict):
        db = weight_dict
        dbfile = open(self.name+"wdict", 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()


    def update_CGL(self, test_cases, load_old=True):
        # first = False
        for req in test_cases:
            if not load_old:
                length_to_node = defaultdict(set)
                length_to_node[0] = {frozenset()}
                nodes_to_children = defaultdict(set)
            else:
                length_to_node, nodes_to_children = self.load_from_file()
                # print(length_to_node, nodes_to_children)
            nodes_to_children[frozenset()] = set()
            for node in req:
                node_len = len(node)
                length_to_node[node_len].add(frozenset(node))
                connected_to_atleast_one = False
                for i in range(node_len-1, -1, -1):
                    old_nodes = length_to_node[i]
                    for old_node in old_nodes:
                        if old_node.issubset(node):
                            nodes_to_children[frozenset(node)].add(frozenset(old_node))
                            connected_to_atleast_one = True
                    if connected_to_atleast_one:
                        break
            # print(nodes_to_children)
            # print(length_to_node)
            for key, val in nodes_to_children.items():
                print(f'{list(key)} :::: {[" ".join(i) for i in val]}')
                # print(f'{list(key)} :::: {[print(va) for va in val]}')
        # print("len to node", length_to_node)
        self.store_in_file(length_to_node, nodes_to_children)
        l, db = self.load_from_file()
        return db



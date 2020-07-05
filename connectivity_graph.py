from itertools import product
from math import prod

from igraph import Graph
import numpy as np


def build_adjacency_graph(board: np.ndarray) -> Graph:
    Tactical_tutorial_graph = Graph(directed=1)
    Tactical_tutorial_graph.add_vertices(prod(board.shape))

    def coord_to_name(coord: tuple) -> str:
        return str(coord)[1: -1]

    Tactical_tutorial_graph.vs["name"] = list(map(lambda coord: coord_to_name(coord), product(*map(range, board.shape))))
    Tactical_tutorial_graph.vs["coord"] = list(product(*map(range, board.shape)))

    for vertex in Tactical_tutorial_graph.vs:
        vertex_coordinates = vertex["coord"]
        if vertex_coordinates[1] == 0:

            adjacent_vertex_coordinates = vertex_coordinates[:1] + (1,) + vertex_coordinates[2:]
            adjacent_vertex = Tactical_tutorial_graph.vs.find(name=coord_to_name(adjacent_vertex_coordinates))

            Tactical_tutorial_graph.add_edges([(vertex, adjacent_vertex), (adjacent_vertex, vertex)])

        else:
            pass
        # add edges

    return Tactical_tutorial_graph







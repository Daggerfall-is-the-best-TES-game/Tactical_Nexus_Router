from collections import defaultdict
from agent import Agent
from environment import GameObject, KeyItem
from towers import Tactical_tutorial
from igraph import plot, Graph
from board import Tactical_tutorial_board
from connectivity_graph import build_adjacency_graph

if __name__ == "__main__":

    print(Tactical_tutorial_board[0, [0, 1], :, :])
    adjacency_graph = build_adjacency_graph(Tactical_tutorial_board)



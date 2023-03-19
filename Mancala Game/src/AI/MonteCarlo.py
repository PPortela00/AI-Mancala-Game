import copy
import math
import random

from src.AI import Leaf
from src.Mancala import Game


class MonteCarlo:
    def __init__(self, util_func, max_iterations=1000, exploration_constant=1.414):
        self.util_func = util_func
        self.max_iterations = max_iterations
        self.exploration_constant = exploration_constant

    def mcts(self, tree):
        """
        Runs Monte Carlo Tree Search on a game tree. Returns the best move index.
        :param tree: TreeBuilder obj
        :return: int, best move index
        """
        for i in range(self.max_iterations):
            # Selection
            selected_node = self.select(tree.root)

            # Expansion
            if not isinstance(selected_node, Leaf):
                expanded_node = self.expand(selected_node)
                simulated_node = expanded_node
            else:
                simulated_node = selected_node

            # Simulation
            result_node = self.simulate(simulated_node)

            # Backpropagation
            self.backpropagate(result_node)

        # Choose best move based on visits
        return max(tree.root.get_children().keys(), key=lambda i: tree.root.get_children()[i].get_visits())

    def select(self, node):
        """
        Selects a node to expand by using the UCT (Upper Confidence Bound for Trees) algorithm
        :param node: Node obj
        :return: Node obj, selected node
        """
        while not isinstance(node, Leaf):
            children = node.get_children()
            values = [self.uct(child, node) for child in children.values()]
            node = children.values()[values.index(max(values))]
        return node

    def expand(self, node):
        """
        Expands a leaf node by creating child nodes for all possible moves
        :param node: Node obj, a leaf node
        :return: Node obj, the newly created child node
        """
        actions = node.get_data().get_actions()
        for i in actions:
            node.add_child(i, Leaf(self.util_func, self.result_func(node, i)))
        return random.choice(list(node.get_children().values()))

    def simulate(self, node):
        """
        Simulates a game from the given node to a terminal state
        :param node: Node obj
        :return: Node obj, the terminal node of the simulated game
        """
        data = node.get_data()
        while not data.is_terminal():
            action = random.choice(data.get_actions())
            data = self.result_func(node, action).get_data()
        return Leaf(self.util_func, data)

    def backpropagate(self, node):
        """
        Updates the visited and utility counts of all nodes in the path from the given node to the root
        :param node: Node obj, the terminal node to start the backpropagation from
        """
        while node is not None:
            node.increment_visits()
            node.add_utility(node.calculate_utility(self.util_func))
            node = node.get_parent()

    def uct(self, node, parent):
        """
        Calculates the UCT (Upper Confidence Bound for Trees) value of a node given its parent node
        :param node: Node obj
        :param parent: Node obj, the parent of node
        :return: float, the UCT value of node
        """
        exploration_term = self.exploration_constant * math.sqrt(math.log(parent.get_visits()) / node.get_visits())
        return node.get_utility() / node.get_visits() + exploration_term

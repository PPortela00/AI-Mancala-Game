import copy
import random

from src.AI import Leaf
from src.Mancala import Game


class Alpha_Beta_Pruning:
    """
    Result_func must always return a node with valid game state
    """
    def __init__(self, util_func, result_func, max_depth=5, noise=200):
        self.util_func = util_func
        self.result_func = result_func
        self.max_depth = max_depth
        self.noise = noise

    def alpha_beta_search(self, tree):
        """
        Runs alpha-beta search on a game tree. Returns the utility with best move
        :param tree: TreeBuilder obj
        :return: (int, int)-tuple with utility and best move index respectively
        """
        v, i = self.max_value(tree.root, float('-inf'), float('inf'), 0)
        return v, i

    def evaluate(self, node):
        utility = node.calculate_utility(self.util_func)
        return utility + random.uniform(-self.noise, self.noise)

    def max_value(self, node, a, b, depth):
        # Check for terminal state (Leaf nodes are only generated in terminal or loop)
        if isinstance(node, Leaf) or depth >= self.max_depth:
            return self.evaluate(node), 0

        data = node.get_data()
        v = float('-inf')
        best_i = -1

        # Iterate over number of actions
        for i in node.get_children().keys():
            data_copy = copy.deepcopy(data)  # Save game state

            # Run max if AI, run min if player
            result_node = self.result_func(node, i)
            if isinstance(data, Game):
                if result_node.get_data().get_player_turn() == 1:
                    v = max(v, self.max_value(result_node, a, b, depth + 1)[0])
                else:
                    v = max(v, self.min_value(result_node, a, b, depth + 1)[0])
            else:
                v = max(v, self.min_value(result_node, a, b, depth + 1)[0])

            node.set_data(data_copy)  # Reset to former game state

            # Alpha-beta pruning
            if v >= b:
                return v, best_i

            if v > a:
                best_i = i

            a = max(a, v)

        return v, best_i

    def min_value(self, node, a, b, depth):
        # Check for terminal state (Leaf nodes are only generated in terminal or loop)
        if isinstance(node, Leaf) or depth >= self.max_depth:
            return self.evaluate(node), 0

        data = node.get_data()
        v = float('inf')
        best_i = -1

        # Iterate over number of actions
        for i in node.get_children().keys():
            data_copy = copy.deepcopy(data)  # Save game state

            # Run max if AI, run min if player
            result_node = self.result_func(node, i)
            if isinstance(data, Game):
                if result_node.get_data().get_player_turn() == 1:
                    v = min(v, self.max_value(result_node, a, b, depth + 1)[0])
                else:
                    v = min(v, self.min_value(result_node, a, b, depth + 1)[0])
            else:
                v = min(v, self.max_value(result_node, a, b, depth + 1)[0])

            node.set_data(data_copy)  # Reset to former game state

            # Alpha-beta pruning
            if v <= a:
                return v, i
            b = min(b, v)

        return v, best_i

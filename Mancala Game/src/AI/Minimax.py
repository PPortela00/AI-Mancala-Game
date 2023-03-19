import copy
import random
from src.AI import Leaf
from src.Mancala import Game


class Minimax:
    """
    Result_func must always return a node with valid game state
    """
    def __init__(self, util_func, result_func, max_depth=2, noise=300):
        self.util_func = util_func
        self.result_func = result_func
        self.max_depth = max_depth
        self.noise = noise
        
    def evaluate(self, node):
        utility = node.calculate_utility(self.util_func)
        return utility + random.uniform(-self.noise, self.noise)
        
    def minimax_search(self, tree):
        v, i = self.max_value(tree.root, 0)
        return v, i
    
    def max_value(self, node, depth):
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
                    v_temp, _ = self.max_value(result_node, depth + 1)
                else:
                    v_temp, _ = self.min_value(result_node, depth + 1)
            else:
                v_temp, _ = self.min_value(result_node, depth + 1)

            if v_temp > v:
                v = v_temp
                best_i = i

            node.set_data(data_copy)  # Reset to former game state

        return v, best_i
    
    def min_value(self, node, depth):
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
                    v_temp, _ = self.max_value(result_node, depth + 1)
                else:
                    v_temp, _ = self.min_value(result_node, depth + 1)
            else:
                v_temp, _ = self.max_value(result_node, depth + 1)

            if v_temp < v:
                v = v_temp
                best_i = i

            node.set_data(data_copy)  # Reset to former game state

        return v, best_i
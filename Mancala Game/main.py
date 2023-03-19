import random
from src.AI import MancalaTreeBuilder, Node, Minimax, Alpha_Beta_Pruning, evaluation_extraturn_capture, evaluation_moves, evaluation_board
from src.Mancala import Game
import time
import tkinter as tk
from interface import Interface
"""
This is the main script which runs the game with either two human players or one human player and one AI.

"""
def print_game(game):

        state = game.get_state()
        slots = list(range(0,6))
        slots_inverso = [5, 4, 3, 2, 1, 0]
        player1_state = state[0]
        player2_state = state[1]
        player2_state.reverse()

        print("Slots:   | ", end=""); print(*slots_inverso, sep=" | ", end=""); print(" |")
        print("=======================================")
        print("Player 2 | ", end="")
        print(*player2_state[1:], sep=" | ", end=""); print(" | Score: {0}".format(player2_state[0]))
        print("---------------------------------------")
        print("Player 1 | ", end="")
        print(*player1_state[0:-1], sep=" | ", end=""); print(" | Score: {0}".format(player1_state[-1]))
        print("=======================================")
        print("Slots:   | ", end=""); print(*slots, sep=" | ", end=""); print(" |")
    
    
        
      
def check_input(str):
    while True:
        try:
            val = int(input(str))
            break
        except ValueError:
            print("Not a recognizable integer, please try again.")

    return val

def check_slot_input(str):
    while True:
        try:
            val = int(input(str))
            if 0 <= val <= 5:
                return val
            else:
                print("Slot index must be a value between 0 and 5. Please try again.")
        except ValueError:
            print("Not a recognizable integer, please try again.")

def selecionar_valor():
    return random.randint(0, 5)

if __name__ == "__main__":
    # Select game mode
    print("")
    print("Welcome to the Mancala Game")
    print("")
    print("Select the game visual mode:")
    print("1 - Console")
    print("2 - Interface")
    type = check_input("Enter your choice: ")
    
    if(type == 2):
        interface = Interface()
        interface.start()
    elif(type == 1):
        print("Select the game mode:")
        print("1 - Human vs. AI")
        print("2 - Human vs. Human")
        print("3 - AI vs. AI")
        print("4 - Random Agent vs. AI")
        mode = check_input("Enter your choice: ")

        rec_limit = None
        total_time = 0
        if (mode == 1):
            # Tree recursion limit
            print("Select the difficulty level:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - World Champion")
            rec_limit = 2 + check_input("Enter your choice: ") * 2

            # Select Algorithm
            print("Select the algorithm:")
            print("1 - Minimax")
            print("2 - Alpha-Beta Pruning")
            algorithm_choice = check_input("Enter your choice: ")
            
            # Select Evaluation Extra-Turn and Capture
            print("Select the Evaluation Extra-Turn and Capture:")
            print("1 - Evaluation Extra-Turn and Capture")
            print("2 - Evaluation Moves")
            print("3 - Evaluation Board")
            evaluation_function = check_input("Enter your choice: ")
            
            
            if(algorithm_choice == 1 and evaluation_function == 1):
                # Minimax algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Minimax object
                minimax = Minimax(evaluation_extraturn_capture, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()
                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 1 and player_turn == 0):
                        slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax.minimax_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 1 and evaluation_function == 2):
                # Minimax algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Minimax object
                minimax = Minimax(evaluation_moves, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()
                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 1 and player_turn == 0):
                        slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax.minimax_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 1 and evaluation_function == 3):
                # Minimax algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Minimax object
                minimax = Minimax(evaluation_board, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()
                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 1 and player_turn == 0):
                        slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax.minimax_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
                        
            elif(algorithm_choice == 2 and evaluation_function == 1):
                # Alpha-Beta Pruning algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Alpha-Beta Pruning object
                minimax_cuts = Alpha_Beta_Pruning(evaluation_extraturn_capture, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()

                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 1 and player_turn == 0):
                        slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax_cuts.alpha_beta_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 2 and evaluation_function == 2):
                # Alpha-Beta Pruning algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Alpha-Beta Pruning object
                minimax_cuts = Alpha_Beta_Pruning(evaluation_moves, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()

                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 1 and player_turn == 0):
                        slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax_cuts.alpha_beta_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 2 and evaluation_function == 3):
                # Alpha-Beta Pruning algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Alpha-Beta Pruning object
                minimax_cuts = Alpha_Beta_Pruning(evaluation_board, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()

                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 1 and player_turn == 0):
                        slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax_cuts.alpha_beta_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
        if(mode == 2):               
            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                print_game(game)

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))

                slot = check_slot_input("Choose which slot to pick up (from 0 to 5): ")
                print("Player {0} choosen slot: {1}".format(1 + player_turn, slot))
                print("")
                game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    print_game(game)
        
        if(mode == 3):
        
            # Tree recursion limit for AI 1
            print("Select difficulty level for the AI 1:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - World Champion")
            rec_limit_player1 = 2 + check_input("Enter your choice: ") * 2

            # Select Algorithm for AI 1
            print("Select Algorithm for the AI 1:")
            print("1 - Minimax")
            print("2 - Alpha-Beta Pruning")
            algorithm_choice_player1 = check_input("Enter your choice: ")
            
            # Select Evaluation Extra-Turn and Capture
            print("Select the Evaluation Extra-Turn and Capture:")
            print("1 - Evaluation Extra-Turn and Capture")
            print("2 - Evaluation Moves")
            print("3 - Evaluation Board")
            evaluation_function_player1 = check_input("Enter your choice: ")
            
            # Tree recursion limit for AI 2 
            print("Select difficulty level for the AI 2:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - World Champion")
            rec_limit_player2 = 2 + check_input("Enter your choice: ") * 2

            # Select  Algorithm for AI 2
            print("Select Algorithm for the AI 2:")
            print("1 - Minimax")
            print("2 - Alpha-Beta Pruning")
            algorithm_choice_player2 = check_input("Enter your choice: ")
        
        # Select Evaluation Extra-Turn and Capture
            print("Select the Evaluation Extra-Turn and Capture:")
            print("1 - Evaluation Extra-Turn and Capture")
            print("2 - Evaluation Moves")
            print("3 - Evaluation Board")
            evaluation_function_player2 = check_input("Enter your choice: ")
            
        # Minimax algorithm
            def result_function_player(node, a):
                children = node.get_children()
                return children[a]
                                
            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                print_game(game)
                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                slot = None
                
        
                if (player_turn == 0  and algorithm_choice_player1 == 1 and evaluation_function_player1 == 1):
                    
                    algo1_player1 = Minimax(evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player1)
                    # AI 1 and Minimax 
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player1)
                    tree.set_root(Node(game))
                    tree.build()
        
                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo1_player1.minimax_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                
                elif (player_turn == 0  and algorithm_choice_player1 == 1 and evaluation_function_player1 == 2):
                    
                    algo1_player1 = Minimax(evaluation_moves, result_function_player, max_depth=rec_limit_player1)
                    # AI 1 and Minimax 
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player1)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo1_player1.minimax_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                
                elif (player_turn == 0  and algorithm_choice_player1 == 1 and evaluation_function_player1 == 3):
                    
                    algo1_player1 = Minimax(evaluation_board, result_function_player, max_depth=rec_limit_player1)
                    # AI 1 and Minimax 
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player1)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo1_player1.minimax_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                
                elif (player_turn == 0  and algorithm_choice_player1 == 2 and evaluation_function_player1 == 1):
                    
                    algo2_player1 = Alpha_Beta_Pruning(evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player1)
                    # AI 1 and Alpha-Beta Pruning
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player1)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo2_player1.alpha_beta_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time

                elif (player_turn == 0  and algorithm_choice_player1 == 2 and evaluation_function_player1 == 2):
                    
                    algo2_player1 = Alpha_Beta_Pruning(evaluation_moves, result_function_player, max_depth=rec_limit_player1)
                    # AI 1 and Alpha-Beta Pruning
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player1)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo2_player1.alpha_beta_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time

                elif (player_turn == 0  and algorithm_choice_player1 == 2 and evaluation_function_player1 == 3):
                    
                    algo2_player1 = Alpha_Beta_Pruning(evaluation_board, result_function_player, max_depth=rec_limit_player1)
                    # AI 1 and Alpha-Beta Pruning
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player1)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo2_player1.alpha_beta_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                
                elif (player_turn == 1  and algorithm_choice_player2 == 1 and evaluation_function_player2 == 1):
                    
                    algo1_player2 = Minimax(evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player2)
                    # AI 2 and Minimax 
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player2)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo1_player2.minimax_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                
                elif (player_turn == 1  and algorithm_choice_player2 == 1 and evaluation_function_player2 == 2):
                    
                    algo1_player2 = Minimax(evaluation_moves, result_function_player, max_depth=rec_limit_player2)
                    # AI 2 and Minimax 
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player2)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo1_player2.minimax_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                    
                elif (player_turn == 1  and algorithm_choice_player2 == 1 and evaluation_function_player2 == 3):
                    
                    algo1_player2 = Minimax(evaluation_board, result_function_player, max_depth=rec_limit_player2)
                    # AI 2 and Minimax 
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player2)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo1_player2.minimax_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time
                        
                elif (player_turn == 1  and algorithm_choice_player2 == 2 and evaluation_function_player2 == 1):
                    
                    algo2_player2 = Alpha_Beta_Pruning(evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player2)
                    # AI 2 and Alpha-Beta Pruning
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player2)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo2_player2.alpha_beta_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time

                elif (player_turn == 1  and algorithm_choice_player2 == 2 and evaluation_function_player2 == 2):
                    
                    algo2_player2 = Alpha_Beta_Pruning(evaluation_moves, result_function_player, max_depth=rec_limit_player2)
                    # AI 2 and Alpha-Beta Pruning
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player2)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo2_player2.alpha_beta_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time

                elif (player_turn == 1  and algorithm_choice_player2 == 2 and evaluation_function_player2 == 3):
                    
                    algo2_player2 = Alpha_Beta_Pruning(evaluation_board, result_function_player, max_depth=rec_limit_player2)
                    # AI 2 and Alpha-Beta Pruning
                    print("AI computing best move:", end="")
                    print("")
                    tree = MancalaTreeBuilder(rec_limit_player2)
                    tree.set_root(Node(game))
                    tree.build()

                    start_time = time.time()  # start measuring the execution time
                    v, slot = algo2_player2.alpha_beta_search(tree)
                    end_time = time.time()  # end measuring the execution time
                    elapsed_time = end_time - start_time
                    print(" {1} (utility: {0})".format(v, slot))
                    print(f"Elapsed time: {elapsed_time:.4f} seconds")
                    total_time = total_time + elapsed_time

                game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    print_game(game)

        if(mode == 4):
            # Tree recursion limit
            print("Select the difficulty level:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - World Champion")
            rec_limit = 2 + check_input("Enter your choice: ") * 2

            # Select Algorithm
            print("Select the algorithm:")
            print("1 - Minimax")
            print("2 - Alpha-Beta Pruning")
            algorithm_choice = check_input("Enter your choice: ")
            
            # Select Evaluation Extra-Turn and Capture
            print("Select the Evaluation Extra-Turn and Capture:")
            print("1 - Evaluation Extra-Turn and Capture")
            print("2 - Evaluation Moves")
            print("3 - Evaluation Board")
            evaluation_function = check_input("Enter your choice: ")
            
            if(algorithm_choice == 1 and evaluation_function == 1):
                # Minimax algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Minimax object
                minimax = Minimax(evaluation_extraturn_capture, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()
                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 4 and player_turn == 0):
                        print("Choose which slot to pick up (from 0 to 5)")
                        slot = selecionar_valor()
                        print("Random Agent choosen slot: {0}".format(slot))
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax.minimax_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time

                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 1 and evaluation_function == 2):
                # Minimax algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Minimax object
                minimax = Minimax(evaluation_moves, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()
                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 4 and player_turn == 0):
                        print("Choose which slot to pick up (from 0 to 5)")
                        slot = selecionar_valor()
                        print("Random Agent choosen slot: {0}".format(slot))
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax.minimax_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time
                        
                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 1 and evaluation_function == 3):
                # Minimax algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Minimax object
                minimax = Minimax(evaluation_board, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()
                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 4 and player_turn == 0):
                        print("Choose which slot to pick up (from 0 to 5)")
                        slot = selecionar_valor()
                        print("Random Agent choosen slot: {0}".format(slot))
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax.minimax_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time
                        
                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
                        
            elif(algorithm_choice == 2 and evaluation_function == 1):
                # Alpha-Beta Pruning algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Alpha-Beta Pruning object
                minimax_cuts = Alpha_Beta_Pruning(evaluation_extraturn_capture, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()

                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 4 and player_turn == 0):
                        print("Choose which slot to pick up (from 0 to 5)")
                        slot = selecionar_valor()
                        print("Random Agent choosen slot: {0}".format(slot))
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax_cuts.alpha_beta_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time
                        
                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 2 and evaluation_function == 2):
                # Alpha-Beta Pruning algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Alpha-Beta Pruning object
                minimax_cuts = Alpha_Beta_Pruning(evaluation_moves, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()

                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 4 and player_turn == 0):
                        print("Choose which slot to pick up (from 0 to 5)")
                        slot = selecionar_valor()
                        print("Random Agent choosen slot: {0}".format(slot))
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax_cuts.alpha_beta_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time
                        
                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
            
            elif(algorithm_choice == 2 and evaluation_function == 3):
                # Alpha-Beta Pruning algorithm
                def result_function(node, a):
                    children = node.get_children()
                    return children[a]

                # Construct Alpha-Beta Pruning object
                minimax_cuts = Alpha_Beta_Pruning(evaluation_board, result_function, max_depth=rec_limit)

                # Run game
                game = Game()
                should_end = game.is_terminal_state()

                print("")
                print("Game started")
                print("")
                game_seq = []
                while not should_end:
                    print_game(game)

                    player_turn = game.get_player_turn()
                    print("\nIt is player {0}'s turn".format(1 + player_turn))

                    slot = None
                    if (mode == 4 and player_turn == 0):
                        print("Choose which slot to pick up (from 0 to 5)")
                        slot = selecionar_valor()
                        print("Random Agent choosen slot: {0}".format(slot))
                        print("")
                    else:
                        # AI
                        print("AI computing best move:", end="")
                        print("")
                        tree = MancalaTreeBuilder(rec_limit)
                        tree.set_root(Node(game))
                        tree.build()

                        start_time = time.time()  # start measuring the execution time
                        v, slot = minimax_cuts.alpha_beta_search(tree)
                        end_time = time.time()  # end measuring the execution time
                        elapsed_time = end_time - start_time
                        print(" {1} (utility: {0})".format(v, slot))
                        print(f"Elapsed time: {elapsed_time:.4f} seconds")
                        total_time = total_time + elapsed_time
                        
                    game_seq.append((player_turn, slot))        #game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                    # Reverse slot if player 2 is playing
                    game.take_slot(slot)

                    winner = 0
                    if game.is_terminal_state():
                        winner = game.end_game()
                        should_end = True
                        print_game(game)
        
        print("")            
        print("Game over, ", end="")
        if winner == 0:
            print("it's a draw!")
        else:
            print("winner is Player {0}".format(winner))
        print("Game sequence:", game_seq)
        print("Total Time Spent", total_time)
    else: print("Select a valid game visual mode 1 - Console or 2 - Interface")
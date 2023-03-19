def evaluation_board(game):
    # Initial variables
    state = game.get_state()
    player_turn = game.get_player_turn()
    opposite_player_turn = 1 if player_turn == 0 else 0
    utility = 0

    # Check player's utility
    utility += check_player_utility(player_turn, state)

    # Check AI utility
    utility += check_player_utility(opposite_player_turn, state)

    # Compute player 1 score
    player_1_score = sum(state[0])

    # Compute player 2 score
    player_2_score = sum(state[1])

    utility += player_2_score - player_1_score
    return utility


def check_player_utility(player_turn, state):
    player1_sum = sum(state[0][0:-1])
    player2_sum = sum(state[1][0:-1])
    player1_score = state[0][-1]
    player2_score = state[1][-1]

    # Determine the difference in score
    score_diff = player1_score - player2_score

    # Determine the difference in pieces
    piece_diff = player1_sum - player2_sum

    # Assign a value to each player's pieces
    if piece_diff == 0:
        piece_value = 0
    elif piece_diff > 0:
        piece_value = 1
    else:
        piece_value = -1

    # Calculate the total score for each player
    total_score = player1_score + player2_score

    # Assign a value to the difference in score
    if total_score == 0:
        score_value = 0
    else:
        score_value = score_diff / total_score

    # Calculate the final evaluation
    utility = 0.5 * score_value + 0.5 * piece_value

    return utility
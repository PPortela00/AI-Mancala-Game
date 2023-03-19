def evaluation_moves(game):
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
    utility = 0
    opposite_player_turn = 1 if player_turn == 0 else 0
    player_moves = 0
    opposite_moves = 0

    for slot, slot_count in enumerate(state[player_turn][0:6]):
        if slot_count > 0:
            player_moves += 1

        opposite_slot = 5 - slot
        opposite_count = state[opposite_player_turn][opposite_slot]
        if opposite_count > 0:
            opposite_moves += 1

    utility += player_moves - opposite_moves
    return utility

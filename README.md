# Mancala Game
Mancala is a popular two-player strategy board game that is played with small stones or seeds and a board with several pits or cups. The game is believed to have originated in Africa, and there are many variations of the game played around the world.

To play the game, each player starts with a certain number of stones or seeds in their designated pits. The objective of the game is to capture more stones or seeds than your opponent.

Mancala is a simple game to learn, but it can be challenging to master. The game requires strategic thinking and planning ahead to make the best moves and outmaneuver your opponent. It's a great game to play with friends and family and can be enjoyed by people of all ages.

## 📒 Rules for the Mancala game
Here are the general rules for playing Mancala:

1. Setup: Each player has six small cups, called "pits," on their side of the board, and one large cup, called the "Mancala," on their right-hand side. The board is set up so that each player's six pits are closest to them, and the Mancalas are at the opposite ends of the board.

2. Initial placement: At the beginning of the game, each player places four stones or seeds in each of their six pits.

3. Starting player: The starting player is determined by any agreed method, such as flipping a coin or playing rock-paper-scissors.

4. Game play: The starting player chooses one of their pits and takes all the stones or seeds from that pit. The player then drops one stone or seed into each of the pits, moving counterclockwise around the board. If the player reaches their own Mancala, they drop one stone or seed into it, but they do not drop a stone or seed into their opponent's Mancala. If the last stone or seed lands in an empty pit on the player's own side of the board, they get to take all the stones or seeds from the pit directly opposite that pit on their opponent's side of the board and add them to their own Mancala.

5. Turn ends: If the last stone or seed lands in the player's own Mancala, they get another turn. If the last stone or seed lands in an empty pit on the player's own side of the board, and the pit opposite on the opponent's side is also empty, the player's turn ends.

6. Capturing: If the last stone or seed lands in an empty pit on the player's own side of the board, and the pit opposite on the opponent's side contains stones or seeds, the player captures all the stones or seeds in the opponent's pit and places them in their own Mancala. The captured stones or seeds do not count toward the player's own score.

7. Winning: The game ends when one player has no stones or seeds left in their pits. The remaining stones or seeds on the board are added to the player's Mancala, and the player with the most stones or seeds in their Mancala at the end of the game wins.

## 🕹️ How to Run/Play the Mancala Game
If on windows double-click run_me.bat or run python main.py in a console when in main.py directory.
The game includes 4 modes (1 - Human vs. AI, 2 - Human vs. Human, 3 - AI vs. AI opponent, 4 - Random Agent vs. AI) so you can play against your friend or agaisnt the computer. You can also watch the computer playing against the computer with different difficulty levels and strategies or against a Random Agent (it will play random numbers).

There are two options: console and interface.
If you choose to play in the console type "1" and then select the difficulty level (1- Easy, 2- Medium, 3- Hard, 4- World Champion).
In the next step choose the algotrithm to play (1- Minimax, 2- Alpha Beta Pruning) and finally the AI strategy (evalutation function).
When running the script you are presented the initial game state:

```
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 4 | 4 | 4 | 4 | 4 | 4 | Score: 0
---------------------------------------
Player 1 | 4 | 4 | 4 | 4 | 4 | 4 | Score: 0
=======================================
Slots:   | 5 | 4 | 3 | 2 | 1 | 0 |

It is player 1's turn
Choose which slot to pick up (index at 0): 
```

You are player 1.

Choose a value in the `Slots: ` row to pick up the corresponding pieces on your side 
and place them anti-clockwise in other slots

When it is the AI's turn it will compute it's next move:

```
It is player 1's turn
Choose which slot to pick up (index at 0): 4
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 4 | 4 | 4 | 5 | 5 | 5 | Score: 0  <-- Notice the 3'rd slot
---------------------------------------
Player 1 | 4 | 4 | 0 | 5 | 0 | 6 | Score: 2
=======================================
Slots:   | 5 | 4 | 3 | 2 | 1 | 0 |

It is player 2's turn
AI computing tree
AI computing best move
AI found utility: -4, move: 3  <-- AI found the best move in slot 3
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 5 | 5 | 5 | 0 | 5 | 5 | Score: 1  <-- Slot 3 has been picked up
---------------------------------------
Player 1 | 5 | 4 | 0 | 5 | 0 | 6 | Score: 2
=======================================
Slots:   | 5 | 4 | 3 | 2 | 1 | 0 |

It is player 1's turn
Choose which slot to pick up (index at 0): 
```

The above printout is explained by the `<--` arrows.

When one of the player's side is empty, the game will sum all the pieces together on each side
and compute the winner. Moreover, it will also record and print the game sequence in a 2-tuple
of (player_turn, move)

```
It is player 1's turn
Choose which slot to pick up (index at 0): 5
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 9 | 2 | 10 | 1 | 9 | 1 | Score: 10
---------------------------------------
Player 1 | 0 | 0 | 0 | 0 | 0 | 0 | Score: 6  <-- Empty side
=======================================

It is player 2's turn
AI computing tree
AI computing best move
AI found utility: 36, move: 5
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 0 | 0 | 0 | 0 | 0 | 0 | Score: 42  <-- All pieces summed together and added to score
---------------------------------------
Player 1 | 0 | 0 | 0 | 0 | 0 | 0 | Score: 6
=======================================
Slots:   | 5 | 4 | 3 | 2 | 1 | 0 |

Game over, winner is Player 2
Game sequence: [(0, 0), (1, 4), (0, 2), (1, 2), (1, 0), (0, 3), (1, 4), (1, 2), (0, 4), (1, 0), (0, 0), (1, 2), (0, 5), (1, 0)]
Press Enter to end...
```
You can also choose to play in the interface, implemented using the tkinder. The rules are the same but it is a more user friendly option.

Start by choosing the mode:
![Optional Text](\images\MenuInterface.jpeg)

Choose the level:
![Optional Text](\images\DifficultyLevel_Choice.jpeg)

We reccommend to choose the Alpha beta pruning algorithm bewtween the both implemented - Minmax and Alpha-Beta Pruning - it is more efficient and fast
![Optional Text](\images\Algorithm_Choice.jpeg)

And to finalize choose the strategy - Evaluation Functions - for the AI Agents:
![Optional Text](\images\EvaluationFunction_Choice.jpeg)

When the game starts, in the Human modes, the user is prompted to insert the number of the slot that is inteded to play in the dialog box - player 1 controls the lower slots and the right bucket (Mancala).
![Optional Text](\images\Slot_Choice.jpeg)

The game finishes when all the seeds are in the mancalas. In the end, it´s possible to visaulize the winner, the number of seeds for each player with the final results.
![Optional Text](\images\GameOver.jpeg)

## 📈 Improvements
The improvements made were as follows:
1. Improvement and Conclusion of the paper that had previously been delivered;
2. Improvement and update of the presentation (this one will not be presented again);
3. Fixing minor bugs (code);
4. Creation of an interface;
5. Elaboration of the game's optional video;

## 📜 Requirements
As requirements for the correct functioning of the game is necessary to have installed a version of Python 3c, tkinder, random, time and a few others libraris/imports that should be considered. 

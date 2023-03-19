import tkinter
import random
from src.AI import MancalaTreeBuilder, Node, Minimax, Alpha_Beta_Pruning, evaluation_extraturn_capture, evaluation_moves, evaluation_board
from src.Mancala import Game
import time
from tkinter import simpledialog

class Interface:
    
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Mancala")
        self.level = None
        self.level_ai1 = None
        self.level_ai2 = None
        self.level_ai3 = None
        self.algorithm = None
        self.algorithm_ai1 = None
        self.algorithm_ai2 = None
        self.algorithm_ai3 = None
        self.evaluation_function = None
        self.evaluation_function_ai1 = None
        self.evaluation_function_ai2 = None
        self.evaluation_function_ai3 = None
        
        # Load the image file and create a PhotoImage object
        icon_image = tkinter.PhotoImage(file='images/Seed.png')

        # Set the image as the window icon
        self.root.wm_iconphoto(True, icon_image)
        self.size = self.w_width, self.w_height = 800, 600
        self.speed = [2, 2]
        self.white = '#FFFFFF'

        self.board = Game.init_board(Game.BOARD_SIZE)
        self.canvas = tkinter.Canvas(self.root, height=self.w_height, width=self.w_width,
                                     background='#d1b48c', highlightbackground='#d1b48c')
        self.canvas.pack()
        self.main_gui()

    def start(self):
        self.root.mainloop()

    # main function
    def main_gui(self):
        
        def style():
            wood_img = tkinter.PhotoImage(file='images/Wood.png')
            style = {
                'font': ("Arial", 12),
                'width': 200,
                'height': 50,
                'fg': 'white',
                'bg': '#AC7D45',
                'highlightthickness': 0,
                'image': wood_img,
                'compound': 'center'
            }
            return style
        button_style =  style()
        # Greatings
        self.canvas.create_text(400, 75, text="Welcome to Mancala Game!", font=(
            "Arial bold", 40), fill="black", anchor='center')
        self.canvas.create_text(400, 350, text="Choose between the following options:", font=(
            "Arial", 16), fill="black", anchor='center')

        # Mancala Game Options
        img = tkinter.PhotoImage(file='images/Mancala_capa.png')

        button1 = tkinter.Button(self.canvas, text="Human vs Human", 
            command=self.human_vs_human,  **button_style)
        button2 = tkinter.Button(self.canvas, text="Human vs AI", 
                                 command=self.choose_difficulty, **button_style)
        button3 = tkinter.Button(self.canvas, text="AI vs AI", 
                                 command=self.choose_difficulty_1,  **button_style)
        button4 = tkinter.Button(self.canvas, text="Random Agent vs AI", 
                                 command=self.choose_difficulty_3,   **button_style)

        # Set up grid layout with 3 rows and 1 column
        self.canvas.grid_rowconfigure(0, weight=1)
        self.canvas.grid_rowconfigure(1, weight=1)
        self.canvas.grid_rowconfigure(2, weight=1)
        self.canvas.grid_columnconfigure(0, weight=1)

        # Place buttons in grid layout with more spacing
        button1.grid(row=0, column=0, padx=20, pady=20)
        button2.grid(row=1, column=0, padx=20, pady=20)
        button3.grid(row=2, column=0, padx=20, pady=20)
        button4.grid(row=2, column=0, padx=20, pady=20)

        # Add the button to the self.canvas
        self.canvas.create_window(
            550, 450, anchor=tkinter.CENTER, window=button1)
        self.canvas.create_window(
            250, 450, anchor=tkinter.CENTER, window=button2)
        self.canvas.create_window(
            550, 550, anchor=tkinter.CENTER, window=button3)
        self.canvas.create_window(
            250, 550, anchor=tkinter.CENTER, window=button4)
        self.canvas.create_image(400, 200, image=img)

        self.root.mainloop()
    
    # print self.board
    def print_board(self, board):

        # self.board rectangle
        self.canvas.create_rectangle(50, 150, 750, 400, fill='white', width=3)

        # draw self.board lines
        self.canvas.create_rectangle(
            100, 150, 700, 200, fill='#c78c54', width=3)
        self.canvas.create_rectangle(
            100, 350, 700, 400, fill='#af916b', width=3)
        self.canvas.create_rectangle(100, 272, 700, 277, fill='black')
        self.canvas.create_rectangle(1, 150, 100, 400, fill='#c78c54', width=3)
        self.canvas.create_rectangle(
            700, 150, 800, 400, fill='#af916b', width=3)

        self.canvas.create_line(200, 150, 200, 400)
        self.canvas.create_line(300, 150, 300, 400)
        self.canvas.create_line(400, 150, 400, 400)
        self.canvas.create_line(500, 150, 500, 400)
        self.canvas.create_line(600, 150, 600, 400)

        # draw self.board numbers
        self.canvas.create_text(650, 175, text="0")
        self.canvas.create_text(550, 175, text="1")
        self.canvas.create_text(450, 175, text="2")
        self.canvas.create_text(350, 175, text="3")
        self.canvas.create_text(250, 175, text="4")
        self.canvas.create_text(150, 175, text="5")
        self.canvas.create_text(650, 375, text="5")
        self.canvas.create_text(550, 375, text="4")
        self.canvas.create_text(450, 375, text="3")
        self.canvas.create_text(350, 375, text="2")
        self.canvas.create_text(250, 375, text="1")
        self.canvas.create_text(150, 375, text="0")
        self.canvas.create_text(51, 250, text="Player 2",
                                font=("Arial bold", 15))
        self.canvas.create_text(
            750, 250, text="Player 1", font=("Arial bold", 15))

        # draw self.board values
        self.canvas.create_text(650, 235, text=int(
            self.board[7]), font=("Arial bold", 15))
        self.canvas.create_text(550, 235, text=int(
            self.board[8]), font=("Arial bold", 15))
        self.canvas.create_text(450, 235, text=int(
            self.board[9]), font=("Arial bold", 15))
        self.canvas.create_text(350, 235, text=int(
            self.board[10]), font=("Arial bold", 15))
        self.canvas.create_text(250, 235, text=int(
            self.board[11]), font=("Arial bold", 15))
        self.canvas.create_text(150, 235, text=int(
            self.board[12]), font=("Arial bold", 15))
        self.canvas.create_text(650, 315, text=int(
            self.board[5]), font=("Arial bold", 15))
        self.canvas.create_text(550, 315, text=int(
            self.board[4]), font=("Arial bold", 15))
        self.canvas.create_text(450, 315, text=int(
            self.board[3]), font=("Arial bold", 15))
        self.canvas.create_text(350, 315, text=int(
            self.board[2]), font=("Arial bold", 15))
        self.canvas.create_text(250, 315, text=int(
            self.board[1]), font=("Arial bold", 15))
        self.canvas.create_text(150, 315, text=int(
            self.board[0]), font=("Arial bold", 15))
        self.canvas.create_text(75, 275, text=int(
            self.board[13]), font=("Arial bold", 15))
        self.canvas.create_text(725, 275, text=int(
            self.board[6]), font=("Arial bold", 15))

    def print_board_state(self, state):

        # self.board rectangle
        self.canvas.create_rectangle(50, 150, 750, 400, fill='white', width=3)

        # draw self.board lines
        self.canvas.create_rectangle(
            100, 150, 700, 200, fill='#c78c54', width=3)
        self.canvas.create_rectangle(
            100, 350, 700, 400, fill='#af916b', width=3)
        self.canvas.create_rectangle(100, 272, 700, 277, fill='black')
        self.canvas.create_rectangle(1, 150, 100, 400, fill='#c78c54', width=3)
        self.canvas.create_rectangle(
            700, 150, 800, 400, fill='#af916b', width=3)

        self.canvas.create_line(200, 150, 200, 400)
        self.canvas.create_line(300, 150, 300, 400)
        self.canvas.create_line(400, 150, 400, 400)
        self.canvas.create_line(500, 150, 500, 400)
        self.canvas.create_line(600, 150, 600, 400)

        # draw self.board numbers
        self.canvas.create_text(650, 175, text="0")
        self.canvas.create_text(550, 175, text="1")
        self.canvas.create_text(450, 175, text="2")
        self.canvas.create_text(350, 175, text="3")
        self.canvas.create_text(250, 175, text="4")
        self.canvas.create_text(150, 175, text="5")
        self.canvas.create_text(650, 375, text="5")
        self.canvas.create_text(550, 375, text="4")
        self.canvas.create_text(450, 375, text="3")
        self.canvas.create_text(350, 375, text="2")
        self.canvas.create_text(250, 375, text="1")
        self.canvas.create_text(150, 375, text="0")
        self.canvas.create_text(51, 250, text="Player 2",
                                font=("Arial bold", 15))
        self.canvas.create_text(
            750, 250, text="Player 1", font=("Arial bold", 15))

        # draw self.board values
        self.canvas.create_text(650, 235, text=int(
            state[1][0]), font=("Arial bold", 15))
        self.canvas.create_text(550, 235, text=int(
            state[1][1]), font=("Arial bold", 15))
        self.canvas.create_text(450, 235, text=int(
            state[1][2]), font=("Arial bold", 15))
        self.canvas.create_text(350, 235, text=int(
            state[1][3]), font=("Arial bold", 15))
        self.canvas.create_text(250, 235, text=int(
            state[1][4]), font=("Arial bold", 15))
        self.canvas.create_text(150, 235, text=int(
            state[1][5]), font=("Arial bold", 15))
        self.canvas.create_text(650, 315, text=int(
            state[0][5]), font=("Arial bold", 15))
        self.canvas.create_text(550, 315, text=int(
            state[0][4]), font=("Arial bold", 15))
        self.canvas.create_text(450, 315, text=int(
            state[0][3]), font=("Arial bold", 15))
        self.canvas.create_text(350, 315, text=int(
            state[0][2]), font=("Arial bold", 15))
        self.canvas.create_text(250, 315, text=int(
            state[0][1]), font=("Arial bold", 15))
        self.canvas.create_text(150, 315, text=int(
            state[0][0]), font=("Arial bold", 15))
        self.canvas.create_text(51, 285, text=int(
            state[1][6]), font=("Arial bold", 15))
        self.canvas.create_text(750, 285, text=int(
            state[0][6]), font=("Arial bold", 15))

    def ai_difficulty_click(self, level):
        self.level = level
        self.choose_algorithm()

    def ai_algorithm_click(self, algorithm):
        self.algorithm = algorithm
        self.choose_evaluation()

    def ai_evaluation_click(self, evaluation_function):
        self.evaluation_function = evaluation_function
        self.human_vs_ai()

    def choose_difficulty(self):
                           
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose the difficulty level for the AI Agent:", font=(
            "Arial", 16), fill="black", anchor='center')

        self.button5 = tkinter.Button(
            self.canvas, text="Easy", command=lambda: self.ai_difficulty_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button6 = tkinter.Button(
            self.canvas, text="Medium", command=lambda: self.ai_difficulty_click(2) , font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button7 = tkinter.Button(
            self.canvas, text="Hard", command=lambda: self.ai_difficulty_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button8 = tkinter.Button(
            self.canvas, text="World Champion", command=lambda: self.ai_difficulty_click(4), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            285, 400, anchor=tkinter.CENTER, window=self.button5)
        self.canvas.create_window(
            510, 400, anchor=tkinter.CENTER, window=self.button6)
        self.canvas.create_window(
            285, 500, anchor=tkinter.CENTER, window=self.button7)
        self.canvas.create_window(
            510, 500, anchor=tkinter.CENTER, window=self.button8)

    def choose_algorithm(self):
        
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an algorithm:", font=(
            "Arial", 16), fill="black", anchor='center')

        self.button9 = tkinter.Button(
            self.canvas, text="Minimax", command=lambda: self.ai_algorithm_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button10 = tkinter.Button(
            self.canvas, text="Alpha-Beta Pruning", command=lambda: self.ai_algorithm_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            400, 400, anchor=tkinter.CENTER, window=self.button9)
        self.canvas.create_window(
            400, 480, anchor=tkinter.CENTER, window=self.button10)

    def choose_evaluation(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an evaluation function:", font=(
            "Arial", 16), fill="black", anchor='center')



        self.button11 = tkinter.Button(
            self.canvas, text="Extra-Turn and Capture", command=lambda: self.ai_evaluation_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button12 = tkinter.Button(
            self.canvas, text="Moves", command=lambda: self.ai_evaluation_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button13 = tkinter.Button(
            self.canvas, text="Board", command=lambda: self.ai_evaluation_click(3),font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            200, 450, anchor=tkinter.CENTER, window=self.button11)
        self.canvas.create_window(
            400, 450, anchor=tkinter.CENTER, window=self.button12)
        self.canvas.create_window(
            600, 450, anchor=tkinter.CENTER, window=self.button13)

    def ai1_difficulty_click(self, level):
        self.level_ai1 = level
        self.choose_algorithm_1()

    def ai1_algorithm_click(self, algorithm):
        self.algorithm_ai1 = algorithm
        self.choose_evaluation_1()

    def ai1_evaluation_click(self, evaluation_function):
        self.evaluation_function_ai1 = evaluation_function
        self.choose_difficulty_2()

    def choose_difficulty_1(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose the difficulty level for the first AI Agent:", font=(
            "Arial", 16), fill="black", anchor='center')

        wood_img = tkinter.PhotoImage(file='images/Wood.png')
        button_style = {
            'font': ("Arial", 12),
            'width': 200,
            'height': 50,
            'fg': 'white',
            'bg': '#AC7D45',
            'highlightthickness': 0,
            'image': wood_img,
            'compound': 'center'
        }
        
        self.button5 = tkinter.Button(
            self.canvas, text="Easy", command=lambda: self.ai1_difficulty_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button5.image = wood_img
        self.button6 = tkinter.Button(
            self.canvas, text="Medium", command=lambda: self.ai1_difficulty_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button7 = tkinter.Button(
            self.canvas, text="Hard", command=lambda: self.ai1_difficulty_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button8 = tkinter.Button(
            self.canvas, text="World Champion", command=lambda: self.ai1_difficulty_click(4), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            285, 400, anchor=tkinter.CENTER, window=self.button5)
        self.canvas.create_window(
            510, 400, anchor=tkinter.CENTER, window=self.button6)
        self.canvas.create_window(
            285, 500, anchor=tkinter.CENTER, window=self.button7)
        self.canvas.create_window(
            510, 500, anchor=tkinter.CENTER, window=self.button8)

    def choose_algorithm_1(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an algorithm:", font=(
            "Arial", 16), fill="black", anchor='center')
      
        self.button9 = tkinter.Button(
            self.canvas, text="Minimax", command=lambda: self.ai1_algorithm_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button10 = tkinter.Button(
            self.canvas, text="Alpha-Beta Pruning", command=lambda: self.ai1_algorithm_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            400, 400, anchor=tkinter.CENTER, window=self.button9)
        self.canvas.create_window(
            400, 480, anchor=tkinter.CENTER, window=self.button10)

    def choose_evaluation_1(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an evaluation function:", font=(
            "Arial", 16), fill="black", anchor='center')



        
        self.button11 = tkinter.Button(
            self.canvas, text="Extra-Turn and Capture", command=lambda: self.ai1_evaluation_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button12 = tkinter.Button(
            self.canvas, text="Moves", command=lambda: self.ai1_evaluation_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button13 = tkinter.Button(
            self.canvas, text="Board", command=lambda: self.ai1_evaluation_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            200, 450, anchor=tkinter.CENTER, window=self.button11)
        self.canvas.create_window(
            400, 450, anchor=tkinter.CENTER, window=self.button12)
        self.canvas.create_window(
            600, 450, anchor=tkinter.CENTER, window=self.button13)

    def ai2_difficulty_click(self, level):
        self.level_ai2 = level
        self.choose_algorithm_2()

    def ai2_algorithm_click(self, algorithm):
        self.algorithm_ai2 = algorithm
        self.choose_evaluation_2()

    def ai2_evaluation_click(self, evaluation_function):
        self.evaluation_function_ai2 = evaluation_function
        self.ai_vs_ai()

    def choose_difficulty_2(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose the difficulty level for the second AI Agent:", font=(
            "Arial", 16), fill="black", anchor='center')
       
        self.button5 = tkinter.Button(
            self.canvas, text="Easy", command=lambda: self.ai2_difficulty_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button6 = tkinter.Button(
            self.canvas, text="Medium", command=lambda: self.ai2_difficulty_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button7 = tkinter.Button(
            self.canvas, text="Hard", command=lambda: self.ai2_difficulty_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button8 = tkinter.Button(
            self.canvas, text="World Champion", command=lambda: self.ai2_difficulty_click(4), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            285, 400, anchor=tkinter.CENTER, window=self.button5)
        self.canvas.create_window(
            510, 400, anchor=tkinter.CENTER, window=self.button6)
        self.canvas.create_window(
            285, 500, anchor=tkinter.CENTER, window=self.button7)
        self.canvas.create_window(
            510, 500, anchor=tkinter.CENTER, window=self.button8)

    def choose_algorithm_2(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an algorithm:", font=(
            "Arial", 16), fill="black", anchor='center')
        
        self.button9 = tkinter.Button(
            self.canvas, text="Minimax", command=lambda: self.ai2_algorithm_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button10 = tkinter.Button(
            self.canvas, text="Alpha-Beta Pruning", command=lambda: self.ai2_algorithm_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            400, 400, anchor=tkinter.CENTER, window=self.button9)
        self.canvas.create_window(
            400, 480, anchor=tkinter.CENTER, window=self.button10)

    def choose_evaluation_2(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an evaluation function:", font=(
            "Arial", 16), fill="black", anchor='center')

        self.button11 = tkinter.Button(
            self.canvas, text="Extra-Turn and Capture", command=lambda: self.ai2_evaluation_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button12 = tkinter.Button(
            self.canvas, text="Moves", command=lambda: self.ai2_evaluation_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button13 = tkinter.Button(
            self.canvas, text="Board", command=lambda: self.ai2_evaluation_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            200, 450, anchor=tkinter.CENTER, window=self.button11)
        self.canvas.create_window(
            400, 450, anchor=tkinter.CENTER, window=self.button12)
        self.canvas.create_window(
            600, 450, anchor=tkinter.CENTER, window=self.button13)

    def ai3_difficulty_click(self, level):
        self.level_ai3 = level
        self.choose_algorithm_3()

    def ai3_algorithm_click(self, algorithm):
        self.algorithm_ai3 = algorithm
        self.choose_evaluation_3()

    def ai3_evaluation_click(self, evaluation_function):
        self.evaluation_function_ai3 = evaluation_function
        self.randomagent_vs_ai()

    def choose_difficulty_3(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose the difficulty level for the AI Agent:", font=(
            "Arial", 16), fill="black", anchor='center')
        
        self.button5 = tkinter.Button(
            self.canvas, text="Easy", command=lambda: self.ai3_difficulty_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button6 = tkinter.Button(
            self.canvas, text="Medium", command=lambda: self.ai3_difficulty_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button7 = tkinter.Button(
            self.canvas, text="Hard", command=lambda: self.ai3_difficulty_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button8 = tkinter.Button(
            self.canvas, text="World Champion", command=lambda: self.ai3_difficulty_click(4), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            285, 400, anchor=tkinter.CENTER, window=self.button5)
        self.canvas.create_window(
            510, 400, anchor=tkinter.CENTER, window=self.button6)
        self.canvas.create_window(
            285, 500, anchor=tkinter.CENTER, window=self.button7)
        self.canvas.create_window(
            510, 500, anchor=tkinter.CENTER, window=self.button8)

    def choose_algorithm_3(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an algorithm:", font=(
            "Arial", 16), fill="black", anchor='center')
       
        self.button9 = tkinter.Button(
            self.canvas, text="Minimax", command=lambda: self.ai3_algorithm_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button10 = tkinter.Button(
            self.canvas, text="Alpha-Beta Pruning", command=lambda: self.ai3_algorithm_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            400, 400, anchor=tkinter.CENTER, window=self.button9)
        self.canvas.create_window(
            400, 480, anchor=tkinter.CENTER, window=self.button10)

    def choose_evaluation_3(self):
        self.canvas.delete('all')
        self.canvas.create_text(400, 350, text="Choose an evaluation function:", font=(
            "Arial", 16), fill="black", anchor='center')

        wood_img = tkinter.PhotoImage(file='images/Wood.png')
        button_style = {
            'font': ("Arial", 12),
            'width': 200,
            'height': 50,
            'fg': 'white',
            'bg': '#AC7D45',
            'highlightthickness': 0,
            'image': wood_img,
            'compound': 'center'
        }
        
        self.button11 = tkinter.Button(
            self.canvas, text="Extra-Turn and Capture", command=lambda: self.ai3_evaluation_click(1), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button12 = tkinter.Button(
            self.canvas, text="Moves", command=lambda: self.ai3_evaluation_click(2), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')
        self.button13 = tkinter.Button(
            self.canvas, text="Board", command=lambda: self.ai3_evaluation_click(3), font=("Arial", 10), width=20, height=3, bg='#C3843A', fg='white')

        self.canvas.create_window(
            200, 450, anchor=tkinter.CENTER, window=self.button11)
        self.canvas.create_window(
            400, 450, anchor=tkinter.CENTER, window=self.button12)
        self.canvas.create_window(
            600, 450, anchor=tkinter.CENTER, window=self.button13)

    def check_slot_input(self, prompt):
        while True:
            try:
                val = simpledialog.askinteger(
                    "Slot Selection", prompt, parent=self.canvas)
                if val is None:
                    # Handle Cancel button or closing the dialog box
                    return None
                elif 0 <= val <= 5:
                    return val
                else:
                    self.canvas.create_text(
                        400, 450,
                        text="Slot index must be a value between 0 and 5. Please try again.",
                        font=("Arial", 14),
                        fill="red")
            except ValueError:
                self.canvas.create_text(
                    400, 450,
                    text="Not a recognizable integer, please try again.",
                    font=("Arial", 14),
                    fill="red")

    def human_vs_human(self):
        global entry
        self.canvas.delete('all')
        self.print_board(self.board)
        self.canvas.create_text(
            400, 50, text='Human vs Human', font=('Arial bold', 25))
        # Run game
        game = Game()
        should_end = game.is_terminal_state()

        print("")
        print("Game started")
        print("")
        game_seq = []

        while not should_end:
            self.canvas.delete('all')
            state = game.get_state()
            self.print_board_state(state)
            self.canvas.update()

            player_turn = game.get_player_turn()
            print("\nIt is player {0}'s turn".format(1 + player_turn))
            if ((1 + player_turn) == 1):
                player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
            else:
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
            slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
            print("Player {0} choosen slot: {1}".format(1 + player_turn, slot))
            print("")
            # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
            game_seq.append((player_turn, slot))
            # Reverse slot if player 2 is playing
            game.take_slot(slot)
            winner = 0
            if game.is_terminal_state():
                winner = game.end_game()
                should_end = True
            self.canvas.update()
            state = game.get_state()
            self.print_board_state(state)
            self.canvas.update()
        self.canvas.create_text(
            400, 450, text='GAME OVER!', font=('Arial bold', 15))
        self.canvas.create_text(
            300, 500, text=f'Player 1: {state[0][6]} seeds')
        self.canvas.create_text(
            500, 500, text=f'Player 2: {state[1][6]} seeds')
        self.canvas.delete(player1)
        self.canvas.delete(player2)
        if (state[0][6] > state[0][6]):
            self.canvas.create_text(
                400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
        elif (state[0][6] < state[1][6]):
            self.canvas.create_text(
                400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
        else:
            self.canvas.create_text(
                400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))

    def human_vs_ai(self):
        global entry
        self.canvas.delete('all')
        self.print_board(self.board)
        self.canvas.create_text(
            400, 50, text='Human vs Artificial Inteligence', font=('Arial bold', 25))

        difficulty = self.level
        algorithm_choice = self.algorithm
        evaluation_function = self.evaluation_function
        total_time = 0
        rec_limit = 2 + difficulty * 2

        if (algorithm_choice == 1 and evaluation_function == 1):
            # Minimax algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Minimax object
            minimax = Minimax(evaluation_extraturn_capture,
                              result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()
            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
                    slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[0][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))

        elif (algorithm_choice == 1 and evaluation_function == 2):
            # Minimax algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Minimax object
            minimax = Minimax(evaluation_moves,
                              result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()
            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
                    slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[0][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 1 and evaluation_function == 3):
            # Minimax algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Minimax object
            minimax = Minimax(evaluation_board,
                              result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()
            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                slot = None
                if (player_turn == 0):
                    slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[0][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 2 and evaluation_function == 1):
            # Alpha-Beta Pruning algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Alpha-Beta Pruning object
            minimax_cuts = Alpha_Beta_Pruning(
                evaluation_extraturn_capture, result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                slot = None
                if (player_turn == 0):
                    slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[0][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))

        elif (algorithm_choice == 2 and evaluation_function == 2):
            # Alpha-Beta Pruning algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Alpha-Beta Pruning object
            minimax_cuts = Alpha_Beta_Pruning(
                evaluation_moves, result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                slot = None
                if (player_turn == 0):
                    slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[0][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 2 and evaluation_function == 3):
            # Alpha-Beta Pruning algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Alpha-Beta Pruning object
            minimax_cuts = Alpha_Beta_Pruning(
                evaluation_board, result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
                    slot = self.check_slot_input("Choose which slot to pick up (from 0 to 5)")
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[0][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))

    def ai_vs_ai(self):

        global entry
        self.canvas.delete('all')
        self.print_board(self.board)
        self.canvas.create_text(
            400, 50, text='Artificial Inteligence vs Artificial Inteligence', font=('Arial bold', 25))

        difficulty1 = self.level_ai1
        difficulty2 = self.level_ai2
        algorithm_choice_player1 = self.algorithm_ai1
        algorithm_choice_player2 = self.algorithm_ai2
        evaluation_function_player1 = self.evaluation_function_ai1
        evaluation_function_player2 = self.evaluation_function_ai2
        total_time = 0
        rec_limit_player1 = 2 + difficulty1 * 2
        rec_limit_player2 = 2 + difficulty2 * 2

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
            self.canvas.delete('all')
            state = game.get_state()
            self.print_board_state(state)
            self.canvas.update()
            player_turn = game.get_player_turn()
            print("\nIt is player {0}'s turn".format(1 + player_turn))
            slot = None

            if (player_turn == 0 and algorithm_choice_player1 == 1 and evaluation_function_player1 == 1):
                player1 = player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo1_player1 = Minimax(
                    evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player1)
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

            elif (player_turn == 0 and algorithm_choice_player1 == 1 and evaluation_function_player1 == 2):
                player1 = player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo1_player1 = Minimax(
                    evaluation_moves, result_function_player, max_depth=rec_limit_player1)
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

            elif (player_turn == 0 and algorithm_choice_player1 == 1 and evaluation_function_player1 == 3):
                player1 = player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo1_player1 = Minimax(
                    evaluation_board, result_function_player, max_depth=rec_limit_player1)
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

            elif (player_turn == 0 and algorithm_choice_player1 == 2 and evaluation_function_player1 == 1):
                player1 = player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo2_player1 = Alpha_Beta_Pruning(
                    evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player1)
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

            elif (player_turn == 0 and algorithm_choice_player1 == 2 and evaluation_function_player1 == 2):
                player1 = player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo2_player1 = Alpha_Beta_Pruning(
                    evaluation_moves, result_function_player, max_depth=rec_limit_player1)
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

            elif (player_turn == 0 and algorithm_choice_player1 == 2 and evaluation_function_player1 == 3):
                player1 = player1 = self.canvas.create_text(
                    700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo2_player1 = Alpha_Beta_Pruning(
                    evaluation_board, result_function_player, max_depth=rec_limit_player1)
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

            elif (player_turn == 1 and algorithm_choice_player2 == 1 and evaluation_function_player2 == 1):
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo1_player2 = Minimax(
                    evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player2)
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

            elif (player_turn == 1 and algorithm_choice_player2 == 1 and evaluation_function_player2 == 2):
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo1_player2 = Minimax(
                    evaluation_moves, result_function_player, max_depth=rec_limit_player2)
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

            elif (player_turn == 1 and algorithm_choice_player2 == 1 and evaluation_function_player2 == 3):
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo1_player2 = Minimax(
                    evaluation_board, result_function_player, max_depth=rec_limit_player2)
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

            elif (player_turn == 1 and algorithm_choice_player2 == 2 and evaluation_function_player2 == 1):
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo2_player2 = Alpha_Beta_Pruning(
                    evaluation_extraturn_capture, result_function_player, max_depth=rec_limit_player2)
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

            elif (player_turn == 1 and algorithm_choice_player2 == 2 and evaluation_function_player2 == 2):
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                algo2_player2 = Alpha_Beta_Pruning(
                    evaluation_moves, result_function_player, max_depth=rec_limit_player2)
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

            elif (player_turn == 1 and algorithm_choice_player2 == 2 and evaluation_function_player2 == 3):
                player2 = self.canvas.create_text(
                    100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                algo2_player2 = Alpha_Beta_Pruning(
                    evaluation_board, result_function_player, max_depth=rec_limit_player2)
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

            # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
            game_seq.append((player_turn, slot))
            # Reverse slot if player 2 is playing
            game.take_slot(slot)

            winner = 0
            if game.is_terminal_state():
                winner = game.end_game()
                should_end = True
                self.canvas.update()
            state = game.get_state()
            self.print_board_state(state)
            self.canvas.update()
        self.canvas.create_text(
            400, 450, text='GAME OVER!', font=('Arial bold', 15))
        self.canvas.create_text(
            300, 500, text=f'Player 1: {state[0][6]} seeds')
        self.canvas.create_text(
            500, 500, text=f'Player 2: {state[1][6]} seeds')
        self.canvas.delete(player1)
        self.canvas.delete(player2)

        if (state[0][6] > state[0][6]):
            self.canvas.create_text(
                400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
        elif (state[0][6] < state[1][6]):
            self.canvas.create_text(
                400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
        else:
            self.canvas.create_text(
                400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))

    def randomagent_vs_ai(self):

        global entry
        self.canvas.delete('all')
        self.print_board(self.board)
        self.canvas.create_text(
            400, 50, text='Random Agent vs Artificial Inteligence', font=('Arial bold', 25))

        def selecionar_valor():
            return random.randint(0, 5)

        difficulty = self.level_ai3
        algorithm_choice = self.algorithm_ai3
        evaluation_function = self.evaluation_function_ai3
        rec_limit = 2 + difficulty * 2
        total_time = 0

        print(difficulty)
        print(algorithm_choice)
        print(evaluation_function)

        if (algorithm_choice == 1 and evaluation_function == 1):
            # Minimax algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Minimax object
            minimax = Minimax(evaluation_extraturn_capture,
                              result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()
            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)

            if (state[0][6] > state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 1 and evaluation_function == 2):
            # Minimax algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Minimax object
            minimax = Minimax(evaluation_moves,
                              result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()
            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 1 and evaluation_function == 3):
            # Minimax algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Minimax object
            minimax = Minimax(evaluation_board,
                              result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()
            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 2 and evaluation_function == 1):
            # Alpha-Beta Pruning algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Alpha-Beta Pruning object
            minimax_cuts = Alpha_Beta_Pruning(
                evaluation_extraturn_capture, result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 2 and evaluation_function == 2):
            # Alpha-Beta Pruning algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Alpha-Beta Pruning object
            minimax_cuts = Alpha_Beta_Pruning(
                evaluation_moves, result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))
        elif (algorithm_choice == 2 and evaluation_function == 3):
            # Alpha-Beta Pruning algorithm
            def result_function(node, a):
                children = node.get_children()
                return children[a]

            # Construct Alpha-Beta Pruning object
            minimax_cuts = Alpha_Beta_Pruning(
                evaluation_board, result_function, max_depth=rec_limit)

            # Run game
            game = Game()
            should_end = game.is_terminal_state()

            print("")
            print("Game started")
            print("")
            game_seq = []
            while not should_end:
                self.canvas.delete('all')
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()

                player_turn = game.get_player_turn()
                print("\nIt is player {0}'s turn".format(1 + player_turn))
                if ((1 + player_turn) == 1):
                    player1 = player1 = self.canvas.create_text(
                        700, 450, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))
                else:
                    player2 = self.canvas.create_text(
                        100, 100, text=f'Player {player_turn+1} turn!', font=('Arial bold', 15))

                slot = None
                if (player_turn == 0):
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

                # game_seq (Player, Slot selected )  Player -> 0 - Player 1 and 1 - Player 2
                game_seq.append((player_turn, slot))
                # Reverse slot if player 2 is playing
                game.take_slot(slot)

                winner = 0
                if game.is_terminal_state():
                    winner = game.end_game()
                    should_end = True
                    self.canvas.update()
                state = game.get_state()
                self.print_board_state(state)
                self.canvas.update()
            self.canvas.create_text(
                400, 450, text='GAME OVER!', font=('Arial bold', 15))
            self.canvas.create_text(
                300, 500, text=f'Player 1: {state[0][6]} seeds')
            self.canvas.create_text(
                500, 500, text=f'Player 2: {state[1][6]} seeds')
            self.canvas.delete(player1)
            self.canvas.delete(player2)
            if (state[0][6] > state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 1 won the game!", font=('Arial bold', 20))
            elif (state[0][6] < state[1][6]):
                self.canvas.create_text(
                    400, 550, text=f"The Player 2 won the game!", font=('Arial bold', 20))
            else:
                self.canvas.create_text(
                    400, 550, text=f"A draw was obtained!", font=('Arial bold', 20))

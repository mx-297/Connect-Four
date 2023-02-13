""" Group members:

Mohamed Ate 202000313 (team leader)
Ahmad sameh 202000949
Muhamed Hesham 202000892
Mohamed ragab salem 202002035
Abdulaziz Amori 202002019

"""

import numpy as np
import pygame
import sys
import math
import random

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROWS = 6
COLUMNS = 7
SQUARE = 100
RADIUS = int(SQUARE/2) - 5

def create_board():

    board = np.zeros((ROWS,COLUMNS))
    return board

def is_valid(board,col):

    if col == None:
        return False

    return board[ROWS -1][col] == 0

def get_next_row(board,col):

    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def drop_piece(board, col, row, piece):

    board[row][col] = piece

def winning_move(board,piece):

    #Vertically
    for r in range(ROWS-3):
        for c in range(COLUMNS):
            if(board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece):

                return True

    #Horizontally
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if(board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece):
                return True

    #positive slope diagonals
    for r in range(ROWS-3):
        for c in range(COLUMNS-3):
            if(board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True

    #negative slope diagonals

    for r in range(3,ROWS):
        for c in range(COLUMNS-3):
            if(board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True

    return False

def print_board(board):

    print(np.flip(board,0))

def get_valid_locations(board):
    
    valid_locations = []
    for c in range(COLUMNS):
        if is_valid(board,c):
            valid_locations.append(c)
    return valid_locations        

# def normal_evaluate_window(window,piece):
    
#     score = 0
    
#     opp_piece = 1
#     if piece == 1:
#         opp_piece = 2

#     if(window.count(piece) == 4):
#         score+=100
    
#     elif(window.count(piece) == 3 and window.count(0) == 1):
#         score+=5
    
#     elif(window.count(piece) == 2 and window.count(0) == 2):
#         score+=2

#     if(window.count(opp_piece) == 3 and window.count(0) == 1):
#         score-=4  


#     return score

def genetic_algorithm_evaluate_window(window,weights,piece):

    score = 0
    
    opp_piece = 1
    if piece == 1:
        opp_piece = 2

    if(window.count(piece) == 4):
        score+=weights[1]
    
    elif(window.count(piece) == 3 and window.count(0) == 1):
        score+=weights[2]
    
    elif(window.count(piece) == 2 and window.count(0) == 2):
        score+=weights[3]

    if(window.count(opp_piece) == 3 and window.count(0) == 1):
        score-=weights[4] 


    return score



def calculate_score_genetic_algorithm(board,piece,weights):
    
    score = 0
    #center

    centers = list(board[:,COLUMNS//2])
    center_count = centers.count(piece)
    score += center_count*weights[0]
    
    #Horizontally
    
    for r in range(ROWS):
        rows = list(board[r,:])
        for c in range(COLUMNS - 3):
            window = rows[c:c+4]
            score += genetic_algorithm_evaluate_window(window,weights,piece)
    
    #Vertically

    for c in range(COLUMNS):
        
        cols = list(board[:,c])
        for r in range(ROWS - 3):
            window = cols[r:r+4]
            
            score += genetic_algorithm_evaluate_window(window,weights,piece)
    
    #Positive diagonals

    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):

            window = [board[r+i][c+i] for i in range(4)]

            score += genetic_algorithm_evaluate_window(window,weights,piece)
    
    #Negative diagonals
    for r in range(3,ROWS):
        for c in range(COLUMNS - 3):
            window = [board[r-i][c+i] for i in range(4)]

            score += genetic_algorithm_evaluate_window(window,weights,piece)

    return score




# def calculate_score(board,piece):
    
#     score = 0
#     #center

#     centers = list(board[:,COLUMNS//2])
#     center_count = centers.count(piece)
#     score += center_count*3
    
#     #Horizontally
    
#     for r in range(ROWS):
#         rows = list(board[r,:])
#         for c in range(COLUMNS - 3):
#             window = rows[c:c+4]

#             score += normal_evaluate_window(window,piece)
    
#     #Vertically

#     for c in range(COLUMNS):
        
#         cols = list(board[:,c])
#         for r in range(ROWS - 3):
#             window = cols[r:r+4]
            
#             score += normal_evaluate_window(window,piece)
    
#     #Positive diagonals

#     for r in range(ROWS - 3):
#         for c in range(COLUMNS - 3):

#             window = [board[r+i][c+i] for i in range(4)]

#             score += normal_evaluate_window(window,piece)
    
#     #Negative diagonals
#     for r in range(3,ROWS):
#         for c in range(COLUMNS - 3):
#             window = [board[r-i][c+i] for i in range(4)]

#             score += normal_evaluate_window(window,piece)

#     return score


def is_terminal_node(board):

    return winning_move(board,1) or winning_move(board,2) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingplayer,piece,opp_piece,weights):

    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    
    if depth == 0 or is_terminal:
        if is_terminal:

            if(winning_move(board,opp_piece)):

                return (None,-10000000000)
            
            elif(winning_move(board,piece)):
                
                return  (None,10000000000)
            
            else:

                return (None,0)
        else:

            return (None,calculate_score_genetic_algorithm(board,piece,weights))
    
    else:

        if(maximizingplayer):
            
            value = -math.inf
            column = random.choice(valid_locations)
        
            for col in valid_locations:

                row = get_next_row(board,col)
                temp_board = board.copy()
                drop_piece(temp_board,col,row,piece)
                
                new_score = minimax(temp_board,depth-1,alpha,beta,False,piece,opp_piece,weights)[1]

                if(new_score > value):

                    value = new_score
                    column = col

                alpha = max(alpha,value)
                if alpha >= beta:
                    break
        
            return column,value

        else:

            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                
                row = get_next_row(board,col)
                temp_board = board.copy()
                drop_piece(temp_board,col,row,opp_piece)

                new_score = minimax(temp_board,depth-1,alpha,beta,True,piece,opp_piece,weights)[1]
                    
                if(new_score < value):
                    value = new_score
                    column = col
                
                beta = min(beta,value)
                if alpha >= beta:
                    break
            
            return column,value


def start_game(player1, player2,weights_player1,weights_player2):
    
    pygame.init()


    width = COLUMNS * SQUARE
    height = (ROWS + 1) * SQUARE
    size = (width,height)
    screen = pygame.display.set_mode(size)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace",75)
    def draw_board(board):

        for r in range(ROWS):
            for c in range(COLUMNS):
                pygame.draw.rect(screen, (0,0,255), (c*SQUARE,(r+1)*SQUARE,SQUARE,SQUARE))
                pygame.draw.circle(screen, BLACK, (int(c * SQUARE + SQUARE / 2),int((r+1) * SQUARE + SQUARE / 2)), RADIUS)
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if(board[r][c] == 1):
                    
                    pygame.draw.circle(screen, RED, (int(c * SQUARE + SQUARE / 2), height - int(r * SQUARE + SQUARE / 2)), RADIUS)

                elif(board[r][c] == 2):
                    
                    pygame.draw.circle(screen, YELLOW, (int(c * SQUARE + SQUARE / 2),height - int(r * SQUARE + SQUARE / 2)), RADIUS)
        pygame.display.update()


    board = create_board()
    print_board(board)
    draw_board(board)

    


    gameover = False
    turn = 0

    while(not gameover):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()
            

        if(turn == player1):
            #pygame.time.wait(1000)

            col,score = minimax(board,4,-math.inf,math.inf,True,1,2,weights_player1)

            #print(col,score)
            if(is_valid(board, col)):

                row = get_next_row(board,col)
                drop_piece(board,col,row,1)
                
                if(winning_move(board,1)):
                    pygame.draw.rect(screen,BLACK,(0,0,width,SQUARE))
                    label = myfont.render("Player 1 wins!!",1,RED)
                    screen.blit(label,(25,10))
                    gameover = True
                    return 1
            else:
                return
                    
    
        else:

            #pygame.time.wait(1000)
            
            col,score = minimax(board,4,-math.inf,math.inf,True,2,1,weights_player2)

            if(is_valid(board, col)):


                row = get_next_row(board,col)
                drop_piece(board,col,row,2)
                if(winning_move(board,2)):
                    
                    pygame.draw.rect(screen,BLACK,(0,0,width,SQUARE))
                    label = myfont.render("Player 2 wins!!",1,YELLOW)
                    screen.blit(label,(25,10))
                    gameover = True
                    return -1
                    
            else:
                return
        draw_board(board)
        print_board(board)
        
        turn+=1
        turn = turn%2


                
def genetic_algorithm(num_of_rounds,popmax,number_of_genes,mutation_rate):

    players_population = []

    for i in range(popmax):
        players_population.append(random.sample(range(0,99),number_of_genes))
        
    for round in range(num_of_rounds):
        
        players_score_sum = []
        players_score = [ [] for i in range(popmax)]

        for player1 in range(len(players_population)-1):
            
            for player2 in range(player1 + 1, len(players_population)):
                print(str(players_population[player1]) + "\t\t" + str(players_population[player2])) 
                score = start_game(0,1,players_population[player1], players_population[player2])
                print(score)
                if score == 1:
                    players_score[player1].append(score)
                    players_score[player2].append(-1)
                elif score == -1:
                    players_score[player1].append(score)
                    players_score[player2].append(1)

                else:
                    players_score[player1].append(0)
                    players_score[player2].append(0)


        for player in range(len(players_score)):

            players_score_sum.append((players_population[player],sum(players_score[player])))

        Sort_Tuple(players_score_sum)

        fittest_players = [players_score_sum[player][0] for player in range(3)]

        players_population = crossover(fittest_players)
        players_population = mutation(players_population,mutation_rate)

    return players_score_sum[0:3], players_score_sum
                

def Sort_Tuple(tup):
 
    tup.sort(key = lambda x: x[1], reverse = True)
    return tup

def crossover(fittest_players):

    players_poulation = [fittest_players[i] for i in range(len(fittest_players))]
    for player1 in range(len(fittest_players) - 1):

        for player2 in range(player1 + 1, len(fittest_players)):
            
            players_poulation.append(fittest_players[player1][0:3] + fittest_players[player2][3:])
    
    return players_poulation

def mutation(players_population,mutation_rate):

    for i in range(3,len(players_population)):

        for weight in range(len(players_population[i])):

            n = random.random()
            if(n <= mutation_rate):

                players_population[i][weight] = random.randint(0,99)
    
    return players_population

print(genetic_algorithm(10,6,5,0.01))
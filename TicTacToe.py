from os import system
import random

def display_board(board):
	system('clear')
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-|-|-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-|-|-')
	print(board[1] + '|' + board[2] + '|' + board[3])	

# test_board = [' '] * 10
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O','X','O', 'X']
# display_board(test_board)

def player_input():
	marker = ''

	# keep asking player 1 to choose X or O
	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()

	# Assigne player 2, the opposite maker
	player1 = marker
	if marker == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

	return (player1, player2)

def place_marker(board, marker, position):
	board[position] = marker 

def win_check(board, mark):
	return ((board[1] == board[2] == board[3]== mark) or 
		(board[4] == board[5] == board[6] == mark) or 
		(board[7] == board[8] == board[9] == mark) or 
		(board[1] == board[4] == board[7] == mark) or 
		(board[2] == board[5] == board[8] == mark) or 
		(board[3] == board[6] == board[9] == mark) or 
		(board[1] == board[5] == board[9] == mark) or 
		(board[3] == board[5] == board[7] == mark))

# print(win_check(test_board, 'X'))

def choose_first():
	first = random.randint(1, 2)
	if first == 1:
		return "Player 1"
	else:
		return "Player 2"


def space_check(board, position):
	if board[position] == ' ':
		return True
	else:
		return False

def full_board_check(board):
	for i in range(1, 10):
		# if board[i] != ' ':
		# 	return False
		if space_check(board, i):
			return False
	return True

def player_choice(board):
	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Choose your next position: (1-9) '))

	return position

def replay():
	replay = input('do you want to replay? Yes or No.: ')
	if replay.lower().startswith('y'):
		return True
	else:
		return False

print('Welcome to Tic Tac Toe!')

while True:
	#reset the board
	theBoard = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first')

	play_game = input('Are you ready to play? Enter Yes or No.: ')

	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':
			# player1's turn

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)

			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print('Congrats! You have won the game!')
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 2'

		else:
			# player2's turn

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)

			if win_check(theBoard, player2_marker):
				display_board(theBoard)
				print('player2 won the game')
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 1'

	if not replay():
			break



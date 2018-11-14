def game_board(board):
	print('\n'*100)
	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])


def mark_assignment():
	player1 = ''
	player2 = ''
	while player1 != 'X' and player1 != 'O':
		print("Enter the mark for player 1 (X or O only):")
		player1 = input()
	if player1 == 'X':
		player2 = 'O'
	elif player1 == 'O':
		player2 = 'X'
	player1mark  = player1
	player2mark = player2
	print("player 1 is {} and player 2 is {}".format(player1, player2))
	playermarks = [player1, player2]
	return playermarks

playermarks = mark_assignment()

def check_victory(boardlist):
	victory = ''
	if boardlist[1] == boardlist[2] == boardlist[3] == playermarks[0] or boardlist[4] == boardlist[5] == boardlist[6] == playermarks[0] or boardlist[7] == boardlist[8] == boardlist[9] == playermarks[0] or boardlist[1] == boardlist[5] == boardlist[9] == playermarks[0] or 	boardlist[3] == boardlist[5] == boardlist[7] == playermarks[0]:
		victory = 'Player 1'
	elif boardlist[1] == boardlist[2] == boardlist[3] == playermarks[1] or boardlist[4] == boardlist[5] == boardlist[6] == playermarks[1] or boardlist[7] == boardlist[8] == boardlist[9] == playermarks[1] or boardlist[1] == boardlist[5] == boardlist[9] == playermarks[1] or 	boardlist[3] == boardlist[5] == boardlist[7] == playermarks[1]:
		victory = 'Player 2'
	else:
		victory  = 'Tie!'
	return victory	

def take_moves():
	moves = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	counter = 1
	game_board(moves)
	while counter != 6:
		#print("counter  = ", counter)
		print("Player1 make your move - enter the number of the position you want to play:")
		plr1 = int(input())
		moves[plr1] = playermarks[0]
		game_board(moves)
		counter += 1
		if check_victory(moves) == 'Player 1' or check_victory(moves) == 'Player 2':
			print("{} has won the game!".format(check_victory(moves)))
			break
		elif counter == 6:
			if check_victory(moves) == 'Player 1' or check_victory(moves) == 'Player 2':
				print("{} has won the game!".format(check_victory(moves)))
			elif check_victory(moves) == 'Tie!':
				print(check_victory(moves))
			break
		print("Player2 make your move - enter the number of the position you want to play:")
		plr2 = int(input())
		moves[plr2] = playermarks[1]
		if check_victory(moves) == 'Player 1' or check_victory(moves) == 'Player 2':
			print("{} has won the game!".format(check_victory(moves)))
			game_board(moves)
			break
		game_board(moves)
	#print(counter)
	return moves

play  = 'Yes'

while play == 'Yes':
	boardlist = take_moves()
	print("Do you want to play again?:")
	play  = input()
	if play == 'No':
		break

#game_board(boardlist)


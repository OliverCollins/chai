''' SET UP THE BOARD '''

# pieces
white_pieces = [['R',0,7], ['N',1,7], ['B',2,7], ['K',3,7], ['Q',4,7], ['B',5,7], ['N',6,7], ['R',7,7]]
black_pieces = [['r',0,0], ['n',1,0], ['b',2,0], ['q',3,0], ['k',4,0], ['b',5,0], ['n',6,0], ['r',7,0]]

# pawns
for x in range(0, 8):
	white_pieces += [['P', x, 6]]
	black_pieces += [['p', x, 1]]

board, BOARD_WIDTH, BOARD_HEIGHT = [], 8, 8

for x in range(0, BOARD_HEIGHT):
	for y in range(0, BOARD_WIDTH):
		empty = True
		for piece in range(0, len(white_pieces)):
			if [white_pieces[piece][1], white_pieces[piece][2]] == [x, y]:
				board += [[white_pieces[piece][0],x,y]]
				empty = False
				break
		for piece in range(0, len(black_pieces)):
			if [black_pieces[piece][1], black_pieces[piece][2]] == [x, y]:
				board += [[black_pieces[piece][0],x,y]]
				empty = False
				break
		if empty:
			board += [['', x, y]]

empty = True

'''
|(0,7)|(1,7)|(2,7)|(3,7)|(4,7)|(5,7)|(6,7)|(7,7)|
|(0,6)|(1,6)|(2,6)|(3,6)|(4,6)|(5,6)|(6,6)|(7,6)|
|(0,5)|(1,5)|(2,5)|(3,5)|(4,5)|(5,5)|(6,5)|(7,5)|
|(0,4)|(1,4)|(2,4)|(3,4)|(4,4)|(5,4)|(6,4)|(7,4)|
|(0,3)|(1,3)|(2,3)|(3,3)|(4,3)|(5,3)|(6,3)|(7,3)|
|(0,2)|(1,2)|(2,2)|(3,2)|(4,2)|(5,2)|(6,2)|(7,2)|
|(0,1)|(1,1)|(2,1)|(3,1)|(4,1)|(5,1)|(6,1)|(7,1)|
|(0,0)|(1,0)|(2,0)|(3,0)|(4,0)|(5,0)|(6,0)|(7,0)|
'''

# Functions

def print_board(board):
	start = [0, 0]
	print("-----------------")
	for a in range(0, 8):
		for b in range(0, 8):
			for x in range(len(board)):

				# If you have the right coordinates
				if board[x][1] == start[0] and board[x][2] == start[1]:

					# Check to see if piece is there
					if board[x][0] == '':
						print("| ", end="")
						start[0] += 1
						if start[0] == 8:
							start[1] += 1
							start[0] = 0
							print("| " + str(7-b)) # print digits on side
					else:
						print("|" + board[x][0], end="") # print chars
						start[0] += 1
						if start[0] == 8:
							start[1] += 1
							start[0] = 0
							print("| " + str(7-b)) # print digits on side

	print("-----------------")
	print("|a|b|c|d|e|f|g|h|")

def is_under_attack(board, piece_pos):
	print("---> Looking for piece at position: " + piece_pos)
	for x in range(0, len(board)):
		if board[x][1] == piece_pos[0] and board[x][2] == piece_pos[1]:
			print("Found piece " + board[x][0] + " at position " + piece_pos)
	print("---> Looking at pieces attacking: " + board[x][0])
	p = board[x][0]
	
	# Look for black pieces attacking the white piece
	if board[x][0] in ['P', 'R', 'N', 'B', 'K', 'Q']:
		
		# Loop through all black pieces and find position for each
		for piece in black_pieces:
			for x in range(0, len(board)):
				if board[x][0] == piece:

					# Find what the piece is attacking
					if piece == 'p':
						if (board[x][1]-1 == piece_pos[0] and board[x][2]-1 == piece_pos[1]) or (board[x][1]+1 == piece_pos[0] and board[x][2]-1 == piece_pos[1]):
							print("---> Pawn is attacking white " + p)
							return True
					if piece == 'r':
						break
					if piece == 'n':
						break
					if piece == 'b':
						break
					if piece == 'q':
						break

	# Look for white pieces attacking the black piece
	else:
		for piece in white_pieces:
			for x in range(0, len(board)):
				if board[x][0] == piece:
					if piece == 'P':
						break
					if piece == 'R':
						break
					if piece == 'N':
						break
					if piece == 'B':
						break
					if piece == 'Q':
						break

	return False

def is_valid_move(move, white_turn):

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	nums = ['0', '1', '2', '3', '4', '5', '6', '7']

	# Check to make sure they are moving
	if move[1:3] == move[3:5]:
		print("---> You need to move to a different spot")
		return False

	# Check to make sure valid length
	if len(move) != 5:
		if len(move) < 5:
			print("---> You typed something too short")
		if len(move) > 5:
			print("---> You typed something too long")
		return False

	# Make sure they are moving their piece
	if white_turn == 1:
		if move[0] not in ['P', 'R', 'N', 'B', 'K', 'Q']:
			print("---> You're trying to move black's piece")
			return False
	if white_turn == 0:
		if move[0] not in ['p', 'r', 'n', 'b', 'k', 'q']:
			print("---> You're trying to move white's piece")
			return False

	# Check to see if moving to a valid column or row
	if move[1] not in letters or move[3] not in letters or move[2] not in nums or move[4] not in nums:
		print("---> You are moving off of the board")
		return False



	''' LOGIC FOR EACH PIECE '''
	piece = move[0]

	# Handle pawn logic
	if piece == 'P' or piece == 'p':

		# Make sure pawn is moving vertical
		if move[1] != move[3]:
			print("---> Pawn must move in the same column")
			return False

		if piece == 'P':

			# Allow en passant if at starting position for paw
			if move[2] == '1':
				if (int(move[4]) - int(move[2])) > 2:
					print("---> Pawn can't move more than 2 positions to start")
					return False

			# Else don't allow en passant
			else:
				if (int(move[4]) - int(move[2])) > 1:
					print("---> Pawn can't move more than 1 position after start")
					return False

		# Same thing but now for black
		elif piece == 'p':
			if move[2] == '6':
				if (int(move[2]) - int(move[4])) > 2:
					print("---> Pawn can't move more than 2 positions to start")
					return False
			else:
				if (int(move[2]) - int(move[4])) > 1:
					print("---> Pawn can't move more than 1 position after start")
					return False



	# Handle rook logic
	if piece == 'R' or piece == 'r':

		 # If changing both row and column
		if move[1] != move[3] and move[2] != move[4]:
			print("---> Rook can only move either horizontally or vertically")
			return False



	# Handle king logic
	if piece == 'K' or piece == 'k':
		if int(move[2]) - int(move[4]) > 1 or int(move[2]) - int(move[4]) < -1 or ord(move[1]) - ord(move[3]) > 1 or ord(move[1]) - ord(move[3]) < -1:
			print("---> King can only move to adjacent squares")
			return False



	# Handle bishop logic
	if piece == 'B' or piece == 'b':
		old_position, new_position = convert_move_to_pos(move[1:3]), convert_move_to_pos(move[3:5])
		if abs(old_position[0] - new_position[0]) != abs(old_position[1] - new_position[1]):
			print("---> Bishop can only move diagonally")
			print(old_position, new_position)
			return False



	# Handle knight logic
	if piece == 'N' or piece == 'n':
		old_position, new_position = convert_move_to_pos(move[1:3]), convert_move_to_pos(move[3:5])

		# Handle all 8 cases

		print(old_position, new_position)
		print((old_position[0]+1), new_position[0], (old_position[1]+2), new_position[1])

		# 2 up 1 right
		if (old_position[0]+1) == new_position[0] and (old_position[1]-2) == new_position[1]:
			print("---> Valid knight move (variation 1)")

		# 1 up 2 right
		elif (old_position[0]+2) == new_position[0] and (old_position[1]-1) == new_position[1]:
			print("---> Valid knight move (variation 2)")

		# 1 down 2 right
		elif (old_position[0]+2) == new_position[0] and (old_position[1]+1) == new_position[1]:
			print("---> Valid knight move (variation 3)")

		# 2 down 1 right
		elif (old_position[0]+1) == new_position[0] and (old_position[1]+2) == new_position[1]:
			print("---> Valid knight move (variation 4)")

		# 2 down 1 left
		elif (old_position[0]-1) == new_position[0] and (old_position[1]+2) == new_position[1]:
			print("---> Valid knight move (variation 5)")

		# 1 down 2 left
		elif (old_position[0]-2) == new_position[0] and (old_position[1]+1) == new_position[1]:
			print("---> Valid knight move (variation 6)")

		# 1 up 2 left
		elif (old_position[0]-2) == new_position[0] and (old_position[1]-1) == new_position[1]:
			print("---> Valid knight move (variation 7)")

		# 2 up 1 left
		elif (old_position[0]-1) == new_position[0] and (old_position[1]-2) == new_position[1]:
			print("---> Valid knight move (variation 8)")

		else:
			print("---> Knight can't move in that manner")
			return False

	return True

# Convert d1 to [3,1]
def convert_move_to_pos(move):
	if move[0] == 'a':
		return [0, 7-int(move[1])]
	if move[0] == 'b':
		return [1, 7-int(move[1])]
	if move[0] == 'c':
		return [2, 7-int(move[1])]
	if move[0] == 'd':
		return [3, 7-int(move[1])]
	if move[0] == 'e':
		return [4, 7-int(move[1])]
	if move[0] == 'f':
		return [5, 7-int(move[1])]
	if move[0] == 'g':
		return [6, 7-int(move[1])]
	if move[0] == 'h':
		return [7, 7-int(move[1])]

def move_piece(move, board):

	new_pos = convert_move_to_pos(move[3:])
	old_pos = convert_move_to_pos(move[1:3])

	# Loop through board and add new piece at position
	for x in range(0, len(board)):
		if board[x][1] == new_pos[0] and board[x][2] == new_pos[1]:
			board[x][0] = move[0]

	for x in range(0, len(board)):
		if board[x][1] == old_pos[0] and board[x][2] == old_pos[1]:
			print(board[x][0])
			board[x][0] = ''

	return board

human_turn = 1
c = input("What color would you like to play as? (w/b): ")
if c == 'w':
	comp = 'b'
else:
	human_turn = 0
	comp = 'w'

while True:

	if human_turn:
		print("===========================================================")
	
		print_board(board)

		# [PIECE, ORIG_POS, NEW_POS]
		move = input("What's the move? ")
		print()

		if is_valid_move(move, human_turn):
			move_piece(move, board)
			human_turn = 1 - human_turn
		else:
			print()
			print("**********************************")
			print("  Sorry that's not a valid move")
			print("**********************************")
			print()

	# Computer's turn
	else:
		print_board(board)

		weights = {"b": 0.32, "d": 0.11}

		for k, v in weights.items():
			print(k, v)

		print("a work in progress")
		exit(0)


# Imports
import random

# Body
def game_start():
	marbles = 17
	print("Let's play the game of Seventeen!")
	return marbles

def rejected(marbles):
	print("\nSorry, that is not a valid option.  Try again!")
	print("Number of marbles left in jar: {}\n".format(marbles))
	return marbles
	
def game_over(user_input):
	print("You removed {} marbles.".format(user_input))
	print("\nThere are no marbles left.  Computer wins!")

def validate_input(user_input, marbles):
	while True:
		try:
			user_input = int(user_input)
		except:
			rejected(marbles)
			user_input = input("Your turn: How many marbles will you remove (1-3)? ")
			continue
		if user_input > 3 or user_input < 1:
			rejected(marbles)
			user_input = input("Your turn: How many marbles will you remove (1-3)? ")
			continue
		elif (marbles - user_input) < 0:
			rejected(marbles)
			user_input = input("Your turn: How many marbles will you remove (1-3)? ")
			continue
		elif (marbles - user_input) == 0:
			game_over(user_input)
			quit()
		else: 
			return user_input

def user_moves(marbles):
	print("Number of marbles left in jar: {}\n".format(marbles))
	user_input = input("Your turn: How many marbles will you remove (1-3)? ")
	user_input = validate_input(user_input, marbles)
	print("You removed {} marbles.".format(user_input))
	marbles -= int(user_input)
	return marbles

def computer_logic(marbles):
	if marbles > 3:
		computer_input = random.randint(1,3)
	elif marbles == 3:
		computer_input = 2
	elif marbles < 3:
		computer_input = 1	
	return computer_input

def computer_moves(marbles):
	print("Number of marbles left in jar: {}\n".format(marbles))
	print("Computer's turn...")
	computer_input = computer_logic(marbles)
	print("Computer removed {} marbles.".format(computer_input))
	marbles -= int(computer_input)
	if marbles == 0:
		print("\nThere are no marbles left.  You win!")
		quit()
	else:
		return marbles

def gameflow(count=0):
	while True:
		if count == 0:
			count += 1
			marbles = game_start()
			marbles = user_moves(marbles)
		elif count % 2 == 0 and marbles != 0:
			count += 1
			marbles = user_moves(marbles)
		elif count % 2 != 0 and marbles != 0:
			count += 1
			marbles = computer_moves(marbles)


##############################################################################
def main():
    gameflow()

if __name__ == "__main__":
    main()

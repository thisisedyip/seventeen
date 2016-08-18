# Imports
import random
import itertools

# Body
def results_print(game_results):
	#count P1 and P2 winners after converting to tuple
	P1 = 0
	P2 = 0
	results_tuple = tuple(game_results)
	for i in range(len(results_tuple)):
		if results_tuple[i][-1] == 'P1':
			P1 += 1
		elif results_tuple[i][-1] == 'P2':
			P2 += 1

	#writing final results to text file
	results_out = [','.join([str(c) for c in lst]) for lst in game_results]
	with open('i206_placein_input_EY.txt', 'w') as fout:
		with open('i206_placein_input.txt', 'r') as fin:
			for idx, turns in enumerate(fin):
				turns = turns.strip()
				fout.write("Game #{}. Play sequence: {}. Winner: {}\n".format((idx+1), results_out[idx][:-3], results_tuple[idx][-1]))
			fout.write("Player 1 won {} times; Player 2 won {} times".format(P1, P2))

def game_start():
	game_turns = []
	game_results = []
	P1 = 0
	P2 = 0
	with open('i206_placein_input.txt', 'r') as fin:
		for line in fin:
			game_turns = [int(s) for s in line.split(',')]
			game_results.append(game_run(game_turns))
	return game_results
		
def game_run(game_turns):
	game_results = []
	idx = 0
	marbles = 17
	count = 0
	while True:	
			if count % 2 == 0 and marbles > 0:
				count += 1
				if marbles < game_turns[idx]:
					game_turns[idx] = marbles
					marbles -= game_turns[idx]
					game_results.append(game_turns[idx])
				else:
					marbles -= game_turns[idx]
					game_results.append(game_turns[idx])
					idx += 1
			elif count % 2 != 0 and marbles > 0:
				count += 1
				computer_turn = computer_moves(marbles)
				marbles -= computer_turn
				game_results.append(computer_turn)
			elif marbles == 0 and count % 2 == 0:
				game_results.append('P1')
				return game_results
			elif marbles == 0 and count % 2 != 0:
				game_results.append('P2')
				return game_results
			else:
				break

def computer_moves(marbles):
	computer_input = int(computer_logic(marbles))
	return computer_input

def computer_logic(marbles):
	if marbles > 3:
		computer_input = random.randint(1,3)
	elif marbles == 3:
		computer_input = 2
	elif marbles > 0 or marbles < 3:
		computer_input = 1	
	return computer_input


##############################################################################
def main():
    results_print(game_start())

if __name__ == "__main__":
    main()

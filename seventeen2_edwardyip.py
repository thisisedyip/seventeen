# Imports
import random

# Body
def results_print(results_out):
	#calculating the winners from outlst
	P1 = 0
	P2 = 0
	for winner in results_out:
		if winner == 'P1':
			P1 += 1
		elif winner == 'P2':
			P2 += 1

	#writing final results to text file
	with open('i206_placein_input_EY.txt', 'w') as fout:
		with open('i206_placein_input.txt', 'r') as fin:
			for idx, turns in enumerate(fin):
				turns = turns.strip()
				fout.write("Game #{}. Play sequence: {}. Winner: {}\n".format((idx+1), turns.replace(',','-').strip(), results_out[idx]))
			fout.write("Player 1 won {} times; Player 2 won {} times".format(P1, P2))

def game_start():
	game_turns = []
	game_results = []
	with open('i206_placein_input.txt', 'r') as fin:
		for line in fin:
			game_turns = [int(s) for s in line.split(',')]
			game_results.append(game_run(game_turns))
		results_out = [' '.join([str(c) for c in lst]) for lst in game_results]
		return results_out
		
def game_run(game_turns):
	game_results = []
	idx = 0
	marbles = 17
	count = 0
	while True:	
			if marbles > 0:
				marbles -= game_turns[idx]
				idx += 1
				count += 1
			elif marbles <= 0 and count % 2 == 0:
				game_results.append("P1")
				return game_results
			elif marbles <=0 and count % 2 != 0:
				game_results.append("P2")
				return game_results
			else:
				break

##############################################################################
def main():
    results_print(game_start())

if __name__ == "__main__":
    main()

# Sample place-in exam, part 2


# Imports
import random


# Body
def load_file():
    with open("i206_placein_input_0.txt", "r") as fin:
        lines = fin.read().splitlines()
    user_moves = {}
    n = 1
    for line in lines:
        user_moves[n] = line.split(",")
        n += 1
    return user_moves


def play_game():
    user_moves = load_file()
    games_sequence = {}
    for game, moves in user_moves.items():
        marbles_left = 17
        moves_sequence = []
        while marbles_left > 0:
            for move in moves:
                if marbles_left == 0:
                    continue
                user_input = move
                if int(user_input) > marbles_left:
                    user_input = str(marbles_left)
                moves_sequence.append(user_input)
                marbles_left -= int(user_input)
                if marbles_left == 0:
                    moves_sequence.append("P2")
                    continue
                computer_input = str(random.randint(1, 3))
                while int(computer_input) > marbles_left:
                    computer_input = str(random.randint(1, 3))
                moves_sequence.append(computer_input)
                marbles_left -= int(computer_input)
                if marbles_left == 0:
                    moves_sequence.append("P1")
                    continue
        games_sequence[game] = moves_sequence
    return games_sequence


def output():
    games_sequence = play_game()
    count_p1 = 0
    count_p2 = 0
    with open("i206_placein_output2_lpdonofrio.txt", "w") as fout:
        for game, moves in games_sequence.items():
            print(moves)
            if moves[-1] == "P1":
                count_p1 += 1
            if moves[-1] == "P2":
                count_p2 += 1
            fout.write("Game #{}. Play sequence: {}. Winner: {}\n".
                       format(str(game), "-".join(moves[:-1]), moves[-1]))
        fout.write("Player 1 won {} times; Player 2 won {} times.".
                   format(count_p1, count_p2))


#########################################################################
def main():

    output()

if __name__ == '__main__':
    main()

import random


def who_win(p1, p2):
    if p1 > p2:
        print("*** PLAYER 1 WON THE GAME ***")
    elif p1 < p2:
        print("*** PLAYER 2 WON THE GAME ***")
    else:
        print("I*** OOPS! GAME DRAW ***")


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class Human_Player(Player):
    def move(self):
        while True:
            move = input("rock,paper,scissors > ")
            if move.lower() in ['rock', 'paper', 'scissors']:
                return move
            elif 'quit' in move.lower():
                quit()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.count = 0
        self.p2.count = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        if beats(move1, move2):
            self.p1.count += 1
            print("*** PLAYER 1 WON ***")
        elif beats(move2, move1):
            self.p2.count += 1
            print("*** PLAYER 2 WON ***")
        else:
            print("***Tie***")

        print(f"Score : player one {self.p1.count} , Player two "
              f"{self.p2.count}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(">>>Game start!<<<\n"
              "*If you want to 'quit' the game.Please enter quit "
              "at anytime when we ask for a input*")
        while True:
            rounds = int(input("Enter the number of rounds you want "
                               "to play!\n"))
            if isinstance(rounds, int):
                break
            elif 'quit' in rounds.lower():
                who_win(self.p1.count, self.p2.count)
                quit()
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        who_win(self.p1.count, self.p2.count)
        while True:
            play = input("Do you want to play again? if 'yes' press 'y' "
                         "and for 'no' press 'n'.")
            if 'y' in play:
                self.p1.count = 0
                self.p2.count = 0
                self.play_game()
                break
            elif 'n' in play:
                print("Thanks for Playing!")
                break


if __name__ == '__main__':
    game = Game(Player(), random.choice([ReflectPlayer(), CyclePlayer(),
                                        RandomPlayer()]))
    game.play_game()

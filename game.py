#!/usr/bin/env python3

from random import randint

def maxthrow():
    """
    Maximize your number by throwing as many 6s as possible.

    :return total number
    """
    dices = 6
    total = 0
    while dices > 0:
        alls = []
        for i in range(dices):
            alls.append(randint(1,6))  # roll dice
        alls.sort()
        print("The diceroll is: ", end="")
        print(alls)
        # always take the highest number
        total += alls[dices-1]
        dices -= 1
        # take the rest only if they are worth it
        minimum_num = hope(dices)
        for i in alls[:dices:]:
            if i >= minimum_num:
                total += i
                dices -= 1
    return total


def hope(dices):
    """
    How many dices are still there? what number should you at least expect?

    :param: dices (int): how many dices are still in the game
    :return minimum_num
    """
    # with only 1 dice left, it should at least be 4
    if dices == 1:
        return 4
    # with only 2 dices left, they should at least be 5
    if dices == 2:
        return 5
    # you'd want 6 in any other case
    else:
        return 6


def minthrow(killer):
    """
    Hunt the other's score down with throwing as many killer numbers as possible

    :param: killer (int): the number you want to target
    :return total reduction points
    """
    input("Now try to roll as many " + str(killer) + "'s as possible. [ENTER] ")
    dices = 6
    total = 0
    while dices > 0:
        before = dices
        alls = []
        for i in range(dices):
            alls.append(randint(1,6))
            if alls[i] == killer:
                total += killer
                dices -= 1
        print("The diceroll is: ", end="")
        print(alls)
        # if you didn't score killer numbers once, you have to stop.
        if dices == before:
            input("This time you didn't roll a " + str(killer) + ". [ENTER] ")
            return total
        # if you reached 6 killer numbers, you can try again with full 6 dicepool.
        elif dices == 0:
            dices = 6
    
def turn():
    """
    try to reach more than 30 points with maxthrow, if success, reduce next ones points

    :return total: points reached or failed
    :return reduction: points draw from next player
    """
    input("Do you want to roll? [ENTER] ")
    total = maxthrow()
    input("You rolled a " + str(total) + "! [ENTER] ")
    total -= 30
    reduction = 0
    if total > 0:
        reduction = minthrow(total)
    return total, reduction


def still(players):
    """
    How many players are still in the game?

    :param: players: list of integers
    :return total (int): list of players alive
    """
    total = 0
    for i in players:
        if i > 0:
            total += 1
    return total


def kill(player, players):
    print("Player " + str(player) + " lost the game. " + str(still(players)) + " players left")


def main():
    amount_players = int(input("How many people want to play? "))
    players = []
    for i in range(amount_players):
        players.append(maxthrow())
        print("Player " + str(i) + " starts with " + str(players[i]) + " points.")
    while still(players) > 1:
        for player in range(len(players)):
            if players[player] > 0:
                print("Player " + str(player) + "'s turn.")
                total, reduction = turn()
                print("Player " + str(player) + " gains " + str(total) + " points!")
                players[player] += total
                print("Player " + str(player) + " has a score of " + str(players[player]) + ".")
                if players[player] <= 0:
                    kill(player, players)
                else:
                    target = player + 1
                    if player + 1 > len(players)-1:
                        target = 0
                    print("Player " + str(player) + " draws " + str(reduction) + " points from player " + str(target) + ".")
                    players[target] -= reduction
                    if players[target] <= 0:
                        kill(target, players)
                input("Next turn? [ENTER] ")
    print("Game Over: Player " + str(player) + " wins the game with " + str(players[player]) + " points!")

if __name__ == "__main__":
    main()

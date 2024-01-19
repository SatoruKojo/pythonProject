numbers = int(input("Let's play a game, enter the number:"))
def odd_or_even(game):
    if numbers % 2 != 0:
        return False
    else:
        return True
print(odd_or_even(numbers))


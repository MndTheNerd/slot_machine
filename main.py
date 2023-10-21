#Global Const
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter the deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("the balance amount must be greater than 0")
        else:
            print("Please Enter a number")

    return amount

def getLines():
    while True:
        lines = input("Enter the lines you want to bet on(1-" + str(MAX_LINES) + ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please Enter a number")

    return lines

def get_bet():
    while True:
        bet = input("Enter the bet amount: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"the bet amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please Enter a number")

    return bet


def main():
    balance = deposit()
    lines = getLines()
    print(balance, lines)

main()

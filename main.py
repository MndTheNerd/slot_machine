import random

#Global Const
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns  # Add this line to return the columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | " )
            else:
                print(column[row], end="")
        print()

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

def get_lines():
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
        bet = input("Enter the bet amount for each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"the bet amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please Enter a number")

    return bet


def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money in your account, your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is : ${total_bet}")

    slot = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slot)

main()

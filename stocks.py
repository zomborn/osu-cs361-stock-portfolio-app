# Author: Nick Zombor
# CS 361 Project: Stock Portfolio Management App


def mainMenu():
    while True:
        print("Main Menu\n")
        print("Please select an option below by inputting the corresponding\n"
              "number and then RETURN or ENTER. Any time during these "
              "actions,\n "
              "you’ll have the option to cancel and return to the main menu:\n")
        options = "[1] View Portfolio: display a list of stocks and # of " \
                  "shares you currently own, then view other options.\n" \
                  "[2] Purchase Stock: add a stock to your portfolio by " \
                  "entering its symbol and # of shares.\n[3] Sell Stock: " \
                  "sell a stock to your portfolio by entering its symbol " \
                  "and # of shares.\n[0] Exit Application\n"
        user_input = input(options)
        if user_input in ["1", "2", "3", "0"]:
            return user_input
        else:
            print("Sorry, your input was not recognized, please enter a "
                  "valid input (1, 2, 3, or 0)\n")


def viewPortfolio(portfolio, stock_names):
    print("Your current stock portfolio:\n")
    if len(portfolio) == 0:
        print("Your stock portfolio is currently empty!\n")
    else:
        print("The stocks you currently own are:\n")
        print("Name\tSymbol\tShares Owned\n")
        for symbol in portfolio:
            print(f"{stock_names[symbol]}\t{symbol}\t{portfolio[symbol]}\n")


def buyStock(portfolio, stock_names):
    while True:
        print("\nPurchase Stock\n")
        print("Please select a stock below to purchase for your portfolio by "
              "inputting the corresponding symbol and then RETURN or ENTER\n")
        print("Symbol\tName")
        for symbol in stock_names:
            print(f"[{symbol}]\t{stock_names[symbol]}")
        user_input = input("Enter Symbol, or 0 to return to Main Menu: ")
        if user_input == "0":
            return portfolio
        elif user_input in stock_names:
            while True:
                num_shares = input(
                    'Please enter the number of shares you would '
                    'like to purchase (whole numbers only), '
                    'or enter 0 to cancel purchase and return to '
                    'main menu: ')
                # validate number of shares input
                if num_shares.isdigit() is False:
                    print("Invalid # of shares entered. Please try again.\n")
                    continue
                else:
                    num_shares = int(num_shares)
                    break
            if user_input in portfolio:
                portfolio[user_input] += num_shares
            else:
                portfolio[user_input] = num_shares
            print(f"Successfully purchased {num_shares} shares of {user_input} "
                  f"stock! Returning to Main Menu.")
            return portfolio
        else:
            print("Sorry, you have inputted an invalid stock symbol. Please "
                  "try again.\n")


def sellStock(portfolio, stock_names):
    while True:
        print("\nSell Stock\n")
        print("Please select a stock to sell from your portfolio below by "
              "inputting the corresponding symbol and then RETURN or ENTER\n")
        print("Symbol\tName\n")
        viewPortfolio(portfolio, stock_names)
        user_input = input("Enter Symbol, or 0 to return to Main Menu: ")
        if user_input == "0":
            return portfolio
        elif user_input in portfolio:
            symbol = user_input
            print(f'Please enter the number of {user_input} shares you would '
                  'like to sell (whole numbers only), '
                  'or enter 0 to cancel sale and return to '
                  'main menu: ')
            while True:
                num_shares = input("Enter # of Shares (0 to cancel) ")
                # validate number of shares input
                if num_shares.isdigit() is False:
                    print("Invalid Input. Please try again.\n")
                    continue
                num_shares = int(num_shares)
                if num_shares > portfolio[symbol]:
                    print(f"You do not own enough shares to sell that amount. "
                          f"Please try again.")
                else:
                    portfolio[symbol] -= num_shares
                    print(f"Successfully sold {num_shares} shares of {symbol} "
                          f"stock! Returning to Main Menu.")
                    return portfolio
        else:
            print("Sorry, you have inputted an invalid stock symbol. Please "
                  "try again.\n")


print(
    "\nWelcome to the Stock Portfolio Management App! \n This app allows you "
    "to buy or sell stocks for your portfolio.\n")
portfolio = dict()
stock_names = {
    "AMZN": "Amazon",
    "DIS": "Disney",
    "INTC": "Intel",
    "AMD": "AMD",
    "MSFT": "Microsoft",
    "GOOGL": "Alphabet",
    "COST": "Costco"
}
while True:
    user_input = mainMenu()
    if user_input == "0":
        break
    elif user_input == "1":
        viewPortfolio(portfolio, stock_names)
    elif user_input == "2":
        portfolio = buyStock(portfolio, stock_names)
    elif user_input == "3":
        portfolio = sellStock(portfolio, stock_names)
    print("Now returning to Main Menu.\n")

import csv
from datetime import datetime

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
    "META": 310,
    "NFLX": 400
}

portfolio = []


def show_available_stocks():
    print("\nAvailable Stocks")
    print("----------------")
    for symbol, price in stock_prices.items():
        print(f"{symbol} = ${price}")


def add_new_stock():
    symbol = input("\nEnter new stock symbol: ").upper().strip()

    if symbol in stock_prices:
        print("Stock already exists.")
        return

    try:
        price = float(input("Enter stock price: "))

        if price <= 0:
            print("Price must be greater than 0.")
            return

        stock_prices[symbol] = price
        print(f"{symbol} added successfully.")

    except ValueError:
        print("Please enter a valid price.")


def add_stock_to_portfolio():
    symbol = input("\nEnter stock symbol to buy: ").upper().strip()

    if symbol not in stock_prices:
        print("Stock not available. First add it using option 3.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        price = stock_prices[symbol]
        investment = price * quantity

        portfolio.append([symbol, quantity, price, investment])
        print(f"{symbol} added to portfolio successfully.")

    except ValueError:
        print("Please enter quantity in numbers only.")


def view_portfolio():
    if len(portfolio) == 0:
        print("\nPortfolio is empty.")
        return

    total = 0

    print("\nYour Portfolio")
    print("--------------")

    for item in portfolio:
        print(
            f"Stock: {item[0]} | Quantity: {item[1]} | "
            f"Price: ${item[2]} | Investment: ${item[3]}"
        )
        total += item[3]

    print(f"\nTotal Investment Value: ${total}")


def save_txt():
    if len(portfolio) == 0:
        print("Portfolio is empty. Add stocks first.")
        return

    total = sum(item[3] for item in portfolio)

    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("======================\n")
        file.write("Generated On: " + str(datetime.now()) + "\n\n")

        for item in portfolio:
            file.write(
                f"Stock: {item[0]}, Quantity: {item[1]}, "
                f"Price: ${item[2]}, Investment: ${item[3]}\n"
            )

        file.write(f"\nTotal Investment Value: ${total}")

    print("TXT report saved successfully.")


def save_csv():
    if len(portfolio) == 0:
        print("Portfolio is empty. Add stocks first.")
        return

    with open("portfolio_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])

        for item in portfolio:
            writer.writerow(item)

    print("CSV report saved successfully.")


while True:
    print("\n===== Stock Portfolio Tracker =====")
    print("1. Show Available Stocks")
    print("2. Add Stock to Portfolio")
    print("3. Add New Stock")
    print("4. View Portfolio")
    print("5. Save Report as TXT")
    print("6. Save Report as CSV")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        show_available_stocks()

    elif choice == "2":
        add_stock_to_portfolio()

    elif choice == "3":
        add_new_stock()

    elif choice == "4":
        view_portfolio()

    elif choice == "5":
        save_txt()

    elif choice == "6":
        save_csv()

    elif choice == "7":
        print("Thank you for using Stock Portfolio Tracker.")
        break

    else:
        print("Invalid choice. Please enter 1 to 7.")
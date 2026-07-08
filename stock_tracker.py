stocks = {
    "AAPL": 180,
    "GOOGL": 2800,
    "TSLA": 250,
    "MSFT": 350,
    "AMZN": 140
}

total = 0

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        total += stocks[stock] * quantity
    else:
        print("Stock not found.")

print("\nTotal Investment Value: $", total)
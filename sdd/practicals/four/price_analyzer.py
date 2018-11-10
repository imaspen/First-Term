"""
Takes 5 prices and returns the total, average, highest, and lowest prices.

AT
18-10-2018
"""


def get_input(prompt):
    """Get the user to enter the (prompt)th price in pence, and strip p if necessary"""
    while True:
        try:
            price = input("Please enter price {0}: ".format(prompt))
            if price[-1] == 'p':
                price = price[:-1]
            return int(price)
        except ValueError:
            print("Please enter a valid price, eg 20p.")


if __name__ == "__main__":
    prices = []
    for i in range(1, 6):
        prices.append(get_input(i))

    total = sum(prices)
    average = total / len(prices)
    highest = max(prices)
    lowest = min(prices)

    print("\nTotal price: {0}p\nAverage price: {1}p\nHighest price: {2}p\nLowest price: {3}p".format(
        total, average, highest, lowest
    ))

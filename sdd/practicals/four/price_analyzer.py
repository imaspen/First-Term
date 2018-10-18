"""
Takes 5 prices and returns the total, average, highest, and lowest prices.

AT
18-10-2018
"""


def get_input(prompt):
    while True:
        try:
            price = input("Please enter price {0}: ".format(prompt))
            if price[-1] == 'p':
                price = price[:-1]
            return int(price)
        except ValueError:
            print("Please enter a valid price, eg 20p.")


prices = []
for i in range(1, 6):
    prices.append(get_input(i))

prices.sort()

total = sum(prices)
average = total / len(prices)
highest = prices[-1]
lowest = prices[0]

print("\nTotal price: {0}p\nAverage price: {1}p\nHighest price: {2}p\nLowest price: {3}p".format(
    total, average, highest, lowest
))

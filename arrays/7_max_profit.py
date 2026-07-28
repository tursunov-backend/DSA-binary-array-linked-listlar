# Maqola: https://www.educative.io/blog/array-interview-questions
# Masala: Aksiyani bitta marta sotib olib, bitta marta sotib eng katta foydani topish
# (Best Time to Buy and Sell Stock).


def max_profit(prices):
    min_price = float('inf')
    profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # -> 5

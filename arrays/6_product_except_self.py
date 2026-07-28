# Maqola: https://www.geeksforgeeks.org/dsa/top-50-array-coding-problems-for-interviews/
# Masala: Har bir indeks uchun o'zidan boshqa barcha elementlar ko'paytmasini topish,
# bo'lish amalisiz (Product of Array Except Self).


def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left_prod = 1
    for i in range(n):
        result[i] = left_prod
        left_prod *= nums[i]
    right_prod = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_prod
        right_prod *= nums[i]
    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))  # -> [24, 12, 8, 6]

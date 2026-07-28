
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

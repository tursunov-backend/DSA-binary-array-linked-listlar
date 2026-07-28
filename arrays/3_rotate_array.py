# Maqola: https://www.tutorialspoint.com/article/top-50-array-coding-problems-for-programming-interviews
# Masala: Massivni k pozitsiyaga o'ngga aylantirish (Rotate Array).


def rotate_array(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k] if k else nums
    return nums


if __name__ == "__main__":
    print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # -> [5, 6, 7, 1, 2, 3, 4]

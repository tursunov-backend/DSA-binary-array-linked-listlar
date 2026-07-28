# Maqola: https://www.geeksforgeeks.org/dsa/top-50-array-coding-problems-for-interviews/
# Masala: Berilgan balandliklar massividan eng ko'p suv sig'diradigan idishni topish
# (Container With Most Water, two-pointer usuli).


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # -> 49

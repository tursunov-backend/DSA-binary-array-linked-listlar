# Maqola: https://www.interviewbit.com/array-interview-questions/
# Masala: Barcha nol qiymatlarni massiv oxiriga surish, tartibni buzmasdan (Move Zeroes).


def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # -> [1, 3, 12, 0, 0]

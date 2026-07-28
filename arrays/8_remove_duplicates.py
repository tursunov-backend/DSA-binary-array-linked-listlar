# Maqola: https://www.interviewbit.com/array-interview-questions/
# Masala: Saralangan massivdan takrorlanuvchi elementlarni joyida (in-place) olib tashlash
# (Remove Duplicates from Sorted Array).


def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write  # nums[:write] - yakuniy natija


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3]
    k = remove_duplicates(arr)
    print(arr[:k])  # -> [1, 2, 3]

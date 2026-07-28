def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2])) 

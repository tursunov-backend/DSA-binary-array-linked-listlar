

def search_range(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [find_bound(True), find_bound(False)]


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 10, 12, 14], 8)) 

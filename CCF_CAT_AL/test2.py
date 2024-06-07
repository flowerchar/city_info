def binary_search(nums, target):
    left_pointer, right_pointer = 0, len(nums) - 1

    while left_pointer <= right_pointer:
        mid = left_pointer + (right_pointer - left_pointer) // 2  # 防止溢出等价于 (left_pointer + right_pointer) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1

    return -1  # 如果未找到目标值，返回 -1

# 测试示例
nums = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
target = 5
print(binary_search(nums, target))  # 输出: 4

target = 100
print(binary_search(nums, target))  # 输出: -1

# 13952062557
# Hogwarts2024

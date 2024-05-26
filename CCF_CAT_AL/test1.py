def bubble_sort(nums, descending):
    length = len(nums)
    for i in range(length):
        for j in range(0, length - i - 1):
            if descending:
                if nums[j] < nums[j + 1]:
                    # 交换 nums[j] 和 nums[j + 1]
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                if nums[j] > nums[j + 1]:
                    # 交换 nums[j] 和 nums[j + 1]
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# 测试示例
nums = [64, 34, 25, 12, 22, 11, 90, 11]
print(bubble_sort(nums, False))  # 升序排序, 输出: [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort(nums, True))   # 降序排序, 输出: [90, 64, 34, 25, 22, 12, 11]

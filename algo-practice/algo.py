from typing import List

# two sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums = [2,7,11,15, 345, 32, 2, 4, 7, -9]
target = -2

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # O(n^2)
    # x + y = target
    # use nested loops
    # outer loop is used as 'x'
    # inner loop is used as 'y'
    # we need to use range() because we can use it to track the index
    # while in inner loop, if x + y = target, then return index of [x, y]
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]
    return None
    
    # O(n)
    # for this approach, loop through list one time, therefore time complexity depends on size of list (n)
    # as we iterate through the list, we need to keep track of the value, and its index, so use a dictionary
    # we also need to use enumerate(), so we have access to index and value
    # x = target - current, think of x + y = target with 'y' moved over to the right
    map = {}
    for index, value in enumerate(nums):
      complement = target - value
      if complement in map:
        return [map[complement], index]
      if value not in map:
        map[value] = index
    return None

solution = Solution()
result = solution.twoSum(nums, target)

print(result)
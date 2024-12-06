from typing import List

nums = [2,7,11,15,345,32,4,-9]
target = -2
s = 'aacc'
t = 'ccac'

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # O(n^2)
    # x + y = target
    # use nested loops
    # outer loop is used as 'x'
    # inner loop is used as 'y'
    # we need to use range() because we can use it to track the index
    # while in inner loop, if x + y = target, then return index of [x, y]
    # for i in range(len(nums)):
    #   for j in range(i + 1, len(nums)):
    #     if nums[i] + nums[j] == target:
    #       return [i, j]
    # return None
    
    # O(n)
    # for this approach, loop through list one time, therefore time complexity depends on size of list (n)
    # as we iterate through the list, we need to keep track of the value, and its index, so use a dictionary
    # we also need to use enumerate(), so we have access to index and value
    # x = target - current, think of x + y = target with 'y' moved over to the right
    # my_map = {}
    # for index, value in enumerate(nums):
    #   complement = target - value
    #   if complement in my_map:
    #     return [my_map[complement], index]
    #   if value not in my_map:
    #     my_map[value] = index
    return None
  
  def containsDuplicate(self, nums: List[int]) -> bool:
    # O(n)
    # use a loop to keep track if current num is in dictionary
    # if current num is in dictionary, return true, else false
    # this is O(n) because time complexity increases linearly with size of list
    # my_map = {}
    # for num in nums:
    #   if num in my_map:
    #     return True
    #   my_map[num] = 1
    # return False
  
    # O(n)
    # by passing in the nums list into a set()
    # then compare length of nums and numsSet
    # if length of numsSet is smaller than length of nums, true
    return (len(set(nums)) < len(nums))
  
  def isAnagram(self, s: str, t: str) -> bool:
    # O(n log n)
    # this is order of n log n because it's using sorted()
    # return sorted(s) == sorted(t)
  
    # O(n)
    # the order of the strings doesn't matter when attempting to prove anagram
    # therefore, loop through each string and store chars in dict
    # then compare dicts after
    sMap, tMap = {}, {}
    if len(s) != len(t):
      return False
    for c in s:
      if c in sMap:
        sMap[c] += 1
      else:
        sMap[c] = 1
    for c in t:
      if c in tMap:
        tMap[c] += 1
      else:
        tMap[c] = 1
    return sMap == tMap


solution = Solution()
# result = solution.twoSum(nums, target)
# result = solution.containsDuplicate(nums)
result = solution.isAnagram(s, t)

print(result)
from typing import List

nums = [100, 4, 200, 1, 3, 2]
# numbers_sorted = [2,7,11,15]
# target = 9
# s = 'aacc'
# s = "A man, a plan, a canal: Panama"
# t = 'ccac'
# strs = ["eat","tea","tan","ate","nat","bat"]
# k = 2
# words = ["i","love","leetcode","i","love","coding"]

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:


  def twoSumSorted(self, numbers_sorted: List[int], target: int) -> List[int]:
    # since the list is already sorted, then we can utilize a 2 pointer solution
    # left pointer would be the first index, right pointer would be the last index
    # add the two indexes together, if it's the target, then return the indicies
    # if it's lesser than the target, move the left pointer to the right by 1
    # if it's more than the target, move the right pointer to the left by 1
    # eventually, the indicies will meet and add to target
    left = 0
    right = len(numbers_sorted) - 1
    while left < right:
      if numbers_sorted[left] + numbers_sorted[right] == target:
        return [left, right]
      elif numbers_sorted[left] + numbers_sorted[right] > target:
        right -= 1
      else:
        left += 1
    return None

  def isPalindrome(self, s: str) -> bool:
    # O(n) loop is iterating over the string once only
    # approach is to make everything lowercase
    # then set 2 lists for insert(0, char) and append(c)
    # once loop is done return the 2 lists as equality
    # lower_s = s.lower()
    # inserted_s = []
    # appended_s = []
    # for c in lower_s:
    #   if c.isalnum():
    #     inserted_s.insert(0,c)
    #     appended_s.append(c)
    # return inserted_s == appended_s

    # O(n) we'll use a 2 pointer solution
    # start at index[0] for the left boundary
    # start at index[len(s) - 1] for the right boundary
    # nested while loops, left and right should match on iteration, if not then false
    # add 1 for left and minus 1 for right
    left = 0
    right = len(s) - 1
    while left < right:
      while left < right and not s[left].isalnum():
        left += 1
      while right > left and not s[right].isalnum():
        right -= 1
      if s[left].lower() != s[right].lower():
        return False
      left += 1
      right -= 1
    return True

  def longestConsecutive(self, nums: List[int]) -> int:
    # brute force method
    # will need to track max_streak and current_streak
    # go with nested loops, for loop then while loop
    # for loop will set current number and current streak
    # then add one to current streak
    # while loop will check if current number + 1 is in nums
    # if it is, then up current streak
    # IF current_streak is more than max_streak, then assign
    # in the end return max streak
    # max_streak = 0
    # for current_num in nums:
    #   next_num = current_num + 1
    #   current_streak = 1

    #   while next_num in nums:
    #     next_num += 1
    #     current_streak += 1
    #     if current_streak > max_streak:
    #       max_streak = current_streak

    # O(n) solution involves using a set for O(1) look ups
    # https://www.youtube.com/watch?v=P6RZZMu_maU - good explanation
    # so we only iterate once through the list while looking up next nums in set
    # it's important that the if statement is checking for current_num - 1 IS NOT in set
    # so it starts counting the streak properly. If it checks for current_num - 1 IS IN set instead
    # then the count of current_num - 1 is not included and longest_streak will always be off by minus 1
    nums_set = set(nums)  # Convert list to a set for O(1) lookups, because python set is implemented as a hash map
    longest_streak = 0

    for num in nums_set:
        # Only start streak if 'num' has NO left neighbor
      if num - 1 not in nums_set:
        current_streak = 1
        while num + 1 in nums_set:
          num += 1
          current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak
  
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # max confusion, skipping for now
    return  
  
  def topKFrequentStrs(self, words: List[str], k: int) -> List[str]:
    # Return the answer sorted by the frequency from highest to lowest. 
    # Sort the words with the same frequency by their lexicographical order.
    #
    # again, use a hash map to track which str has appeared and how many times
    # loop through words list
    # because we need sort in lexicographical order, sort by frequency in descending order
    str_map = {}
    for word in words:
      if word in str_map:
        str_map[word] += 1
      else:
        str_map[word] = 1
    return [item[0] for item in sorted(str_map.items(), key=lambda item: (-item[1], item[0]))[:k]]  
  
  def topKFrequentNums(self, nums: List[int], k: int) -> List[int]:
    # O(n log n)
    # the approach here is to use a map
    # as we iterate through the list, track the number as key and times appeared as value
    # then sort the map and return only the k most frequent appeared keys
    nums_map = {}
    for num in nums:
      if num in nums_map:
        nums_map[num] += 1
      else:
        nums_map[num] = 1
    return [item[0] for item in sorted(nums_map.items(), key=lambda item: -item[1])[:k]]  
  
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # O(n log n)
    # take out each element and sort
    # once sorted, put into dictionary as keys
    # the value should be the actual string before sorting
    # then push the values for each key into a list
    str_map = {}
    for str in strs:
      key = ''.join(sorted(str))
      if key in str_map:
        str_map[key].append(str)
      else:
        str_map[key] = [str]
    return list(str_map.values())  
  
  def isAnagram(self, s: str, t: str) -> bool:
    # O(n log n)
    # this is order of n log n because it's using sorted()
    # return sorted(s) == sorted(t)
  
    # O(n)
    # the order of the strings doesn't matter when attempting to prove anagram
    # therefore, loop through each string and store chars in dict
    # then compare dicts after
    # sMap, tMap = {}, {}
    # if len(s) != len(t):
    #   return False
    # for c in s:
    #   if c in sMap:
    #     sMap[c] += 1
    #   else:
    #     sMap[c] = 1
    # for c in t:
    #   if c in tMap:
    #     tMap[c] += 1
    #   else:
    #     tMap[c] = 1
    return sMap == tMap
  
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

solution = Solution()
result = solution.threeSum(nums)
# result = solution.twoSumSorted(numbers_sorted, target)
# result = solution.isPalindrome(nums)
# result = solution.longestConsecutive(nums)
# result = solution.productExceptSelf(nums)
# result = solution.topKFrequentStrs(words, k)
# result = solution.topKFrequentNums(nums, k)
# result = solution.groupAnagrams(strs)
# result = solution.isAnagram(s, t)
# result = solution.containsDuplicate(nums)
# result = solution.twoSum(nums, target)

print(result)
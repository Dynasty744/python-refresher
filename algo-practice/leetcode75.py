from typing import List

word1 = "ab"
word2 = "pqrs"
nums = [0,1,0,3,12]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      # O(n) using 2 pointers
      # instead of moving 0s to the right
      # focus on moving non 0s to the left
      # left and right will start at the beginning of the list
      # iterate through the list, whenever right pointer is a non 0
      # swap the value with the one on left pointer
      # then immediately increment left pointer
      left = 0
      for right in range(len(nums)):
        if nums[right]:
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
      return nums
      
    def mergeAlternately(self, word1: str, word2: str) -> str:
      # O(n)
      # setup 2 variables to hold the length of the 2 strings
      # setup 2 pointers to use as indexes for the 2 strings
      # while the index of either string is smaller than length of either string
      # if index of first string is < than length of first string
      # then add the indexed char to res
      # then increment the index
      # perform same steps for the second string
      # return result
      l1 = len(word1)
      l2 = len(word2)
      p1 = 0
      p2 = 0
      res = []

      while p1 < l1 or p2 < l2:
        if p1 < l1:
          res += word1[p1]
          p1 += 1
        if p2 < l2:
          res += word2[p2]
          p2 += 1
          
      return ''.join(res)    

solution = Solution()
result = solution.moveZeroes(nums)
# result = solution.mergeAlternately(word1, word2)
print(result)
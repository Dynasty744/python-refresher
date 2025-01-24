from typing import List
from math import gcd

# word1 = "ab"
# word2 = "pqrs"
# s = "the sky is blue"
# t = "acbgdc"
# flowerbed = [1,0,0,0,1]
# nums = [1,12,-5,-6,50,3]
# k = 3
# s = "abciiidef"
# n = 1
# nums = [3,1,3,4,3]
# k = 5
# nums = [0,1,0,3,12]
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
str1 = "ABABAB"
str2 = "ABAB"

class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    # O(m+n)
    # first we check if the strings are divisible
    # we can do this by concatinating them together in different orders
    # if they are different, then that means they're not divisible
    # otherwise, there must be a common substring that can be used to divide both strings
    # we can make our approach by identifying the length of both strings
    # then getting the greatest common divisor of both length
    # then simply return the string sliced by the gcd
    if str1 + str2 != str2 + str1:
      return ""
    
    max_length = gcd(len(str1), len(str2))

    return str1[:max_length]

  def longestSubarray(self, nums: List[int]) -> int:
    # O(n) sliding window solution
    # start with left and right on zero
    # on iteration, we keep track of zeros encountered
    # key is knowing when window is valid vs invalid
    # valid means zeros encounted is less or equal to 1
    # invalid means zeros encountered is greater than 1
    # when window is invalid, we increment left
    # if left is zero, then decrement num of zeros count
    # keep track of max ones by calculating size of window
    # remember to subtract 1 because we're removing the zero
    longest = 0
    num_zeros = 0
    left = 0

    for right in range(len(nums)):
      if nums[right] == 0:
        num_zeros += 1
      while num_zeros > 1:
        if nums[left] == 0:
          num_zeros -= 1
        left += 1
      longest = max(longest, right - left + 1)
    
    return longest + 1

  def longestOnes(self, nums: List[int], k: int) -> int:
    # O(n) sliding window solution
    # key here is determining if window is valid or invalid
    # valid means the number of zeros flipped is lesser or equal to k
    # invalid means we've gone over k
    # while window is invalid, we keep incrementing left pointer
    # until left pointer value is a zero, then we decrement number of zeros
    # we keep track of max window size throughout all this
    max_length = 0
    num_zeros = 0
    left = 0

    for right in range(len(nums)):
      if not nums[right]:
        num_zeros += 1
      while num_zeros > k:
        if nums[left] == 0:
          num_zeros -= 1
        left += 1
      max_length = max(max_length, right - left + 1)
    
    return max_length

  def maxVowels(self, s: str, k: int) -> int:
    # O(n) sliding window technique
    # key to this one is get the count of the first window
    # then add or subtract count based on if next char is in vowel
    vowels = set('aeiou')
    max_vowels = 0
    count = 0

    for i in range(k):
      if s[i] in vowels:
        count += 1
    
    max_vowels = count

    for i in range(k, len(s)): # 'i' continues from 'k', which is the start of the sliding window
      if s[i] in vowels: # so if the next char is a vowel, then +1
        count += 1
      if s[i - k] in vowels: # if left most char is a vowel, then -1, since it's getting removed
        count -= 1
      max_vowels = max(max_vowels, count)

    return max_vowels

  def findMaxAverage(self, nums: List[int], k: int) -> float:
    # O(n) sliding windows
    # key to this one is adding right to current_sum then subtracting left
    # this is how we 'slide' the window
    # window length is set within the for loop
    current_sum = sum(nums[:k])
    max_average = current_sum / k
    
    for i in range(k, len(nums)):
      current_sum += nums[i] - nums[i - k]
      max_average = max(max_average, current_sum / k)

    return max_average

  def reverseWords(self, s: str) -> str:
    # O(n) using built-in function
    # first split the string into list format
    # then apply the reverse method to the list
    # then return by joining via space
    word_list = s.split()
    word_list.reverse()

    return ' '.join(word_list)

  def reverseVowels(self, s: str) -> str:
    # O(n) 2 pointer approach
    # we'll use a set() for vowels for O(1) look up
    # convert the string to a list()
    # set pointers on both ends of the string
    # while left is lesser than right
    # and while left or right is not in vowels
    # move the pointer inwards
    # this enables iterations to happen until both are at vowels
    # if both are vowels, then we use tuple unpacking / simultaneous assignment
    # make sure to return by joining()
    vowels = set('aeiouAEIOU')
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
      while left < right and s[left] not in vowels:
        left += 1
      while left < right and s[right] not in vowels:
        right -= 1
      
      if s[left] in vowels and s[right] in vowels:
        s[left], s[right] = s[right], s[left]
        right -= 1
        left += 1
    
    return ''.join(s)
    
  def maxOperations(self, nums: List[int], k: int) -> int:
    # O(n) 2 pointer solution
    # we want to sort nums list to take advantage of the 2 pointer technique
    # setting the 2 pointers on either end of the list
    # we know that if the sum of 2 pointers is greater than target
    # then we decrement the right pointer
    # and if the sum of 2 pointers is less than target
    # then we increment the left pointer
    # question is misleading by stating the element should be removed
    # it doesn't need to be removed, because pointers have already moved on
    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1
    
    while left < right:
      if nums[left] + nums[right] > k:
        right -= 1
      elif nums[left] + nums[right] < k:
        left += 1
      else:
        count += 1
        left += 1
        right -= 1
    
    return count

  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    # O(n)
    # start by placing 0s on both sides of the flowerbed
    # then start iterate through by skipping the first and last index
    # for each iteration check that all 3 positions are 0s
    # if yes, then we place a 1
    # and decrement n by 1
    # return is n equal or less than 0
    f = [0] + flowerbed + [0]

    for i in range(1, len(f) - 1):
      if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
        f[i] = 1
        n -= 1
    
    return n <= 0

  def isSubsequence(self, s: str, t: str) -> bool:
    # O(n) 2 pointers
    # we're checking if 's' is a substring of 't'
    # start by setting pointers 'i' and 'j' at 0 for the 2 strings
    # while both pointers are lesser than the len of the 2 strings
    # we only want to move pointer 's' if there's a match with 'j'
    # we increment 'j' in both cases, so we do that outside of if statement
    # then we return true if pointer 'i' is equal to length of 's'
    # because that means we've gotten to the end of the string
    # and there's a full match of the substring
    i, j = 0, 0
    while i < len(s) and j < len(t):
      if s[i] == t[j]:
        i += 1
      j += 1
    return True if i == len(s) else False

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
result = solution.longestSubarray(nums)
# result = solution.longestOnes(nums, k)
# result = solution.maxVowels(s, k)
# result = solution.findMaxAverage(nums, k)
# result = solution.reverseWords(s)
# result = solution.reverseVowels(s)
# result = solution.maxOperations(nums, k)
# result = solution.canPlaceFlowers(flowerbed, n)
# result = solution.isSubsequence(s, t)
# result = solution.moveZeroes(nums)
# result = solution.mergeAlternately(word1, word2)
print(result)